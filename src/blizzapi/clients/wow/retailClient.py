from blizzapi.core.baseClient import BaseClient
from blizzapi.core.fetch import dynamic, profile, static


class RetailClient(BaseClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.namespace_template = "{namespace}-{region}"

    ### Achievements API ###
    @static("/data/wow/achievement/index")
    def achievements_index(self):
        pass

    @static("/data/wow/achievement/{achievementId}")
    def achievement(self, achievementId: int):
        pass

    @static("/data/wow/media/achievement/{achievementId}")
    def achievement_media(self, achievementId: int):
        pass

    @static("/data/wow/achievement-category/index")
    def achievement_categories_index(self):
        pass

    @static("/data/wow/achievement-category/{achievementCategoryId}")
    def achievement_category(self, achievementCategoryId: int):
        pass

    ### Titles API ###
    @static("/data/wow/title/index")
    def title_index(self):
        pass

    @static("/data/wow/title/{titleId}")
    def title(self, titleId: int):
        pass

    ### Toys API ###
    @static("/data/wow/toy/index")
    def toy_index(self):
        pass

    @static("/data/wow/toy/{toyId}")
    def toy(self, toyId: int):
        pass

    ### WoW Token API ###
    @dynamic("/data/wow/token/index")
    def wow_token_index(self):
        pass

    # @profile("/profile/wow/character/{realmSlug}/{characterName}")
    # def character_profile(self, realmSlug:str, characterName:str):
    #    pass

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

    @profile("/profile/wow/character/{realmSlug}/{characterName}/achievements")
    def character_achievements_summary(self, realmSlug: str, characterName: str):
        pass

    @profile("/profile/wow/character/{realmSlug}/{characterName}")
    def character_profile(self, realmSlug: str, characterName: str):
        pass

    ### Character Mythic Keystone Profile API ###
    @profile("/profile/wow/character/{realmSlug}/{characterName}/mythic-keystone-profile")
    def character_mythic_keystone_profile_index(self, realmSlug: str, characterName: str):
        pass

    @profile("/profile/wow/character/{realmSlug}/{characterName}/mythic-keystone-profile/season/{seasonId}")
    def character_mythic_keystone_season_details(self, realmSlug: str, characterName: str, seasonId: int):
        pass

    ### Character Media API ###
    @profile("/profile/wow/character/{realmSlug}/{characterName}/character-media")
    def character_media(self, realmSlug: str, characterName: str):
        pass
