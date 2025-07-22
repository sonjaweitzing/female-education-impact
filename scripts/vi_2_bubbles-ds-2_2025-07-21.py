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

# After creating fig, ax
fig, ax = plt.subplots(figsize=(13,8))

# Add text field for bubble size
ax.text(
    0.98, 0.98, 'Bubble size: Population',
    transform=ax.transAxes,
    fontsize=12, color='black',
    ha='right', va='top',
    bbox=dict(facecolor='white', alpha=0.7, edgecolor='none')
)

# Set axis limits and labels
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
ax.set_title(f'Fertility Rate vs Gender Ratio Mean Years in School \n\n{fertility.columns[0]}')
ax.grid(True, linestyle='--', alpha=0.5)
cbar = plt.colorbar(scatterplot, ax=ax)
cbar.set_label('GDP per Capita (USD)')

time_res = 10
time_speed = 1
time_steps = time_res * (fertility.shape[1] - 1)

label_texts = [ax.text(0, 0, '', fontsize=9, ha='center', va='bottom') for _ in range(10)]

def animate(i):
    ''' Animate the bubble chart by interpolating positions and sizes'''
    t = i / time_res
    t_low = int(t)
    f = t - t_low

    p_interp = (1-f) * positions[:,t_low,:] + f * positions[:,t_low + 1,:]
    scatterplot.set_offsets(p_interp)
    s_interp = (1-f) * size[:,t_low] + f * size[:,t_low + 1]
    scatterplot.set_sizes(s_interp)
    c_interp = (1-f) * color[:,t_low] + f * color[:,t_low + 1]
    scatterplot.set_array(c_interp)
    ax.set_title(f'Fertility Rate vs Gender Ratio Mean Years in School \n\n{fertility.columns[t_low + 1]}')

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
description = 'bubbles-gender-ratio-school-fertility'
# anim.save(f'../visualizations/anim_ds2_{timestamp}.mp4', writer='ffmpeg', fps=30) # version conflicting with matplotlib
anim.save(f'../visualizations/an_2_{description}_{timestamp}.gif', writer='pillow', fps=30)

plt.show()

# create a JSON file with the metadata
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
  "output": f'../visualizations/ani_2_{description}_{timestamp}.gif',
  "author": "sonjaweitzing",
  "created_with": [
    "Python",
    "pandas",
    "matplotlib",
    "numpy"
  ],
  "created_on": timestamp
}

with open(f'../visualizations/md_2_an-{description}_{timestamp}.json', 'w') as f:
    json.dump(metadata, f, indent=4)


def plot_bubble_chart_for_year_ds2(year, fertility, gender_school, gdp, population, description='bubble-chart'):
    """
    Plots a bubble chart for the given year.
    Bubble size corresponds to population.
    """
    if year not in fertility.columns:
        raise ValueError(f"Year {year} not found in dataset columns.")

    idx = fertility.columns.get_loc(year)
    x = gender_school.iloc[:, idx]
    y = fertility.iloc[:, idx]
    sizes = population.iloc[:, idx] * 2e-6
    colors = gdp.iloc[:, idx]

    fig, ax = plt.subplots(figsize=(13,8))
    scatterplot = ax.scatter(
        x, y, s=sizes, c=colors,
        norm=mcolors.LogNorm(vmin=np.nanmin(gdp.values), vmax=np.nanmax(gdp.values))
    )
    ax.set_xlabel('Gender Ratio Mean Years in School [percent]')
    ax.set_ylabel('Fertility Rate [Babies per woman]')
    ax.set_title(f'Fertility Rate vs Gender Ratio Mean Years in School\n\n{year}')
    ax.grid(True, linestyle='--', alpha=0.5)
    cbar = plt.colorbar(scatterplot, ax=ax)
    cbar.set_label('GDP per Capita (USD)')

    # Add text field for bubble size
    ax.text(
        0.98, 0.98, 'Bubble size: Population',
        transform=ax.transAxes,
        fontsize=12, color='black',
        ha='right', va='top',
        bbox=dict(facecolor='white', alpha=0.7, edgecolor='none')
    )

    # Label the 10 biggest countries by population
    biggest_idx = np.argsort(sizes)[-10:]
    for idx in biggest_idx:
        ax.text(x.iloc[idx], y.iloc[idx], fertility.index[idx], fontsize=9, ha='center', va='bottom')

    # save the figure
    timestamp = get_timestamp()
    fig.savefig(f'../visualizations/pl_2_{description}-{year}_{timestamp}.pdf', bbox_inches='tight')

    # Create metadata for the plot
    metadata = {
      "title": "Bubble Chart: Gender Ratio in Schooling vs Fertility Rate",
      "description": "Bubble chart showing the relationship between gender ratio in mean years of schooling (women as percent of men, ages 25-34) and fertility rate for a given year. Bubble size represents population, and color encodes GDP per capita.",
      "data_sources": {
        "fertility": "../data/processed/ds_2_filtered_fertility_2025-07-21T20:55:35.csv",
        "gdp_per_capita": "../data/processed/ds_2_filtered_gdp_2025-07-21T20:55:35.csv",
        "gender_schooling": "../data/processed/ds_2_filtered_gender_school_2025-07-21T20:55:35.csv",
        "population": "../data/processed/ds_2_filtered_population_2025-07-21T20:55:35.csv"
      },
      "variables": {
        "x": "Gender Ratio Mean Years in School (women as percent of men, ages 25-34)",
        "y": "Fertility Rate (babies per woman)",
        "size": "Population",
        "color": "GDP per Capita (USD)"
      },
      "countries": "All countries in the datasets",
      "year": year,
      "output": f'../visualizations/pl_2_{description}-{year}_{timestamp}.pdf',
      "author": "sonjaweitzing",
      "created_with": [
        "Python",
        "pandas",
        "matplotlib",
        "numpy"
      ],
      "created_on": timestamp
    }

    with open(f'../visualizations/md_2_pl-{description}-{year}_{timestamp}.json', 'w') as f:
        json.dump(metadata, f, indent=4)

# Plot bubble chart for the year 2015
plot_bubble_chart_for_year_ds2('2015', fertility, gender_school, gdp, population, description)
plot_bubble_chart_for_year_ds2('1970', fertility, gender_school, gdp, population, description)


