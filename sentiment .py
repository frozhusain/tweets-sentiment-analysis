# importing important libraries
from textblob import TextBlob
import matplotlib.pyplot as plt
# open file where all tweets are present
readMe = open('tweetextracted3.txt','r').readlines()
val=[0,0,0]
p=1
x=0
y=0
t=0
#check tweets and check their polarity and declare them as +,- or neutral
for c in readMe:
    print(c)
    ap=TextBlob(c)
    z=ap.sentiment
    if z.polarity>0:
        print("positive")
        x+=1
        val[0]+=1
    if z.polarity<0:  
        print("negative")
        y+=1
        val[1]+=1
    if z.polarity==0:
        print("neutral")
        t+=1
        val[2]+=1
    print('\n')
    print(p)
    p=p+1
print("total positive tweets::",x)
print("total negative tweets::",y)
print("total neutral tweets::",t)
l=["positive ","negative","neutral"]
#plot cicular graph 
plt.figure(figsize=(5,5))
plt.pie(val,labels=l,autopct="%.1f%%")
plt.show()
