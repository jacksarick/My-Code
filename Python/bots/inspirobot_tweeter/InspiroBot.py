import tweepy
import urllib2

# twitter crap
consumer_key = "uGrShu4GnN5TOTQHLU7d61aIm"
consumer_secret = "RWpcnM191iY0zsxeXeENZ3O2PayhNtuH54hKWo4xrgH8tz9XJe"

access_token = "4717423181-ZiIHqKgOyxQ66MXSdTGORTXgICphU047mIdVy8W"
access_token_secret = "WUzTfkG7KdAYFYsv3o1iPg2hUYapS0qf9IdspgzQ1h3oS"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Get the image
req = urllib2.Request('http://inspirobot.me/api?generate=true', headers={ 'User-Agent': 'Mozilla/5.0' })
img_src = urllib2.urlopen(req).read()
urllib2.urlretrieve(img_src, "new_image.jpg")

api.update_with_media("new_image.jpg")