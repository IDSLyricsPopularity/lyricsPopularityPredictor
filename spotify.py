import pandas as pd
import numpy as np
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from Utils.utils import client_id, client_secret

df = pd.read_csv('Datasets/train2.0_english.csv')

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#Add new column to store popularity score from spotify
df["popularity"] = np.nan

#Get popularity values for tracks from spotify
for index, row in df.iterrows():
    if(index % 1000 == 0):
        print(index, " / ", df.shape[0])
    if pd.notnull(row["track_name"]) and pd.notnull(row["artist_name"]):
        try:
            results = sp.search(q='track:' + row["track_name"] +' artist:' + row["artist_name"], type='track', limit=1)
            if results.get("tracks").get("items"):
                df.loc[index, 'popularity'] = results.get("tracks").get("items")[0].get("popularity")
        except:
            print("Something went wrong with track " + row["track_name"] + " : " + row["artist_name"])

df = df[df['popularity'].notna()]
print(df.head())
print(df.notna().sum())
print(df.info())
df.to_csv('Datasets/train_popularity.csv', mode='a', header=False, index=False)
