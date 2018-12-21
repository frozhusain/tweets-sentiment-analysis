import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

hashtag_phrase=input("enter the keyword to search tweets::")
ckey="cO4PJdfaFSvX25BB7ysQio7Q2"
csecret="31REzY4Q8NRZuqQxlwCtBcgZZeqZyLiClxEyAoerhX6M91TfUb"
atoken="2476790046-ueMP4B4lfaxkNgKpcqcdxlFAW5ZpTQuXE3dEfX1"
asecret="iA1pKvofwVpbzhgtUyGQY9glulVn8mqzryoPRbIk0Csbk"

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
ob = tweepy.API(auth)
p=1
for tweet in tweepy.Cursor(ob.search,hashtag_phrase, lang="en", tweet_mode='extended').items(100):
    print(tweet.full_text.replace('\n',' ').encode('utf-8'))
    print('\n')
    print(p)
    s=tweet.full_text.replace('\n',' ').encode('utf-8')
    saveFile=open('tweetextracted3.txt','a')
    saveFile.write(str(p))
    saveFile.write(str(s))
    saveFile.write('\n')
    saveFile.close()
    p=p+1
         

