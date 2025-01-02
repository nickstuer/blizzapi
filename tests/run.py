import os
import sys
from pprint import pprint
import getpass
import keyring

# Add the 'src' folder to the folder path to import (since we are in /tests)
testdir = os.path.dirname(__file__)
srcdir = "../src"
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

from blizzapi import ClassicEraClient

username = getpass.getuser()
clientid = keyring.get_password("wow-clientid", username)
clientsecret = keyring.get_password("wow-clientsecret", username)

if not clientid or not clientsecret:
    print("Please enter your client id and client secret")
    clientid = input("Client id: ")
    clientsecret = getpass.getpass("Client secret: ")
    keyring.set_password("wow-clientid", username, clientid)
    keyring.set_password("wow-clientsecret", username, clientsecret)

client = ClassicEraClient(client_id=clientid, client_secret=clientsecret)

#result = client.wow_token_index()
#result = client.achievements_index()

result = client.character_profile('doomhowl', 'thetusk')
pprint(result)

#result = client.guild_roster('doomhowl', 'onlyfangs') # Guild API is currently broken on Blizzard's end
#pprint(result)

result = client.connected_realm_search(fields={"status.type": "DOWN"})
pprint(result)
