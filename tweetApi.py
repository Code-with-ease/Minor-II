import tweepy 
# from flask import Flask,jsonify,request
# Fill the X's with the credentials obtained by  
# following the above mentioned procedure. 
consumer_key = "KSJYU03lzzH8ySUEKVaom1RBR" 
consumer_secret = "c9nBuKvwLjFNg3KconDt0jxmVWB6K85QsHunCYspNhAzTlmRel"
access_key = "929607063889571841-OaRHMUWEkaF0KDozhSbVP21lbImuGkq"
access_secret = "1rMYWNFPC7w8T3BEMLBGO64oHh0j3H1xuOAKWHA1150qE"
# app = Flask(__name__)
# Function to extract tweets 
def get_tweets(username): 
        # username=request.args.get('username')
        # Authorization to consumer key and consumer secret 
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
        # Access to user's access key and access secret 
        auth.set_access_token(access_key, access_secret) 
  
        # Calling api 
        api = tweepy.API(auth) 
  
        # 200 tweets to be extracted 
        number_of_tweets=2000
        tweets = api.user_timeline(screen_name=username,count=number_of_tweets) 
        # Empty Array 
        tmp=[]  
        
        # create array of tweet information: username,  
        # tweet id, date/time, text 
        tweets_for_csv = [(tweet.text,tweet.user.screen_name,tweet.user.profile_image_url,tweet.id_str,tweet.created_at) for tweet in tweets] # CSV file created  
        for j,name,url,id,time in tweets_for_csv:
        	# print(j)
        	# Appending tweets to the empty array tmp
                tweet_url="https://twitter.com/"+username+"/status/"+id
                tmp.append([j,username,url,tweet_url,time.date(),id]) 
  
        # Printing the tweets 
        return tmp[0:3]
def get_timeline(username): 
        # username=request.args.get('username')
        # Authorization to consumer key and consumer secret 
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
        # Access to user's access key and access secret 
        auth.set_access_token(access_key, access_secret) 
  
        # Calling api 
        api = tweepy.API(auth) 
  
        # 200 tweets to be extracted 
        number_of_tweets=200
        
        tweets = api.user_timeline(screen_name = username,count=number_of_tweets, tweet_mode="extended")

        tweets_list = []
        for tweet in tweets:
                if(hasattr(tweet, 'retweeted_status')):
                        text = tweet.retweeted_status.full_text
                else:
                        text = tweet.full_text
                # replies = get_replies(username,tweet.id)
                tweet_json={
                        "text":text,
                        "id_str":tweet.id_str,
                        "in_reply_to_user_id_str":tweet.in_reply_to_user_id_str,
                        "time":tweet.created_at
                }
                tweets_list.append(tweet_json)
        return tweets_list
def get_replies(username,tweetId):
        # username=request.args.get('username')
        # tweetId=request.args.get('tweetId')

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
        # Access to user's access key and access secret 
        auth.set_access_token(access_key, access_secret) 
  
        # Calling api 
        api = tweepy.API(auth) 
        searched_tweets = api.search(q='to:${username}',since_id=tweetId,rpp=100,count=1000, tweet_mode="extended")
        replies=[]
        for tweet in searched_tweets:
                if(tweet.in_reply_to_user_id_str==tweetId):
                        if(hasattr(tweet, 'retweeted_status')):
                                text = tweet.retweeted_status.full_text
                        else:
                                text = tweet.full_text
                        tweet_json={
                        "text":text,
                        "id_str":tweet.id_str,
                        "in_reply_to_user_id_str":tweet.in_reply_to_user_id_str,
                        "time":tweet.created_at}
                        replies.append(tweet_json)
        print(replies)
        return replies
def get_tweets_arr(username):
  tweets_arr=[]
  data=get_timeline(username)
  for d in data:
    tweets_arr.append(d["text"])
  return tweets_arr
# get_timeline("SrBachchan")
