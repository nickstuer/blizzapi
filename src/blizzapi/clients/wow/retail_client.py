from blizzapi.core.base_client import BaseClient
from blizzapi.core.fetch import dynamic, profile, static


class RetailClient(BaseClient):
    def __init__(self, *args: tuple, **kwargs: dict):
        super().__init__(*args, **kwargs)
        self.namespace_template = "{namespace}-{region}"

    #########################################
    # Game Data API
    #########################################

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

    ### Auction House API ###
    @dynamic("/data/wow/connected-realm/{connectedRealmId}/auctions")
    def auctions(self, connectedRealmId: int):
        pass

    @dynamic("/data/wow/auctions/commodities")
    def commodities(self):
        pass

    ### Azerite Essences API ###
    @static("/data/wow/azerite-essence/index")
    def azerite_essences_index(self):
        pass

    @static("/data/wow/azerite-essence/{azeriteEssenceId}")
    def azerite_essence(self, azeriteEssenceId: int):
        pass

    @static("/data/wow/search/azerite-essence")
    def azerite_essence_search(self, *args, **kwargs):
        pass

    @static("/data/wow/media/azerite-essence/{azeriteEssenceId}")
    def azerite_essence_media(self, azeriteEssenceId: int):
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

    ### Covenant API ###
    @static("/data/wow/covenant/index")
    def covenant_index(self):
        pass

    @static("/data/wow/covenant/{covenantId}")
    def covenant(self, covenantId: int):
        pass

    @static("/data/wow/media/covenant/{covenantId}")
    def covenant_media(self, covenantId: int):
        pass

    @static("/data/wow/covenant/soulbind/index")
    def soulbind_index(self):
        pass

    @static("/data/wow/covenant/soulbind/{soulbindId}")
    def soulbind(self, soulbindId: int):
        pass

    @static("/data/wow/covenant/conduit/index")
    def conduit_index(self):
        pass

    @static("/data/wow/covenant/conduit/{conduitId}")
    def conduit(self, conduitId: int):
        pass

    ### Creater API ###
    @static("/data/wow/creature/{creatureId}")
    def creature(self, creatureId: int):
        pass

    @static("/data/wow/search/creature")
    def creature_search(self, *args, **kwargs):
        pass

    @static("/data/wow/media/creature-display/{creatureDisplayId}")
    def creature_display_media(self, creatureDisplayId: int):
        pass

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

    ### Heirloom API ###
    @static("/data/wow/heirloom/index")
    def heirloom_index(self):
        pass

    @static("/data/wow/heirloom/{heirloomId}")
    def heirloom(self, heirloomId: int):
        pass

    ### Item API ###
    @static("/data/wow/item/{itemId}")
    def item(self, itemId: int):
        pass

    @static("/data/wow/search/item")
    def item_search(self, *args, **kwargs):
        pass

    @static("/data/wow/media/item/{itemId}")
    def item_media(self, itemId: int):
        pass

    @static("/data/wow/item-class/index")
    def item_classes_index(self):
        pass

    @static("/data/wow/item-class/{itemClassId}")
    def item_class(self, itemClassId: int):
        pass

    @static("/data/wow/item-set/index")
    def item_sets_index(self):
        pass

    @static("/data/wow/item-set/{itemSetId}")
    def item_set(self, itemSetId: int):
        pass

    @static("/data/wow/item-class/{itemClassId}/item-subclass/{itemSubclassId}")
    def item_subclass(self, itemClassId: int, itemSubclassId: int):
        pass

    ### Item Appereance API ###
    @static("/data/wow/item-appearance/{appearanceId}")
    def item_appearance(self, appearanceId: int):
        pass

    @static("/data/wow/search/item-appearance")
    def item_appearance_search(self, *args, **kwargs):
        pass

    @static("/data/wow/item-appearance/set/index")
    def item_appearance_set_index(self):
        pass

    @static("/data/wow/item-appearance/set/{appearanceSetId}")
    def item_appearance_set(self, appearanceSetId: int):
        pass

    @static("/data/wow/item-appearance/slot/index")
    def item_appearance_slot_index(self):
        pass

    @static("/data/wow/item-appearance/slot/{slotType}")
    def item_appearance_slot(self, slotType: str):
        pass

    ### Journal API ###
    @static("/data/wow/journal-expansion/index")
    def journal_expansion_index(self):
        pass

    @static("/data/wow/journal-expansion/{journalExpansionId}")
    def journal_expansion(self, journalExpansionId: int):
        pass

    @static("/data/wow/journal-encounter/index")
    def journal_encounter_index(self):
        pass

    @static("/data/wow/journal-encounter/{journalEncounterId}")
    def journal_encounter(self, journalEncounterId: int):
        pass

    @static("/data/wow/search/journal-encounter")
    def journal_encounter_search(self, *args, **kwargs):
        pass

    @static("/data/wow/journal-instance/index")
    def journal_instance_index(self):
        pass

    @static("/data/wow/journal-instance/{journalInstanceId}")
    def journal_instance(self, journalInstanceId: int):
        pass

    @static("/data/wow/media/journal-instance/{journalInstanceId}")
    def journal_instance_media(self, journalInstanceId: int):
        pass

    ### Media Search API ###
    @static("/data/wow/search/media")
    def media_search(self, *args, **kwargs):
        pass

    ### Modified Crafting API ###
    @static("/data/wow/modified-crafting/index")
    def modified_crafting_index(self):
        pass

    @static("/data/wow/modified-crafting/category/index")
    def modified_crafting_category_index(self):
        pass

    @static("/data/wow/modified-crafting/category/{categoryId}")
    def modified_crafting_category(self, categoryId: int):
        pass

    @static("/data/wow/modified-crafting/reagent-slot-type/index")
    def modified_crafting_reagent_slot_type_index(self):
        pass

    @static("/data/wow/modified-crafting/reagent-slot-type/{slotTypeId}")
    def modified_crafting_reagent_slot_type(self, slotTypeId: int):
        pass

    ### Mounts API ###
    @static("/data/wow/mount/index")
    def mount_index(self):
        pass

    @static("/data/wow/mount/{mountId}")
    def mount(self, mountId: int):
        pass

    @static("/data/wow/search/mount")
    def mount_search(self, *args, **kwargs):
        pass

    ### Mythic Keystone Affix API ###
    @static("/data/wow/keystone-affix/index")
    def mythic_keystone_affixes_index(self):
        pass

    @static("/data/wow/keystone-affix/{keystoneAffixId}")
    def mythic_keystone_affix(self, keystoneAffixId: int):
        pass

    @static("/data/wow/media/keystone-affix/{keystoneAffixId}")
    def mythic_keystone_affix_media(self, keystoneAffixId: int):
        pass

    ### Mythic Keystone Dungeon API ###
    @dynamic("/data/wow/mythic-keystone/index")
    def mythic_keystone_index(self):
        pass

    @dynamic("/data/wow/mythic-keystone/dungeon/index")
    def mythic_keystone_dungeon_index(self):
        pass

    @dynamic("/data/wow/mythic-keystone/dungeon/{dungeonId}")
    def mythic_keystone_dungeon(self, dungeonId: int):
        pass

    @dynamic("/data/wow/mythic-keystone/period/index")
    def mythic_keystone_periods_index(self):
        pass

    @dynamic("/data/wow/mythic-keystone/period/{periodId}")
    def mythic_keystone_period(self, periodId: int):
        pass

    @dynamic("/data/wow/mythic-keystone/season/index")
    def mythic_keystone_season_index(self):
        pass

    @dynamic("/data/wow/mythic-keystone/season/{seasonId}")
    def mythic_keystone_season(self, seasonId: int):
        pass

    ### Mythic Keystone Leaderboard API ###
    @dynamic("/data/wow/connected-realm/{connectedRealmId}/mythic-leaderboard/index")
    def mythic_keystone_leaderboard_index(self, connectedRealmId: int):
        pass

    @dynamic("/data/wow/connected-realm/{connectedRealmId}/mythic-leaderboard/{dungeonId}/period/{period}")
    def mythic_keystone_leaderboard(self, connectedRealmId: int, dungeonId: int, period: int):
        pass

    ### Mythic Raid Leaderboard API ###
    @dynamic("/data/wow/leaderboard/hall-of-fame/{raid}/{faction}")
    def mythic_raid_leaderboard(self, raid: str, faction: str):
        pass

    ### Pet API ###
    @static("/data/wow/pet/index")
    def pets_index(self):
        pass

    @static("/data/wow/pet/{petId}")
    def pet(self, petId: int):
        pass

    @static("/data/wow/media/pet/{petId}")
    def pet_media(self, petId: int):
        pass

    @static("/data/wow/pet-ability/index")
    def pet_abilities_index(self):
        pass

    @static("/data/wow/pet-ability/{petAbilityId}")
    def pet_ability(self, petAbilityId: int):
        pass

    @static("/data/wow/media/pet-ability/{petAbilityId}")
    def pet_ability_media(self, petAbilityId: int):
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

    @static("/data/wow/playable-class/{classId}/pvp-talent-slots")
    def pvp_talent_slots(self, classId: int):
        pass

    ### Playable Race API ###
    @static("/data/wow/playable-race/index")
    def playable_races_index(self):
        pass

    @static("/data/wow/playable-race/{playableRaceId}")
    def playable_race(self, playableRaceId: int):
        pass

    ### Playable Specialization API ###
    @static("/data/wow/playable-specialization/index")
    def playable_specializations_index(self):
        pass

    @static("/data/wow/playable-specialization/{specId}")
    def playable_specialization(self, specId: int):
        pass

    @static("/data/wow/media/playable-specialization/{specId}")
    def playable_specialization_media(self, specId: int):
        pass

    ### Power Type API ###
    @static("/data/wow/power-type/index")
    def power_types_index(self):
        pass

    @static("/data/wow/power-type/{powerTypeId}")
    def power_type(self, powerTypeId: int):
        pass

    ### Profession API ###
    @static("/data/wow/profession/index")
    def professions_index(self):
        pass

    @static("/data/wow/profession/{professionId}")
    def profession(self, professionId: int):
        pass

    @static("/data/wow/media/profession/{professionId}'")
    def profession_media(self, professionId: int):
        pass

    @static("/data/wow/profession/{professionId}/skill-tier/{skillTierId}")
    def profession_skill_tier(self, professionId: int, skillTierId: int):
        pass

    @static("/data/wow/recipe/{recipeId}")
    def recipe(self, recipeId: int):
        pass

    @static("/data/wow/media/recipe/{recipeId}")
    def recipe_media(self, recipeId: int):
        pass

    ### PvP Season API ###
    @static("/data/wow/pvp-season/index")
    def pvp_seasons_index(self):
        pass

    @static("/data/wow/pvp-season/{pvpSeasonId}")
    def pvp_season(self, pvpSeasonId: int):
        pass

    @static("/data/wow/pvp-season/{pvpSeasonId}/pvp-leaderboard/index")
    def pvp_leaderboards_index(self, pvpRegionId: int, pvpSeasonId: int):
        pass

    @static("/data/wow/pvp-season/{pvpSeasonId}/pvp-leaderboard/{pvpBracket}")
    def pvp_leaderboard(self, pvpRegionId: int, pvpSeasonId: int, pvpBracket: str):
        pass

    @static("/data/wow/pvp-season/{pvpSeasonId}/pvp-reward/index")
    def pvp_rewards_index(self, pvpRegionId: int, pvpSeasonId: int):
        pass

    ### PvP Tier API ###
    @static("/data/wow/pvp-tier/index")
    def pvp_tiers_index(self):
        pass

    @static("/data/wow/pvp-tier/{pvpTierId}")
    def pvp_tier(self, pvpTierId: int):
        pass

    @static("/data/wow/media/pvp-tier/{pvpTierId}")
    def pvp_tier_media(self, pvpTierId: int):
        pass

    # Quest API ###
    @static("/data/wow/quest/index")
    def quest_index(self):
        pass

    @static("/data/wow/quest/{questId}")
    def quest(self, questId: int):
        pass

    @static("/data/wow/quest/category/index")
    def quest_category_index(self):
        pass

    @static("/data/wow/quest/category/{questCategoryId}")
    def quest_category(self, questCategoryId: int):
        pass

    @static("/data/wow/quest/area/index")
    def quest_area_index(self):
        pass

    @static("/data/wow/quest/area/{questAreaId}")
    def quest_area(self, questAreaId: int):
        pass

    @static("/data/wow/quest/type/index")
    def quest_types_index(self):
        pass

    @static("/data/wow/quest/type/{questTypeId}")
    def quest_type(self, questTypeId: int):
        pass

    ### Realm API ###
    @dynamic("/data/wow/realm/index")
    def realms_index(self):
        pass

    @dynamic("/data/wow/realm/{realmSlug}")
    def realm(self, realmSlug: str):
        pass

    @dynamic("/data/wow/search/realm")
    def realm_search(self, *args, **kwargs):
        pass

    ### Recipe API ###
    @dynamic("/data/wow/region/index")
    def regions_index(self):
        pass

    @dynamic("/data/wow/region/{regionId}")
    def region(self, regionId: int):
        pass

    ### Reputation API ###
    @static("/data/wow/reputation-faction/index")
    def reputation_factions_index(self):
        pass

    @static("/data/wow/reputation-faction/{reputationFactionId}")
    def reputation_faction(self, reputationFactionId: int):
        pass

    @static("/data/wow/reputation-tiers/index")
    def reputation_tiers_index(self):
        pass

    @static("/data/wow/reputation-tiers/{reputationTiersId}")
    def reputation_tiers(self, reputationTiersId: int):
        pass

    ### Spell API ###
    @static("/data/wow/spell/{spellId}")
    def spell(self, spellId: int):
        pass

    @static("/data/wow/media/spell/{spellId}")
    def spell_media(self, spellId: int):
        pass

    @static("/data/wow/search/spell")
    def spell_search(self, *args, **kwargs):
        pass

    ### Talent API ###
    @static("/data/wow/talent-tree/index")
    def talent_tree_index(self):
        pass

    @static("/data/wow/talent-tree/{talentTreeId}/playable-specialization/{specId}")
    def talent_tree(self, talentTreeId: int, specId: int):
        pass

    @static("/data/wow/talent-tree/{talentTreeId}")
    def talent_tree_nodes(self, talentTreeId: int):
        pass

    @static("/data/wow/talent/index")
    def talents_index(self):
        pass

    @static("/data/wow/talent/{talentId}")
    def talent(self, talentId: int):
        pass

    @static("/data/wow/pvp-talent/index")
    def pvp_talents_index(self):
        pass

    @static("/data/wow/pvp-talent/{pvpTalentId")
    def pvp_talent(self, pvpTalentId: int):
        pass

    ### Tech Talent API ###
    @static("/data/wow/tech-talent-tree/index")
    def tech_talent_tree_index(self):
        pass

    @static("/data/wow/tech-talent-tree/{techTalentTreeId}")
    def tech_talent_tree(self, techTalentTreeId: int):
        pass

    @static("/data/wow/tech-talent/index")
    def tech_talents_index(self):
        pass

    @static("/data/wow/tech-talent/{techTalentId}")
    def tech_talent(self, techTalentId: int):
        pass

    @static("/data/wow/media/tech-talent/{techTalentId}")
    def tech_talent_media(self, techTalentId: int):
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

    #########################################
    # Profile API
    #########################################

    ### Account Profile API ###
    @profile("/profile/user/wow")
    def account_profile_summary(self):
        pass

    @profile("/profile/user/wow/protected-character/{realmId}-{characterId}")
    def protected_character_profile_summary(self, realmId: int, characterId: int):
        pass

    @profile("/profile/user/wow/collections")
    def account_collections_index(self):
        pass

    @profile("/profile/user/wow/collections/heirlooms")
    def account_heirlooms_collection_summary(self):
        pass

    @profile("/profile/user/wow/collections/mounts")
    def account_mounts_collection_summary(self):
        pass

    @profile("/profile/user/wow/collections/pets")
    def account_pets_collection_summary(self):
        pass

    @profile("/profile/user/wow/collections/toys")
    def account_toys_collection_summary(self):
        pass

    @profile("/profile/user/wow/collections/transmogs")
    def account_transmogs_collection_summary(self):
        pass

    ### Character Achievements API ###
    @profile("/profile/wow/character/{realmSlug}/{characterName}/achievements")
    def character_achievements_summary(self, realmSlug: str, characterName: str):
        pass

    @profile("/profile/wow/character/{realmSlug}/{characterName}/achievements/statistics")
    def character_achievements_statistics(self, realmSlug: str, characterName: str):
        pass

    ### Character Apperance API ###
    @profile("/profile/wow/character/{realmSlug}/{characterName}/appearance")
    def character_appearance_summary(self, realmSlug: str, characterName: str):
        pass

    ### Character Collections API ###
    @profile("/profile/wow/character/{realmSlug}/{characterName}/collections")
    def character_collections_index(self, realmSlug: str, characterName: str):
        pass

    @profile("/profile/wow/character/{realmSlug}/{characterName}/collections/heirlooms")
    def character_heirlooms_collection_summary(self, realmSlug: str, characterName: str):
        pass

    @profile("/profile/wow/character/{realmSlug}/{characterName}/collections/mounts")
    def character_mounts_collection_summary(self, realmSlug: str, characterName: str):
        pass

    @profile("/profile/wow/character/{realmSlug}/{characterName}/collections/pets")
    def character_pets_collection_summary(self, realmSlug: str, characterName: str):
        pass

    @profile("/profile/wow/character/{realmSlug}/{characterName}/collections/toys")
    def character_toys_collection_summary(self, realmSlug: str, characterName: str):
        pass

    @profile("/profile/wow/character/{realmSlug}/{characterName}/collections/transmogs")
    def character_transmogs_collection_summary(self, realmSlug: str, characterName: str):
        pass

    ### Character Encounters API ###
    @profile("/profile/wow/character/{realmSlug}/{characterName}/encounters")
    def character_encounters_summary(self, realmSlug: str, characterName: str):
        pass

    @profile("/profile/wow/character/{realmSlug}/{characterName}/encounters/dungeons")
    def character_dungeons(self, realmSlug: str, characterName: str):
        pass

    @profile("/profile/wow/character/{realmSlug}/{characterName}/encounters/raids")
    def character_raids(self, realmSlug: str, characterName: str):
        pass

    ### Character Equipment API ###
    @profile("/profile/wow/character/{realmSlug}/{characterName}/equipment")
    def character_equipment_summary(self, realmSlug: str, characterName: str):
        pass

    ### Character Hunter Pets API ###
    @profile("/profile/wow/character/{realmSlug}/{characterName}/hunter-pets")
    def character_hunter_pets(self, realmSlug: str, characterName: str):
        pass

    ### Character Media API ###
    @profile("/profile/wow/character/{realmSlug}/{characterName}/character-media")
    def character_media(self, realmSlug: str, characterName: str):
        pass

    ### Character Mythic Keystone Profile API ###
    @profile("/profile/wow/character/{realmSlug}/{characterName}/mythic-keystone-profile")
    def character_mythic_keystone_profile_index(self, realmSlug: str, characterName: str):
        pass

    @profile("/profile/wow/character/{realmSlug}/{characterName}/mythic-keystone-profile/season/{seasonId}")
    def character_mythic_keystone_season_details(self, realmSlug: str, characterName: str, seasonId: int):
        pass

    ### Character Profession API ###
    @profile("/profile/wow/character/{realmSlug}/{characterName}/professions")
    def character_professions_summary(self, realmSlug: str, characterName: str):
        pass

    ### Character Profile API ###
    @profile("/profile/wow/character/{realmSlug}/{characterName}")
    def character_profile_summary(self, realmSlug: str, characterName: str):
        pass

    @profile("/profile/wow/character/{realmSlug}/{characterName}/status")
    def character_profile_status(self, realmSlug: str, characterName: str):
        pass

    ### Character PvP API ###
    @profile("/profile/wow/character/{realmSlug}/{characterName}/pvp-bracket/{pvpBracket}")
    def character_pvp_bracket_statistics(self, realmSlug: str, characterName: str, pvpBracket: str):
        pass

    @profile("/profile/wow/character/{realmSlug}/{characterName}/pvp-summary")
    def character_pvp_summary(self, realmSlug: str, characterName: str):
        pass

    ### Character Quests API ###
    @profile("/profile/wow/character/{realmSlug}/{characterName}/quests")
    def character_quests(self, realmSlug: str, characterName: str):
        pass

    @profile("/profile/wow/character/{realmSlug}/{characterName}/quests/completed")
    def character_completed_quests(self, realmSlug: str, characterName: str):
        pass

    ### Character Reputations API ###
    @profile("/profile/wow/character/{realmSlug}/{characterName}/reputations")
    def character_reputations_summary(self, realmSlug: str, characterName: str):
        pass

    ### Character Soulbinds API ###
    @profile("/profile/wow/character/{realmSlug}/{characterName}/soulbinds")
    def character_soulbinds(self, realmSlug: str, characterName: str):
        pass

    ### Character Specialization API ###
    @profile("/profile/wow/character/{realmSlug}/{characterName}/specializations")
    def character_specializations_summary(self, realmSlug: str, characterName: str):
        pass

    @profile("/profile/wow/character/{realmSlug}/{characterName}/statistics")
    def character_statistics_summary(self, realmSlug: str, characterName: str):
        pass

    ### Character Titles API ###
    @profile("/profile/wow/character/{realmSlug}/{characterName}/titles")
    def character_titles(self, realmSlug: str, characterName: str):
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
