import json, time, sys,tweepy
from tweepy import StreamListener
from tweepy.api import API
from django.shortcuts import render, render_to_response
from django.http import HttpResponse

class SListener(tweepy.StreamListener):

    def __init__(self, api=None):
        self.api = api or API()
        self.n = 0
        self.m = 1

    def on_status(self, status):
        if status.coordinates:
            text=status.text.encode('utf8')
            print('Text: \t'+text)
            user_name=status.user.name.encode('utf8')
            place=status.place.full_name
            lat=status.coordinates['coordinates'][1]
            lon=status.coordinates['coordinates'][0]
            context_dict = {'lat': lat,'lon':lon,'text':text}
            self.n = self.n+1
            return render_to_response('maps/tweetmap.html')
            if self.n < self.m:
                return True
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