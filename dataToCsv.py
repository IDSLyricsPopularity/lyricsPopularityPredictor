import pandas as pd
import numpy as np
import ast

dataset_path = 'Datasets/mxm_dataset_train.txt'
dataset_processed_path = 'Datasets/mxm_dataset_train2.0.csv'
mxm_api_dataset_path = 'Datasets/train2.0.csv'
reverse_mapping_path = 'Datasets/mxm_reverse_mapping.txt'
combined_train_path = 'Datasets/combined_train2.0.csv'

def merge_mxm_api_dataset(data):
    '''
        Merges data from both data sources
        Format:
            track_id            mxm_track_id    track_name	                        artist_id    ...   i      the    you    to     and ....
        0   TRAAAAV128F421A322	4623710	        A Poor Recipe for Civic Cohesion	140677.0           6.0	  4.0	 2.0	2.0	   5.0
        1   TRAAABD128F429CF47	6477168	        Soul Deep	                        15105.0	           10.0   0.0	 17.0	8.0	   2.0
        ...
    '''
    colnames=['mxm_track_id', 'track_name', 'artist_id', 'artist_name', 'genre', 'rating', 'num_favourite'] 
    mxm_data = pd.read_csv(mxm_api_dataset_path, names=colnames, header=None)
    # delete empty rows
    mxm_data = mxm_data[mxm_data['track_name'].notna()]
    final = pd.merge(mxm_data, data, on='mxm_track_id')

    # rearangement of columns - put track_id as second column
    track_id_col = final.pop('track_id')
    final.insert(1, 'track_id', track_id_col)
    final.to_csv(combined_train_path, header=True)

def data_to_csv():
    '''
        Creates a dataframe with words as columns and saves it to csv file
        Format:
            track_id            mxm_track_id   i      the    you    to     and ....
        0   TRAAAAV128F421A322	4623710	       6.0	  4.0	 2.0	2.0	   5.0
        1   TRAAABD128F429CF47	6477168	       10.0   0.0	 17.0	8.0	   2.0
        ...

    '''

    # from where to read lines from original dataset
    offset = 0
    first_batch = offset == 0

    with open(dataset_path) as f:
        lines = f.read().splitlines()

    # words on line 17, ignore first %-sign character
    words = lines[17][1:].split(',')
    songs_lines = lines[(18 + offset):]

    # unstem words
    unstemmer = pd.read_csv(reverse_mapping_path, sep='<SEP>', engine='python', names=['stemmed', 'original'])
    mapping = {row.stemmed: row.original for idx, row in unstemmer.iterrows()}
    # using unstemmed versions of words
    words = [mapping[stemmed] for stemmed in words]

    data = pd.DataFrame(columns=['track_id', 'mxm_track_id'] + words)
    row_no = offset
    for line in songs_lines:
        word_counts = np.zeros(5000)
        track_id, mxm_track_id = line.split(',')[:2]
        bow = line.split(',')[2:]
        for i_c in bow:
            index, count = i_c.split(':')
            word_counts[int(index)-1] = count
        data.loc[row_no] = [track_id, int(mxm_track_id)] + list(word_counts)
        row_no = row_no + 1
        if row_no % 500 == 0:
            data.to_csv(dataset_processed_path, mode='a', header=first_batch, index=False)
            first_batch=False
            print("successfull: ", row_no)
            data = pd.DataFrame(columns=['track_id', 'mxm_track_id'] + words)

def main():
    data_to_csv()

if __name__=='__main__':
    main()