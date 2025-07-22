import pandas as pd

# Provenance demo script for sorting country GDP data using merge sort

def merge_sort_kv(arr):
    ''' Sorts an array of (key, value) pairs by value using merge sort '''
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_kv(arr[:mid])
    right = merge_sort_kv(arr[mid:])
    return merge_kv(left, right)

def merge_kv(left, right):
    ''' Merges two sorted arrays of (key, value) pairs by value '''
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][1] < right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Demo script to sort GDP data for 2015

# Load the filtered dataset
df = pd.read_csv('../data/processed/ds_2_filtered_gdp_2025-07-21T20:55:35.csv')

# Create (country, gdp) pairs, dropping rows with missing GDP
country_gdp_2015 = list(zip(df['country'], df['2015']))
country_gdp_2015 = [(country, gdp) for country, gdp in country_gdp_2015 if pd.notnull(gdp)]

# Sort by GDP
sorted_country_gdp_2015 = merge_sort_kv(country_gdp_2015)

# reverse the order to get descending GDP
sorted_country_gdp_2015.reverse()

print("Sorted (country, GDP per capita) for 2015:")
print(sorted_country_gdp_2015)