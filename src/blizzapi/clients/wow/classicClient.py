from blizzapi.core.baseClient import BaseClient
from blizzapi.core.fetch import dynamic, profile, static


class ClassicClient(BaseClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.namespace_template = "{namespace}-classic-{region}"

    #########################################
    # Game Data API
    #########################################

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

    ### Creater API ###
    @static("/data/wow/creature-family/index")
    def creature_families_index(self):
        pass

    @static("/data/wow/creature-family/{familyId}")
    def creature_family(self, familyId: int):
        pass

    @static("/data/wow/creature-type/index")
    def creature_types_index(self):
        pass

    @static("/data/wow/creature-type/{typeId}")
    def creature_type(self, typeId: int):
        pass

    @static("/data/wow/creature/{creatureId}")
    def creature(self, creatureId: int):
        pass

    @static("/data/wow/search/creature")
    def creature_search(self, *args, **kwargs):
        pass

    @static("/data/wow/media/creature-display/{creatureDisplayId}")
    def creature_display_media(self, creatureDisplayId: int):
        pass

    @static("/data/wow/media/creature-family/{creatureFamilyId}")
    def creature_family_media(self, creatureFamilyId: int):
        pass

    ### Guild Crest API ###
    @static("/data/wow/guild-crest/index")
    def guild_crest_components_index(self):
        pass

    @static("/data/wow/media/guild-crest/border/{borderId")
    def guild_crest_border_media(self, borderId: int):
        pass

    @static("/data/wow/media/guild-crest/emblem/{emblemId}")
    def guild_crest_emblem_media(self, emblemId: int):
        pass

    ### Item API ###
    @static("/data/wow/item-class/index")
    def item_classes_index(self):
        pass

    @static("/data/wow/item-class/{itemClassId}")
    def item_class(self, itemClassId: int):
        pass

    @static("/data/wow/item-class/{itemClassId}/item-subclass/{itemSubclassId}")
    def item_subclass(self, itemClassId: int, itemSubclassId: int):
        pass

    @static("/data/wow/item/{itemId}")
    def item(self, itemId: int):
        pass

    @static("/data/wow/media/item/{itemId}")
    def item_media(self, itemId: int):
        pass

    @static("/data/wow/search/item")
    def item_search(self, *args, **kwargs):
        pass

    ### Media Search API ###
    @static("/data/wow/search/media")
    def media_search(self, *args, **kwargs):
        pass

    ### Playable Class API ###
    @static("/data/wow/playable-class/index")
    def playable_classes_index(self):
        pass

    @static("/data/wow/playable-class/{classId}")
    def playable_class(self, classId: int):
        pass

    @static("/data/wow/media/playable-class/{playableClassId}")
    def playable_class_media(self, playableClassId: int):
        pass

    ### Playable Race API ###
    @static("/data/wow/playable-race/index")
    def playable_races_index(self):
        pass

    @static("/data/wow/playable-race/{playableRaceId}")
    def playable_race(self, playableRaceId: int):
        pass

    ### Power Type API ###
    @static("/data/wow/power-type/index")
    def power_types_index(self):
        pass

    @static("/data/wow/power-type/{powerTypeId}")
    def power_type(self, powerTypeId: int):
        pass

    ### PvP Season API ###
    @static("/data/wow/pvp-season/index")
    def pvp_seasons_index(self):
        pass

    @static("/data/wow/pvp-season/{pvpSeasonId}")
    def pvp_season(self, pvpSeasonId: int):
        pass

    @static("/data/wow/pvp-region/index")
    def pvp_regions_index(self):
        pass

    @static("/data/wow/pvp-region/{pvpRegionId}/pvp-season/index")
    def pvp_regionional_season_index(self, pvpRegionId: int):
        pass

    @static("/data/wow/pvp-region/{pvpRegionId}/pvp-season/{pvpSeasonId}")
    def pvp_regionional_season(self, pvpRegionId: int, pvpSeasonId: int):
        pass

    @static(
        "/data/wow/pvp-region/{pvpRegionId}/pvp-season/{pvpSeasonId}/pvp-leaderboard/index"
    )
    def pvp_regionional_leaderboard_index(self, pvpRegionId: int, pvpSeasonId: int):
        pass

    @static(
        "/data/wow/pvp-region/{pvpRegionId}/pvp-season/{pvpSeasonId}/pvp-leaderboard/{pvpBracket}"
    )
    def pvp_leaderboard(self, pvpRegionId: int, pvpSeasonId: int, pvpBracket: str):
        pass

    @static(
        "/data/wow/pvp-region/{pvpRegionId}/pvp-season/{pvpSeasonId}/pvp-reward/index"
    )
    def pvp_rewards_index(self, pvpRegionId: int, pvpSeasonId: int):
        pass

    ### Realm API ###
    @static("/data/wow/realm/index")
    def realms_index(self):
        pass

    @static("/data/wow/realm/{realmSlug}")
    def realm(self, realmSlug: str):
        pass

    @static("/data/wow/search/realm")
    def realm_search(self, *args, **kwargs):
        pass

    ### Region API ###
    @static("/data/wow/region/index")
    def regions_index(self):
        pass

    @static("/data/wow/region/{regionId}")
    def region(self, regionId: int):
        pass

    @static("/data/wow/token/index")  # CN only
    def wow_token_index(self):
        pass

    #########################################
    # Profile API
    #########################################

    ### Account Profile API ###
    @profile("/profile/user/wow")
    def account_profile(self):
        pass

    @profile("/profile/user/wow/protected-character/{realmId}-{characterId}")
    def protected_character_profile_summary(self, realmId: int, characterId: int):
        pass

    ### Character Profile API ###
    @profile("/profile/wow/character/{realmSlug}/{characterName}")
    def character_profile(self, realmSlug: str, characterName: str):
        pass

    @profile("/profile/wow/character/{realmSlug}/{characterName}/status")
    def character_profile_status(self, realmSlug: str, characterName: str):
        pass

    ### Character Apperance API ###
    @profile("/profile/wow/character/{realmSlug}/{characterName}/appearance")
    def character_appearance(self, realmSlug: str, characterName: str):
        pass

    ### Character Equipment API ###
    @profile("/profile/wow/character/{realmSlug}/{characterName}/equipment")
    def character_equipment(self, realmSlug: str, characterName: str):
        pass

    ### Character Hunter Pets API ###
    @profile("/profile/wow/character/{realmSlug}/{characterName}/hunter-pets")
    def character_hunter_pets(self, realmSlug: str, characterName: str):
        pass

    ### Character Media API ###
    @profile("/profile/wow/character/{realmSlug}/{characterName}/character-media")
    def character_media(self, realmSlug: str, characterName: str):
        pass

    ### Character PvP API ###
    @profile(
        "/profile/wow/character/{realmSlug}/{characterName}/pvp-bracket/{pvpBracket}"
    )
    def character_pvp_bracket_statistics(
        self, realmSlug: str, characterName: str, pvpBracket: str
    ):
        pass

    @profile("/profile/wow/character/{realmSlug}/{characterName}/pvp-summary")
    def character_pvp_summary(self, realmSlug: str, characterName: str):
        pass

    ### Character Specializations API ###
    @profile("/profile/wow/character/{realmSlug}/{characterName}/specializations")
    def character_specializations_summary(self, realmSlug: str, characterName: str):
        pass

    ### Character Statistics API ###
    @profile("/profile/wow/character/{realmSlug}/{characterName}/statistics")
    def character_statistics_summary(self, realmSlug: str, characterName: str):
        pass

    ### Character Achievements API ###
    @profile("/profile/wow/character/{realmSlug}/{characterName}/achievements")
    def character_achievements_summary(self, realmSlug: str, characterName: str):
        pass

    @profile(
        "/profile/wow/character/{realmSlug}/{characterName}/achievements/statistics"
    )
    def character_achievements_statistics(self, realmSlug: str, characterName: str):
        pass

    ### Guild API ###
    @profile("/data/wow/guild/{realmSlug}/{nameSlug}")
    def guild(self, realmSlug: str, nameSlug: str):
        pass

    @profile("/data/wow/guild/{realmSlug}/{nameSlug}/activity")
    def guild_activity(self, realmSlug: str, nameSlug: str):
        pass

    @profile("/data/wow/guild/{realmSlug}/{nameSlug}/achievements")
    def guild_achievements(self, realmSlug: str, nameSlug: str):
        pass

    @profile("/data/wow/guild/{realmSlug}/{nameSlug}/roster")
    def guild_roster(self, realmSlug: str, nameSlug: str):
        pass
