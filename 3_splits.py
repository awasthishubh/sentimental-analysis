import pandas as pd

keywords=["sad","unhappy","happy","fun"]

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
    df['text'] = df['text'].apply(lambda x: x.replace(',',' '))
    df['text']= df['text'].str.split()

    df.to_csv(keyword+'_split.csv')