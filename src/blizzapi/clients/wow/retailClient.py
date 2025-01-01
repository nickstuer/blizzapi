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
