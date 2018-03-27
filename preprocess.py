import nltk
from nltk.corpus import stopwords
import enchant
import re
import string
#to create a dictionary of stopwords
stop_words=set(stopwords.words('english'))
d=enchant.Dict("en_US")
def clean_data(word):
    #to remove urls
    word=re.sub(r'^https?:\/\/.*[\r\n]*','',word)
    #remove digits
    word=re.sub("\d+","",word)  
    word=re.sub(r'//*',"",word)
    word=re.sub(r'http\S+',"",word)
    #remove single alphabets
    word=re.sub(r'\b\w\b',"",word)
    word=re.sub(r'rt',"",word)
    #to remove punctuations
    word=filter(lambda x:x not in string.punctuation,word)
    word = word.rstrip('?:!.,;"!@ ')
    word=word.replace(r'\u','')
    word=re.sub(r'\s+','\s',word)
    return word

def clean_stopwords(tweet_words):
    #to remove stopwords from tweets
    for word in list(tweet_words):
        word.lower()
        if word in stop_words:
            tweet_words.remove(word)
        else:
            #remove non-english words
            if d.check(word)==False:
                tweet_words.remove(word)
                
    return tweet_words
    
