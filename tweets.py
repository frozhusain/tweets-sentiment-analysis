import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
#input #MeToo to get tweets about it
hashtag_phrase=input("enter the keyword to search tweets::")
#add your own keys
ckey="           "
csecret="             "
atoken="          "
asecret="     "

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
ob = tweepy.API(auth)
p=1
#extract only 100 at once in english language 
for tweet in tweepy.Cursor(ob.search,hashtag_phrase, lang="en", tweet_mode='extended').items(100):
    print(tweet.full_text.replace('\n',' ').encode('utf-8'))
    print('\n')
    print(p)
#every time it will append tweets to a file     
    s=tweet.full_text.replace('\n',' ').encode('utf-8')
    saveFile=open('tweetextracted3.txt','a')
    saveFile.write(str(p))
    saveFile.write(str(s))
    saveFile.write('\n')
    saveFile.close()
    p=p+1
         

