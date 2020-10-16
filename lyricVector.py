
import nltk
import re
import pandas as pd
from nltk.stem import PorterStemmer
porter = PorterStemmer()
unstemmer = pd.read_csv('Datasets/mxm_reverse_mapping.txt', sep='<SEP>', engine='python', names=['stemmed', 'original'])
#nltk.download('punkt')
lyrics = "I loved, he loves, before we loved college! Colleges rule!"

def makeVector(lyrics):
    words = createBagOfWords(lyrics)
    df = pd.read_csv('Datasets/words.csv',names=['words'])
    df['track']=0

    for index, row in df.iterrows():
        df.loc[index, 'track'] = words.get(row['words'], 0)

    return df['track']

def createBagOfWords(lyrics):
    corpus = nltk.sent_tokenize(lyrics)
    for i in range(len(corpus )):
        corpus [i] = corpus [i].lower()
        corpus [i] = re.sub(r'\W',' ',corpus [i])
        corpus [i] = re.sub(r'\s+',' ',corpus [i])

    bagOfWords = {}
    for sentence in corpus:
        tokens = nltk.word_tokenize(sentence)
        for token in tokens:
            token = porter.stem(token)
            token = unstemmer.loc[unstemmer['stemmed'] == token, 'original'].values[0]
            if token not in bagOfWords.keys():
                bagOfWords[token] = 1
            else:
                bagOfWords[token] += 1
    return bagOfWords

print(makeVector(lyrics))

'''
This creates words.csv that has all stopwords removed from vocanulary.csv:
import csv
import nltk
from sklearn.feature_extraction import stop_words
from nltk.corpus import stopwords
#nltk.download('stopwords')

with open('Datasets/vocabulary.csv') as f:
    reader = csv.reader(f)
    vocab = [word for word in reader]
    
vocab = vocab[0]

words = []
for i in range(len(vocab)):
    if vocab[i] not in stop_words.ENGLISH_STOP_WORDS and vocab[i] not in stopwords.words('english'):
        words.append(vocab[i])

with open('Datasets/words.csv', 'w') as f:
    for item in words:
        f.write("%s\n" % item)'''
