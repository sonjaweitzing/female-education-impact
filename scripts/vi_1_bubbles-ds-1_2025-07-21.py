import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from utils import get_timestamp
import json

# Load delete_datasets
df = pd.read_csv('../data/processed/ds_1_filtered_womans-educational-attainment-vs-fertility_2025-07-21T20:55:36.csv')
df = df[['Entity', 'Year',
         'Fertility rate - Sex: all - Age: all - Variant: estimates',
         'Combined - average years of education for 15-64 years female youth and adults',
         'Population (historical)',
         'World regions according to OWID']]
df = df.dropna(subset=[
    'Fertility rate - Sex: all - Age: all - Variant: estimates',
    'Combined - average years of education for 15-64 years female youth and adults',
    'Population (historical)'
])

# Build country-to-region mapping
region_df = df[['Entity', 'World regions according to OWID']].dropna(subset=['World regions according to OWID'])
region_map = region_df.drop_duplicates(subset=['Entity']).set_index('Entity')['World regions according to OWID'].to_dict()

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

# After creating fig, ax
fig, ax = plt.subplots(figsize=(13,8))

# Add text field for bubble size
ax.text(
    1.03, 0.5, 'Bubble size: Population',
    transform=ax.transAxes,
    fontsize=12, color='black',
    ha='left', va='center',
    rotation=90,
    bbox=dict(facecolor='white', alpha=0.7, edgecolor='none')
)

# Set axis limits and labels
ax.set(xlim=(0,20), ylim=(0,8))
scatterplot = ax.scatter(
    positions[:, 0, 0],
    positions[:, 0, 1],
    s=size[:,0],
    c=colors
)
world_line, = ax.plot(world_edu, world_fert, color='red', lw=2, label='World')
ax.set_xlabel('Mean Years in School (Female, 15-64) [years]')
ax.set_ylabel('Fertility Rate [Babies per woman]')
ax.set_title(f'Fertility Rate vs Woman Mean Years in School \n\n{str(years[0])}')
ax.grid(True, linestyle='--', alpha=0.5)

# Legend for regions
handles = [plt.Line2D([0], [0], marker='o', color='w', label=r,
                      markerfacecolor=region_to_color[r], markersize=10)
           for r in unique_regions]
ax.legend(handles=handles + [world_line], loc='upper right')

time_res = 20
time_speed = 2
time_steps = time_res * (fertility_bubble.shape[1] - 1)

def animate(i):
    ''' Animate the bubble chart by interpolating positions and sizes'''
    t = i / time_res
    t_low = int(t)
    f = t - t_low

    p_interp = (1-f) * positions[:,t_low,:] + f * positions[:,t_low + 1,:]
    scatterplot.set_offsets(p_interp)
    s_interp = (1-f) * size[:,t_low] + f * size[:,t_low + 1]
    scatterplot.set_sizes(s_interp)
    ax.set_title(f'Fertility Rate vs Woman Mean Years in School \n\n{str(years[t_low + 1])}')

    # World line interpolation
    world_edu_interp = (1-f) * world_edu[:t_low+1] + f * np.append(world_edu[:t_low], world_edu[t_low+1])
    world_fert_interp = (1-f) * world_fert[:t_low+1] + f * np.append(world_fert[:t_low], world_fert[t_low+1])
    world_line.set_data(world_edu_interp, world_fert_interp)


anim = FuncAnimation(fig, animate, interval=(1000*time_speed)/time_res, frames=time_steps)

# save the visualizations with timestamp
timestamp = get_timestamp()
description = 'bubbles-woman-education-years-fertility'
# anim.save(f'../visualizations/anim_ds1_{timestamp}.mp4', writer='ffmpeg', fps=30) # version conflicting with matplotlib
anim.save(f'../visualizations/an_1_{description}_{timestamp}.gif', writer='pillow', fps=30)

plt.show()

