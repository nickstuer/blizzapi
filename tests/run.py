import getpass
import keyring
from pprint import pprint
import sys
import os

# Add the 'src' folder to the folder path to import (since we are in /tests)
testdir = os.path.dirname(__file__)
srcdir = '../src'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

import blizzapi as blizz

username = getpass.getuser()
clientid = keyring.get_password('wow-clientid', username)
clientsecret = keyring.get_password('wow-clientsecret', username)

if not clientid or not clientsecret:
    print('Please enter your client id and client secret')
    clientid = input('Client id: ')
    clientsecret = getpass.getpass('Client secret: ')
    keyring.set_password('wow-clientid', username, clientid)
    keyring.set_password('wow-clientsecret', username, clientsecret)

client = blizz.ClassicEraClient(client_id=clientid, client_secret=clientsecret)

#pprint(client.character_profile('eredar', 'toilet'))
#pprint(client.character_profile('doomhowl', 'realrat'))
#pprint(client.wow_token_index())
#pprint(client.achievements_index())


result = client.connected_realm_search(fields = {'status.type': 'DOWN'})
pprint(result)