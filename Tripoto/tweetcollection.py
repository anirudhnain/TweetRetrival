import tweepy,json

#Consumer Keys and access tokens, used for OAuth
consumer_key = 'WDpZcbcXK6C4RASBaWPn2EsRM'
consumer_secret = 'p2PIw953cXOhfhjeADZUdLeaPnqwlb0DoiEv5ylmSvUqv67lWr'
access_token = '2911455882-iJf4Hs056YOAQc2P5u8aE3bAySFFW67n5SXKb6d'
access_token_secret = '3R1mtgGpMpg13QxVuFfIxoPgpSkVODtVjTQLWSVYt82IL'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# # Creates the user object. The me() method returns the user whose authentication keys were used.
user = api.me()

print('Name:' + user.name)
# print('User Id:' + user.id_str)
print('Location: '+user.location)
print('Geo-Enabled: '+str(user.status.coordinates))
# print('Status: '+user.get_status())
# print('Follows:  '+str(user.friends_count))


for tweet in tweepy.Cursor(api.search,geocode='26.933968699999998,75.9236825,10mi').items(10): 
    text=tweet.text.encode('ascii', errors='ignore')
    id=unicode(str(tweet.id),"utf-8")
    print('Tweet Text: \n'+text.decode('ascii')+'\n')

# for friend in tweepy.Cursor(api.friends).items(10): 
#     print('Id : '+str(friend.id)+' Name : '+friend.screen_name+'\n')
# for i in tweepy.Cursor(api.home_timeline).items(10):
#     print('Retweeted Status :' +str(i.retweeted)+'\n')
#     print('Original User Id : ' + i.user.id_str)
#     text=i.text.encode('ascii', errors='ignore')
#     id=unicode(str(i.id),"utf-8")
#     print('Tweet Text: \n'+text.decode('ascii')+'\n')
#     print('Original User Name : ' + i.user.screen_name)