# create a JSON file with the dataset metadata
metadata = {
  "title": "Women's Educational Attainment vs Fertility Rate (Animated Bubble Chart)",
  "description": "An animated bubble chart visualizing the relationship between mean years of education for women (ages 15-64) and fertility rate across countries and regions over time. Bubble size represents population. Bubble color encodes world regions according to Our World in Data (OWID).",
  "data_source": "../data/processed/womens-educational-attainment-vs-fertility_filtered.csv",
  "variables": {
    "x": "Combined - average years of education for 15-64 years female youth and adults",
    "y": "Fertility rate - Sex: all - Age: all - Variant: estimates",
    "size": "Population (historical)",
    "color": "World regions according to OWID"
  },
  "regions": "World regions according to OWID",
  "time_range": "Years covered in the dataset",
  "output": f'../visualizations/an_1_{description}_{timestamp}.gif',
  "author": "sonjaweitzing",
  "created_with": [
    "Python",
    "pandas",
    "matplotlib",
    "numpy"
  ],
  "created_on": timestamp,
}

with open(f'../visualizations/md_1_an-{description}_{timestamp}.json', 'w') as f:
    json.dump(metadata, f, indent=4)


# Function to plot bubble chart for a specific year
import os

def plot_bubble_for_year(df, year, description):
    # Filter and prepare data
    df_year = df[df['Year'] == year].dropna(subset=[
        'Fertility rate - Sex: all - Age: all - Variant: estimates',
        'Combined - average years of education for 15-64 years female youth and adults',
        'Population (historical)'
    ])
    df_year = df_year[df_year['Entity'] != 'World']

    # Assign colors by region
    regions = df_year['World regions according to OWID'].fillna('Unknown')
    unique_regions = sorted(set(regions))
    color_list = plt.cm.tab20.colors if len(unique_regions) <= 20 else plt.cm.nipy_spectral(np.linspace(0, 1, len(unique_regions)))
    region_to_color = {r: color_list[i] for i, r in enumerate(unique_regions)}
    colors = [region_to_color[r] for r in regions]

    # Plot
    fig, ax = plt.subplots(figsize=(13,8))
    ax.text(
        1.03, 0.5, 'Bubble size: Population',
        transform=ax.transAxes,
        fontsize=12, color='black',
        ha='left', va='center',
        rotation=90,
        bbox=dict(facecolor='white', alpha=0.7, edgecolor='none')
    )
    ax.set(xlim=(0,20), ylim=(0,8))
    scatterplot = ax.scatter(
        df_year['Combined - average years of education for 15-64 years female youth and adults'],
        df_year['Fertility rate - Sex: all - Age: all - Variant: estimates'],
        s=df_year['Population (historical)'] * 2e-6,
        c=colors
    )
    ax.set_xlabel('Mean Years in School (Female, 15-64) [years]')
    ax.set_ylabel('Fertility Rate [Babies per woman]')
    ax.set_title(f'Fertility Rate vs Woman Mean Years in School \n\n{year}')
    ax.grid(True, linestyle='--', alpha=0.5)

    # Legend for regions
    handles = [plt.Line2D([0], [0], marker='o', color='w', label=r,
                          markerfacecolor=region_to_color[r], markersize=10)
               for r in unique_regions]
    ax.legend(handles=handles, loc='upper right')

    plt.tight_layout()

    # Generate output paths
    timestamp = get_timestamp()
    plot_path = f'../visualizations/pl_1_{description}_{year}_{timestamp}.pdf'
    metadata_path = f'../visualizations/md_1_pl-{description}_{year}_{timestamp}.json'

    plt.savefig(plot_path)

    # Metadata
    metadata = {
      "title": f"Women's Educational Attainment vs Fertility Rate ({year}, Bubble Chart)",
      "description": f"Bubble chart visualizing the relationship between mean years of education for women (ages 15-64) and fertility rate across countries and regions for {year}. Bubble size represents population. Bubble color encodes world regions according to Our World in Data (OWID).",
      "data_source": "../data/processed/womens-educational-attainment-vs-fertility_filtered.csv",
      "variables": {
        "x": "Combined - average years of education for 15-64 years female youth and adults",
        "y": "Fertility rate - Sex: all - Age: all - Variant: estimates",
        "size": "Population (historical)",
        "color": "World regions according to OWID"
      },
      "regions": "World regions according to OWID",
      "year": year,
      "output": plot_path,
      "author": "sonjaweitzing",
      "created_with": [
        "Python",
        "pandas",
        "matplotlib",
        "numpy"
      ],
      "created_on": timestamp,
    }
    with open(metadata_path, 'w') as f:
        json.dump(metadata, f, indent=4)


# Plot for 1970 and 2015
plot_bubble_for_year(df, 1970, description)
plot_bubble_for_year(df, 2015, description)