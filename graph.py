import matplotlib.pyplot as plt                                           # Graphing and data visualization library for python
import preprocess                                                         # Including file which removes stopwords
def plot(tweet_scores,total_tweets):                                      # Function where all the scores and total number of tweets are send
	
	height=[]
	pos=0                                                                 # Taking positive tweets and initializing them to zero
	neg=0                                                                 # Taking negaative tweets and initializing them to zero
	neu=0                                                                 # Taking positive tweets and initializing them to zero
	for scores in tweet_scores:                                           # Checking each score in tweet_scores
		if scores>0:                                                      # If score is greater than zero 
			pos+=1                                                        # It means positive tweet
		elif scores<0:                                                    # If score is less than zero
			neg+=1                                                        # It means negative tweet
		else:
			neu+=1                                                        # Else neutral tweet
			
	height.append(pos)
	height.append(neg)
	height.append(neu)
	
	labels=['Positive Tweet','Negative Tweets','Neutral Tweets']          # Defining labels
	colors=['red','blue','green']                                         # Defining colors
	
	plt.pie(height,labels=labels,colors=colors,startangle=90,shadow=True,explode=(0,0,0),radius=1.2,autopct='%1.1f%%')     # Defining pie chart
	plt.legend()                                                          # Plotting the legend
	plt.show()                                                            # Showing the plot
	
	
def new_tweet_score(tweets,sentiment,term_sentiments):
	
	new_score=[]
	total=0
	
	for tweet in tweets:
		tweet_score=0
		total+=1
		tweet_words=tweet.split()
		tweet_words=preprocess.clean_stopwords(tweet_words)
		for word in tweet_words:
			word=word.lower()
			word=preprocess.clean_data(word)
			
			if word in sentiment:
				tweet_score+=sentiment[word]
			else:
				tweet_score+=term_sentiments[word]
				
		new_score.append(tweet_score)
		
	plot(new_score,total)