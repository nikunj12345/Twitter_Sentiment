import sys                                                                   # For using system specific argument
import json                                                                  # Since json file is generated
import error                                                                 # To check whether arguments passed are correct
import preprocess                                                            # To remove stopwords and other irrelevant data
import os                                                                    # It injects all modules 

#Error handling
if error.check_cmd(len(sys.argv)) == True:                                   # It import error file and check whether all conditions are satisfied
    sentimentData = sys.argv[1]                                              # 2nd argument must be AFINN-111.txt 
    twitterData = sys.argv[2]                                                # 3rd argument must be the gennerated file output.txt
else:
    sys.exit(-1)                                                             # exit status

#decode tweets in utf-8 format    
def tweet_dict(twitterData):                                                 # define function whose name is tweet_dict
    
    twitter_list_dict = []                                                   # for indexing purpose and storing it in twitter_list_dict
    twitterfile = open(twitterData)                                          # Opens the output or twitterData file with name twitterfile
    for line in twitterfile:                                                 # for loop for scanning all the lines in twitterfile
        twitter_list_dict.append(json.loads(line.decode('utf-8-sig')))       # for loop for scanning all the lines in twitterfile

    twitterfile.close()                                                      # closing the file name twitterfile
    return twitter_list_dict                                                 # returning the result in twitter_list_dict

def sentiment_dict(sentimentData):                                           # defining function whose name is sentiment_dict
    
    afinnfile = open(sentimentData)                                          # opens the AFINN-111 or sentimentData file with name afinnfile
    scores = {}                                                              # creating a dictionary with name scores
    for line in afinnfile:                                                   # for loop to check every line in afinnfile
        term, score  = line.split("\t")                                      # splitting afinnfile according to \t in term and score 
        scores[term] = int(score)                                            # assigning score according to the term

    afinnfile.close()                                                        # closing the file afinnfile
    return scores                                                            # return value of score according to index
    
def main():                                                                  # main begins
    
    tweets = tweet_dict(twitterData)                                         # contains tweets
    sentiment = sentiment_dict(sentimentData)                                # contains dictionary of scores
    
    for index in range(len(tweets)):                                         # checking all the index in tweets file
        tweet_word = tweets[index]['text'].split()                           # tokenizing every word of tweet
        tweet_word = preprocess.clean_stopwords(tweet_word)                  # removing stopwords from list of words
        sent_score = 0                                                       # initially sentiment score is 0
        for word in tweet_word:                                              # accessing tweet word by word
            word=word.lower()                                                # converting word to lower case because all words in sentiment file are in lower case
            word=preprocess.clean_data(word)                                 # removing punctuations and url's from tweets

            if not (word.encode('utf-8', 'ignore') == ""):                   # if the scanned word is not the decoded one then ignore it
                if word.encode('utf-8') in sentiment.keys():                 # checking if word from tweet is present in sentiment file
                    sent_score = sent_score + int(sentiment[word])           # calculating sentiment score of word
                        
                else:
                    sent_score = sent_score                                  # if sentiment doesn't match then copy the sent_score
                        
            print ("word:",word.encode("utf-8"),"sentiment_score",int(sent_score))# printing the result to stdout
    
if __name__ == '__main__':
    main()                                                                   # To import script into another module 
