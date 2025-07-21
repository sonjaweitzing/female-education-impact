import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.animation import FuncAnimation
from utils import get_timestamp
import json

# Load datasets
fertility = pd.read_csv('../data/processed/ds_2_filtered_fertility_2025-07-21T20:55:35.csv', index_col=0)
gdp = pd.read_csv('../data/processed/ds_2_filtered_gdp_2025-07-21T20:55:35.csv', index_col=0)
gender_school = pd.read_csv('../data/processed/ds_2_filtered_gender_school_2025-07-21T20:55:35.csv', index_col=0)
population = pd.read_csv('../data/processed/ds_2_filtered_population_2025-07-21T20:55:35.csv', index_col=0)

# Prepare arrays
fertility_array = fertility.to_numpy()
gender_school_array = gender_school.to_numpy()
gdp_array = gdp.to_numpy()
population_array = population.to_numpy()

positions = np.stack((gender_school_array, fertility_array), axis=-1)
size_scale = 2 * 10**-6
size = population_array * size_scale
color = gdp_array

countries = fertility.index.tolist()

fig, ax = plt.subplots(figsize=(13,8))
ax.set(xlim=(0,120), ylim=(0,8))
scatterplot = ax.scatter(
    positions[:, 0, 0],
    positions[:, 0, 1],
    s=size[:,0],
    c=color[:,0],
    norm=mcolors.LogNorm(vmin=np.nanmin(gdp_array), vmax=np.nanmax(gdp_array))
)
ax.set_xlabel('Gender Ratio Mean Years in School [percent]')
ax.set_ylabel('Fertility Rate [Babies per woman]')
ax.set_title(f'{fertility.columns[0]}')
ax.grid(True, linestyle='--', alpha=0.5)
cbar = plt.colorbar(scatterplot, ax=ax)
cbar.set_label('GDP per Capita (USD)')

time_res = 4
time_speed = 0.1
time_steps = time_res * (fertility.shape[1] - 1)

label_texts = [ax.text(0, 0, '', fontsize=9, ha='center', va='bottom') for _ in range(10)]

def animate(i):
    t = i / time_res
    t_low = int(t)
    f = t - t_low

    p_interp = (1-f) * positions[:,t_low,:] + f * positions[:,t_low + 1,:]
    scatterplot.set_offsets(p_interp)
    s_interp = (1-f) * size[:,t_low] + f * size[:,t_low + 1]
    scatterplot.set_sizes(s_interp)
    c_interp = (1-f) * color[:,t_low] + f * color[:,t_low + 1]
    scatterplot.set_array(c_interp)
    ax.set_title(f'{fertility.columns[t_low + 1]}')

    # Label the 10 biggest countries by population at this time step
    pop_interp = s_interp
    biggest_idx = np.argsort(pop_interp)[-10:]
    for j, idx in enumerate(biggest_idx):
        label_texts[j].set_position((p_interp[idx,0], p_interp[idx,1]))
        label_texts[j].set_text(countries[idx])
    for j in range(10, len(label_texts)):
        label_texts[j].set_text('')

anim = FuncAnimation(fig, animate, interval=(1000*time_speed)/time_res, frames=time_steps)

# save the visualizations with timestamp
timestamp = get_timestamp()
# anim.save(f'../visualizations/anim_ds2_{timestamp}.mp4', writer='ffmpeg', fps=30) # version conflicting with matplotlib
anim.save(f'../visualizations/anim_ds2no_{timestamp}.gif', writer='pillow', fps=30)

plt.show()

# create a JSON file with the dataset metadata
metadata = {
  "title": "Gender Ratio in Schooling vs Fertility Rate (Animated Bubble Chart)",
  "description": "An animated bubble chart visualizing the relationship between the gender ratio in mean years of schooling (women as percent of men, ages 25-34) and fertility rate across countries over time. Bubble size represents population, and color encodes GDP per capita.",
  "data_sources": {
    "fertility": "../data/processed/ds_2_filtered_children_per_woman_total_fertility_2025-07-18.csv",
    "gdp_per_capita": "../data/processed/ds_2_filtered_gdp_pcap_2025-07-18.csv",
    "gender_schooling": "../data/processed/ds_2_filtered_mean_years_in_school_women_percent_men_25_to_34_years_2025-07-18.csv",
    "population": "../data/processed/ds_2_filtered_pop_2025-07-18.csv"
  },
  "variables": {
    "x": "Gender Ratio Mean Years in School (women as percent of men, ages 25-34)",
    "y": "Fertility Rate (babies per woman)",
    "size": "Population",
    "color": "GDP per Capita (USD)"
  },
  "countries": "All countries in the datasets",
  "time_range": "Years covered in the datasets",
  "output": "../visualizations/anim_ds2no_<timestamp>.gif",
  "author": "sonjaweitzing",
  "created_with": [
    "Python",
    "pandas",
    "matplotlib",
    "numpy"
  ],
  "created_on": "<timestamp>"
}

# with open(f'../visualizations/md_1_bubbles-woman-education-fertility_{timestamp}', 'w') as f:
#     json.dump(metadata, f, indent=4)

with open(f'../visualizations/md_2_bubbles-gender-ratio-schooling-fertility_{timestamp}.json', 'w') as f:
    json.dump(metadata, f, indent=4)




