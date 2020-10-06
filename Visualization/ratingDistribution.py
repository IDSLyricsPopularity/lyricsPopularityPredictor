import pandas as pd
import matplotlib.pyplot as plt

colnames=['mxm_track_id', 'track_name', 'artist_id', 'artist_name', 'genre', 'rating', 'num_favourite', 'popularity'] 
df = pd.read_csv('Datasets/train_popularity.csv', names=colnames, header=None)

df['popularity'].plot(kind='hist', bins=101, range=(0,100))
plt.xlabel('Popularity')
plt.title('Popularity Distribution of The Tracks')

plt.show()


'''
#Use this if you want to check rating for lyrics instead.
df['rating'].plot(kind='hist', bins=99, range=(2,100))
plt.xlabel('Rating')
plt.title('Lyrics rating Distribution')
'''