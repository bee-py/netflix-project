# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

netflix_df = pd.read_csv('netflix_data.csv')

#What was the most frequent movie duration in the 1990s?

movies_subset = netflix_df[netflix_df['type'] == 'Movie']
year_x = movies_subset[movies_subset['release_year'] >= 1990]
year_subset = year_x[year_x['release_year'] < 2000]
dura = year_subset['duration']

plt.hist(dura)
plt.title ('Distribution of mmovie lengths in the 1990s')
plt.xlabel ('Duration (mins)')
plt.ylabel ('No. of movies')
plt.show()
duration = 100

#Counting the number of short action movies
genre_subset = year_subset[year_subset['genre'] == 'Action']

#Using for loop as a counter
short_action = 0
for lab, row in genre_subset.iterrows() :
    if row['duration'] < 90 :
        short_action = short_action + 1
    else :
        short_action = short_action
print (short_action)

short_action_alt = (genre_subset['duration'] < 90).sum()

print (short_action_alt)
