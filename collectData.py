import pandas as pd
import apiConnect as api

track_names = []
artist_ids = []
artist_names = []
genre_lists = []
ratings = []
favs = []

def read_mxm_track_ids():
    '''
    Read mxm_track_id from mxm_dataset_train.txt

    Return:
        - list of mxm_track_id
    '''

    results = []
    with open('Datasets/mxm_dataset_train.txt') as f:
        for line in f:
            if line[:2] == 'TR':
                parts = line.split(',')
                results.append(parts[1])

    return results


def collect_data(id):
    '''
    Collect data based on the mxm_track_id from Musixmatch API.
    Data includes:
        * track_name
        * artist_id
        * artist_name
        * genre_list
        * rating: track rating in Musixmatch from 0 to 100 identifying the popularity of the track
        * fav: how many users have this track in their list of favourites in Musixmatch
    
    Params:
        - id: mxm_track_id in Musixmatch
    '''

    info = api.track_get(id)

    track_names.append(info['track_name'])
    artist_ids.append(info['artist_id'])
    artist_names.append(info['artist_name'])
    genre_lists.append(info['genre_list'])
    ratings.append(info['rating'])
    favs.append(info['fav'])

def collect_and_save_data():
    '''
    Collect and save tracks data based on mxm_track_id.
    Data includes:
        * track_name
        * artist_id
        * artist_name
        * genre_list
        * rating: track rating in Musixmatch from 0 to 100 identifying the popularity of the track
        * fav: how many users have this track in their list of favourites in Musixmatch
    '''

    counter = 204000
    batch_size = 1000
    end = False
    mxm_track_id_list = read_mxm_track_ids()
    
    while not end:
        if (counter + batch_size) > len(mxm_track_id_list):
            batch_size = len(mxm_track_id_list) - counter
            end = True
        
        print(counter, batch_size)
        df = pd.DataFrame({'id': mxm_track_id_list[counter:(counter + batch_size)]})

        df['id'].apply(collect_data)

        df['track_name'] = track_names
        df['artist_id'] = artist_ids
        df['artist_name'] = artist_names
        df['genre_list'] = genre_lists
        df['rating'] = ratings
        df['num_favourite'] = favs

        df.to_csv('Datasets/train2.0.csv', mode='a', header=False, index=False)

        counter = counter + batch_size

        del track_names[:]
        del artist_ids[:]
        del artist_names[:]
        del genre_lists[:]
        del ratings[:]
        del favs[:]

def main(): 
    collect_and_save_data()

if __name__=='__main__':
    main()
