import tweepy                                                                            # Open-source enable python to communicate with twitter
from tweepy import OAuthHandler                                                          # Twitter stop basic authentication
from tweepy import Stream                                                                # Establishes a streaming session and routes message to streamlistener
from tweepy.streaming import StreamListener
import sys
import os

#to register our client application with Twitter
api_key = "Dbf0NKPtMWGcSSzgEb7qkKeqt"                                                     # Consumer key
api_secret = "0sOfDImqTsHiwPAu2BliRlmIAGSAsLPaE6zW3ame3uUEHMr1zG"                         # Secret key 
access_token = "916730152435908608-RtnouOBzS3eXypyxhZ91YXUDJ9iNDyf"                       # Access token key
access_token_secret = "FHDBTwj8wjNo0Kp8MlLcmTD6JOM808f771aFdRpJILjoL"                     # Access token secret key

                                                                                          # Creating OAuthHandler instance
auth = OAuthHandler(api_key, api_secret)
                                                                                          # To make our data secure we set access token keys
auth.set_access_token(access_token, access_token_secret)
                                                                                          # Construct the API instance
# Creation of the actual interface ,using authentication                                  # Connecting to twitter API using stream
api = tweepy.API(auth)                                                                    # 3) Connect twitter API using stream

																						  # Error handling
if(not api):
    print("Problem connecting to API")
    sys.exit(-1)
    
filename=raw_input("Enter filename for collecting data based on the filter:\n")
                                                                                          # To check if file exits or not
if os.path.isfile(filename):
    print "File already exits.."
    sys.exit(-1)
                                                                                          # Create a class inheriting from StreamListener    
class MyListener(StreamListener):                                                         # 1) create class and inherit streamListener

    print("Please wait atleast 3 minutes for data to accumulate")
    print("Press Ctrl+c to terminate")
    def on_data(self, data):                                                              # Method to collect data
        try:
            #open a file to collect tweets
            with open(filename, 'a') as f:                                                # Collect data in file name output and append data accordingly
                f.write(data)
                return True                                                               # If all data has came return true
            #to catch exceptions such as KeyBoardInterrupt when Ctrl+c is pressed
        except BaseException as e:                                                        # To handle exception error if whole data has not come
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):                                                           # In case of internet connection error throughs the exception
        print(status)
        return True
    
#using class to create stream object
twitter_stream = Stream(auth, MyListener())                                               # 2) create stream object 
#filter data based on weather and location
twitter_stream.filter(track=['weather'],locations=[28.1,76.7,29.1,77.7])                  # Change the keyword here




