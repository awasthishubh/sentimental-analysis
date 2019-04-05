

import pandas as pd
import string

keywords=["sad","unhappy","happy","fun"]

wordbag=pd.DataFrame(data = [])
for keyword in keywords:
    df = pd.read_csv(keyword+'.csv')
    
    df = df.dropna(axis=0, how = 'any')
    def removetext(text):
        return ''.join([i if ord(i) < 128 else '' for i in text])
    df['text'] = df['text'].apply(removetext)
    df['text'] = df['text'].apply(lambda x: x.lower())
    df['text'] = df['text'].apply(lambda x: x.replace('.',' '))
    df['text'] = df['text'].apply(lambda x: x.replace('\n',' '))
    df['text'] = df['text'].apply(lambda x: x.replace('?',' '))
    df['text'] = df['text'].apply(lambda x: x.replace('!',' '))
    df['text'] = df['text'].apply(lambda x: x.replace('"',' '))
    df['text'] = df['text'].apply(lambda x: x.replace(';',' '))
    df['text'] = df['text'].apply(lambda x: x.replace('#',' '))
    df['text'] = df['text'].apply(lambda x: x.replace('&amp',' '))
    df['text'] = df['text'].apply(lambda x: x.replace(',',' '))

    array = df['text'].str.split(None, expand=True).stack().value_counts()

    d = {'word': array.index, 'frequency':array}
    df2 = pd.DataFrame(data = d)
    df2 = df2.dropna(axis=0, how = 'any')
    wordbag=pd.concat([wordbag,df2])

wordbag = wordbag.drop_duplicates(subset = 'word').reset_index(drop=True)
wordbag.to_csv('wordbag.csv')

