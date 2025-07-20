import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

df = pd.read_csv('../datasets/owid/womens-educational-attainment-vs-fertility_filtered.csv')
df = df[['Entity', 'Year',
         'Fertility rate - Sex: all - Age: all - Variant: estimates',
         'Combined - average years of education for 15-64 years female youth and adults',
         'Population (historical)',
         'Region']]
df = df.dropna(subset=[
    'Fertility rate - Sex: all - Age: all - Variant: estimates',
    'Combined - average years of education for 15-64 years female youth and adults',
    'Population (historical)'
])

# Build country-to-region mapping using the new Region column
region_df = df[['Entity', 'Region']].dropna(subset=['Region'])
region_map = region_df.drop_duplicates(subset=['Entity']).set_index('Entity')['Region'].to_dict()

# Pivot data
fertility = df.pivot(index='Entity', columns='Year', values='Fertility rate - Sex: all - Age: all - Variant: estimates')
education = df.pivot(index='Entity', columns='Year', values='Combined - average years of education for 15-64 years female youth and adults')
population = df.pivot(index='Entity', columns='Year', values='Population (historical)')

common_countries = fertility.index.intersection(education.index).intersection(population.index)
common_years = fertility.columns.intersection(education.columns).intersection(population.columns)

# Separate "World" data
world_edu = education.loc["World", common_years].to_numpy()
world_fert = fertility.loc["World", common_years].to_numpy()

# Remove "World" from bubble data
bubble_countries = [c for c in common_countries if c != "World"]
fertility_bubble = fertility.loc[bubble_countries, common_years].to_numpy()
education_bubble = education.loc[bubble_countries, common_years].to_numpy()
population_bubble = population.loc[bubble_countries, common_years].to_numpy()
countries = bubble_countries
years = list(common_years)

positions = np.stack((education_bubble, fertility_bubble), axis=-1)
size_scale = 2 * 10**-6
size = population_bubble * size_scale

# Assign colors by region
regions = [region_map.get(c, 'Unknown') for c in countries]
unique_regions = sorted(set(regions))
color_list = plt.cm.tab20.colors if len(unique_regions) <= 20 else plt.cm.nipy_spectral(np.linspace(0, 1, len(unique_regions)))
region_to_color = {r: color_list[i] for i, r in enumerate(unique_regions)}
colors = [region_to_color[r] for r in regions]

fig, ax = plt.subplots(figsize=(13,8))
ax.set(xlim=(0,20), ylim=(0,8))
scatterplot = ax.scatter(
    positions[:, 0, 0],
    positions[:, 0, 1],
    s=size[:,0],
    c=colors
)
world_line, = ax.plot(world_edu, world_fert, color='red', lw=2, label='World')
ax.set_xlabel('Mean Years in School (Female, 15-64)')
ax.set_ylabel('Fertility Rate')
ax.set_title(str(years[0]))
ax.grid(True, linestyle='--', alpha=0.5)

# Legend for regions
handles = [plt.Line2D([0], [0], marker='o', color='w', label=r,
                      markerfacecolor=region_to_color[r], markersize=10)
           for r in unique_regions]
ax.legend(handles=handles + [world_line], loc='upper right')

time_res = 4
time_speed = 1
time_steps = time_res * (fertility_bubble.shape[1] - 1)

def animate(i):
    t = i / time_res
    t_low = int(t)
    f = t - t_low

    p_interp = (1-f) * positions[:,t_low,:] + f * positions[:,t_low + 1,:]
    scatterplot.set_offsets(p_interp)
    s_interp = (1-f) * size[:,t_low] + f * size[:,t_low + 1]
    scatterplot.set_sizes(s_interp)
    ax.set_title(str(years[t_low + 1]))

    # World line interpolation
    world_edu_interp = (1-f) * world_edu[:t_low+1] + f * np.append(world_edu[:t_low], world_edu[t_low+1])
    world_fert_interp = (1-f) * world_fert[:t_low+1] + f * np.append(world_fert[:t_low], world_fert[t_low+1])
    world_line.set_data(world_edu_interp, world_fert_interp)


anim = FuncAnimation(fig, animate, interval=(1000*time_speed)/time_res, frames=time_steps)
plt.show()