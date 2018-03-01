import bs4
import requests
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.probability import FreqDist
from nltk.corpus import stopwords

# First, use request and beautifulsoup to request news story from espn and write into new text file
res=requests.get('http://www.espn.com/nba/story/_/id/22590062/zach-lowe-drazen-petrovic-lasting-basketball-legacy-nba')
soup=bs4.BeautifulSoup(res.text, "html.parser")
espn=open('espn.txt','w')
title=soup.select('h1')
for i in range(2):
        espn.write(title[i].text +'\n'+'\n')
text=soup.select('p')
for i in range(len(text)):
        espn.write(text[i].text +'\n')
espn.close()
espn=open('espn.txt')
o_espn=espn.read()                                 # o_espn stands for the "original espn text"

# Next, filter out the stopwords in the article using nltk.corpus library of stopwords, we set the stop words to english
stop_words=set(stopwords.words('english'))
words=o_espn.split()
nf_words=[word for word in words if word not in stop_words]         # nf_words is noise free words
nf_espn=" ".join(nf_words)                                          # new espn text without stopwords

# Next we define a function for lemmatization using the nltk wordnet lemmatizer
# first we lemmatize each word by its POS and if it is different then we append to lem_words otherwise, we append the
# original word.  Then we concatenate the list back into a lemmatized text
def lemmatize(text):
        lem = WordNetLemmatizer()
        words=text.split()
        lem_words=[]
        for word in words:
                if lem.lemmatize(word,'n') != word:
                        lem_words.append(lem.lemmatize(word,'n'))
                elif lem.lemmatize(word,'v') != word:
                        lem_words.append(lem.lemmatize(word,'v'))
                elif lem.lemmatize(word,'r') !=word:
                        lem_words.append(lem.lemmatize(word,'r'))
                else:
                        lem_words.append(word)
        text = " ".join(lem_words)
        return text

# Next define a function for bigrams by simply splitting a text and appending a tuple of 2 consecutive words to the
# bigrams list
def Bigrams(text):
    bigrams = []
    words=tuple(text.split())
    for i in range(len(words) - 1):
        bigrams.append(words[i:i + 2])
    return bigrams

#####################################################
# Next we call the lemmatization function on the noise-free espn article
lem_text=lemmatize(nf_espn)

# Then we pass the lemmatized text to the bigrams functions and use FreqDist to find the frequency of each bigram
# in the text.  We find the 5 most common bigrams using fdist.most_common() and store in bigrams_5
fdist=FreqDist(Bigrams(lem_text))
bigrams_5=fdist.most_common(5)

# Next we tokenize the noise-free/lemmatized text by sentence
sentences=sent_tokenize(lemmatize(nf_espn))

# We need to check each sentence for the occurrence of one of the frequently used bigrams.  Here I used
# nested for loops and appended the sentence to the summation list
summation=[]
for sentence in sentences:
    words=word_tokenize(sentence)
    for i in range(len(words)):
        for j in range(5):
            if bigrams_5[j][0][0] == words[i] and bigrams_5[j][0][1] == words[i+1]:
                summation.append(sentence)

# Finally, we join the sentences in the summation list in order to create a summary of the text
summary=" ".join(summation)
print(summary)