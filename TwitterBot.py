from random  import randint
from time    import sleep
from tweepy  import OAuthHandler, API

infile = open('Facts.txt', 'r')
Facts = []
for line in infile:
    Facts.append(line.strip('\n'))
infile.close()

Hashtags = ['#science', '#facts', '#interestingfact', '#hmmm', '#follow', '#interesting', '#factoid', '#funfact', '#wow', '#braindrop']

#Credentials to access Twitter API 
ACCESS_TOKEN    = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
ACCESS_SECRET   = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
CONSUMER_KEY    = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
CONSUMER_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

#Initiate the connection to Twitter API
Auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
Auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
TwitterBot = API(Auth)

outfile = open('Log.txt', 'w')
i = 1
while i < len(Facts):
    TwitterBot.update_status(Facts[i]+' '+Hashtags[randint(0,len(Hashtags)-1)]) # Tweet a fact as well as a random hashtag
    outfile.write(str(i)+': '+Facts[i]) # Keep a log of tweeted facts in case server shuts off
    sleep(randint(3000, 3600)*5) # Tweet every 4-5 hours to prevent bot recognition
    i += 1
