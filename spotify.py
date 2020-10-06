import pandas as pd
import numpy as np
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from Utils.utils import client_id, client_secret

colnames=['mxm_track_id', 'track_name', 'artist_id', 'artist_name', 'genre', 'rating', 'num_favourite'] 
df = pd.read_csv('Datasets/train2.0.csv', names=colnames, header=None)

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#Add new column to store popularity score from spotify
df["popularity"] = np.nan

for index, row in df.iterrows():
    if pd.notnull(row["track_name"]) and pd.notnull(row["artist_name"]):
        results = sp.search(q='track:' + row["track_name"] +' artist:' + row["artist_name"], type='track', limit=1)
        if results.get("tracks").get("items"):
            df["popularity"][index] = results.get("tracks").get("items")[0].get("popularity")

print("-----Done-----")
df.to_csv('Datasets/train_popularity.csv', mode='a', header=False, index=False)



#token_url = "https://accounts.spotify.com/api/token"
#method = "POST"
#token_data = {
#    "grant_type": "client_crendentials"
#}

#        track_url = urllib.parse.quote(row["track_name"])
#        artist_url = urllib.parse.quote(row["artist_name"])
#        url = base_url + "?q=track%3A" + track_url + "%20artist%3" + artist_url + "&type=track&limit=1"
        
