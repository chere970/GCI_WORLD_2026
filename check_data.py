import pandas as pd
anime_data = pd.read_csv('MyAnimeList-Database-master/data/anime.csv')
anime_list = pd.read_csv('MyAnimeList-Database-master/data/animelist.csv')
anime_synop = pd.read_csv('MyAnimeList-Database-master/data/anime_with_synopsis.csv')

# print(anime_data.head())
# anime_data.info()
# print(anime_data.describe())
cols_to_use=[""]
print(anime_data[['Name','Score']])