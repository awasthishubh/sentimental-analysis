import pandas as pd
import numpy as np

fun = pd.read_csv('fun_split.csv')
happy = pd.read_csv('happy_split.csv')
unhappy = pd.read_csv('unhappy_split.csv')
sad = pd.read_csv('sad_split.csv')
wordbag = pd.read_csv('wordbag.csv')
wordbag = wordbag.drop_duplicates()
print(wordbag['word'])

# classify 1 for +ve and - for -ve
fun['type'] = 1
happy['type'] = 1
unhappy['type'] = 0
sad['type'] = 0
   
df = pd.concat([happy,sad,unhappy,fun]).reset_index(drop=True)


#Seperate the data into a +ve and -ve
train_positive = df[df['type'] ==1]
train_negative = df[df['type'] ==0]

positive_instance = len(train_positive)
negative_instance = len(train_negative)
print(positive_instance)
print(negative_instance)

frequency = {"word":wordbag['word']}
word_bank = [0]*len(frequency['word'])
positive = [0]*len(frequency['word'])
negative = [0]*len(frequency['word'])

for i in range(len(frequency['word'])):
    word = frequency['word'].iloc[i]
    # print(word)
    word_bank[i] = word
    
    check = str("'") + word + str("'")
    
    #Find +ve/-ve count
    count = 0
    for j in range(len(train_positive)):
        appears = train_positive['text'].iloc[j].count(check)
        
        if appears > 0:
            count = count + 1
    positive[i] = count
            
    count = 0  
    for k in range(len(train_negative)):
        appears = train_negative['text'].iloc[k].count(check)
        if appears > 0:
            count = count + 1
    negative[i] = count

d = {'word': word_bank, 'positive': positive, 'negative': negative}
ftable = pd.DataFrame(data = d)

ftable.to_csv('ftable.csv')