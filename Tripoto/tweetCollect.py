from streaming import SListener
from BoundingBox import BoundingBox
import time, tweepy, sys, math

#Consumer Keys and access tokens, used for OAuth
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

def main():

    lat=26.9339339
    lon=75.9236237

    r=1 # radius

    box=BoundingBox()
    coord_obj=box.get_bounding_box(lat,lon,r)
    coordinates=[coord_obj.lon_min,coord_obj.lat_min,coord_obj.lon_max,coord_obj.lat_max]

    print coordinates
 
    stream = tweepy.streaming.Stream(auth, SListener())

    print "Streaming started..."

    try: 
        stream.filter(locations = coordinates,async=True)
    except:
        print "error!"
        stream.disconnect()

    print "Streaming started Asynchronosly"

if __name__ == '__main__':
    main()