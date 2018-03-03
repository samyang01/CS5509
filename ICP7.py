# Extract the following web URL text using BeautifulSoup
# https://en.wikipedia.org/wiki/Python_(programming_language)
# 2.Save it in input.txt
# 3.Applythe following on the text and show output:
# Tokenization
# Stemming
# POS
# Lemmatization
# Trigram
# Named Entity Recognition

import nltk
import requests
import bs4
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk import pos_tag, ne_chunk

res=requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)')
soup=bs4.BeautifulSoup(res.text,"html.parser")
input=open('input.txt','w')
text=soup.select('p')
for text in text:
    input.write(text.text +'\n')
input.close()
a=open('input.txt')
input=a.read()

# tokenizing words
tokens=word_tokenize(input)
#print(tokens)

# stemming
ps=PorterStemmer()
Stems=[]
for word in tokens:
    Stems.append(ps.stem(word))
#print(Stems)

# parts of speech tagging
POS=nltk.pos_tag(tokens)

# lemmitazation
lem=WordNetLemmatizer()
lem_words=[]
for word in tokens:
    if lem.lemmatize(word, 'n') != word:
        lem_words.append(lem.lemmatize(word,'n'))
    elif lem.lemmatize(word, 'v') != word:
        lem_words.append(lem.lemmatize(word, 'v'))
    else:
        lem_words.append(word)
    #print(lem_words)

# Trigrams
trigrams=[]
for i in range(len(tokens)):
    trigrams.append(tokens[i:i+3])
#print(trigrams)

# Named Entity Recognition
NER=nltk.ne_chunk(POS)
print(NER)