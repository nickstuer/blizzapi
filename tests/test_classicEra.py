import getpass
import keyring
from blizzapi import ClassicEraClient  # noqa: E402

class TestClassicEra:
    username = getpass.getuser()
    clientid = keyring.get_password("wow-clientid", username)
    clientsecret = keyring.get_password("wow-clientsecret", username)

    client = ClassicEraClient(client_id=clientid, client_secret=clientsecret)


    def test_character_profile(self):
        result = self.client.character_profile("doomhowl", "thetusk")
        assert result['name'] == "Thetusk"