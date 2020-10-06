import requests, json
import numpy as np
from Utils.utils import KEY as apikey

base_url = 'https://api.musixmatch.com/ws/1.1/'

def track_get(mxm_track_id):
    '''
    Request data of each track from Musixmatch API.

    Params:
        - track_id: track id in Musixmatch
    Return:
        - track data in json format included: 
            * track_name
            * artist_id
            * artist_name
            * genre_list
            * rating: track rating in Musixmatch from 0 to 100 identifying the popularity of the track
            * fav: how many users have this track in their list of favourites in Musixmatch
    '''
    method='track.get'

    url = base_url + method + '?' + '&'.join(['track_id='+mxm_track_id, 'apikey='+apikey])
    response = requests.get(url).json()['message']['body']

    if response:
        res = response['track']

        genres = []
        if res['primary_genres']:
            for genre in res['primary_genres']['music_genre_list']:

                genre_info = {
                    'genre_id': genre['music_genre']['music_genre_id'],
                    'genre_name': genre['music_genre']['music_genre_name']
                }

                genres.append(genre_info)

        info = {
            'track_name': res['track_name'],
            'artist_id': res['artist_id'],
            'artist_name': res['artist_name'],
            'genre_list': genres,
            'rating': res['track_rating'],
            'fav': res['num_favourite']
        }
    else:
        info = {
            'track_name': '',
            'artist_id': '',
            'artist_name': '',
            'genre_list': [],
            'rating': np.nan,
            'fav': np.nan
        }

    return info
