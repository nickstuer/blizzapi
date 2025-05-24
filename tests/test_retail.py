import getpass
import keyring
from blizzapi import RetailClient  # noqa: E402
from pprint import pprint

class TestRetail:
    username = getpass.getuser()
    clientid = keyring.get_password("wow-clientid", username)
    clientsecret = keyring.get_password("wow-clientsecret", username)

    client = RetailClient(client_id=clientid, client_secret=clientsecret)


    def test_character_profile(self):
        result = self.client.character_profile("eredar", "toilet")
        assert result['name'] == "Toilet"

    def test_character_achievements_summary(self):
        result = self.client.character_achievements_summary("eredar", "toilet")
        #assert result['name'] == "Toilet"
        #pprint(result['achievements'])

        achvs = result['achievements']

        visit1 = False
        visit2 = False
        for ach in achvs:
            if ach['id'] == 40984:
                visit1 = True
                name = ach['achievement']['name']
                assert name == "Big Fan"
                assert ach['completed_timestamp'] == 1730161080000

            if ach['id'] == 41130:
                visit2 = True
                name = ach['achievement']['name']
                assert name == "Elders of Khaz Algar"
                assert ach['criteria']['is_completed'] == False


        assert visit1 == True
        assert visit2 == True

    def test_achievement_media(self):
        result = self.client.achievement_media(20597)
       
        pprint(result)

        assert result['id'] == 20597
        assert result['assets'][0]['file_data_id'] == 571554
        assert result['assets'][0]['value'] == "https://render.worldofwarcraft.com/us/icons/56/ability_paladin_blindinglight2.jpg"   

