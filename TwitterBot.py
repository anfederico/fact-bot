from random  import randint
from time    import sleep
from tweepy  import OAuthHandler, API
import giphypop
import requests
import shutil

#import Giphy API
g = giphypop.Giphy()

infile = open('Facts.txt', 'r')
Facts = []
for line in infile:
    Facts.append(line.strip('\n'))
infile.close()

Hashtags = ['#science', '#facts', '#interestingfact', '#hmmm', '#interesting', '#funfact', '#wow', '#braindrop', '#datshitdo', '#mindHasBeenBlown']


# Credentials to access Twitter API
ACCESS_TOKEN    = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
ACCESS_SECRET   = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
CONSUMER_KEY    = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
CONSUMER_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

# Initiate the connection to Twitter API
Auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
Auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
TwitterBot = API(Auth)

outfile = open('Log.txt', 'a')
i = 0
while i < len(Facts):

    #Randomly select a tweet with the OMG tittle
    img = g.screensaver('omg')

    #Download the file
    r = requests.get(img.media_url, stream=True)
    if r.status_code == 200:
        with open('image.gif', 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)

    TwitterBot.update_with_media('image.gif', Facts[i] + ' ' + Hashtags[randint(0,len(Hashtags)-1)])
    outfile.write(str(i)+': '+Facts[i]+'\n') # Keep a log of tweeted facts in case server shuts off
    outfile.flush()
    sleep(randint(3000, 3600)*5) # Tweet every 4-5 hours to prevent bot recognition
    i += 1
