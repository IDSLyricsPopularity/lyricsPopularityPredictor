import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import re
import nltk
from nltk.stem import PorterStemmer

DATASET_PATH = 'Datasets/final_songs.csv'
VOCAB_PATH = 'Datasets/vocabulary.csv'
UNSTEMMER_PATH = 'Datasets/mxm_reverse_mapping.txt'

def makeVector(lyrics):
    words = createBagOfWords(lyrics)
    df = pd.read_csv(VOCAB_PATH, names=['words'])
    df['track'] = 0

    for index, row in df.iterrows():
        df.loc[index, 'track'] = words.get(row['words'], 0)

    return np.array(df['track'])

def createBagOfWords(lyrics):
    corpus = nltk.sent_tokenize(lyrics)
    porter = PorterStemmer()
    unstemmer = pd.read_csv(UNSTEMMER_PATH, sep='<SEP>', engine='python', names=['stemmed', 'original'])
    for i in range(len(corpus)):
        corpus [i] = corpus[i].lower()
        corpus [i] = re.sub(r'\W',' ',corpus[i])
        corpus [i] = re.sub(r'\s+',' ',corpus[i])

    bagOfWords = {}
    for sentence in corpus:
        tokens = nltk.word_tokenize(sentence)
        for token in tokens:
            token = porter.stem(token)

            # if word is not in our vocabulary -> don't process it
            if token not in unstemmer['stemmed'].values:
                continue

            token = unstemmer.loc[unstemmer['stemmed'] == token, 'original'].values[0]
            if token not in bagOfWords.keys():
                bagOfWords[token] = 1
            else:
                bagOfWords[token] += 1

    return bagOfWords

def transform_genrename(genre):
    return genre.replace('/', '-')

def predict(model, word_freq):
    return model.predict(word_freq.reshape(1, -1))

@st.cache
def download_punkt():
    nltk.download('punkt')

@st.cache
def load_dataset():
    df = pd.read_csv(DATASET_PATH)
    genres = list(df.columns[-50:])
    return df, genres

@st.cache
def load_model(genre):
    genre = transform_genrename(genre)
    filename = f"Models/logReg/{genre}.sav"
    model = pickle.load(open(filename, 'rb'))
    return model

@st.cache
def load_wordcloud(genre):
    genre = transform_genrename(genre)
    filename = f"Wordclouds/{genre}.png"
    return plt.imread(filename)

# start of the script
'# Test your lyrics!'
'This tool is made for songwriters all over the world. Using machine learning, we will try to predict the popularity of your song lyrics by comparing it to thousands of other songs. Give it a try!'
download_punkt()
df, genres = load_dataset()
selected_genre = st.selectbox(
    'Pick a genre of your song:',
    genres
)

wc_img = load_wordcloud(selected_genre)
f"Just so you know what words are popular in {selected_genre}"
st.image(wc_img, use_column_width=True)
#st.image(wc_img, width=500)

song_text = st.text_area(
    "Now give us your lyrics and we'll analyze it:", 
    value="'Cause you're a sky, 'cause you're a sky full of stars",
    height=400
)

# popularity predictions
model = load_model(selected_genre)
if st.button('Analyze it'):
    word_freq = makeVector(song_text)
    prediction = predict(model, word_freq)
    prediction = int(prediction)
    
    # show corresponding heart picture
    filename = f"Images/hearts{prediction}.png"
    heart_img = plt.imread(filename)
    st.image(heart_img, width = 300)
    if prediction == 0:
        'Nice job! But keep working on it'
    elif prediction == 1:
        'Very good choice of words!'
    elif prediction == 2:
        'Wow, almost perfect! This is gonna be very popular'
    else:
        'YOU NAILED IT! Perfect..'

    ''
    ''
    '### Here are few songs that have similar popularity as your hit!'
    # similar songs
    df_similar = df[(df['popularity_class'] == prediction) & (df[selected_genre] == 1)]
    
    # show 5 random songs
    random_ids = [np.random.randint(df_similar.shape[0]) for i in range(5)]
    df_similar.iloc[random_ids, [1, 2, 3]]

    'NOTE: "popularity" is a number between 0-100 where 100 is the best'