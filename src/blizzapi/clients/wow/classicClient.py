from blizzapi.core.goFetch import dynamic, profile, static
from blizzapi.core.constants import API_BASE_URI, TOKEN_AUTH_URI
from blizzapi.core.enums import Region, Language
from blizzapi.core.oAuth2Client import OAuth2Client
from blizzapi.clients.wow.baseClient import BaseClient

class ClassicClient(BaseClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.namespace_template = '{namespace}-classic-{region}'
        
    ### Character Profile API ###
    @profile("/profile/wow/character/{realmSlug}/{characterName}")
    def character_profile(self, realmSlug:str, characterName:str):
        pass

    @profile("/profile/wow/character/{realmSlug}/{characterName}/status")
    def character_profile_status(self, realmSlug:str, characterName:str):
        pass
