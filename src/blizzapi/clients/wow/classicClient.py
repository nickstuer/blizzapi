from blizzapi.core.fetch import dynamic, profile, static
from blizzapi.core.baseClient import BaseClient


class ClassicClient(BaseClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.namespace_template = "{namespace}-classic-{region}"

    ### Action House API ###
    @dynamic("/data/wow/connected-realm/{connectedRealmId}/auctions/index")
    def auction_house_index(self, connectedRealmId: int):
        pass

    @dynamic("/data/wow/connected-realm/{connectedRealmId}/auctions/{auctionHouseId}")
    def auctions(self, connectedRealmId: int, auctionHouseId: int):
        pass

    ### Connected Realm API ###
    @dynamic("/data/wow/connected-realm/index")
    def connected_realms_index(self):
        pass

    @dynamic("/data/wow/connected-realm/{connectedRealmId}")
    def connected_realm(self, connectedRealmId: int):
        pass

    @dynamic("/data/wow/search/connected-realm")
    def connected_realm_search(self, *args, **kwargs):
        pass

    ### Character Profile API ###
    @profile("/profile/wow/character/{realmSlug}/{characterName}")
    def character_profile(self, realmSlug: str, characterName: str):
        pass

    @profile("/profile/wow/character/{realmSlug}/{characterName}/status")
    def character_profile_status(self, realmSlug: str, characterName: str):
        pass
