'''
@author: Crystal Cheung
@date: 8.18.14
'''

import json
import requests
import sys

def main():
  if len(sys.argv) < 2:
    print 'wrong number of args'
    sys.exit(1)

  user = sys.argv[1]
  getFollows(user)

  # get access token using authlink
  # this too hard
  #authlink = 'https://api.twitch.tv/kraken/oauth2/authorize?response_type=token&client_id=ikvb89ckyvspox2yhu2umowprnbu1p3&redirect_uri=http://localhost&scope=user_follows_edit'

  #auth = requests.get(authlink, allow_redirects=True)
  #print auth.history[0].headers
  #hdr = auth.headers
  #print hdr

def getFollows(user):
  channels = []

  lnk = 'https://api.twitch.tv/kraken/users/' + user + '/follows/channels'
  # get list containing data for each channel followed
  followList = requests.get(lnk).json()['follows']
  for name in followList:
    channels.append(name["channel"]["display_name"])
  # display name for each channel, aka broadcasting user
  for displayName in channels:
    link = 'https://api.twitch.tv/kraken/streams/' + displayName
    #print link
    resp = requests.get(link)
    if resp.json()['stream'] == None:
      print displayName + ' is offline'
    # user is online
    else:
      print displayName + ' is online'


main()
