import json, time, sys,tweepy
from tweepy import StreamListener
from tweepy.api import API

class SListener(tweepy.StreamListener):

    def __init__(self, api=None):
        self.api = api or API()
        self.n = 0
        self.m = 100

    def on_status(self, status):
        if status.coordinates:
            print ('Text: \t'+status.text.encode('utf8'))
            print ('User Name: \t'+status.user.name.encode('utf8'))
            print ('Place: \t'+status.place.full_name)
            print ('Coordinates: \t'+'lat: \t' + str(status.coordinates['coordinates'][1])+'\t lon: \t' + str(status.coordinates['coordinates'][0]))
            self.n = self.n+1
            if self.n < self.m: return True
            else:
                print 'tweets = '+str(self.n)
                return False

    def on_limit(self, track):
        sys.stderr.write(track + "\n")
        return

    def on_error(self, status_code):
        sys.stderr.write('Error: ' + str(status_code) + "\n")
        return False

    def on_timeout(self):
        sys.stderr.write("Timeout, sleeping for 60 seconds...\n")
        time.sleep(60)
        return 
