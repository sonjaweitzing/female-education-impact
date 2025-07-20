import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.animation import FuncAnimation

# Load datasets
fertility = pd.read_csv('../datasets/gapminder/children_per_woman_total_fertility_filtered.csv', index_col=0)
gender_school = pd.read_csv('../datasets/gapminder/mean_years_in_school_woman_percent_men_25_to_34_years_filtered.csv', index_col=0)
gdp = pd.read_csv('../datasets/gapminder/gdp_pcap_filtered.csv', index_col=0)
population = pd.read_csv('../datasets/gapminder/pop_filtered.csv', index_col=0)

# Prepare arrays
fertility_array = fertility.to_numpy()
gender_school_array = gender_school.to_numpy()
gdp_array = gdp.to_numpy()
population_array = population.to_numpy()

# print shape of the arrays
print(f'fertility shape: {fertility_array.shape}')
print(f'gender_school shape: {gender_school_array.shape}')
print(f'gdp shape: {gdp_array.shape}')
print(f'population shape: {population_array.shape}')

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
ax.set_xlabel('Gender Ratio Mean Years in School')
ax.set_ylabel('Fertility Rate')
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
plt.show()

# # Show the plot for the year 2000
# year = '2000'  # Change this if your column name is different
# year_idx = fertility.columns.get_loc(year)
#
# fig, ax = plt.subplots(figsize=(13, 8))
# scatterplot = ax.scatter(
#     positions[:, year_idx, 0],
#     positions[:, year_idx, 1],
#     s=size[:, year_idx],
#     c=color[:, year_idx],
#     vmin=0.0,
#     vmax=np.nanmax(gdp_array)
# )
# ax.set_xlabel('Gender Ratio Mean Years in School')
# ax.set_ylabel('Fertility Rate')
# ax.set_title(year)
# ax.grid(True, linestyle='--', alpha=0.5)
# cbar = plt.colorbar(scatterplot, ax=ax)
# cbar.set_label('GDP per Capita (USD)')
#
# plt.show()
#



