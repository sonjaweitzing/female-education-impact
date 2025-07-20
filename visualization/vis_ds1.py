import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

df = pd.read_csv('../datasets/owid/womens-educational-attainment-vs-fertility.csv')
df = df[['Entity', 'Year',
         'Fertility rate - Sex: all - Age: all - Variant: estimates',
         'Combined - average years of education for 15-64 years female youth and adults',
         'Population (historical)']]
df = df.dropna(subset=[
    'Fertility rate - Sex: all - Age: all - Variant: estimates',
    'Combined - average years of education for 15-64 years female youth and adults',
    'Population (historical)'
])

# Pivot data
fertility = df.pivot(index='Entity', columns='Year', values='Fertility rate - Sex: all - Age: all - Variant: estimates')
education = df.pivot(index='Entity', columns='Year', values='Combined - average years of education for 15-64 years female youth and adults')
population = df.pivot(index='Entity', columns='Year', values='Population (historical)')

common_countries = fertility.index.intersection(education.index).intersection(population.index)
common_years = fertility.columns.intersection(education.columns).intersection(population.columns)

# Separate "World" data
world_mask = (np.array(common_countries) == "World")
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

fig, ax = plt.subplots(figsize=(13,8))
ax.set(xlim=(0,20), ylim=(0,8))
scatterplot = ax.scatter(
    positions[:, 0, 0],
    positions[:, 0, 1],
    s=size[:,0],
    c='blue'
)
world_line, = ax.plot(world_edu, world_fert, color='red', lw=2, label='World')
ax.set_xlabel('Mean Years in School (Female, 15-64)')
ax.set_ylabel('Fertility Rate')
ax.set_title(str(years[0]))
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend()

time_res = 4
time_speed = 0.5
time_steps = time_res * (fertility_bubble.shape[1] - 1)

label_texts = [ax.text(0, 0, '', fontsize=9, ha='center', va='bottom') for _ in range(10)]

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