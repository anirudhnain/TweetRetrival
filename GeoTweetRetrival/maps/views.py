from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from tweetCollect import tweetCollection

def index(request):

	context_dict = {'boldmessage': "Finding your current co-ordinates",'mapping':"Mapping your co-ordinates"}

	return render(request, 'maps/index.html', context_dict)

def search(request):
	if 'qd' in request.GET:
		print request.GET['qd']

		coordinates=request.GET['qd'].split( );
		lat=float(coordinates[0])
		lon=float(coordinates[1])
		tweetobj=tweetCollection()
		tweetobj.tweets(lat,lon)

	return render_to_response('maps/final.html')

