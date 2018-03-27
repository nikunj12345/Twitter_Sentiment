from __future__ import division                                                   # To carry out division in float type
import sys                                                                        # For using command line argument
import json                                                                       # Since json file is generated
import error                                                                      # To check whether arguments passed are correct
import preprocess                                                                 # To remove stopwords and other irrelevant data
import graph                                                                      # To include gpie chart
term_sentiments={} 
def computeSentiment(tweets,sentiments):

        tweet_scores=[]
        #term_sentiments={}
        
        for tweet in tweets:
                tweet_score=0													  # For every tweet set score as 0
                tweet_words=tweet.split() 										  # Tokenize every tweet
                tweet_words=preprocess.clean_stopwords(tweet_words)               # Remove all stowprds from list of tweets

                for word in tweet_words:                                          # For every word in tweet
                        word=word.lower()                                         # Convert it to lower case
                        word=preprocess.clean_data(word)                          # Preprocess data
                        
                        if word in sentiments:                                    # If word is present in sentiment file
								word_score=sentiments[word]                       # Set word score as sentiment score
								tweet_score+=word_score                           # Add score to corressponding tweet score

                        else:
                                word_score=0
                                tweet_score+=word_score

                                
                                                                                  # Add the term and its sentiment to the dictionary 
                        if word not in term_sentiments.keys():
                                term_sentiments[word]=word_score
                                                                                  # Print term_sentiments
                                                                                  # Add the tweet and score to tweet_scores
                tweet_scores.append([tweet,tweet_score])
		                                                                          # Print tweet_scores
        for term in term_sentiments:

                                                                                  # Now for every term in dictionary of terms check if term is in known sentiments
                if term not in sentiments:

                                                                                  # Unknown terms have a base score of zero and assuming they have occured once
                        new_score=0
                        occur=1

                                                                                  # Find all tweets that contain new term
                        for i in range(0,len(tweet_scores)):
                                if term in tweet_scores[i][0]:
                                        new_score+=tweet_scores[i][1]
                                        occur+=1

                                                                                  # Normalize the new score by number of occurences
                        new_score/=occur
                        term_sentiments[term]=new_score

                print term+" "+str(format(term_sentiments[term],'.3f'))
		
		
		
		
def sentiment_dict(sentimentData):
    
    afinnfile = open(sentimentData)
    scores = {} 
    for line in afinnfile:
        term, score  = line.split("\t") 
        scores[term] = int(score)  

    afinnfile.close()
    return scores
	
def tweet_dict(tweetsdata):

    tweets=open(tweetsdata)
    tweet_text=[]
    for line in tweets:
		tweet = json.loads(line)
		if 'text' in tweet:
			text = tweet['text'].lower()
			tweet_text.append(text.encode('utf-8'))
    return tweet_text

def main():
                                                                                # Error handling
        if error.check_cmd(len(sys.argv)) == True:
            words = sys.argv[1] 
            tweets = sys.argv[2]
        else:
            sys.exit(-1)
			
	tweet_texts = tweet_dict(tweets)

                                                                               # Create dictionary of terms and their scores
        scores=sentiment_dict(words)
	
																			   # Compute sentiment of terms
        computeSentiment(tweet_texts,scores)
		
	ch = raw_input("If you wan't to see pie chart press y or Y otherwise n or N to exit:\n")
	if ch=='y' or ch=='Y':
			graph.new_tweet_score(tweet_texts,scores,term_sentiments)
			sys.exit(-1)
	else:
			sys.exit(-1)
				
        


if __name__ == '__main__':
    main()                                                                     # To import script into another module
