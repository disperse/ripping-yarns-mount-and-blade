from header_game_menus import *
from header_parties import *
from header_items import *
from header_mission_templates import *
from header_music import *
from header_terrain_types import *

from module_constants import *

####################################################################################################################
#  (menu-id, menu-flags, menu_text, mesh-name, [<operations>], [<options>]),
#
#   Each game menu is a tuple that contains the following fields:
#  
#  1) Game-menu id (string): used for referencing game-menus in other files.
#     The prefix menu_ is automatically added before each game-menu-id
#
#  2) Game-menu flags (int). See header_game_menus.py for a list of available flags.
#     You can also specify menu text color here, with the menu_text_color macro
#  3) Game-menu text (string).
#  4) mesh-name (string). Not currently used. Must be the string "none"
#  5) Operations block (list). A list of operations. See header_operations.py for reference.
#     The operations block is executed when the game menu is activated.
#  6) List of Menu options (List).
#     Each menu-option record is a tuple containing the following fields:
#   6.1) Menu-option-id (string) used for referencing game-menus in other files.
#        The prefix mno_ is automatically added before each menu-option.
#   6.2) Conditions block (list). This must be a valid operation block. See header_operations.py for reference. 
#        The conditions are executed for each menu option to decide whether the option will be shown to the player or not.
#   6.3) Menu-option text (string).
#   6.4) Consequences block (list). This must be a valid operation block. See header_operations.py for reference. 
#        The consequences are executed for the menu option that has been selected by the player.
#
#
# Note: The first Menu is the initial character creation menu.
####################################################################################################################

game_menus = [
  ("start_game_0",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "Welcome, adventurer, to Mount and Blade: Warband. Before beginning the game you must create your character. Remember that in the traditional medieval society depicted in the game, war and politics are usually dominated by male members of the nobility. That does not however mean that you should not choose to play a female character, or one who is not of noble birth. Male nobles may have a somewhat easier start, but women and commoners can attain all of the same goals -- and in fact may have a much more interesting if more challenging early game.",
    "none",
    [],
    [
     ("continue",[],"Continue...",

      #[(change_screen_map)],
      [(change_screen_return, 0)],
       # [(jump_to_menu, "mnu_start_game_1"),
       #  ]
       ),
      ("go_back",[],"Go back",
       [
         (change_screen_quit),
       ]),
    ]
  ),

#   ("start_phase_2",mnf_disable_all_keys,
#     "You hear about Calradia, a land torn between rival kingdoms battling each other for supremacy,\
#  a haven for knights and mercenaries,  cutthroats and adventurers, all willing to risk their lives in pursuit of fortune, power, or glory...\
#  In this land which holds great dangers and even greater opportunities, you believe you may leave your past behind and start a new life.\
#  You feel that finally, you hold the key of your destiny in your hands, free to choose as you will,\
#  and that whatever course you take, great adventures will await you. Drawn by the stories you hear about Calradia and its kingdoms, you...",
#     "none",
#     [],
#     [
#       ("town_1",[(eq, "$current_startup_quest_phase", 0),],"join a caravan to Praven, in the Kingdom of Swadia.",
#        [
#          (assign, "$current_town", "p_town_6"),
#          (assign, "$g_starting_town", "$current_town"),
#          (assign, "$g_journey_string", "str_journey_to_praven"),
# 		 (jump_to_menu, "mnu_start_phase_2_5"),
# #         (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
# #         (change_screen_return),
#        ]),
#
#       ("town_2",[(eq, "$current_startup_quest_phase", 0),],"join a caravan to Reyvadin, in the Kingdom of the Vaegirs.",
#        [
#          (assign, "$current_town", "p_town_8"),
#          (assign, "$g_starting_town", "$current_town"),
#          (assign, "$g_journey_string", "str_journey_to_reyvadin"),
# 		 (jump_to_menu, "mnu_start_phase_2_5"),
# #         (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
# #         (change_screen_return),
#        ]),
#
#       ("town_3",[(eq, "$current_startup_quest_phase", 0),],"join a caravan to Tulga, in the Khergit Khanate.",
#        [
#          (assign, "$current_town", "p_town_10"),
#          (assign, "$g_starting_town", "$current_town"),
#          (assign, "$g_journey_string", "str_journey_to_tulga"),
# 		 (jump_to_menu, "mnu_start_phase_2_5"),
# #         (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
# #         (change_screen_return),
#        ]),
#
#       ("town_4",[(eq, "$current_startup_quest_phase", 0),],"take a ship to Sargoth, in the Kingdom of the Nords.",
#        [
#          (assign, "$current_town", "p_town_1"),
#          (assign, "$g_starting_town", "$current_town"),
#          (assign, "$g_journey_string", "str_journey_to_sargoth"),
# 		 (jump_to_menu, "mnu_start_phase_2_5"),
# #         (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
# #         (change_screen_return),
#        ]),
#
#       ("town_5",[(eq, "$current_startup_quest_phase", 0),],"take a ship to Jelkala, in the Kingdom of the Rhodoks.",
#        [
#          (assign, "$current_town", "p_town_5"),
#          (assign, "$g_starting_town", "$current_town"),
#          (assign, "$g_journey_string", "str_journey_to_jelkala"),
# 		 (jump_to_menu, "mnu_start_phase_2_5"),
# #         (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
# #         (change_screen_return),
#        ]),
#
#       ("town_6",[(eq, "$current_startup_quest_phase", 0),],"join a caravan to Shariz, in the Sarranid Sultanate.",
#        [
#          (assign, "$current_town", "p_town_19"),
#          (assign, "$g_starting_town", "$current_town"),
#          (assign, "$g_journey_string", "str_journey_to_shariz"),
# 		 (jump_to_menu, "mnu_start_phase_2_5"),
# #         (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
# #         (change_screen_return),
#        ]),
#
#
#       ("tutorial_cheat",[(eq,1,0)],"{!}CHEAT!",
#        [
#          (change_screen_return),
#          (assign, "$cheat_mode", 1),
#          (set_show_messages, 0),
# 		 (add_xp_to_troop, 15000, "trp_player"),
#          (troop_raise_skill, "trp_player", skl_leadership, 7),
#          (troop_raise_skill, "trp_player", skl_prisoner_management, 5),
#          (troop_raise_skill, "trp_player", skl_inventory_management, 10),
#          (party_add_members, "p_main_party", "trp_swadian_knight", 10),
#          (party_add_members, "p_main_party", "trp_vaegir_knight", 10),
#          (party_add_members, "p_main_party", "trp_vaegir_archer", 10),
#          (party_add_members, "p_main_party", "trp_swadian_sharpshooter", 10),
#          (troop_add_item, "trp_player","itm_scale_armor",0),
#          (troop_add_item, "trp_player","itm_full_helm",0),
#
#          (troop_add_item, "trp_player","itm_hafted_blade_b",0),
#          (troop_add_item, "trp_player","itm_hafted_blade_a",0),
#          (troop_add_item, "trp_player","itm_morningstar",0),
#          (troop_add_item, "trp_player","itm_tutorial_spear",0),
#          (troop_add_item, "trp_player","itm_tutorial_staff",0),
#          (troop_add_item, "trp_player","itm_tutorial_staff_no_attack",0),
#          (troop_add_item, "trp_player","itm_arena_lance",0),
#          (troop_add_item, "trp_player","itm_practice_staff",0),
#          (troop_add_item, "trp_player","itm_practice_lance",0),
#          (troop_add_item, "trp_player","itm_practice_javelin",0),
#          (troop_add_item, "trp_player","itm_scythe",0),
#          (troop_add_item, "trp_player","itm_pitch_fork",0),
#          (troop_add_item, "trp_player","itm_military_fork",0),
#          (troop_add_item, "trp_player","itm_battle_fork",0),
#          (troop_add_item, "trp_player","itm_boar_spear",0),
#          (troop_add_item, "trp_player","itm_jousting_lance",0),
#          (troop_add_item, "trp_player","itm_double_sided_lance",0),
#          (troop_add_item, "trp_player","itm_glaive",0),
#          (troop_add_item, "trp_player","itm_poleaxe",0),
#          (troop_add_item, "trp_player","itm_polehammer",0),
#          (troop_add_item, "trp_player","itm_staff",0),
#          (troop_add_item, "trp_player","itm_quarter_staff",0),
#          (troop_add_item, "trp_player","itm_iron_staff",0),
#          (troop_add_item, "trp_player","itm_shortened_spear",0),
#          (troop_add_item, "trp_player","itm_spear",0),
#          (troop_add_item, "trp_player","itm_war_spear",0),
#          (troop_add_item, "trp_player","itm_military_scythe",0),
#          (troop_add_item, "trp_player","itm_light_lance",0),
#          (troop_add_item, "trp_player","itm_lance",0),
#          (troop_add_item, "trp_player","itm_heavy_lance",0),
#          (troop_add_item, "trp_player","itm_great_lance",0),
#          (troop_add_item, "trp_player","itm_pike",0),
#          (troop_add_item, "trp_player","itm_ashwood_pike",0),
#          (troop_add_item, "trp_player","itm_awlpike",0),
#          (troop_add_item, "trp_player","itm_throwing_spears",0),
#          (troop_add_item, "trp_player","itm_javelin",0),
#          (troop_add_item, "trp_player","itm_jarid",0),
#
#          (troop_add_item, "trp_player","itm_long_axe_b",0),
#
#          (set_show_messages, 1),
#
#          (try_for_range, ":cur_place", scenes_begin, scenes_end),
#            (scene_set_slot, ":cur_place", slot_scene_visited, 1),
#          (try_end),
#
#          (call_script, "script_get_player_party_morale_values"),
#          (party_set_morale, "p_main_party", reg0),
#        ]
# 	   ),
#     ]
#   ),
#
#
#
#
#   (
#     "start_game_3",mnf_disable_all_keys,
#     "Choose your scenario:",
#     "none",
#     [
#       (assign, "$g_custom_battle_scenario", 0),
#       (assign, "$g_custom_battle_scenario", "$g_custom_battle_scenario"),
# ##      #Default banners
# ##      (troop_set_slot, "trp_banner_background_color_array", 126, 0xFF212221),
# ##      (troop_set_slot, "trp_banner_background_color_array", 127, 0xFF212221),
# ##      (troop_set_slot, "trp_banner_background_color_array", 128, 0xFF2E3B10),
# ##      (troop_set_slot, "trp_banner_background_color_array", 129, 0xFF425D7B),
# ##      (troop_set_slot, "trp_banner_background_color_array", 130, 0xFF394608),
#       ],
#     [
# ##      ("custom_battle_scenario_1",[], "Skirmish 1",
# ##       [
# ##           (assign, "$g_custom_battle_scenario", 0),
# ##           (jump_to_menu, "mnu_custom_battle_2"),
# ##
# ##        ]
# ##       ),
# ####      ("custom_battle_scenario_2",[],"Siege Attack 1",
# ####       [
# ####           (assign, "$g_custom_battle_scenario", 1),
# ####           (jump_to_menu, "mnu_custom_battle_2"),
# ####
# ####        ]
# ####       ),
# ##      ("custom_battle_scenario_3",[],"Skirmish 2",
# ##       [
# ##           (assign, "$g_custom_battle_scenario", 1),
# ##           (jump_to_menu, "mnu_custom_battle_2"),
# ##
# ##        ]
# ##       ),
# ##       ("custom_battle_scenario_4",[],"Siege Defense",
# ##       [
# ##           (assign, "$g_custom_battle_scenario", 2),
# ##           (jump_to_menu, "mnu_custom_battle_2"),
# ##        ]
# ##       ),
# ##       ("custom_battle_scenario_5",[],"Skirmish 3",
# ##       [
# ##           (assign, "$g_custom_battle_scenario", 3),
# ##           (jump_to_menu, "mnu_custom_battle_2"),
# ##        ]
# ##       ),
# ##      ("custom_battle_scenario_6",[],"Siege Attack",
# ##       [
# ##           (assign, "$g_custom_battle_scenario", 4),
# ##           (jump_to_menu, "mnu_custom_battle_2"),
# ##
# ##        ]
# ##       ),
#       ("go_back",[],"Go back",
#        [(change_screen_quit),
#         ]
# 		),
#     ]
#   ),
#
# ##  ("start_game_3",mnf_disable_all_keys,
# ##    "Choose your scenario:",
# ##    "none",
# ##    [
# ##      (assign, "$g_custom_battle_scenario", 0),
# ##      (assign, "$g_custom_battle_scenario", "$g_custom_battle_scenario"),
# ####      #Default banners
# ####      (troop_set_slot, "trp_banner_background_color_array", 126, 0xFF212221),
# ####      (troop_set_slot, "trp_banner_background_color_array", 127, 0xFF212221),
# ####      (troop_set_slot, "trp_banner_background_color_array", 128, 0xFF2E3B10),
# ####      (troop_set_slot, "trp_banner_background_color_array", 129, 0xFF425D7B),
# ####      (troop_set_slot, "trp_banner_background_color_array", 130, 0xFF394608),
# ##      ],
# ##    [
# ####      ("custom_battle_scenario_1",[], "Skirmish 1",
# ####       [
# ####           (assign, "$g_custom_battle_scenario", 0),
# ####           (jump_to_menu, "mnu_custom_battle_2"),
# ####
# ####        ]
# ####       ),
# ######      ("custom_battle_scenario_2",[],"Siege Attack 1",
# ######       [
# ######           (assign, "$g_custom_battle_scenario", 1),
# ######           (jump_to_menu, "mnu_custom_battle_2"),
# ######
# ######        ]
# ######       ),
# ####      ("custom_battle_scenario_3",[],"Skirmish 2",
# ####       [
# ####           (assign, "$g_custom_battle_scenario", 1),
# ####           (jump_to_menu, "mnu_custom_battle_2"),
# ####
# ####        ]
# ####       ),
# ####       ("custom_battle_scenario_4",[],"Siege Defense",
# ####       [
# ####           (assign, "$g_custom_battle_scenario", 2),
# ####           (jump_to_menu, "mnu_custom_battle_2"),
# ####        ]
# ####       ),
# ####       ("custom_battle_scenario_5",[],"Skirmish 3",
# ####       [
# ####           (assign, "$g_custom_battle_scenario", 3),
# ####           (jump_to_menu, "mnu_custom_battle_2"),
# ####        ]
# ####       ),
# ####      ("custom_battle_scenario_6",[],"Siege Attack",
# ####       [
# ####           (assign, "$g_custom_battle_scenario", 4),
# ####           (jump_to_menu, "mnu_custom_battle_2"),
# ####
# ####        ]
# ####       ),
# ##      ("go_back",[],"Go back",
# ##       [(change_screen_quit),
# ##        ]
# ##       ),
# ##    ]
# ##  ),
#
#   (
#     "tutorial",mnf_disable_all_keys,
#     "You approach a field where the locals are training with weapons. You can practice here to improve your combat skills.",
#     "none",
#     [
#       (try_begin),
#         (eq, "$g_tutorial_entered", 1),
#         (change_screen_quit),
#       (else_try),
#         (set_passage_menu, "mnu_tutorial"),
# ##        (try_begin),
# ##          (eq, "$tutorial_1_finished", 1),
# ##          (str_store_string, s1, "str_finished"),
# ##        (else_try),
# ##          (str_store_string, s1, "str_empty_string"),
# ##        (try_end),
# ##        (try_begin),
# ##          (eq, "$tutorial_2_finished", 1),
# ##          (str_store_string, s2, "str_finished"),
# ##        (else_try),
# ##          (str_store_string, s2, "str_empty_string"),
# ##        (try_end),
# ##        (try_begin),
# ##          (eq, "$tutorial_3_finished", 1),
# ##          (str_store_string, s3, "str_finished"),
# ##        (else_try),
# ##          (str_store_string, s3, "str_empty_string"),
# ##        (try_end),
# ##        (try_begin),
# ##          (eq, "$tutorial_4_finished", 1),
# ##          (str_store_string, s4, "str_finished"),
# ##        (else_try),
# ##          (str_store_string, s4, "str_empty_string"),
# ##        (try_end),
# ##        (try_begin),
# ##          (eq, "$tutorial_5_finished", 1),
# ##          (str_store_string, s5, "str_finished"),
# ##        (else_try),
# ##          (str_store_string, s5, "str_empty_string"),
# ##        (try_end),
#         (assign, "$g_tutorial_entered", 1),
#       (try_end),
#     ],
#     [
# ##      ("tutorial_1",
# ##      [(eq,1,0),],
# ##      "Tutorial #1: Basic movement and weapon selection. {s1}",
# ##      [
# ##        #(modify_visitors_at_site,"scn_tutorial_1"),(reset_visitors,0),
# ####           (set_jump_mission,"mt_tutorial_1"),
# ####           (jump_to_scene,"scn_tutorial_1"),(change_screen_mission)]),
# ##      ]),
# ##
# ##      ("tutorial_2",[(eq,1,0),],"Tutorial #2: Fighting with a shield. {s2}",[
# ####           (modify_visitors_at_site,"scn_tutorial_2"),(reset_visitors,0),
# ####           (set_visitor,1,"trp_tutorial_maceman"),
# ####           (set_visitor,2,"trp_tutorial_archer"),
# ####           (set_jump_mission,"mt_tutorial_2"),
# ####           (jump_to_scene,"scn_tutorial_2"),(change_screen_mission)]),
# ##           (modify_visitors_at_site,"scn_tutorial_training_ground"),
# ##           (reset_visitors, 0),
# ##           (set_player_troop, "trp_player"),
# ##           (set_visitor,0,"trp_player"),
# ##           (set_jump_mission,"mt_ai_training"),
# ##           (jump_to_scene,"scn_tutorial_training_ground"),
# ##           (change_screen_mission)]),
# ##
# ##      ("tutorial_3",[(eq,1,0),],"Tutorial #3: Fighting without a shield. {s3}",[
# ##           (modify_visitors_at_site,"scn_tutorial_3"),(reset_visitors,0),
# ##           (set_visitor,1,"trp_tutorial_maceman"),
# ##           (set_visitor,2,"trp_tutorial_swordsman"),
# ##           (set_jump_mission,"mt_tutorial_3"),
# ##           (jump_to_scene,"scn_tutorial_3"),(change_screen_mission)]),
# ##      ("tutorial_3b",[(eq,0,1)],"Tutorial 3 b",[(try_begin),
# ##                                                  (ge, "$tutorial_3_state", 12),
# ##                                                  (modify_visitors_at_site,"scn_tutorial_3"),(reset_visitors,0),
# ##                                                  (set_visitor,1,"trp_tutorial_maceman"),
# ##                                                  (set_visitor,2,"trp_tutorial_swordsman"),
# ##                                                  (set_jump_mission,"mt_tutorial_3_2"),
# ##                                                  (jump_to_scene,"scn_tutorial_3"),
# ##                                                  (change_screen_mission),
# ##                                                (else_try),
# ##                                                  (display_message,"str_door_locked",0xFFFFAAAA),
# ##                                                (try_end)], "Next level"),
# ##      ("tutorial_4",[(eq,1,0),],"Tutorial #4: Riding a horse. {s4}",[
# ##           (modify_visitors_at_site,"scn_tutorial_training_ground"),
# ##           (reset_visitors, 0),
# ##           (set_player_troop, "trp_player"),
# ##           (assign, "$g_player_troop", "trp_player"),
# ##           (troop_raise_attribute, "$g_player_troop", ca_strength, 12),
# ##           (troop_raise_attribute, "$g_player_troop", ca_agility, 9),
# ##           (troop_raise_attribute, "$g_player_troop", ca_charisma, 5),
# ##           (troop_raise_skill, "$g_player_troop", skl_shield, 3),
# ##           (troop_raise_skill, "$g_player_troop", skl_athletics, 2),
# ##           (troop_raise_skill, "$g_player_troop", skl_riding, 3),
# ##           (troop_raise_skill, "$g_player_troop", skl_power_strike, 1),
# ##           (troop_raise_skill, "$g_player_troop", skl_power_draw, 5),
# ##           (troop_raise_skill, "$g_player_troop", skl_weapon_master, 4),
# ##           (troop_raise_skill, "$g_player_troop", skl_ironflesh, 1),
# ##           (troop_raise_skill, "$g_player_troop", skl_horse_archery, 6),
# ##           (troop_raise_proficiency_linear, "$g_player_troop", wpt_one_handed_weapon, 70),
# ##           (troop_raise_proficiency_linear, "$g_player_troop", wpt_two_handed_weapon, 70),
# ##           (troop_raise_proficiency_linear, "$g_player_troop", wpt_polearm, 70),
# ##           (troop_raise_proficiency_linear, "$g_player_troop", wpt_crossbow, 70),
# ##           (troop_raise_proficiency_linear, "$g_player_troop", wpt_throwing, 70),
# ##
# ##        (troop_clear_inventory, "$g_player_troop"),
# ##        (troop_add_item, "$g_player_troop","itm_leather_jerkin",0),
# ##        (troop_add_item, "$g_player_troop","itm_leather_boots",0),
# ##        (troop_add_item, "$g_player_troop","itm_practice_sword",0),
# ##        (troop_add_item, "$g_player_troop","itm_quarter_staff",0),
# ##        (troop_equip_items, "$g_player_troop"),
# ##        (set_visitor,0,"trp_player"),
# ##        (set_visitor,32,"trp_tutorial_fighter_1"),
# ##        (set_visitor,33,"trp_tutorial_fighter_2"),
# ##        (set_visitor,34,"trp_tutorial_fighter_3"),
# ##        (set_visitor,35,"trp_tutorial_fighter_4"),
# ##        (set_visitor,40,"trp_tutorial_master_archer"),
# ##        (set_visitor,41,"trp_tutorial_archer_1"),
# ##        (set_visitor,42,"trp_tutorial_archer_1"),
# ##        (set_visitor,60,"trp_tutorial_master_horseman"),
# ##        (set_visitor,61,"trp_tutorial_rider_1"),
# ##        (set_visitor,62,"trp_tutorial_rider_1"),
# ##        (set_visitor,63,"trp_tutorial_rider_2"),
# ##        (set_visitor,64,"trp_tutorial_rider_2"),
# ##        (set_jump_mission,"mt_tutorial_training_ground"),
# ##        (jump_to_scene,"scn_tutorial_training_ground"),
# ##        (change_screen_mission),
# ##      ]),
# ##
# ##      ("tutorial_5",
# ##      [
# ##        (eq,1,0),
# ##      ],
# ##      "Tutorial #5: Commanding a band of soldiers. {s5}",
# ##      [
# ##        (modify_visitors_at_site,"scn_tutorial_5"),(reset_visitors,0),
# ##        (set_visitor,0,"trp_player"),
# ##        (set_visitor,1,"trp_vaegir_infantry"),
# ##        (set_visitor,2,"trp_vaegir_infantry"),
# ##        (set_visitor,3,"trp_vaegir_infantry"),
# ##        (set_visitor,4,"trp_vaegir_infantry"),
# ##        (set_jump_mission,"mt_tutorial_5"),
# ##        (jump_to_scene,"scn_tutorial_5"),
# ##        (change_screen_mission),
# ##      ]),
# ##
# ##      ("tutorial_edit_custom_battle_scenes",
# ##      [(eq,1,0),],
# ##      "(NO TRANSLATE) tutorial_edit_custom_battle_scenes",
# ##      [
# ##        (jump_to_menu,"mnu_custom_battle_scene"),
# ##      ]),
#
#       ("continue",[],"Continue...",
#       [
#         (modify_visitors_at_site,"scn_tutorial_training_ground"),
#         (reset_visitors, 0),
#         (set_player_troop, "trp_player"),
#         (assign, "$g_player_troop", "trp_player"),
#         (troop_raise_attribute, "$g_player_troop", ca_strength, 12),
#         (troop_raise_attribute, "$g_player_troop", ca_agility, 9),
#         (troop_raise_attribute, "$g_player_troop", ca_charisma, 5),
#         (troop_raise_skill, "$g_player_troop", skl_shield, 3),
#         (troop_raise_skill, "$g_player_troop", skl_athletics, 2),
#         (troop_raise_skill, "$g_player_troop", skl_riding, 3),
#         (troop_raise_skill, "$g_player_troop", skl_power_strike, 1),
#         (troop_raise_skill, "$g_player_troop", skl_power_draw, 5),
#         (troop_raise_skill, "$g_player_troop", skl_weapon_master, 4),
#         (troop_raise_skill, "$g_player_troop", skl_ironflesh, 1),
#         (troop_raise_skill, "$g_player_troop", skl_horse_archery, 6),
#         (troop_raise_proficiency_linear, "$g_player_troop", wpt_one_handed_weapon, 70),
#         (troop_raise_proficiency_linear, "$g_player_troop", wpt_two_handed_weapon, 70),
#         (troop_raise_proficiency_linear, "$g_player_troop", wpt_polearm, 70),
#         (troop_raise_proficiency_linear, "$g_player_troop", wpt_crossbow, 70),
#         (troop_raise_proficiency_linear, "$g_player_troop", wpt_throwing, 70),
#
#         (troop_clear_inventory, "$g_player_troop"),
#         (troop_add_item, "$g_player_troop","itm_leather_jerkin",0),
#         (troop_add_item, "$g_player_troop","itm_leather_boots",0),
#         (troop_add_item, "$g_player_troop","itm_practice_sword",0),
#         (troop_add_item, "$g_player_troop","itm_quarter_staff",0),
#         (troop_equip_items, "$g_player_troop"),
#         (set_visitor,0,"trp_player"),
#         (set_visitor,32,"trp_tutorial_fighter_1"),
#         (set_visitor,33,"trp_tutorial_fighter_2"),
#         (set_visitor,34,"trp_tutorial_fighter_3"),
#         (set_visitor,35,"trp_tutorial_fighter_4"),
#         (set_visitor,40,"trp_tutorial_master_archer"),
#         (set_visitor,41,"trp_tutorial_archer_1"),
#         (set_visitor,42,"trp_tutorial_archer_1"),
#         (set_visitor,60,"trp_tutorial_master_horseman"),
#         (set_visitor,61,"trp_tutorial_rider_1"),
#         (set_visitor,62,"trp_tutorial_rider_1"),
#         (set_visitor,63,"trp_tutorial_rider_2"),
#         (set_visitor,64,"trp_tutorial_rider_2"),
#         (set_jump_mission,"mt_tutorial_training_ground"),
#         (jump_to_scene,"scn_tutorial_training_ground"),
#         (change_screen_mission),
#         ]),
#
#       ("go_back_dot",
#       [],
#       "Go back.",
#        [
#          (change_screen_quit),
#        ]),
#     ]
#   ),
#
#   ("reports",0,
#    "Character Renown: {reg5}^Honor Rating: {reg6}^Party Morale: {reg8}^Party Size Limit: {reg7}^",
#    "none",
#    [(call_script, "script_game_get_party_companion_limit"),
#     (assign, ":party_size_limit", reg0),
#     (troop_get_slot, ":renown", "trp_player", slot_troop_renown),
#     (assign, reg5, ":renown"),
#     (assign, reg6, "$player_honor"),
#     (assign, reg7, ":party_size_limit"),
#     #(call_script, "script_get_player_party_morale_values"),
#     #(party_set_morale, "p_main_party", reg0),
#     (party_get_morale, reg8, "p_main_party"),
#    ],
#     [
#       ("cheat_faction_orders",[(ge,"$cheat_mode",1)],"{!}Cheat: Faction orders.",
#        [(jump_to_menu, "mnu_faction_orders"),
#         ]
#        ),
#
#       ("view_character_report",[],"View character report.",
#        [(jump_to_menu, "mnu_character_report"),
#         ]
#        ),
#       ("view_party_size_report",[],"View party size report.",
#        [(jump_to_menu, "mnu_party_size_report"),
#         ]
#        ),
#
#       ("view_npc_mission_report",[],"View companion mission report.",
#        [(jump_to_menu, "mnu_companion_report"),
#         ]
#        ),
#
#       ("view_weekly_budget_report",[],"View weekly budget report.",
#        [
#          (assign, "$g_apply_budget_report_to_gold", 0),
#          (start_presentation, "prsnt_budget_report"),
#         ]
#        ),
#
#       ("view_morale_report",[],"View party morale report.",
#        [(jump_to_menu, "mnu_morale_report"),
#         ]
#        ),
#
# #NPC companion changes begin
#       ("lord_relations",[],"View list of known lords by relation.",
#        [
# 		(jump_to_menu, "mnu_lord_relations"),
#         ]
#        ),
#
#       ("courtship_relations",[],"View courtship relations.",
#        [
# 		(jump_to_menu, "mnu_courtship_relations"),
#         ]
#        ),
#
#       ("status_check",[(eq,"$cheat_mode",1)],"{!}NPC status check.",
#        [
#         (try_for_range, ":npc", companions_begin, companions_end),
#             (main_party_has_troop, ":npc"),
#             (str_store_troop_name, 4, ":npc"),
#             (troop_get_slot, reg3, ":npc", slot_troop_morality_state),
#             (troop_get_slot, reg4, ":npc", slot_troop_2ary_morality_state),
#             (troop_get_slot, reg5, ":npc", slot_troop_personalityclash_state),
#             (troop_get_slot, reg6, ":npc", slot_troop_personalityclash2_state),
#             (troop_get_slot, reg7, ":npc", slot_troop_personalitymatch_state),
#             (display_message, "@{!}{s4}: M{reg3}, 2M{reg4}, PC{reg5}, 2PC{reg6}, PM{reg7}"),
#         (try_end),
#         ]
#        ),
#
# #NPC companion changes end
#
#       ("view_faction_relations_report",[],"View faction relations report.",
#        [(jump_to_menu, "mnu_faction_relations_report"),
#         ]
#        ),
#       ("resume_travelling",[],"Resume travelling.",
#        [(change_screen_return),
#         ]
#        ),
#       ]
#   ),
#
#   (
#     "custom_battle_scene",menu_text_color(0xFF000000)|mnf_disable_all_keys,
#     "(NO_TRANS)",
#
#     "none",
#     [],
#     [
#
#       ("quick_battle_scene_1",[],"{!}quick_battle_scene_1",
#        [
#            (set_jump_mission,"mt_ai_training"),
#            (jump_to_scene,"scn_quick_battle_scene_1"),(change_screen_mission)
# 		]
#        ),
#       ("quick_battle_scene_2",[],"{!}quick_battle_scene_2",
#        [
#            (set_jump_mission,"mt_ai_training"),
#            (jump_to_scene,"scn_quick_battle_scene_2"),(change_screen_mission)
# 		]
#        ),
#       ("quick_battle_scene_3",[],"{!}quick_battle_scene_3",
#        [
#            (set_jump_mission,"mt_ai_training"),
#            (jump_to_scene,"scn_quick_battle_scene_3"),(change_screen_mission)
# 		]
#        ),
#       ("quick_battle_scene_4",[],"{!}quick_battle_scene_4",
#        [
#            (set_jump_mission,"mt_ai_training"),
#            (jump_to_scene,"scn_quick_battle_scene_4"),(change_screen_mission)
# 		]
#        ),
#       ("quick_battle_scene_5",[],"{!}quick_battle_scene_5",
#        [
#            (set_jump_mission,"mt_ai_training"),
#            (jump_to_scene,"scn_quick_battle_scene_5"),(change_screen_mission)
# 		]
#        ),
#
#       ("go_back",[],"{!}Go back",
#        [(change_screen_quit),
#         ]
#        ),
#       ]
#   ),
#
#   #depreciated
# ##  (
# ##    "custom_battle_2",mnf_disable_all_keys,
# ##    "{s16}",
# ##    "none",
# ##    [
# ##     (assign, "$g_battle_result", 0),
# ##     (set_show_messages, 0),
# ##
# ##     (troop_clear_inventory, "trp_player"),
# ##     (troop_raise_attribute, "trp_player", ca_strength, -1000),
# ##     (troop_raise_attribute, "trp_player", ca_agility, -1000),
# ##     (troop_raise_attribute, "trp_player", ca_charisma, -1000),
# ##     (troop_raise_attribute, "trp_player", ca_intelligence, -1000),
# ##     (troop_raise_skill, "trp_player", skl_shield, -1000),
# ##     (troop_raise_skill, "trp_player", skl_athletics, -1000),
# ##     (troop_raise_skill, "trp_player", skl_riding, -1000),
# ##     (troop_raise_skill, "trp_player", skl_power_strike, -1000),
# ##     (troop_raise_skill, "trp_player", skl_power_throw, -1000),
# ##     (troop_raise_skill, "trp_player", skl_weapon_master, -1000),
# ##     (troop_raise_skill, "trp_player", skl_horse_archery, -1000),
# ##     (troop_raise_skill, "trp_player", skl_ironflesh, -1000),
# ##     (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, -10000),
# ##     (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, -10000),
# ##     (troop_raise_proficiency_linear, "trp_player", wpt_polearm, -10000),
# ##     (troop_raise_proficiency_linear, "trp_player", wpt_archery, -10000),
# ##     (troop_raise_proficiency_linear, "trp_player", wpt_crossbow, -10000),
# ##     (troop_raise_proficiency_linear, "trp_player", wpt_throwing, -10000),
# ##
# ##     (reset_visitors),
# ####   Scene 1 Start "Shalow Lake War"
# ##     (try_begin),
# ##       (eq, "$g_custom_battle_scenario", 0),
# ##       (assign, "$g_player_troop", "trp_knight_1_15"),
# ##       (set_player_troop, "$g_player_troop"),
# ##
# ##       (assign, "$g_custom_battle_scene", "scn_quick_battle_1"),
# ##       (modify_visitors_at_site, "$g_custom_battle_scene"),
# ##       (set_visitor, 0, "$g_player_troop"),
# ##
# ###       (troop_add_item, "trp_player","itm_bascinet",0),
# ###       (troop_add_item, "trp_player","itm_mail_with_surcoat",0),
# ###       (troop_add_item, "trp_player","itm_bastard_sword_a",0),
# ###       (troop_add_item, "trp_player","itm_war_bow",0),
# ###       (troop_add_item, "trp_player","itm_khergit_arrows",0),
# ###       (troop_add_item, "trp_player","itm_kite_shield",0),
# ###       (troop_add_item, "trp_player","itm_hunter",0),
# ###       (troop_add_item, "trp_player","itm_mail_chausses",0),
# ###       (troop_equip_items, "trp_player"),
# ##
# ##       (set_visitors, 1, "trp_farmer", 13),
# ##       (set_visitors, 2, "trp_swadian_sergeant", 5),
# ##       (set_visitors, 3, "trp_swadian_sharpshooter", 4),
# ##       (set_visitors, 4, "trp_swadian_man_at_arms", 8),
# ##       (set_visitors, 5, "trp_swadian_knight", 3),
# ##       (set_visitors, 6, "trp_peasant_woman", 7),
# ##
# ####     Enemy
# ##       (set_visitors, 16, "trp_vaegir_infantry", 6),
# ##       (set_visitors, 17, "trp_vaegir_archer", 6),
# ##       (set_visitors, 18, "trp_vaegir_horseman", 4),
# ##       (set_visitors, 19, "trp_vaegir_knight", 10),
# ##       (set_visitors, 20, "trp_vaegir_guard", 6),
# ##       (str_store_string, s16, "str_custom_battle_1"),
# ##
# ####   SCENE 3 Start "Mountain Bandit Hunt"
# ##     (else_try),
# ##       (eq, "$g_custom_battle_scenario", 1),
# ##       (assign, "$g_player_troop", "trp_knight_2_5"),
# ##       (set_player_troop, "$g_player_troop"),
# ##
# ##       (assign, "$g_custom_battle_scene", "scn_quick_battle_3"),
# ##       (modify_visitors_at_site, "$g_custom_battle_scene"),
# ##       (set_visitor, 0, "$g_player_troop"),
# ##
# ##       (set_visitors, 1, "trp_vaegir_archer", 4),
# ##       (set_visitors, 2, "trp_vaegir_archer", 5),
# ##       (set_visitors, 3, "trp_vaegir_veteran", 4),
# ##       (set_visitors, 4, "trp_vaegir_horseman", 4),
# ##       (set_visitors, 5, "trp_vaegir_footman", 2),
# ##       (set_visitors, 6, "trp_vaegir_knight", 4),
# #### ENEMY
# ##
# ##       (set_visitors, 16, "trp_mountain_bandit", 4),
# ##       (set_visitors, 17, "trp_bandit", 8),
# ##       (set_visitors, 18, "trp_mountain_bandit", 8),
# ##       (set_visitors, 19, "trp_mountain_bandit", 6),
# ##       (set_visitors, 20, "trp_sea_raider", 5),
# ##       (set_visitors, 21, "trp_mountain_bandit", 4),
# ##       (set_visitors, 22, "trp_brigand", 6),
# ##       (set_visitors, 23, "trp_sea_raider", 8),
# ##       (set_visitors, 25, "trp_brigand", 10),
# ##       (str_store_string, s16, "str_custom_battle_2"),
# ##
# ####   SCENE 4 Start "Grand Stand"
# ##     (else_try),
# ##       (eq, "$g_custom_battle_scenario", 2),
# ##       (assign, "$g_player_troop", "trp_kingdom_5_lady_1"),
# ##       (set_player_troop, "$g_player_troop"),
# ##
# ##       (troop_raise_attribute, "$g_player_troop", ca_strength, 12),
# ##       (troop_raise_attribute, "$g_player_troop", ca_agility, 9),
# ##       (troop_raise_attribute, "$g_player_troop", ca_charisma, 5),
# ##       (troop_raise_attribute, "$g_player_troop", ca_intelligence, 5),
# ##       (troop_raise_skill, "$g_player_troop", skl_shield, 3),
# ##       (troop_raise_skill, "$g_player_troop", skl_athletics, 2),
# ##       (troop_raise_skill, "$g_player_troop", skl_riding, 3),
# ##       (troop_raise_skill, "$g_player_troop", skl_power_strike, 4),
# ##       (troop_raise_skill, "$g_player_troop", skl_power_draw, 5),
# ##       (troop_raise_skill, "$g_player_troop", skl_weapon_master, 4),
# ##       (troop_raise_skill, "$g_player_troop", skl_ironflesh, 6),
# ##       (troop_raise_proficiency_linear, "$g_player_troop", wpt_one_handed_weapon, 100),
# ##       (troop_raise_proficiency_linear, "$g_player_troop", wpt_two_handed_weapon, 30),
# ##       (troop_raise_proficiency_linear, "$g_player_troop", wpt_polearm, 20),
# ##       (troop_raise_proficiency_linear, "$g_player_troop", wpt_crossbow, 110),
# ##       (troop_raise_proficiency_linear, "$g_player_troop", wpt_throwing, 10),
# ##
# ##       (assign, "$g_custom_battle_scene", "scn_quick_battle_4"),
# ##       (modify_visitors_at_site, "$g_custom_battle_scene"),
# ##       (set_visitor, 0, "$g_player_troop"),
# ##
# ##       (troop_clear_inventory, "$g_player_troop"),
# ##       (troop_add_item, "$g_player_troop","itm_helmet_with_neckguard",0),
# ##       (troop_add_item, "$g_player_troop","itm_plate_armor",0),
# ##       (troop_add_item, "$g_player_troop","itm_iron_greaves",0),
# ##       (troop_add_item, "$g_player_troop","itm_mail_chausses",0),
# ##       (troop_add_item, "$g_player_troop","itm_tab_shield_small_round_c",0),
# ##       (troop_add_item, "$g_player_troop","itm_heavy_crossbow",0),
# ##       (troop_add_item, "$g_player_troop","itm_bolts",0),
# ##       (troop_add_item, "$g_player_troop","itm_sword_medieval_b_small",0),
# ##       (troop_equip_items, "$g_player_troop"),
# #### US
# ##       (set_visitors, 1, "trp_vaegir_infantry", 4),
# ##       (set_visitors, 2, "trp_vaegir_archer", 3),
# ##       (set_visitors, 3, "trp_vaegir_infantry", 4),
# ##       (set_visitors, 4, "trp_vaegir_archer", 3),
# ##       (set_visitors, 5, "trp_vaegir_infantry", 3),
# ##       (set_visitors, 6, "trp_vaegir_footman", 5),
# ##       (set_visitors, 7, "trp_vaegir_footman", 4),
# ##       (set_visitors, 8, "trp_vaegir_archer", 3),
# ##
# #### ENEMY
# ##       (set_visitors, 16, "trp_swadian_footman", 8),
# ##       (set_visitors, 17, "trp_swadian_crossbowman", 9),
# ##       (set_visitors, 18, "trp_swadian_sergeant", 7),
# ##       (set_visitors, 19, "trp_swadian_sharpshooter", 8),
# ##       (set_visitors, 20, "trp_swadian_militia", 13),
# ##       (str_store_string, s16, "str_custom_battle_3"),
# ##
# ####   Scene 5 START
# ##     (else_try),
# ##       (eq, "$g_custom_battle_scenario", 3),
# ##       (assign, "$g_player_troop", "trp_knight_1_10"),
# ##       (set_player_troop, "$g_player_troop"),
# ##
# ##       (assign, "$g_custom_battle_scene", "scn_quick_battle_5"),
# ##       (modify_visitors_at_site, "$g_custom_battle_scene"),
# ##       (set_visitor, 0, "$g_player_troop"),
# ##
# #### US
# ##       (set_visitors, 1, "trp_swadian_knight", 3),
# ##       (set_visitors, 2, "trp_swadian_sergeant", 4),
# ##       (set_visitors, 3, "trp_swadian_sharpshooter", 8),
# ##       (set_visitors, 4, "trp_swadian_man_at_arms", 8),
# ##       (set_visitors, 5, "trp_swadian_knight", 2),
# ##
# ####     enemy
# ##       (set_visitors, 16, "trp_vaegir_infantry", 8),
# ##       (set_visitors, 17, "trp_vaegir_archer", 10),
# ##       (set_visitors, 18, "trp_vaegir_horseman", 4),
# ##       (set_visitors, 19, "trp_vaegir_knight", 10),
# ##       (set_visitors, 20, "trp_vaegir_guard", 7),
# ##       (str_store_string, s16, "str_custom_battle_4"),
# ##
# ##     (else_try),
# ##       (eq, "$g_custom_battle_scenario", 4),
# ##
# ####       (assign, "$g_custom_battle_scene", "scn_quick_battle_6"),
# ##       (assign, "$g_custom_battle_scene", "scn_quick_battle_7"),
# ##
# ###   Player Wear
# ##       (assign, "$g_player_troop", "trp_knight_4_9"),
# ##       (set_player_troop, "$g_player_troop"),
# ##
# ##       (modify_visitors_at_site, "$g_custom_battle_scene"),
# ##       (set_visitor, 0, "$g_player_troop"),
# ##
# ##       (set_visitors, 1, "trp_nord_archer", 4),
# ##       (set_visitors, 2, "trp_nord_archer", 4),
# ##       (set_visitors, 3, "trp_nord_champion", 4),
# ##       (set_visitors, 4, "trp_nord_veteran", 5),
# ##       (set_visitors, 5, "trp_nord_warrior", 5),
# ##       (set_visitors, 6, "trp_nord_trained_footman", 8),
# ##
# #### ENEMY
# ##       (set_visitors, 11, "trp_vaegir_knight", 2),
# ##       (set_visitors, 12, "trp_vaegir_guard", 6),
# ##       (set_visitors, 13, "trp_vaegir_infantry", 8),
# ##       (set_visitors, 14, "trp_vaegir_veteran", 10),
# ##       (set_visitors, 16, "trp_vaegir_skirmisher", 5),
# ##       (set_visitors, 17, "trp_vaegir_archer", 4),
# ##       (set_visitors, 18, "trp_vaegir_marksman", 2),
# ##       (set_visitors, 19, "trp_vaegir_skirmisher", 4),
# ##       (set_visitors, 20, "trp_vaegir_skirmisher", 3),
# ##       (set_visitors, 21, "trp_vaegir_skirmisher", 3),
# ##       (set_visitors, 22, "trp_vaegir_skirmisher", 3),
# ##       (set_visitors, 23, "trp_vaegir_archer", 2),
# ##       (str_store_string, s16, "str_custom_battle_5"),
# ##     (try_end),
# ##     (set_show_messages, 1),
# ##     ],
# ##
# ##    [
# ##      ("custom_battle_go",[],"Start.",
# ##       [(try_begin),
# ##          (eq, "$g_custom_battle_scenario", 2),
# ####          (set_jump_mission,"mt_custom_battle_siege"),
# ##        (else_try),
# ##          (eq, "$g_custom_battle_scenario", 4),
# ####          (set_jump_mission,"mt_custom_battle_5"),
# ##        (else_try),
# ####          (set_jump_mission,"mt_custom_battle"),
# ##        (try_end),
# ##        (jump_to_menu, "mnu_custom_battle_end"),
# ##        (jump_to_scene,"$g_custom_battle_scene"),
# ##        (change_screen_mission),
# ##        ]
# ##       ),
# ##      ("leave_custom_battle_2",[],"Cancel.",
# ##       [(jump_to_menu, "mnu_start_game_3"),
# ##        ]
# ##       ),
# ##    ]
# ##  ),
#
#
#   (
#     "custom_battle_end",mnf_disable_all_keys,
#     "The battle is over. {s1} Your side killed {reg5} enemies and lost {reg6} troops over the battle. You personally slew {reg7} men in the fighting.",
#     "none",
#     [(music_set_situation, 0),
#      (assign, reg5, "$g_custom_battle_team2_death_count"),
#      (assign, reg6, "$g_custom_battle_team1_death_count"),
#      (get_player_agent_kill_count, ":kill_count"),
#      (get_player_agent_kill_count, ":wound_count", 1),
#      (store_add, reg7, ":kill_count", ":wound_count"),
#      (try_begin),
#        (eq, "$g_battle_result", 1),
#        (str_store_string, s1, "str_battle_won"),
#      (else_try),
#        (str_store_string, s1, "str_battle_lost"),
#      (try_end),
#
#      (try_begin),
#        (ge, "$g_custom_battle_team2_death_count", 100),
#        (unlock_achievement, ACHIEVEMENT_LOOK_AT_THE_BONES),
#      (try_end),
#      ],
#     [
#       ("continue",[],"Continue.",
#        [(change_screen_quit),
#         ]
#        ),
#     ]
#   ),
#
#   ("start_game_1",menu_text_color(0xFF000000)|mnf_disable_all_keys,
#     "Select your character's gender.",
#     "none",
#     [],
#     [
#       ("start_male",[],"Male",
#        [
#          (troop_set_type,"trp_player", 0),
#          (assign,"$character_gender",tf_male),
#          (jump_to_menu,"mnu_start_character_1"),
#         ]
#        ),
#       ("start_female",[],"Female",
#        [
#          (troop_set_type, "trp_player", 1),
#          (assign, "$character_gender", tf_female),
#          (jump_to_menu, "mnu_start_character_1"),
#        ]
#        ),
# 	  ("go_back",[],"Go back",
#        [
# 	     (jump_to_menu,"mnu_start_game_0"),
#        ]),
#     ]
#   ),
#
#   (
#     "start_character_1",mnf_disable_all_keys,
#     "You were born years ago, in a land far away. Your father was...",
#     "none",
#     [
#     (str_clear,s10),
#     (str_clear,s11),
#     (str_clear,s12),
#     (str_clear,s13),
#     (str_clear,s14),
#     (str_clear,s15),
#     ],
#     [
#     ("start_noble",[],"An impoverished noble.",[
#       (assign,"$background_type",cb_noble),
#       (assign, reg3, "$character_gender"),
#       (str_store_string,s10,"@You came into the world a {reg3?daughter:son} of declining nobility,\
#  owning only the house in which they lived. However, despite your family's hardships,\
#  they afforded you a good education and trained you from childhood for the rigors of aristocracy and life at court."),
# 	(jump_to_menu,"mnu_start_character_2"),
#     ]),
#     ("start_merchant",[],"A travelling merchant.",[
#       (assign,"$background_type",cb_merchant),
#       (assign, reg3, "$character_gender"),
#       (str_store_string,s10,"@You were born the {reg3?daughter:son} of travelling merchants,\
#  always moving from place to place in search of a profit. Although your parents were wealthier than most\
#  and educated you as well as they could, you found little opportunity to make friends on the road,\
#  living mostly for the moments when you could sell something to somebody."),
# 	(jump_to_menu,"mnu_start_character_2"),
#     ]),
#     ("start_guard",[],"A veteran warrior.",[
#       (assign,"$background_type",cb_guard),
#       (assign, reg3, "$character_gender"),
#       (str_store_string,s10,"@As a child, your family scrabbled out a meagre living from your father's wages\
#  as a guardsman to the local lord. It was not an easy existence, and you were too poor to get much of an\
#  education. You learned mainly how to defend yourself on the streets, with or without a weapon in hand."),
# 	(jump_to_menu,"mnu_start_character_2"),
#     ]),
#     ("start_forester",[],"A hunter.",[
#       (assign,"$background_type",cb_forester),
#       (assign, reg3, "$character_gender"),
#       (str_store_string,s11,"@{reg3?daughter:son}"),
#       (str_store_string,s10,"@You were the {reg3?daughter:son} of a family who lived off the woods,\
#  doing whatever they needed to make ends meet. Hunting, woodcutting, making arrows,\
#  even a spot of poaching whenever things got tight. Winter was never a good time for your family\
#  as the cold took animals and people alike, but you always lived to see another dawn,\
#  though your brothers and sisters might not be so fortunate."),
# 	(jump_to_menu,"mnu_start_character_2"),
#     ]),
#     ("start_nomad",[],"A steppe nomad.",[
#       (assign,"$background_type",cb_nomad),
#       (assign, reg3, "$character_gender"),
#       (str_store_string,s11,"@{reg3?daughter:son}"),
#       (str_store_string,s10,"@You were a child of the steppe, born to a tribe of wandering nomads who lived\
#  in great camps throughout the arid grasslands.\
#  Like the other tribesmen, your family revered horses above almost everything else, and they taught you\
#  how to ride almost before you learned how to walk. "),
# 	(jump_to_menu,"mnu_start_character_2"),
#     ]),
#     ("start_thief",[],"A thief.",[
#       (assign,"$background_type",cb_thief),
#       (assign, reg3, "$character_gender"),
#       (str_store_string,s10,"@As the {reg3?daughter:son} of a thief, you had very little 'formal' education.\
#  Instead you were out on the street, begging until you learned how to cut purses, cutting purses\
#  until you learned how to pick locks, all the way through your childhood.\
#  Still, these long years made you streetwise and sharp to the secrets of cities and shadowy backways."),
# 	(jump_to_menu,"mnu_start_character_2"),
#     ]),
# ##    ("start_priest",[],"Priests.",[
# ##      (assign,"$background_type",cb_priest),
# ##      (assign, reg3, "$character_gender"),
# ##      (str_store_string,s10,"@A {reg3?daughter:son} that nobody wanted, you were left to the church as a baby,\
# ## a foundling raised by the priests and nuns to their own traditions.\
# ## You were only one of many other foundlings and orphans, but you nonetheless received a lot of attention\
# ## as well as many years of study in the church library and before the altar. They taught you many things.\
# ## Gradually, faith became such a part of your life that it was no different from the blood coursing through your veins."),
# ##	(jump_to_menu,"mnu_start_character_2"),
# ##    ]),
#     ("go_back",[],"Go back",
#      [(jump_to_menu,"mnu_start_game_1"),
#     ]),
#     ]
#   ),
#   (
#     "start_character_2",0,
#     "{s10}^^ You started to learn about the world almost as soon as you could walk and talk. You spent your early life as...",
#     "none",
#     [],
#     [
#       ("page",[
#           ],"A page at a nobleman's court.",[
#       (assign,"$background_answer_2", cb2_page),
#       (assign, reg3, "$character_gender"),
#       (str_store_string,s11,"@As a {reg3?girl:boy} growing out of childhood,\
#  you were sent to live in the court of one of the nobles of the land.\
#  There, your first lessons were in humility, as you waited upon the lords and ladies of the household.\
#  But from their chess games, their gossip, even the poetry of great deeds and courtly love, you quickly began to learn about the adult world of conflict\
#  and competition. You also learned from the rough games of the other children, who battered at each other with sticks in imitation of their elders' swords."),
# 	(jump_to_menu,"mnu_start_character_3"),
#     ]),
#       ("apprentice",[
#           ],"A craftsman's apprentice.",[
#       (assign,"$background_answer_2", cb2_apprentice),
#       (assign, reg3, "$character_gender"),
#       (str_store_string,s11,"@As a {reg3?girl:boy} growing out of childhood,\
#  you apprenticed with a local craftsman to learn a trade. After years of hard work and study under your\
#  new master, he promoted you to journeyman and employed you as a fully paid craftsman for as long as\
#  you wished to stay."),
# 	(jump_to_menu,"mnu_start_character_3"),
#     ]),
#       ("stockboy",[
#           ],"A shop assistant.",[
#       (assign,"$background_answer_2",cb2_merchants_helper),
#       (assign, reg3, "$character_gender"),
#       (str_store_string,s11,"@As a {reg3?girl:boy} growing out of childhood,\
#  you apprenticed to a wealthy merchant, picking up the trade over years of working shops and driving caravans.\
#  You soon became adept at the art of buying low, selling high, and leaving the customer thinking they'd\
#  got the better deal."),
# 	(jump_to_menu,"mnu_start_character_3"),
#     ]),
#       ("urchin",[
#           ],"A street urchin.",[
#       (assign,"$background_answer_2",cb2_urchin),
#       (assign, reg3, "$character_gender"),
#       (str_store_string,s11,"@As a {reg3?girl:boy} growing out of childhood,\
#  you took to the streets, doing whatever you must to survive.\
#  Begging, thieving and working for gangs to earn your bread, you lived from day to day in this violent world,\
#  always one step ahead of the law and those who wished you ill."),
# 	(jump_to_menu,"mnu_start_character_3"),
#     ]),
#       ("nomad",[
#           ],"A steppe child.",[
#       (assign,"$background_answer_2",cb2_steppe_child),
#       (assign, reg3, "$character_gender"),
#       (str_store_string,s11,"@As a {reg3?girl:boy} growing out of childhood,\
#  you rode the great steppes on a horse of your own, learning the ways of the grass and the desert.\
#  Although you sometimes went hungry, you became a skillful hunter and pathfinder in this trackless country.\
#  Your body too started to harden with muscle as you grew into the life of a nomad {reg3?woman:man}."),
# 	(jump_to_menu,"mnu_start_character_3"),
#     ]),
#
# ##      ("mummer",[],"Mummer.",[
# ##      (assign,"$background_answer_2",5),
# ##      (assign, reg3, "$character_gender"),
# ##      (str_store_string,s13,"@{reg3?woman:man}"),
# ##      (str_store_string,s12,"@{reg3?girl:boy}"),
# ##      (str_store_string,s11,"@As a {s12} growing out of childhood,\
# ## you attached yourself to a troupe of wandering entertainers, going from town to town setting up mummer's\
# ## shows. It was a life of hard work, selling, begging and stealing your living from the punters who flocked\
# ## to watch your antics. Over time you became a performer well capable of attracting a crowd."),
# ##	(jump_to_menu,"mnu_start_character_3"),
# ##    ]),
# ##      ("courtier",[],"Courtier.",[
# ##      (assign,"$background_answer_2",6),
# ##      (assign, reg3, "$character_gender"),
# ##      (str_store_string,s13,"@{reg3?woman:man}"),
# ##      (str_store_string,s12,"@{reg3?girl:boy}"),
# ##      (str_store_string,s11,"@As a {s12} growing out of childhood,\
# ## you spent much of your life at court, inserting yourself into the tightly-knit circles of nobility.\
# ## With the years you became more and more involved with the politics and intrigue demanded of a high-born {s13}.\
# ## You could not afford to remain a stranger to backstabbing and political violence, even if you wanted to."),
# ##	(jump_to_menu,"mnu_start_character_3"),
# ##    ]),
# ##      ("noble",[],"Noble in training.",[
# ##      (assign,"$background_answer_2",7),
# ##      (assign, reg3, "$character_gender"),
# ##      (str_store_string,s13,"@{reg3?woman:man}"),
# ##      (str_store_string,s12,"@{reg3?girl:boy}"),
# ##      (try_begin),
# ##      (eq,"$character_gender",tf_male),
# ##      (str_store_string,s11,"@As a {s12} growing out of childhood,\
# ## you were trained and educated to perform the duties and wield the rights of a noble landowner.\
# ## The managing of taxes and rents were equally important in your education as diplomacy and even\
# ## personal defence. You learned everything you needed to become a lord of your own hall."),
# ##      (else_try),
# ##      (str_store_string,s11,"@As a {s12} growing out of childhood,\
# ## you were trained and educated to the duties of a noble {s13}. You learned much about the household arts,\
# ## but even more about diplomacy and decorum, and all the things that a future husband might choose to speak of.\
# ## Truly, you became every inch as shrewd as any lord, though it would be rude to admit it aloud."),
# ##      (try_end),
# ##	(jump_to_menu,"mnu_start_character_3"),
# ##    ]),
# ##      ("acolyte",[],"Cleric acolyte.",[
# ##    (assign,"$background_answer_2",8),
# ##      (assign, reg3, "$character_gender"),
# ##      (str_store_string,s13,"@{reg3?woman:man}"),
# ##      (str_store_string,s12,"@{reg3?girl:boy}"),
# ##      (str_store_string,s11,"@As a {s12} growing out of childhood,\
# ## you became an acolyte in the church, the lowest rank on the way to priesthood.\
# ## Years of rigorous learning and hard work followed. You were one of several acolytes,\
# ## performing most of the menial labour in the church in addition to being trained for more holy tasks.\
# ## On the night of your adulthood you were allowed to conduct your first service.\
# ## After that you were no longer an acolyte {s12}, but a {s13} waiting to take your vows into the service of God."),
# ##	(jump_to_menu,"mnu_start_character_3"),
# ##    ]),
#       ("go_back",[],"Go back.",
#      [(jump_to_menu,"mnu_start_character_1"),
#     ]),
#     ]
#   ),
#   (
#     "start_character_3",mnf_disable_all_keys,
#     "{s11}^^ Then, as a young adult, life changed as it always does. You became...",
#     "none",
#     [(assign, reg3, "$character_gender"),],
#     [
# ##      ("bravo",[],"A travelling bravo.",[
# ##        (assign,"$background_answer_3",1),
# ##      (str_store_string,s14,"@{reg3?daughter:man}"),
# ##      (str_store_string,s13,"@{reg3?woman:man}"),
# ##      (str_store_string,s12,"@Though the distinction felt sudden to you,\
# ## somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
# ## You left your old life behind to travel the roads as a mercenary, a bravo, guarding caravans for coppers\
# ## or bashing in heads for silvers. You became a {s14} of the open road, working with bandits as often as against.\
# ## Going from fight to fight, you grew experienced at battle, and you learned what it was to kill."),
# ##	(jump_to_menu,"mnu_start_character_4"),
# ##        ]),
# ##      ("merc",[],"A sellsword in foreign lands.",[
# ##        (assign,"$background_answer_3",2),
# ##      (str_store_string,s14,"@{reg3?daughter:man}"),
# ##      (str_store_string,s13,"@{reg3?woman:man}"),
# ##      (str_store_string,s12,"@Though the distinction felt sudden to you,\
# ## somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
# ## You signed on with a mercenary company and travelled far from your home. The life you found was rough and\
# ## ready, marching to the beat of strange drums and learning unusual ways of fighting.\
# ## There were men who taught you how to wield any weapon you desired, and plenty of battles to hone your skills.\
# ## You were one of the charmed few who survived through every campaign in which you marched."),
# ##	(jump_to_menu,"mnu_start_character_4"),
# ##        ]),
#
#       ("squire",[(eq,"$character_gender",tf_male)],"A squire.",[
#         (assign,"$background_answer_3",cb3_squire),
#       (str_store_string,s14,"@{reg3?daughter:man}"),
#       (str_store_string,s12,"@Though the distinction felt sudden to you,\
#  somewhere along the way you had become a {reg3?woman:man}, and the whole world seemed to change around you.\
#  When you were named squire to a noble at court, you practiced long hours with weapons,\
#  learning how to deal out hard knocks and how to take them, too.\
#  You were instructed in your obligations to your lord, and of your duties to those who might one day be your vassals.\
#  But in addition to learning the chivalric ideal, you also learned about the less uplifting side\
#  -- old warriors' stories of ruthless power politics, of betrayals and usurpations,\
#  of men who used guile as well as valor to achieve their aims."),
# 	(jump_to_menu,"mnu_start_character_4"),
#         ]),
#       ("lady",[(eq,"$character_gender",tf_female)],"A lady-in-waiting.",[
#         (assign,"$background_answer_3",cb3_lady_in_waiting),
#       (str_store_string,s14,"@{reg3?daughter:man}"),
#       (str_store_string,s13,"@{reg3?woman:man}"),
#       (str_store_string,s12,"@Though the distinction felt sudden to you,\
#  somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
#  You joined the tightly-knit circle of women at court, ladies who all did proper ladylike things,\
#  the wives and mistresses of noble men as well as maidens who had yet to find a husband.\
#  However, even here you found politics at work as the ladies schemed for prominence and fought each other\
#  bitterly to catch the eye of whatever unmarried man was in fashion at court.\
#  You soon learned ways of turning these situations and goings-on to your advantage. With it came the\
#  realisation that you yourself could wield great influence in the world, if only you applied yourself\
#  with a little bit of subtlety."),
# 	(jump_to_menu,"mnu_start_character_4"),
#         ]),
#       ("troubadour",[],"A troubadour.",[
#         (assign,"$background_answer_3",cb3_troubadour),
#       (str_store_string,s14,"@{reg3?daughter:man}"),
#       (str_store_string,s13,"@{reg3?woman:man}"),
#       (str_store_string,s12,"@Though the distinction felt sudden to you,\
#  somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
#  You set out on your own with nothing except the instrument slung over your back and your own voice.\
#  It was a poor existence, with many a hungry night when people failed to appreciate your play,\
#  but you managed to survive on your music alone. As the years went by you became adept at playing the\
#  drunken crowds in your taverns, and even better at talking anyone out of anything you wanted."),
# 	(jump_to_menu,"mnu_start_character_4"),
#         ]),
#       ("student",[],"A university student.",[
#         (assign,"$background_answer_3",cb3_student),
#       (str_store_string,s12,"@Though the distinction felt sudden to you,\
#  somewhere along the way you had become a {reg3?woman:man}, and the whole world seemed to change around you.\
#  You found yourself as a student in the university of one of the great cities,\
#  where you studied theology, philosophy, and medicine.\
#  But not all your lessons were learned in the lecture halls.\
#  You may or may not have joined in with your fellows as they roamed the alleys in search of wine, women, and a good fight.\
#  However, you certainly were able to observe how a broken jaw is set,\
#  or how an angry townsman can be persuaded to set down his club and accept cash compensation for the destruction of his shop."),
# 	(jump_to_menu,"mnu_start_character_4"),
#         ]),
#       ("peddler",[],"A goods peddler.",[
#         (assign,"$background_answer_3",cb3_peddler),
#       (str_store_string,s14,"@{reg3?daughter:man}"),
#       (str_store_string,s13,"@{reg3?woman:man}"),
#       (str_store_string,s12,"@Though the distinction felt sudden to you,\
#  somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
#  Heeding the call of the open road, you travelled from village to village buying and selling what you could.\
#  It was not a rich existence, but you became a master at haggling even the most miserly elders into\
#  giving you a good price. Soon, you knew, you would be well-placed to start your own trading empire..."),
# 	(jump_to_menu,"mnu_start_character_4"),
#         ]),
#       ("craftsman",[],"A smith.",[
#         (assign,"$background_answer_3", cb3_craftsman),
#       (str_store_string,s14,"@{reg3?daughter:man}"),
#       (str_store_string,s13,"@{reg3?woman:man}"),
#       (str_store_string,s12,"@Though the distinction felt sudden to you,\
#  somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
#  You pursued a career as a smith, crafting items of function and beauty out of simple metal.\
#  As time wore on you became a master of your trade, and fine work started to fetch fine prices.\
#  With food in your belly and logs on your fire, you could take pride in your work and your growing reputation."),
# 	(jump_to_menu,"mnu_start_character_4"),
#         ]),
#       ("poacher",[],"A game poacher.",[
#         (assign,"$background_answer_3", cb3_poacher),
#       (str_store_string,s14,"@{reg3?daughter:man}"),
#       (str_store_string,s13,"@{reg3?woman:man}"),
#       (str_store_string,s12,"@Though the distinction felt sudden to you,\
#  somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
#  Dissatisfied with common men's desperate scrabble for coin, you took to your local lord's own forests\
#  and decided to help yourself to its bounty, laws be damned. You hunted stags, boars and geese and sold\
#  the precious meat under the table. You cut down trees right under the watchmen's noses and turned them into\
#  firewood that warmed many freezing homes during winter. All for a few silvers, of course."),
# 	(jump_to_menu,"mnu_start_character_4"),
#         ]),
# ##      ("preacher",[],"Itinerant preacher.",[
# ##        (assign,"$background_answer_3",6),
# ##      (str_store_string,s14,"@{reg3?daughter:man}"),
# ##      (str_store_string,s13,"@{reg3?woman:man}"),
# ##      (str_store_string,s12,"@Though the distinction felt sudden to you,\
# ## somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
# ## You packed your few belongings and went out into the world to spread the word of God. You preached to\
# ## anyone who would listen, and impressed many with the passion of your sermons. Though you had taken a vow\
# ## to remain in poverty through your itinerant years, you never lacked for food, drink or shelter; the\
# ## hospitality of the peasantry was always generous to a rising {s13} of God."),
# ##	(jump_to_menu,"mnu_start_character_4"),
# ##        ]),
#       ("go_back",[],"Go back.",
#        [(jump_to_menu,"mnu_start_character_2"),
#         ]
#        ),
#     ]
#   ),
#
#   (
#     "start_character_4",mnf_disable_all_keys,
#     "{s12}^^But soon everything changed and you decided to strike out on your own as an adventurer. What made you take this decision was...",
#     #Finally, what made you decide to strike out on your own as an adventurer?",
#     "none",
#     [],
#     [
#       ("revenge",[],"Personal revenge.",[
#         (assign,"$background_answer_4", cb4_revenge),
#       (str_store_string,s13,"@Only you know exactly what caused you to give up your old life and become an adventurer.\
#  Still, it was not a difficult choice to leave, with the rage burning brightly in your heart.\
#  You want vengeance. You want justice. What was done to you cannot be undone,\
#  and these debts can only be paid in blood..."),
#         (jump_to_menu,"mnu_choose_skill"),
#         ]),
#       ("death",[],"The loss of a loved one.",[
#         (assign,"$background_answer_4",cb4_loss),
#       (str_store_string,s13,"@Only you know exactly what caused you to give up your old life and become an adventurer.\
#  All you can say is that you couldn't bear to stay, not with the memories of those you loved so close and so\
#  painful. Perhaps your new life will let you forget,\
#  or honour the name that you can no longer bear to speak..."),
#         (jump_to_menu,"mnu_choose_skill"),
#         ]),
#       ("wanderlust",[],"Wanderlust.",[
#         (assign,"$background_answer_4",cb4_wanderlust),
#       (str_store_string,s13,"@Only you know exactly what caused you to give up your old life and become an adventurer.\
#  You're not even sure when your home became a prison, when the familiar became mundane, but your dreams of\
#  wandering have taken over your life. Whether you yearn for some faraway place or merely for the open road and the\
#  freedom to travel, you could no longer bear to stay in the same place. You simply went and never looked back..."),
#         (jump_to_menu,"mnu_choose_skill"),
#         ]),
# ##      ("fervor",[],"Religious fervor.",[
# ##        (assign,"$background_answer_4",4),
# ##      (str_store_string,s13,"@Only you know exactly what caused you to give up your old life and become an adventurer.\
# ## Regardless, the intense faith burning in your soul would not let you find peace in any single place.\
# ## There were others in the world, souls to be washed in the light of God. Now you preach wherever you go,\
# ## seeking to bring salvation and revelation to the masses, be they faithful or pagan. They will all know the\
# ## glory of God by the time you're done..."),
# ##        (jump_to_menu,"mnu_choose_skill"),
# ##        ]),
#       ("disown",[],"Being forced out of your home.",[
#         (assign,"$background_answer_4",cb4_disown),
#       (str_store_string,s13,"@Only you know exactly what caused you to give up your old life and become an adventurer.\
#  However, you know you cannot go back. There's nothing to go back to. Whatever home you may have had is gone\
#  now, and you must face the fact that you're out in the wide wide world. Alone to sink or swim..."),
#         (jump_to_menu,"mnu_choose_skill"),
#         ]),
#      ("greed",[],"Lust for money and power.",[
#         (assign,"$background_answer_4",cb4_greed),
#       (str_store_string,s13,"@Only you know exactly what caused you to give up your old life and become an adventurer.\
#  To everyone else, it's clear that you're now motivated solely by personal gain.\
#  You want to be rich, powerful, respected, feared.\
#  You want to be the one whom others hurry to obey.\
#  You want people to know your name, and tremble whenever it is spoken.\
#  You want everything, and you won't let anyone stop you from having it..."),
#         (jump_to_menu,"mnu_choose_skill"),
#         ]),
#       ("go_back",[],"Go back.",
#        [(jump_to_menu,"mnu_start_character_3"),
#         ]
#        ),
#     ]
#   ),
#
#
#   (
#     "choose_skill",mnf_disable_all_keys,
#     "{s13}",
#     "none",
#     [(assign,"$current_string_reg",10),
# 	 (assign, ":difficulty", 0),
#
# 	 (try_begin),
# 		(eq, "$character_gender", tf_female),
# 		(str_store_string, s14, "str_woman"),
# 		(val_add, ":difficulty", 1),
# 	 (else_try),
# 		(str_store_string, s14, "str_man"),
# 	 (try_end),
#
# 	 (try_begin),
#         (eq,"$background_type",cb_noble),
# 		(str_store_string, s15, "str_noble"),
# 		(val_sub, ":difficulty", 1),
# 	 (else_try),
# 		(str_store_string, s15, "str_common"),
# 	 (try_end),
#
# 	 (try_begin),
# 		(eq, ":difficulty", -1),
# 		(str_store_string, s16, "str_may_find_that_you_are_able_to_take_your_place_among_calradias_great_lords_relatively_quickly"),
# 	 (else_try),
# 		(eq, ":difficulty", 0),
# 		(str_store_string, s16, "str_may_face_some_difficulties_establishing_yourself_as_an_equal_among_calradias_great_lords"),
# 	 (else_try),
# 		(eq, ":difficulty", 1),
# 		(str_store_string, s16, "str_may_face_great_difficulties_establishing_yourself_as_an_equal_among_calradias_great_lords"),
# 	 (try_end),
# 	],
#     [
# ##      ("start_swordsman",[],"Swordsmanship.",[
# ##        (assign, "$starting_skill", 1),
# ##        (str_store_string, s14, "@You are particularly talented at swordsmanship."),
# ##        (jump_to_menu,"mnu_past_life_explanation"),
# ##        ]),
# ##      ("start_archer",[],"Archery.",[
# ##        (assign, "$starting_skill", 2),
# ##        (str_store_string, s14, "@You are particularly talented at archery."),
# ##        (jump_to_menu,"mnu_past_life_explanation"),
# ##        ]),
# ##      ("start_medicine",[],"Medicine.",[
# ##        (assign, "$starting_skill", 3),
# ##        (str_store_string, s14, "@You are particularly talented at medicine."),
# ##        (jump_to_menu,"mnu_past_life_explanation"),
# ##        ]),
#       ("begin_adventuring",[],"Become an adventurer and ride to your destiny.",[
#            (set_show_messages, 0),
#            (try_begin),
#              (eq,"$character_gender",0),
#              (troop_raise_attribute, "trp_player",ca_strength,1),
#              (troop_raise_attribute, "trp_player",ca_charisma,1),
#            (else_try),
#              (troop_raise_attribute, "trp_player",ca_agility,1),
#              (troop_raise_attribute, "trp_player",ca_intelligence,1),
#            (try_end),
#
#            (troop_raise_attribute, "trp_player",ca_strength,1),
#            (troop_raise_attribute, "trp_player",ca_agility,1),
#            (troop_raise_attribute, "trp_player",ca_charisma,1),
#
#            (troop_raise_skill, "trp_player","skl_leadership",1),
#            (troop_raise_skill, "trp_player","skl_riding",1),
# ##           (try_begin),
# ##             (eq, "$starting_skill", 1),
# ##             (troop_raise_attribute, "trp_player",ca_agility,1),
# ##             (troop_raise_attribute, "trp_player",ca_strength,1),
# ##             (troop_raise_skill, "trp_player",skl_power_strike,2),
# ##             (troop_raise_proficiency, "trp_player",0,30),
# ##             (troop_raise_proficiency, "trp_player",1,20),
# ##           (else_try),
# ##             (eq, "$starting_skill", 2),
# ##             (troop_raise_attribute, "trp_player",ca_strength,2),
# ##             (troop_raise_skill, "trp_player",skl_power_draw,2),
# ##             (troop_raise_proficiency, "trp_player",3,50),
# ##           (else_try),
# ##             (troop_raise_attribute, "trp_player",ca_intelligence,1),
# ##             (troop_raise_attribute, "trp_player",ca_charisma,1),
# ##             (troop_raise_skill, "trp_player",skl_first_aid,1),
# ##             (troop_raise_skill, "trp_player",skl_wound_treatment,1),
# ##             (troop_add_item, "trp_player","itm_winged_mace",0),
# ##             (troop_raise_proficiency, "trp_player",0,15),
# ##             (troop_raise_proficiency, "trp_player",1,15),
# ##             (troop_raise_proficiency, "trp_player",2,15),
# ##           (try_end),
#
#
#       (try_begin),
#         (eq,"$background_type",cb_noble),
#         (eq,"$character_gender",tf_male),
#         (troop_raise_attribute, "trp_player",ca_intelligence,1),
#         (troop_raise_attribute, "trp_player",ca_charisma,2),
#         (troop_raise_skill, "trp_player",skl_weapon_master,1),
#         (troop_raise_skill, "trp_player",skl_power_strike,1),
#         (troop_raise_skill, "trp_player",skl_riding,1),
#         (troop_raise_skill, "trp_player",skl_tactics,1),
#         (troop_raise_skill, "trp_player",skl_leadership,1),
#         (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,10),
#         (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,10),
#         (troop_raise_proficiency, "trp_player",wpt_polearm,10),
#
#         (troop_add_item, "trp_player","itm_tab_shield_round_a",imod_battered),
#         (troop_set_slot, "trp_player", slot_troop_renown, 100),
#         (call_script, "script_change_player_honor", 3),
#
#
# ##        (troop_add_item, "trp_player","itm_red_gambeson",imod_plain),
# ##        (troop_add_item, "trp_player","itm_sword",imod_plain),
# ##        (troop_add_item, "trp_player","itm_dagger",imod_balanced),
# ##        (troop_add_item, "trp_player","itm_woolen_hose",0),
# ##        (troop_add_item, "trp_player","itm_dried_meat",0),
# ##        (troop_add_item, "trp_player","itm_saddle_horse",imod_plain),
#         (troop_add_gold, "trp_player", 100),
#       (else_try),
#         (eq,"$background_type",cb_noble),
#         (eq,"$character_gender",tf_female),
#         (troop_raise_attribute, "trp_player",ca_intelligence,2),
#         (troop_raise_attribute, "trp_player",ca_charisma,1),
#         (troop_raise_skill, "trp_player",skl_wound_treatment,1),
#         (troop_raise_skill, "trp_player",skl_riding,2),
#         (troop_raise_skill, "trp_player",skl_first_aid,1),
#         (troop_raise_skill, "trp_player",skl_leadership,1),
#         (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,20),
#
#         (troop_set_slot, "trp_player", slot_troop_renown, 50),
#         (troop_add_item, "trp_player","itm_tab_shield_round_a",imod_battered),
#
# ##        (troop_add_item, "trp_player","itm_dress",imod_sturdy),
# ##        (troop_add_item, "trp_player","itm_dagger",imod_watered_steel),
# ##        (troop_add_item, "trp_player","itm_woolen_hose",0),
# ##        (troop_add_item, "trp_player","itm_hunting_crossbow",0),
# ##        (troop_add_item, "trp_player","itm_bolts",0),
# ##        (troop_add_item, "trp_player","itm_smoked_fish",0),
# ##        (troop_add_item, "trp_player","itm_courser",imod_spirited),
#         (troop_add_gold, "trp_player", 100),
#       (else_try),
#         (eq,"$background_type",cb_merchant),
#         (troop_raise_attribute, "trp_player",ca_intelligence,2),
#         (troop_raise_attribute, "trp_player",ca_charisma,1),
#         (troop_raise_skill, "trp_player",skl_riding,1),
#         (troop_raise_skill, "trp_player",skl_leadership,1),
#         (troop_raise_skill, "trp_player",skl_trade,2),
#         (troop_raise_skill, "trp_player",skl_inventory_management,1),
#         (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,10),
#
# ##        (troop_add_item, "trp_player","itm_leather_jacket",0),
# ##        (troop_add_item, "trp_player","itm_leather_boots",0),
# ##        (troop_add_item, "trp_player","itm_fur_hat",0),
# ##        (troop_add_item, "trp_player","itm_dagger",0),
# ##        (troop_add_item, "trp_player","itm_hunting_crossbow",0),
# ##        (troop_add_item, "trp_player","itm_bolts",0),
# ##        (troop_add_item, "trp_player","itm_smoked_fish",0),
# ##        (troop_add_item, "trp_player","itm_saddle_horse",0),
# ##        (troop_add_item, "trp_player","itm_sumpter_horse",0),
# ##        (troop_add_item, "trp_player","itm_salt",0),
# ##        (troop_add_item, "trp_player","itm_salt",0),
# ##        (troop_add_item, "trp_player","itm_salt",0),
# ##        (troop_add_item, "trp_player","itm_pottery",0),
# ##        (troop_add_item, "trp_player","itm_pottery",0),
#
#         (troop_add_gold, "trp_player", 250),
#         (troop_set_slot, "trp_player", slot_troop_renown, 20),
#       (else_try),
#         (eq,"$background_type",cb_guard),
#         (troop_raise_attribute, "trp_player",ca_strength,1),
#         (troop_raise_attribute, "trp_player",ca_agility,1),
#         (troop_raise_attribute, "trp_player",ca_charisma,1),
#         (troop_raise_skill, "trp_player","skl_ironflesh",1),
#         (troop_raise_skill, "trp_player","skl_power_strike",1),
#         (troop_raise_skill, "trp_player","skl_weapon_master",1),
#         (troop_raise_skill, "trp_player","skl_leadership",1),
#         (troop_raise_skill, "trp_player","skl_trainer",1),
#         (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,10),
#         (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,15),
#         (troop_raise_proficiency, "trp_player",wpt_polearm,20),
#         (troop_raise_proficiency, "trp_player",wpt_throwing,10),
#         (troop_add_item, "trp_player","itm_tab_shield_kite_b",imod_battered),
#
# ##        (troop_add_item, "trp_player","itm_leather_jerkin",imod_ragged),
# ##        (troop_add_item, "trp_player","itm_skullcap",imod_rusty),
# ##        (troop_add_item, "trp_player","itm_spear",0),
# ##        (troop_add_item, "trp_player","itm_arming_sword",imod_chipped),
# ##        (troop_add_item, "trp_player","itm_hunting_crossbow",0),
# ##        (troop_add_item, "trp_player","itm_hunter_boots",0),
# ##        (troop_add_item, "trp_player","itm_leather_gloves",imod_ragged),
# ##        (troop_add_item, "trp_player","itm_bolts",0),
# ##        (troop_add_item, "trp_player","itm_smoked_fish",0),
# ##        (troop_add_item, "trp_player","itm_saddle_horse",imod_swaybacked),
#         (troop_add_gold, "trp_player", 50),
#         (troop_set_slot, "trp_player", slot_troop_renown, 10),
#       (else_try),
#         (eq,"$background_type",cb_forester),
#         (troop_raise_attribute, "trp_player",ca_strength,1),
#         (troop_raise_attribute, "trp_player",ca_agility,2),
#         (troop_raise_skill, "trp_player","skl_power_draw",1),
#         (troop_raise_skill, "trp_player","skl_tracking",1),
#         (troop_raise_skill, "trp_player","skl_pathfinding",1),
#         (troop_raise_skill, "trp_player","skl_spotting",1),
#         (troop_raise_skill, "trp_player","skl_athletics",1),
#         (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,10),
#         (troop_raise_proficiency, "trp_player",wpt_archery,30),
# ##        (troop_add_item, "trp_player","itm_short_bow",imod_bent),
# ##        (troop_add_item, "trp_player","itm_arrows",0),
# ##        (troop_add_item, "trp_player","itm_axe",imod_chipped),
# ##        (troop_add_item, "trp_player","itm_rawhide_coat",0),
# ##        (troop_add_item, "trp_player","itm_hide_boots",0),
# ##        (troop_add_item, "trp_player","itm_dried_meat",0),
# ##        (troop_add_item, "trp_player","itm_sumpter_horse",imod_heavy),
# ##        (troop_add_item, "trp_player","itm_furs",0),
#         (troop_add_gold, "trp_player", 30),
#       (else_try),
#         (eq,"$background_type",cb_nomad),
#         (eq,"$character_gender",tf_male),
#         (troop_raise_attribute, "trp_player",ca_strength,1),
#         (troop_raise_attribute, "trp_player",ca_agility,1),
#         (troop_raise_attribute, "trp_player",ca_intelligence,1),
#         (troop_raise_skill, "trp_player","skl_power_draw",1),
#         (troop_raise_skill, "trp_player","skl_horse_archery",1),
#         (troop_raise_skill, "trp_player","skl_pathfinding",1),
#         (troop_raise_skill, "trp_player","skl_riding",2),
#         (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,10),
#         (troop_raise_proficiency, "trp_player",wpt_archery,30),
#         (troop_raise_proficiency, "trp_player",wpt_throwing,10),
#         (troop_add_item, "trp_player","itm_tab_shield_small_round_a",imod_battered),
# ##        (troop_add_item, "trp_player","itm_javelin",imod_bent),
# ##        (troop_add_item, "trp_player","itm_sword_khergit_1",imod_rusty),
# ##        (troop_add_item, "trp_player","itm_nomad_armor",0),
# ##        (troop_add_item, "trp_player","itm_hide_boots",0),
# ##        (troop_add_item, "trp_player","itm_horse_meat",0),
# ##        (troop_add_item, "trp_player","itm_steppe_horse",0),
#         (troop_add_gold, "trp_player", 15),
#         (troop_set_slot, "trp_player", slot_troop_renown, 10),
#       (else_try),
#         (eq,"$background_type",cb_nomad),
#         (eq,"$character_gender",tf_female),
#         (troop_raise_attribute, "trp_player",ca_strength,1),
#         (troop_raise_attribute, "trp_player",ca_agility,1),
#         (troop_raise_attribute, "trp_player",ca_intelligence,1),
#         (troop_raise_skill, "trp_player","skl_wound_treatment",1),
#         (troop_raise_skill, "trp_player","skl_first_aid",1),
#         (troop_raise_skill, "trp_player","skl_pathfinding",1),
#         (troop_raise_skill, "trp_player","skl_riding",2),
#         (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,5),
#         (troop_raise_proficiency, "trp_player",wpt_archery,20),
#         (troop_raise_proficiency, "trp_player",wpt_throwing,5),
#         (troop_add_item, "trp_player","itm_tab_shield_small_round_a",imod_battered),
# ##        (troop_add_item, "trp_player","itm_javelin",imod_bent),
# ##        (troop_add_item, "trp_player","itm_sickle",imod_plain),
# ##        (troop_add_item, "trp_player","itm_nomad_armor",0),
# ##        (troop_add_item, "trp_player","itm_hide_boots",0),
# ##        (troop_add_item, "trp_player","itm_steppe_horse",0),
# ##        (troop_add_item, "trp_player","itm_grain",0),
#         (troop_add_gold, "trp_player", 20),
#       (else_try),
#         (eq,"$background_type",cb_thief),
#         (troop_raise_attribute, "trp_player",ca_agility,3),
#         (troop_raise_skill, "trp_player","skl_athletics",2),
#         (troop_raise_skill, "trp_player","skl_power_throw",1),
#         (troop_raise_skill, "trp_player","skl_inventory_management",1),
#         (troop_raise_skill, "trp_player","skl_looting",1),
#         (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,20),
#         (troop_raise_proficiency, "trp_player",wpt_throwing,20),
#         (troop_add_item, "trp_player","itm_throwing_knives",0),
# ##        (troop_add_item, "trp_player","itm_stones",0),
# ##        (troop_add_item, "trp_player","itm_cudgel",imod_plain),
# ##        (troop_add_item, "trp_player","itm_dagger",imod_rusty),
# ##        (troop_add_item, "trp_player","itm_shirt",imod_tattered),
# ##        (troop_add_item, "trp_player","itm_black_hood",imod_tattered),
# ##        (troop_add_item, "trp_player","itm_wrapping_boots",imod_ragged),
#         (troop_add_gold, "trp_player", 25),
# ##      (else_try),
# ##        (eq,"$background_type",cb_priest),
# ##        (troop_raise_attribute, "trp_player",ca_strength,1),
# ##        (troop_raise_attribute, "trp_player",ca_intelligence,2),
# ##        (troop_raise_attribute, "trp_player",ca_charisma,1),
# ##        (troop_raise_skill, "trp_player",skl_wound_treatment,1),
# ##        (troop_raise_skill, "trp_player",skl_leadership,1),
# ##        (troop_raise_skill, "trp_player",skl_prisoner_management,1),
# ##        (troop_raise_proficiency, "trp_player",0,10),
# ##        (troop_add_item, "trp_player","itm_robe",0),
# ##        (troop_add_item, "trp_player","itm_wrapping_boots",0),
# ##        (troop_add_item, "trp_player","itm_club",0),
# ##        (troop_add_item, "trp_player","itm_smoked_fish",0),
# ##        (troop_add_item, "trp_player","itm_sumpter_horse",0),
# ##        (troop_add_gold, "trp_player", 10),
# ##        (troop_set_slot, "trp_player", slot_troop_renown, 10),
#       (try_end),
#
#     (try_begin),
#         (eq,"$background_answer_2",cb2_page),
#         (troop_raise_attribute, "trp_player",ca_charisma,1),
#         (troop_raise_attribute, "trp_player",ca_strength,1),
#         (troop_raise_skill, "trp_player","skl_power_strike",1),
#         (troop_raise_skill, "trp_player","skl_persuasion",1),
#         (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,15),
#         (troop_raise_proficiency, "trp_player",wpt_polearm,5),
#     (else_try),
#         (eq,"$background_answer_2",cb2_apprentice),
#         (troop_raise_attribute, "trp_player",ca_intelligence,1),
#         (troop_raise_attribute, "trp_player",ca_strength,1),
#         (troop_raise_skill, "trp_player","skl_engineer",1),
#         (troop_raise_skill, "trp_player","skl_trade",1),
#     (else_try),
#         (eq,"$background_answer_2",cb2_urchin),
#         (troop_raise_attribute, "trp_player",ca_agility,1),
#         (troop_raise_attribute, "trp_player",ca_intelligence,1),
#         (troop_raise_skill, "trp_player","skl_spotting",1),
#         (troop_raise_skill, "trp_player","skl_looting",1),
#         (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,15),
#         (troop_raise_proficiency, "trp_player",wpt_throwing,5),
#     (else_try),
#         (eq,"$background_answer_2",cb2_steppe_child),
#         (troop_raise_attribute, "trp_player",ca_strength,1),
#         (troop_raise_attribute, "trp_player",ca_agility,1),
#         (troop_raise_skill, "trp_player","skl_horse_archery",1),
#         (troop_raise_skill, "trp_player","skl_power_throw",1),
#         (troop_raise_proficiency, "trp_player",wpt_archery,15),
#         (call_script,"script_change_troop_renown", "trp_player", 5),
#     (else_try),
#         (eq,"$background_answer_2",cb2_merchants_helper),
#         (troop_raise_attribute, "trp_player",ca_intelligence,1),
#         (troop_raise_attribute, "trp_player",ca_charisma,1),
#         (troop_raise_skill, "trp_player","skl_inventory_management",1),
#         (troop_raise_skill, "trp_player","skl_trade",1),
# ##	(else_try),
# ##        (eq,"$background_answer_2",5),
# ##        (troop_raise_attribute, "trp_player",ca_intelligence,1),
# ##        (troop_raise_attribute, "trp_player",ca_charisma,1),
# ##        (troop_raise_skill, "trp_player",skl_leadership,1),
# ##        (troop_raise_skill, "trp_player",skl_athletics,1),
# ##        (troop_raise_skill, "trp_player",skl_riding,1),
# ##        (troop_raise_proficiency, "trp_player",1,5),
# ##        (troop_raise_proficiency, "trp_player",2,5),
# ##        (call_script,"script_change_troop_renown", "trp_player", 15),
# ##	(else_try),
# ##        (eq,"$background_answer_2",6),
# ##        (troop_raise_attribute, "trp_player",ca_charisma,3),
# ##        (troop_raise_attribute, "trp_player",ca_agility,1),
# ##        (troop_raise_skill, "trp_player",skl_weapon_master,1),
# ##        (troop_raise_proficiency, "trp_player",0,15),
# ##        (troop_raise_proficiency, "trp_player",2,10),
# ##        (troop_raise_proficiency, "trp_player",4,10),
# ##        (call_script,"script_change_troop_renown", "trp_player", 20),
# ##	(else_try),
# ##        (eq,"$background_answer_2",7),
# ##        (troop_raise_attribute, "trp_player",ca_intelligence,1),
# ##        (troop_raise_attribute, "trp_player",ca_charisma,2),
# ##        (troop_raise_skill, "trp_player",skl_leadership,1),
# ##        (troop_raise_skill, "trp_player",skl_tactics,1),
# ##        (troop_raise_proficiency, "trp_player",0,10),
# ##        (troop_raise_proficiency, "trp_player",1,10),
# ##        (call_script,"script_change_troop_renown", "trp_player", 15),
# ##	(else_try),
# ##        (eq,"$background_answer_2",8),
# ##        (troop_raise_attribute, "trp_player",ca_agility,1),
# ##        (troop_raise_attribute, "trp_player",ca_intelligence,1),
# ##        (troop_raise_attribute, "trp_player",ca_charisma,1),
# ##        (troop_raise_skill, "trp_player",skl_leadership,1),
# ##        (troop_raise_skill, "trp_player",skl_surgery,1),
# ##        (troop_raise_skill, "trp_player",skl_first_aid,1),
# ##        (troop_raise_proficiency, "trp_player",2,10),
# ##        (call_script,"script_change_troop_renown", "trp_player", 5),
# 	(try_end),
#
# 	(try_begin),
# ##        (eq,"$background_answer_3",1),
# ##        (troop_raise_attribute, "trp_player",ca_strength,1),
# ##        (troop_raise_skill, "trp_player",skl_power_strike,1),
# ##        (troop_raise_skill, "trp_player",skl_shield,1),
# ##        (troop_add_gold, "trp_player", 10),
# ##        (try_begin),
# ##        (this_or_next|player_has_item,"itm_sword"),
# ##        (troop_has_item_equipped,"trp_player","itm_sword"),
# ##        (troop_remove_item, "trp_player","itm_sword"),
# ##        (try_end),
# ##        (try_begin),
# ##        (this_or_next|player_has_item,"itm_arming_sword"),
# ##        (troop_has_item_equipped,"trp_player","itm_arming_sword"),
# ##        (troop_remove_item, "trp_player","itm_arming_sword"),
# ##        (try_end),
# ##        (troop_add_item, "trp_player","itm_short_sword",0),
# ##        (troop_add_item, "trp_player","itm_wooden_shield",imod_battered),
# ##        (troop_raise_proficiency, "trp_player",0,10),
# ##        (troop_raise_proficiency, "trp_player",4,10),
# ##    (else_try),
# ##        (eq,"$background_answer_3",2),
# ##        (troop_raise_attribute, "trp_player",ca_agility,1),
# ##        (troop_raise_skill, "trp_player",skl_weapon_master,1),
# ##        (troop_raise_skill, "trp_player",skl_shield,1),
# ##        (try_begin),
# ##        (this_or_next|player_has_item,"itm_hide_boots"),
# ##        (troop_has_item_equipped,"trp_player","itm_hide_boots"),
# ##        (troop_remove_item, "trp_player","itm_hide_boots"),
# ##        (try_end),
# ##        (troop_add_item, "trp_player","itm_khergit_guard_helmet",imod_crude),
# ##        (troop_add_item, "trp_player","itm_mail_chausses",imod_crude),
# ##        (troop_add_item, "trp_player","itm_sword_khergit_1",imod_plain),
# ##        (troop_add_gold, "trp_player", 20),
# ##        (troop_raise_proficiency, "trp_player",2,20),
# ##    (else_try),
#         (eq,"$background_answer_3",cb3_poacher),
#         (troop_raise_attribute, "trp_player",ca_strength,1),
#         (troop_raise_attribute, "trp_player",ca_agility,1),
#         (troop_raise_skill, "trp_player","skl_power_draw",1),
#         (troop_raise_skill, "trp_player","skl_tracking",1),
#         (troop_raise_skill, "trp_player","skl_spotting",1),
#         (troop_raise_skill, "trp_player","skl_athletics",1),
#         (troop_add_gold, "trp_player", 10),
#         (troop_raise_proficiency, "trp_player",wpt_polearm,10),
#         (troop_raise_proficiency, "trp_player",wpt_archery,35),
#
#         (troop_add_item, "trp_player","itm_axe",imod_chipped),
#         (troop_add_item, "trp_player","itm_rawhide_coat",0),
#         (troop_add_item, "trp_player","itm_hide_boots",0),
#         (troop_add_item, "trp_player","itm_hunting_bow",0),
#         (troop_add_item, "trp_player","itm_barbed_arrows",0),
#         (troop_add_item, "trp_player","itm_sumpter_horse",imod_heavy),
#         (troop_add_item, "trp_player","itm_dried_meat",0),
#         (troop_add_item, "trp_player","itm_dried_meat",0),
#         (troop_add_item, "trp_player","itm_furs",0),
#         (troop_add_item, "trp_player","itm_furs",0),
#     (else_try),
#         (eq,"$background_answer_3",cb3_craftsman),
#         (troop_raise_attribute, "trp_player",ca_strength,1),
#         (troop_raise_attribute, "trp_player",ca_intelligence,1),
#
#         (troop_raise_skill, "trp_player","skl_weapon_master",1),
#         (troop_raise_skill, "trp_player","skl_engineer",1),
#         (troop_raise_skill, "trp_player","skl_tactics",1),
#         (troop_raise_skill, "trp_player","skl_trade",1),
#
#         (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,15),
#         (troop_add_gold, "trp_player", 100),
#
#
#         (troop_add_item, "trp_player","itm_leather_boots",imod_ragged),
#         (troop_add_item, "trp_player","itm_coarse_tunic",0),
#
#         (troop_add_item, "trp_player","itm_sword_medieval_b", imod_balanced),
#         (troop_add_item, "trp_player","itm_hunting_crossbow",0),
#         (troop_add_item, "trp_player","itm_bolts",0),
#
#         (troop_add_item, "trp_player","itm_tools",0),
#         (troop_add_item, "trp_player","itm_saddle_horse",0),
#         (troop_add_item, "trp_player","itm_smoked_fish",0),
#     (else_try),
#         (eq,"$background_answer_3",cb3_peddler),
#         (troop_raise_attribute, "trp_player",ca_charisma,1),
#         (troop_raise_attribute, "trp_player",ca_intelligence,1),
#         (troop_raise_skill, "trp_player","skl_riding",1),
#         (troop_raise_skill, "trp_player","skl_trade",1),
#         (troop_raise_skill, "trp_player","skl_pathfinding",1),
#         (troop_raise_skill, "trp_player","skl_inventory_management",1),
#
#         (troop_add_item, "trp_player","itm_leather_gloves",imod_plain),
#         (troop_add_gold, "trp_player", 90),
#         (troop_raise_proficiency, "trp_player",wpt_polearm,15),
#
#         (troop_add_item, "trp_player","itm_leather_jacket",0),
#         (troop_add_item, "trp_player","itm_leather_boots",imod_ragged),
#         (troop_add_item, "trp_player","itm_fur_hat",0),
#         (troop_add_item, "trp_player","itm_staff",0),
#         (troop_add_item, "trp_player","itm_hunting_crossbow",0),
#         (troop_add_item, "trp_player","itm_bolts",0),
#         (troop_add_item, "trp_player","itm_saddle_horse",0),
#         (troop_add_item, "trp_player","itm_sumpter_horse",0),
#
#         (troop_add_item, "trp_player","itm_linen",0),
#         (troop_add_item, "trp_player","itm_pottery",0),
#         (troop_add_item, "trp_player","itm_wool",0),
#         (troop_add_item, "trp_player","itm_wool",0),
#         (troop_add_item, "trp_player","itm_smoked_fish",0),
# ##    (else_try),
# ##        (eq,"$background_answer_3",6),
# ##        (troop_raise_attribute, "trp_player",ca_strength,1),
# ##        (troop_raise_attribute, "trp_player",ca_charisma,1),
# ##        (troop_raise_skill, "trp_player",skl_shield,1),
# ##        (troop_raise_skill, "trp_player",skl_wound_treatment,1),
# ##        (troop_raise_skill, "trp_player",skl_first_aid,1),
# ##        (troop_raise_skill, "trp_player",skl_surgery,1),
# ##        (troop_add_item, "trp_player","itm_leather_gloves",imod_ragged),
# ##        (troop_add_item, "trp_player","itm_quarter_staff",imod_heavy),
# ##        (troop_add_item, "trp_player","itm_black_hood",0),
# ##        (troop_add_gold, "trp_player", 10),
# ##        (troop_raise_proficiency, "trp_player",2,20),
#     (else_try),
#         (eq,"$background_answer_3",cb3_troubadour),
#         (troop_raise_attribute, "trp_player",ca_charisma,2),
#
#         (troop_raise_skill, "trp_player","skl_weapon_master",1),
#         (troop_raise_skill, "trp_player","skl_persuasion",1),
#         (troop_raise_skill, "trp_player","skl_leadership",1),
#         (troop_raise_skill, "trp_player","skl_pathfinding",1),
#
#         (troop_add_gold, "trp_player", 80),
#         (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,25),
#         (troop_raise_proficiency, "trp_player",wpt_crossbow,10),
#
#         (troop_add_item, "trp_player","itm_tabard",imod_sturdy),
#         (troop_add_item, "trp_player","itm_leather_boots",imod_ragged),
#         (troop_add_item, "trp_player","itm_sword_medieval_a", imod_rusty),
#         (troop_add_item, "trp_player","itm_hunting_crossbow", 0),
#         (troop_add_item, "trp_player","itm_bolts", 0),
#         (troop_add_item, "trp_player","itm_saddle_horse",imod_swaybacked),
#         (troop_add_item, "trp_player","itm_smoked_fish",0),
#     (else_try),
#         (eq,"$background_answer_3",cb3_squire),
#         (troop_raise_attribute, "trp_player",ca_strength,1),
#         (troop_raise_attribute, "trp_player",ca_agility,1),
#         (troop_raise_skill, "trp_player","skl_riding",1),
#         (troop_raise_skill, "trp_player","skl_weapon_master",1),
#         (troop_raise_skill, "trp_player","skl_power_strike",1),
#         (troop_raise_skill, "trp_player","skl_leadership",1),
#
#         (troop_add_gold, "trp_player", 20),
#         (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,30),
#         (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,30),
#         (troop_raise_proficiency, "trp_player",wpt_polearm,30),
#         (troop_raise_proficiency, "trp_player",wpt_archery,10),
#         (troop_raise_proficiency, "trp_player",wpt_crossbow,10),
#         (troop_raise_proficiency, "trp_player",wpt_throwing,10),
#
#         (troop_add_item, "trp_player","itm_leather_jerkin",imod_ragged),
#         (troop_add_item, "trp_player","itm_leather_boots",imod_tattered),
#
#         (troop_add_item, "trp_player","itm_sword_medieval_a", imod_rusty),
#         (troop_add_item, "trp_player","itm_hunting_crossbow",0),
#         (troop_add_item, "trp_player","itm_bolts",0),
#         (troop_add_item, "trp_player","itm_saddle_horse",imod_swaybacked),
#         (troop_add_item, "trp_player","itm_smoked_fish",0),
#     (else_try),
#         (eq,"$background_answer_3",cb3_lady_in_waiting),
#         (eq,"$character_gender",tf_female),
#         (troop_raise_attribute, "trp_player",ca_intelligence,1),
#         (troop_raise_attribute, "trp_player",ca_charisma,1),
#
#         (troop_raise_skill, "trp_player","skl_persuasion",2),
#         (troop_raise_skill, "trp_player","skl_riding",1),
#         (troop_raise_skill, "trp_player","skl_wound_treatment",1),
#
#         (troop_add_item, "trp_player","itm_dagger", 0),
#         (troop_add_item, "trp_player","itm_hunting_crossbow",0),
#         (troop_add_item, "trp_player","itm_bolts",0),
#         (troop_add_item, "trp_player","itm_courser", imod_spirited),
#         (troop_add_item, "trp_player","itm_woolen_hood",imod_sturdy),
#         (troop_add_item, "trp_player","itm_woolen_dress",imod_sturdy),
#         (troop_add_gold, "trp_player", 100),
#         (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,10),
#         (troop_raise_proficiency, "trp_player",wpt_crossbow,15),
#         (troop_add_item, "trp_player","itm_smoked_fish",0),
#     (else_try),
#         (eq,"$background_answer_3",cb3_student),
#         (troop_raise_attribute, "trp_player",ca_intelligence,2),
#
#         (troop_raise_skill, "trp_player","skl_weapon_master",1),
#         (troop_raise_skill, "trp_player","skl_surgery",1),
#         (troop_raise_skill, "trp_player","skl_wound_treatment",1),
#         (troop_raise_skill, "trp_player","skl_persuasion",1),
#
#         (troop_add_gold, "trp_player", 80),
#         (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,20),
#         (troop_raise_proficiency, "trp_player",wpt_crossbow,20),
#
#         (troop_add_item, "trp_player","itm_linen_tunic",imod_sturdy),
#         (troop_add_item, "trp_player","itm_woolen_hose",0),
#         (troop_add_item, "trp_player","itm_sword_medieval_a", imod_rusty),
#         (troop_add_item, "trp_player","itm_hunting_crossbow", 0),
#         (troop_add_item, "trp_player","itm_bolts", 0),
#         (troop_add_item, "trp_player","itm_saddle_horse",imod_swaybacked),
#         (troop_add_item, "trp_player","itm_smoked_fish",0),
#         (store_random_in_range, ":book_no", books_begin, books_end),
#         (troop_add_item, "trp_player",":book_no",0),
#     (try_end),
#
#       (try_begin),
#         (eq,"$background_answer_4",cb4_revenge),
#         (troop_raise_attribute, "trp_player",ca_strength,2),
#         (troop_raise_skill, "trp_player","skl_power_strike",1),
#       (else_try),
#         (eq,"$background_answer_4",cb4_loss),
#         (troop_raise_attribute, "trp_player",ca_charisma,2),
#         (troop_raise_skill, "trp_player","skl_ironflesh",1),
#       (else_try),
#         (eq,"$background_answer_4",cb4_wanderlust),
#         (troop_raise_attribute, "trp_player",ca_agility,2),
#         (troop_raise_skill, "trp_player","skl_pathfinding",1),
# ##        (else_try),
# ##        (eq,"$background_answer_4",4),
# ##        (troop_raise_attribute, "trp_player",ca_charisma,1),
# ##        (troop_raise_skill, "trp_player",skl_wound_treatment,1),
# ##        (troop_raise_proficiency, "trp_player",5,10),
#       (else_try),
#         (eq,"$background_answer_4",cb4_disown),
#         (troop_raise_attribute, "trp_player",ca_strength,1),
#         (troop_raise_attribute, "trp_player",ca_intelligence,1),
#         (troop_raise_skill, "trp_player","skl_weapon_master",1),
#       (else_try),
#         (eq,"$background_answer_4",cb4_greed),
#         (troop_raise_attribute, "trp_player",ca_agility,1),
#         (troop_raise_attribute, "trp_player",ca_intelligence,1),
#         (troop_raise_skill, "trp_player","skl_looting",1),
#       (try_end),
#
#
#            (try_begin),
#              (eq, "$background_type", cb_noble),
#              (jump_to_menu, "mnu_auto_return"),
# #normal_banner_begin
#              (start_presentation, "prsnt_banner_selection"),
# #custom_banner_begin
# #             (start_presentation, "prsnt_custom_banner"),
#            (else_try),
#              (change_screen_return, 0),
#            (try_end),
#            (set_show_messages, 1),
#         ]),
#       ("go_back_dot",[],"Go back.",[
#         (jump_to_menu,"mnu_start_character_4"),
#         ]),
#     ]
#   ),
#
#   (
#     "past_life_explanation",mnf_disable_all_keys,
#     "{s3}",
#     "none",
#     [
#      (try_begin),
#        (gt,"$current_string_reg",14),
#        (assign,"$current_string_reg",10),
#      (try_end),
#      (str_store_string_reg,s3,"$current_string_reg"),
#      (try_begin),
#        (ge,"$current_string_reg",14),
#        (str_store_string,s5,"@Back to the beginning..."),
#      (else_try),
#        (str_store_string,s5,"@View next segment..."),
#      (try_end),
#      ],
#     [
#       ("view_next",[],"{s5}",[
#         (val_add,"$current_string_reg",1),
#         (jump_to_menu, "mnu_past_life_explanation"),
#         ]),
#       ("continue",[],"Continue...",
#        [
#         ]),
#       ("go_back_dot",[],"Go back.",[
#         (jump_to_menu, "mnu_choose_skill"),
#         ]),
#     ]
#   ),
#
#   (
#     "auto_return",0,
#     "{!}This menu automatically returns to caller.",
#     "none",
#     [(change_screen_return, 0)],
#     [
#     ]
#   ),
#   ("morale_report",0,
#    "{s1}",
#    "none",
#    [
#      (call_script, "script_get_player_party_morale_values"),
#
#      (assign, ":target_morale", reg0),
#      (assign, reg1, "$g_player_party_morale_modifier_party_size"),
#      (try_begin),
#        (gt, reg1, 0),
#        (str_store_string, s2, "@{!} -"),
#      (else_try),
#        (str_store_string, s2, "str_space"),
#      (try_end),
#
#      (assign, reg2, "$g_player_party_morale_modifier_leadership"),
#      (try_begin),
#        (gt, reg2, 0),
#        (str_store_string, s3, "@{!} +"),
#      (else_try),
#        (str_store_string, s3, "str_space"),
#      (try_end),
#
#      (try_begin),
#        (gt, "$g_player_party_morale_modifier_no_food", 0),
#        (assign, reg7, "$g_player_party_morale_modifier_no_food"),
#        (str_store_string, s5, "@^No food:  -{reg7}"),
#      (else_try),
#        (str_store_string, s5, "str_space"),
#      (try_end),
#      (assign, reg3, "$g_player_party_morale_modifier_food"),
#      (try_begin),
#        (gt, reg3, 0),
#        (str_store_string, s4, "@{!} +"),
#      (else_try),
#        (str_store_string, s4, "str_space"),
#      (try_end),
#
#      (try_begin),
#        (gt, "$g_player_party_morale_modifier_debt", 0),
#        (assign, reg6, "$g_player_party_morale_modifier_debt"),
#        (str_store_string, s6, "@^Wage debt:  -{reg6}"),
#      (else_try),
#        (str_store_string, s6, "str_space"),
#      (try_end),
#
#      (party_get_morale, reg5, "p_main_party"),
#      (store_sub, reg4, reg5, ":target_morale"),
#      (try_begin),
#        (gt, reg4, 0),
#        (str_store_string, s7, "@{!} +"),
#      (else_try),
#        (str_store_string, s7, "str_space"),
#      (try_end),
#
#      (assign, reg6, 50),
#
#      (str_store_string, s1, "str_current_party_morale_is_reg5_current_party_morale_modifiers_are__base_morale__50_party_size_s2reg1_leadership_s3reg2_food_variety_s4reg3s5s6_recent_events_s7reg4_total__reg5___"),
#
#      (try_for_range, ":kingdom_no", npc_kingdoms_begin, npc_kingdoms_end),
#        (faction_get_slot, ":faction_morale", ":kingdom_no",  slot_faction_morale_of_player_troops),
#        (val_div, ":faction_morale", 100),
#        (neq, ":faction_morale", 0),
#        (assign, reg6, ":faction_morale"),
#        (str_store_faction_name, s9, ":kingdom_no"),
#        (str_store_string, s1, "str_s1extra_morale_for_s9_troops__reg6_"),
#      (try_end),
#     ],
#     [
#       ("continue",[],"Continue...",
#       [
#         (jump_to_menu, "mnu_reports"),
#       ]),
#     ]
#   ),
#
#
#   ("courtship_relations",0,
#    "{s1}",
#    "none",
#    [(str_store_string, s1, "str_courtships_in_progress_"),
#     (try_for_range, ":lady", kingdom_ladies_begin, kingdom_ladies_end),
# 		(troop_slot_eq, ":lady", slot_troop_met, 2),
# 		(call_script, "script_troop_get_relation_with_troop", "trp_player", ":lady"),
# 		(gt, reg0, 0),
# 		(assign, reg3, reg0),
#
# 		(str_store_troop_name, s2, ":lady"),
#
# 		(store_current_hours, ":hours_since_last_visit"),
# 		(troop_get_slot, ":last_visit_hour", ":lady", slot_troop_last_talk_time),
# 		(val_sub, ":hours_since_last_visit", ":last_visit_hour"),
# 		(store_div, ":days_since_last_visit", ":hours_since_last_visit", 24),
# 		(assign, reg4, ":days_since_last_visit"),
#
# 		(str_store_string, s1, "str_s1_s2_relation_reg3_last_visit_reg4_days_ago"),
# 	(try_end),
#
# 	(str_store_string, s1, "str_s1__poems_known"),
# 	(try_begin),
# 		 (gt, "$allegoric_poem_recitations", 0),
# 		 (str_store_string, s1, "str_s1_storming_the_castle_of_love_allegoric"),
# 	(try_end),
# 	(try_begin),
# 		 (gt, "$tragic_poem_recitations", 0),
# 		 (str_store_string, s1, "str_s1_kais_and_layali_tragic"),
# 	(try_end),
# 	(try_begin),
# 		 (gt, "$comic_poem_recitations", 0),
# 		 (str_store_string, s1, "str_s1_a_conversation_in_the_garden_comic"),
# 	(try_end),
# 	(try_begin),
# 		 (gt, "$heroic_poem_recitations", 0),
# 		 (str_store_string, s1, "str_s1_helgered_and_kara_epic"),
# 	(try_end),
# 	(try_begin),
# 		 (gt, "$mystic_poem_recitations", 0),
# 		 (str_store_string, s1, "str_s1_a_hearts_desire_mystic"),
# 	(try_end),
#
#     ],
#     [
#       ("continue",[],"Continue...",
#        [(jump_to_menu, "mnu_reports"),
#         ]
#        ),
#       ]
#   ),
#
#
#   ("lord_relations",0,
#    "{s1}",
#    "none",
#    [
#     (try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
# 		(troop_set_slot, ":active_npc", slot_troop_temp_slot, 0),
# 	(try_end),
#
# 	(str_clear, s1),
#     (try_for_range, ":unused", active_npcs_begin, active_npcs_end),
# 		(assign, ":score_to_beat", -100),
# 		(assign, ":best_relation_remaining_npc", -1),
# 		(try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
# 			(troop_slot_eq, ":active_npc", slot_troop_temp_slot, 0),
# 			(troop_slot_eq, ":active_npc", slot_troop_occupation, slto_kingdom_hero),
# 			(troop_slot_ge, ":active_npc", slot_troop_met, 1),
#
# 			(call_script, "script_troop_get_player_relation", ":active_npc"),
# 			(assign, ":relation_with_player", reg0),
# 			(ge, ":relation_with_player", ":score_to_beat"),
#
# 			(assign, ":score_to_beat", ":relation_with_player"),
# 			(assign, ":best_relation_remaining_npc", ":active_npc"),
# 		(try_end),
# 		(gt, ":best_relation_remaining_npc", -1),
#
# 		(str_store_troop_name_link, s4, ":best_relation_remaining_npc"),
# 		(assign, reg4, ":score_to_beat"),
# 		(str_store_string, s1, "@{!}{s1}^{s4}: {reg4}"),
# 		(troop_set_slot, ":best_relation_remaining_npc", slot_troop_temp_slot, 1),
# 	(try_end),
#
#
#     ],
#     [
#       ("continue",[],"Continue...",
#        [(jump_to_menu, "mnu_reports"),
#         ]
#        ),
#       ]
#   ),
#
#
#
#   ("companion_report",0,
#    "{s7}{s1}",
#    "none",
#    [
#    (str_clear, s1),
#    (str_store_string, s7, "str_no_companions_in_service"),
#
#    (try_begin),
# 	(troop_get_slot, ":spouse_or_betrothed", "trp_player", slot_troop_spouse),
# 	(try_begin),
# 		(troop_get_type, ":is_female", "trp_player"),
# 		(eq, ":is_female", 1),
# 		(str_store_string, s8, "str_husband"),
# 	(else_try),
# 		(str_store_string, s8, "str_wife"),
# 	(try_end),
#
# 	(try_begin),
# 		(le, ":spouse_or_betrothed", 0),
# 		(troop_get_slot, ":spouse_or_betrothed", "trp_player", slot_troop_betrothed),
# 		(str_store_string, s8, "str_betrothed"),
# 	(try_end),
# 	(gt, ":spouse_or_betrothed", 0),
#
# 	(str_store_troop_name, s4, ":spouse_or_betrothed"),
# 	(troop_get_slot, ":cur_center", ":spouse_or_betrothed", slot_troop_cur_center),
# 	(try_begin),
# 		(is_between, ":cur_center", centers_begin, centers_end),
# 		(str_store_party_name, s5, ":cur_center"),
# 	(else_try),
# 		(troop_slot_eq, ":spouse_or_betrothed", slot_troop_occupation, slto_kingdom_hero),
# 		(str_store_string, s5, "str_leading_party"),
# 	(else_try),
# 		(str_store_string, s5, "str_whereabouts_unknown"),
#     (try_end),
# 	(str_store_string, s3, "str_s4_s8_s5"),
# 	(str_store_string, s2, s1),
# 	(str_store_string, s1, "str_s2_s3"),
#
#    (try_end),
#
#
#    (try_begin),
#     (ge, "$cheat_mode", 1),
# 	(ge, "$npc_to_rejoin_party", 0),
#     (str_store_troop_name, s5, "$npc_to_rejoin_party"),
# 	(str_store_string, s1, "@{!}DEBUG -- {s1}^NPC in rejoin queue: {s5}^"),
#    (try_end),
#
#
#    (try_for_range, ":companion", companions_begin, companions_end),
# 		(str_clear, s2),
# 		(str_clear, s3),
#
# 		(try_begin),
# 			(troop_get_slot, ":days_left", ":companion", slot_troop_days_on_mission),
#
# 			(troop_slot_eq, ":companion", slot_troop_occupation, slto_player_companion),
#
#
# 			(str_store_troop_name, s4, ":companion"),
#
# 			(try_begin),
# 				(troop_slot_eq, ":companion", slot_troop_current_mission, npc_mission_kingsupport),
# 				(str_store_string, s8, "str_gathering_support"),
# 				(try_begin),
# 					(eq, ":days_left", 1),
# 					(str_store_string, s5, "str_expected_back_imminently"),
# 				(else_try),
# 					(assign, reg3, ":days_left"),
# 					(str_store_string, s5, "str_expected_back_in_approximately_reg3_days"),
# 				(try_end),
# 			(else_try),
# 				(troop_slot_eq, ":companion", slot_troop_current_mission, npc_mission_gather_intel),
# 				(troop_get_slot, ":town_with_contacts", ":companion", slot_troop_town_with_contacts),
# 				(str_store_party_name, s11, ":town_with_contacts"),
#
# 				(str_store_string, s8, "str_gathering_intelligence"),
# 				(try_begin),
# 					(eq, ":days_left", 1),
# 					(str_store_string, s5, "str_expected_back_imminently"),
# 				(else_try),
# 					(assign, reg3, ":days_left"),
# 					(str_store_string, s5, "str_expected_back_in_approximately_reg3_days"),
# 				(try_end),
# 			(else_try),	#This covers most diplomatic missions
#
# 				(troop_slot_ge, ":companion", slot_troop_current_mission, npc_mission_peace_request),
# 				(neg|troop_slot_ge, ":companion", slot_troop_current_mission, 8),
#
# 				(troop_get_slot, ":faction", ":companion", slot_troop_mission_object),
# 				(str_store_faction_name, s9, ":faction"),
# 				(str_store_string, s8, "str_diplomatic_embassy_to_s9"),
# 				(try_begin),
# 					(eq, ":days_left", 1),
# 					(str_store_string, s5, "str_expected_back_imminently"),
# 				(else_try),
# 					(assign, reg3, ":days_left"),
# 					(str_store_string, s5, "str_expected_back_in_approximately_reg3_days"),
# 				(try_end),
# 			(else_try),
# 				(eq, ":companion", "$g_player_minister"),
# 				(str_store_string, s8, "str_serving_as_minister"),
# 				(try_begin),
# 					(is_between, "$g_player_court", centers_begin, centers_end),
# 					(str_store_party_name, s9, "$g_player_court"),
# 					(str_store_string, s5, "str_in_your_court_at_s9"),
# 				(else_try),
# 					(str_store_string, s5, "str_whereabouts_unknown"),
# 				(try_end),
# 			(else_try),
# 				(main_party_has_troop, ":companion"),
# 				(str_store_string, s8, "str_under_arms"),
# 				(str_store_string, s5, "str_in_your_party"),
# 			(else_try),
# 				(troop_slot_eq, ":companion", slot_troop_current_mission, npc_mission_rejoin_when_possible),
# 				(str_store_string, s8, "str_attempting_to_rejoin_party"),
# 				(str_store_string, s5, "str_whereabouts_unknown"),
# 			(else_try),	#Companions who are in a center
# 				(troop_slot_ge, ":companion", slot_troop_cur_center, 1),
#
# 				(str_store_string, s8, "str_separated_from_party"),
# 				(str_store_string, s5, "str_whereabouts_unknown"),
# 	        (else_try), #Excludes companions who have occupation = retirement
#                 (try_begin),
#                   (check_quest_active, "qst_lend_companion"),
#                   (quest_slot_eq, "qst_lend_companion", slot_quest_target_troop, ":companion"),
#                   (str_store_string, s8, "@On loan,"),
#                 (else_try),
#                   (check_quest_active, "qst_lend_surgeon"),
#                   (quest_slot_eq, "qst_lend_surgeon", slot_quest_target_troop, ":companion"),
#                   (str_store_string, s8, "@On loan,"),
#                 (else_try),
# 				  (troop_set_slot, ":companion", slot_troop_current_mission, npc_mission_rejoin_when_possible),
#                   (str_store_string, s8, "str_attempting_to_rejoin_party"),
#                 (try_end),
#
# 	        	(str_store_string, s5, "str_whereabouts_unknown"),
# 				(try_begin),
# 					(ge, "$cheat_mode", 1),
# 					(troop_get_slot, reg2, ":companion", slot_troop_current_mission),
# 					(troop_get_slot, reg3, ":companion", slot_troop_days_on_mission),
# 					(troop_get_slot, reg4, ":companion", slot_troop_prisoner_of_party),
# 					(troop_get_slot, reg4, ":companion", slot_troop_playerparty_history),
#
# 					(display_message, "@{!}DEBUG: {s4} current mission: {reg2}, days on mission: {reg3}, prisoner: {reg4}, pphistory: {reg5}"),
# 				(try_end),
# 			(try_end),
#
# 			(str_store_string, s3, "str_s4_s8_s5"),
#
# 			(str_store_string, s2, s1),
# 			(str_store_string, s1, "str_s2_s3"),
#
# 			(str_clear, s7), #"no companions in service"
# 		(else_try),
# 			(neg|troop_slot_eq, ":companion", slot_troop_occupation, slto_kingdom_hero),
# 			(troop_slot_ge, ":companion", slot_troop_prisoner_of_party, centers_begin),
#
# 			(str_store_troop_name, s4, ":companion"),
# 			(str_store_string, s8, "str_missing_after_battle"),
# 			(str_store_string, s5, "str_whereabouts_unknown"),
#
# 			(str_store_string, s3, "str_s4_s8_s5"),
# 			(str_store_string, s2, s1),
# 			(str_store_string, s1, "str_s2_s3"),
# 			(str_clear, s7), #"no companions in service"
#
# 		(try_end),
#
#    (try_end),
#
#
#     ],
#     [
#       ("continue",[],"Continue...",
#        [(jump_to_menu, "mnu_reports"),
#         ]
#        ),
#       ]
#   ),
#
#
#
#
#
#
#
#   ("character_report",0,
#    "{s9}",
#    "none",
#    [(try_begin),
#       (gt, "$g_player_reading_book", 0),
#       (player_has_item, "$g_player_reading_book"),
#       (str_store_item_name, s8, "$g_player_reading_book"),
#       (str_store_string, s9, "@You are currently reading {s8}."),
#     (else_try),
#       (assign, "$g_player_reading_book", 0),
#       (str_store_string, s9, "@You are not reading any books."),
#     (try_end),
#     (assign, ":num_friends", 0),
#     (assign, ":num_enemies", 0),
#     (str_store_string, s6, "@none"),
#     (str_store_string, s8, "@none"),
#     (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
# 	  (this_or_next|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
# 		(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_inactive_pretender),
# 	  (call_script, "script_troop_get_player_relation", ":troop_no"),
#       (assign, ":player_relation", reg0),
#       #(troop_get_slot, ":player_relation", ":troop_no", slot_troop_player_relation),
#       (try_begin),
#         (gt, ":player_relation", 20),
#         (try_begin),
#           (eq, ":num_friends", 0),
#           (str_store_troop_name, s8, ":troop_no"),
#         (else_try),
#           (eq, ":num_friends", 1),
#           (str_store_troop_name, s7, ":troop_no"),
#           (str_store_string, s8, "@{s7} and {s8}"),
#         (else_try),
#           (str_store_troop_name, s7, ":troop_no"),
#           (str_store_string, s8, "@{!}{s7}, {s8}"),
#         (try_end),
#         (val_add, ":num_friends", 1),
#       (else_try),
#         (lt, ":player_relation", -20),
#         (try_begin),
#           (eq, ":num_enemies", 0),
#           (str_store_troop_name, s6, ":troop_no"),
#         (else_try),
#           (eq, ":num_enemies", 1),
#           (str_store_troop_name, s5, ":troop_no"),
#           (str_store_string, s6, "@{s5} and {s6}"),
#         (else_try),
#           (str_store_troop_name, s5, ":troop_no"),
#           (str_store_string, s6, "@{!}{s5}, {s6}"),
#         (try_end),
#         (val_add, ":num_enemies", 1),
#       (try_end),
#     (try_end),
#
# 	#lord recruitment changes begin
# 	(str_clear, s12),
# 	(try_begin),
# 		(gt, "$player_right_to_rule", 0),
# 		(assign, reg12, "$player_right_to_rule"),
# 		(str_store_string, s12, "str__right_to_rule_reg12"),
# 	(try_end),
#
# 	(str_clear, s15),
# 	(try_begin),
# 		(this_or_next|gt, "$claim_arguments_made", 0),
# 		(this_or_next|gt, "$ruler_arguments_made", 0),
# 		(this_or_next|gt, "$victory_arguments_made", 0),
# 		(this_or_next|gt, "$lords_arguments_made", 0),
# 		(eq, 1, 0),
#
# 		(assign, reg3, "$claim_arguments_made"),
# 		(assign, reg4, "$ruler_arguments_made"),
# 		(assign, reg5, "$victory_arguments_made"),
# 		(assign, reg6, "$lords_arguments_made"),
# 		(assign, reg7, "$benefit_arguments_made"),
#
# 		(str_store_string, s15, "str_political_arguments_made_legality_reg3_rights_of_lords_reg4_unificationpeace_reg5_rights_of_commons_reg6_fief_pledges_reg7"),
# 	(try_end),
#
# 	#lord recruitment changes begin
#
#     (assign, reg3, "$player_honor"),
#     (troop_get_slot, reg2, "trp_player", slot_troop_renown),
#
#     (str_store_string, s9, "str_renown_reg2_honour_rating_reg3s12_friends_s8_enemies_s6_s9"),
#
#     (call_script, "script_get_number_of_hero_centers", "trp_player"),
#     (assign, ":no_centers", reg0),
#     (try_begin),
#       (gt, ":no_centers", 0),
#       (try_for_range, ":i_center", 0, ":no_centers"),
#         (call_script, "script_troop_get_leaded_center_with_index", "trp_player", ":i_center"),
#         (assign, ":cur_center", reg0),
#         (try_begin),
#           (eq, ":i_center", 0),
#           (str_store_party_name, s8, ":cur_center"),
#         (else_try),
#           (eq, ":i_center", 1),
#           (str_store_party_name, s7, ":cur_center"),
#           (str_store_string, s8, "@{s7} and {s8}"),
#         (else_try),
#           (str_store_party_name, s7, ":cur_center"),
#           (str_store_string, s8, "@{!}{s7}, {s8}"),
#         (try_end),
#       (try_end),
#       (str_store_string, s9, "@Your estates are: {s8}.^{s9}"),
#     (try_end),
#     (try_begin),
#       (gt, "$players_kingdom", 0),
#
#       (str_store_faction_name, s8, "$players_kingdom"),
#       (try_begin),
#         (this_or_next|is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
#         (neg|faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
#         #(str_store_string, s9, "@You are a lord of {s8}.^{s9}"),
#         (str_store_string, s9, "str_you_are_a_lord_lady_of_s8_s9"),
#       (else_try),
#         (str_store_string, s9, "str_you_are_king_queen_of_s8_s9"),
#       (try_end),
#
#     (try_end),
#     ],
#     [
#
# 	#lord recruitment changes begin
#
# 	("continue",[(eq,"$cheat_mode",1)],"{!}CHEAT! - increase Right to Rule",
#        [
# 	   (val_add, "$player_right_to_rule", 10),
# 	   (jump_to_menu, "mnu_character_report"),
#        ]
#        ),
#
#
# 	("continue",[(eq,"$cheat_mode",1),
# 		(str_store_troop_name, s14, "$g_talk_troop"),
# 	],"{!}CHEAT! - increase your relation with {s14}",
#        [
# 	   (call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 10),
# 	   (jump_to_menu, "mnu_character_report"),
#        ]
#        ),
#
#
# 	("continue",[(eq,"$cheat_mode",1)],"{!}CHEAT! - increase honor",
#        [
# 	   (val_add, "$player_honor", 10),
# 	   (jump_to_menu, "mnu_character_report"),
#        ]
#        ),
#
# 	("continue",[(eq,"$cheat_mode",1)],"{!}CHEAT! - increase renown",
#        [
# 	   (troop_get_slot, ":renown", "trp_player", slot_troop_renown),
# 	   (val_add, ":renown", 50),
# 	   (troop_set_slot, "trp_player", slot_troop_renown, ":renown"),
#
# 	   (jump_to_menu, "mnu_character_report"),
#        ]
#        ),
#
# 	("continue",[(eq,"$cheat_mode",1)],"{!}CHEAT! - increase persuasion",
#        [
# 	   (troop_raise_skill, "trp_player", "skl_persuasion", 1),
#
# 	   (jump_to_menu, "mnu_character_report"),
#        ]
#        ),
#
#
#
# 	("continue",[],"Continue...",
#        [(jump_to_menu, "mnu_reports"),
#         ]
#        ),
#
# 	#lord recruitment changes end
#
# 	   ]
#   ),
#
#   ("party_size_report",0,
#    "{s1}",
#    "none",
#    [(call_script, "script_game_get_party_companion_limit"),
#     (assign, ":party_size_limit", reg0),
#
#     (store_skill_level, ":leadership", "skl_leadership", "trp_player"),
#     (val_mul, ":leadership", 5),
#     (store_attribute_level, ":charisma", "trp_player", ca_charisma),
#
#     (troop_get_slot, ":renown", "trp_player", slot_troop_renown),
#     (val_div, ":renown", 25),
#     (try_begin),
#       (gt, ":leadership", 0),
#       (str_store_string, s2, "@{!} +"),
#     (else_try),
#       (str_store_string, s2, "str_space"),
#     (try_end),
#     (try_begin),
#       (gt, ":charisma", 0),
#       (str_store_string, s3, "@{!} +"),
#     (else_try),
#       (str_store_string, s3, "str_space"),
#     (try_end),
#     (try_begin),
#       (gt, ":renown", 0),
#       (str_store_string, s4, "@{!} +"),
#     (else_try),
#       (str_store_string, s4, "str_space"),
#     (try_end),
#     (assign, reg5, ":party_size_limit"),
#     (assign, reg1, ":leadership"),
#     (assign, reg2, ":charisma"),
#     (assign, reg3, ":renown"),
#     (str_store_string, s1, "@Current party size limit is {reg5}.^Current party size modifiers are:^^Base size:  +30^Leadership: {s2}{reg1}^Charisma: {s3}{reg2}^Renown: {s4}{reg3}^TOTAL:  {reg5}"),
#     ],
#     [
#       ("continue",[],"Continue...",
#        [(jump_to_menu, "mnu_reports"),
#         ]
#        ),
#       ]
#   ),
#
#   ("faction_relations_report",0,
#    "{s1}",
#    "none",
#    [(str_clear, s2),
#     (try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
#       (faction_slot_eq, ":cur_kingdom", slot_faction_state, sfs_active),
#       (neq, ":cur_kingdom", "fac_player_supporters_faction"),
#       (store_relation, ":cur_relation", "fac_player_supporters_faction", ":cur_kingdom"),
#       (try_begin),
#         (ge, ":cur_relation", 90),
#         (str_store_string, s3, "@Loyal"),
#       (else_try),
#         (ge, ":cur_relation", 80),
#         (str_store_string, s3, "@Devoted"),
#       (else_try),
#         (ge, ":cur_relation", 70),
#         (str_store_string, s3, "@Fond"),
#       (else_try),
#         (ge, ":cur_relation", 60),
#         (str_store_string, s3, "@Gracious"),
#       (else_try),
#         (ge, ":cur_relation", 50),
#         (str_store_string, s3, "@Friendly"),
#       (else_try),
#         (ge, ":cur_relation", 40),
#         (str_store_string, s3, "@Supportive"),
#       (else_try),
#         (ge, ":cur_relation", 30),
#         (str_store_string, s3, "@Favorable"),
#       (else_try),
#         (ge, ":cur_relation", 20),
#         (str_store_string, s3, "@Cooperative"),
#       (else_try),
#         (ge, ":cur_relation", 10),
#         (str_store_string, s3, "@Accepting"),
#       (else_try),
#         (ge, ":cur_relation", 0),
#         (str_store_string, s3, "@Indifferent"),
#       (else_try),
#         (ge, ":cur_relation", -10),
#         (str_store_string, s3, "@Suspicious"),
#       (else_try),
#         (ge, ":cur_relation", -20),
#         (str_store_string, s3, "@Grumbling"),
#       (else_try),
#         (ge, ":cur_relation", -30),
#         (str_store_string, s3, "@Hostile"),
#       (else_try),
#         (ge, ":cur_relation", -40),
#         (str_store_string, s3, "@Resentful"),
#       (else_try),
#         (ge, ":cur_relation", -50),
#         (str_store_string, s3, "@Angry"),
#       (else_try),
#         (ge, ":cur_relation", -60),
#         (str_store_string, s3, "@Hateful"),
#       (else_try),
#         (ge, ":cur_relation", -70),
#         (str_store_string, s3, "@Revengeful"),
#       (else_try),
#         (str_store_string, s3, "@Vengeful"),
#       (try_end),
#       (str_store_faction_name, s4, ":cur_kingdom"),
#       (assign, reg1, ":cur_relation"),
#       (str_store_string, s2, "@{!}{s2}^{s4}: {reg1} ({s3})"),
#     (try_end),
#     (str_store_string, s1, "@Your relation with the factions are:^{s2}"),
#
#
#
#     ],
#     [
#       ("continue",[],"Continue...",
#        [(jump_to_menu, "mnu_reports"),
#         ]
#        ),
#       ]
#   ),
#
#
#
#
#   (
#     "simple_encounter",mnf_enable_hot_keys|mnf_scale_picture,
#     "{s2} You have {reg10} troops fit for battle against their {reg11}.",
#     "none",
#     [
#         (assign, "$g_enemy_party", "$g_encountered_party"),
#         (assign, "$g_ally_party", -1),
#         (call_script, "script_encounter_calculate_fit"),
#         (try_begin),
#           (eq, "$new_encounter", 1),
#           (assign, "$new_encounter", 0),
#           (assign, "$g_encounter_is_in_village", 0),
#           (assign, "$g_encounter_type", 0),
#           (try_begin),
#             (party_slot_eq, "$g_enemy_party", slot_party_ai_state, spai_raiding_around_center),
#             (party_get_slot, ":village_no", "$g_enemy_party", slot_party_ai_object),
#
#             (store_distance_to_party_from_party, ":dist", ":village_no", "$g_enemy_party"),
#
#             (try_begin),
#               (lt, ":dist", raid_distance),
#               (assign, "$g_encounter_is_in_village", ":village_no"),
#               (assign, "$g_encounter_type", enctype_fighting_against_village_raid),
#             (try_end),
#           (try_end),
#           (try_begin),
#             (gt, "$g_player_raiding_village", 0),
#             (assign, "$g_encounter_is_in_village", "$g_player_raiding_village"),
#             (assign, "$g_encounter_type", enctype_catched_during_village_raid),
#             (party_quick_attach_to_current_battle, "$g_encounter_is_in_village", 1), #attach as enemy
#             (str_store_string, s1, "@Villagers"),
#             (display_message, "str_s1_joined_battle_enemy"),
#           (else_try),
#             (eq, "$g_encounter_type", enctype_fighting_against_village_raid),
#             (party_quick_attach_to_current_battle, "$g_encounter_is_in_village", 0), #attach as friend
#             (str_store_string, s1, "@Villagers"),
#             (display_message, "str_s1_joined_battle_friend"),
#             # Let village party join battle at your side
#           (try_end),
#
#           (call_script, "script_let_nearby_parties_join_current_battle", 0, 0),
#           (call_script, "script_encounter_init_variables"),
#           (assign, "$encountered_party_hostile", 0),
#           (assign, "$encountered_party_friendly", 0),
#           (try_begin),
#             (gt, "$g_encountered_party_relation", 0),
#             (assign, "$encountered_party_friendly", 1),
#           (try_end),
#           (try_begin),
#             (lt, "$g_encountered_party_relation", 0),
#             (assign, "$encountered_party_hostile", 1),
#             (try_begin),
#               (encountered_party_is_attacker),
#               (assign, "$cant_leave_encounter", 1),
#             (try_end),
#           (try_end),
#           (assign, "$talk_context", tc_party_encounter),
#           (call_script, "script_setup_party_meeting", "$g_encountered_party"),
#         (else_try), #second or more turn
# #          (try_begin),
# #            (call_script, "script_encounter_calculate_morale_change"),
# #          (try_end),
#           (try_begin),
#             # We can leave battle only after some troops have been killed.
#             (eq, "$cant_leave_encounter", 1),
#             (call_script, "script_party_count_members_with_full_health", "p_main_party_backup"),
#             (assign, ":org_total_party_counts", reg0),
#             (call_script, "script_party_count_members_with_full_health", "p_encountered_party_backup"),
#             (val_add, ":org_total_party_counts", reg0),
#
#             (call_script, "script_party_count_members_with_full_health", "p_main_party"),
#             (assign, ":cur_total_party_counts", reg0),
#             (call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
#             (val_add, ":cur_total_party_counts", reg0),
#
#             (store_sub, ":leave_encounter_limit", ":org_total_party_counts", 10),
#             (lt, ":cur_total_party_counts", ":leave_encounter_limit"),
#             (assign, "$cant_leave_encounter", 0),
#           (try_end),
#           (eq, "$g_leave_encounter",1),
#           (change_screen_return),
#         (try_end),
#
#         #setup s2
#         (try_begin),
#           (party_is_active, "$g_encountered_party"),
#           (str_store_party_name, s1,"$g_encountered_party"),
#           (try_begin),
#             (eq, "$g_encounter_type", 0),
#             (str_store_string, s2,"@You have encountered {s1}."),
#           (else_try),
#             (eq, "$g_encounter_type", enctype_fighting_against_village_raid),
#             (str_store_party_name, s3, "$g_encounter_is_in_village"),
#             (str_store_string, s2,"@You have engaged {s1} while they were raiding {s3}."),
#           (else_try),
#             (eq, "$g_encounter_type", enctype_catched_during_village_raid),
#             (str_store_party_name, s3, "$g_encounter_is_in_village"),
#             (str_store_string, s2,"@You were caught by {s1} while your forces were raiding {s3}."),
#           (try_end),
#         (try_end),
#         (try_begin),
#           (call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
#           (assign, ":num_enemy_regulars_remaining", reg0),
#           (assign, ":enemy_finished", 0),
#           (try_begin),
#             (eq, "$g_battle_result", 1), #battle won
#
#             (this_or_next|le, ":num_enemy_regulars_remaining", 0), #battle won
#             (le, ":num_enemy_regulars_remaining",  "$num_routed_enemies"), #replaced for above line because we do not want routed agents to spawn again in next turn of battle.
#
#             (assign, ":enemy_finished",1),
#           (else_try),
#             (eq, "$g_engaged_enemy", 1),
#
#             (this_or_next|le, ":num_enemy_regulars_remaining", 0),
#             (le, "$g_enemy_fit_for_battle", "$num_routed_enemies"),  #replaced for above line because we do not want routed agents to spawn again in next turn of battle.
#
#             (ge, "$g_friend_fit_for_battle",1),
#             (assign, ":enemy_finished",1),
#           (try_end),
#
#           (this_or_next|eq, ":enemy_finished",1),
#           (eq,"$g_enemy_surrenders",1),
#           (assign, "$g_next_menu", -1),
#           (jump_to_menu, "mnu_total_victory"),
#         (else_try),
#           (call_script, "script_party_count_members_with_full_health", "p_main_party"),
#           (assign, ":num_our_regulars_remaining", reg0),
#           (assign, ":friends_finished",0),
#           (try_begin),
#             (eq, "$g_battle_result", -1),
#
#             #(eq, ":num_our_regulars_remaining", 0), #battle lost
#             (le, ":num_our_regulars_remaining",  "$num_routed_us"), #replaced for above line because we do not want routed agents to spawn again in next turn of battle.
#
#             (assign,  ":friends_finished", 1),
#           (else_try),
#             (eq, "$g_engaged_enemy", 1),
#             (ge, "$g_enemy_fit_for_battle",1),
#             (le, "$g_friend_fit_for_battle",0),
#             (assign,  ":friends_finished",1),
#           (try_end),
#
#           (this_or_next|eq,  ":friends_finished",1),
#           (eq,"$g_player_surrenders",1),
#
#           (assign, "$g_next_menu", "mnu_captivity_start_wilderness"),
#           (jump_to_menu, "mnu_total_defeat"),
#         (try_end),
#
#
#         (try_begin),
#           (eq, "$g_encountered_party_template", "pt_looters"),
#           (set_background_mesh, "mesh_pic_bandits"),
#         (else_try),
#           (eq, "$g_encountered_party_template", "pt_mountain_bandits"),
#           (set_background_mesh, "mesh_pic_mountain_bandits"),
#         (else_try),
#           (eq, "$g_encountered_party_template", "pt_steppe_bandits"),
#           (set_background_mesh, "mesh_pic_steppe_bandits"),
#         (else_try),
#           (eq, "$g_encountered_party_template", "pt_taiga_bandits"),
#           (set_background_mesh, "mesh_pic_steppe_bandits"),
#         (else_try),
#           (eq, "$g_encountered_party_template", "pt_sea_raiders"),
#           (set_background_mesh, "mesh_pic_sea_raiders"),
#         (else_try),
#           (eq, "$g_encountered_party_template", "pt_forest_bandits"),
#           (set_background_mesh, "mesh_pic_forest_bandits"),
#         (else_try),
#           (eq, "$g_encountered_party_template", "pt_deserters"),
#           (set_background_mesh, "mesh_pic_deserters"),
#         (else_try),
#           (eq, "$g_encountered_party_template", "pt_kingdom_hero_party"),
# 		  (party_stack_get_troop_id, ":leader_troop", "$g_encountered_party", 0),
# 		  (ge, ":leader_troop", 1),
# 		  (troop_get_slot, ":leader_troop_faction", ":leader_troop", slot_troop_original_faction),
# 		  (try_begin),
# 			(eq, ":leader_troop_faction", fac_kingdom_1),
#             (set_background_mesh, "mesh_pic_swad"),
# 		  (else_try),
# 			(eq, ":leader_troop_faction", fac_kingdom_2),
#             (set_background_mesh, "mesh_pic_vaegir"),
# 		  (else_try),
# 			(eq, ":leader_troop_faction", fac_kingdom_3),
#             (set_background_mesh, "mesh_pic_khergit"),
# 		  (else_try),
# 			(eq, ":leader_troop_faction", fac_kingdom_4),
#             (set_background_mesh, "mesh_pic_nord"),
# 		  (else_try),
# 			(eq, ":leader_troop_faction", fac_kingdom_5),
#             (set_background_mesh, "mesh_pic_rhodock"),
# 		  (else_try),
# 			(eq, ":leader_troop_faction", fac_kingdom_6),
#             (set_background_mesh, "mesh_pic_sarranid_encounter"),
# 		  (try_end),
#         (try_end),
#     ],
#     [
#       ("encounter_attack",
#       [
#         (eq, "$encountered_party_friendly", 0),
#         (neg|troop_is_wounded, "trp_player"),
#       ],
#       "Charge the enemy.",
#       [
#         (assign, "$g_battle_result", 0),
#         (assign, "$g_engaged_enemy", 1),
#
#         (party_get_template_id, ":encountered_party_template", "$g_encountered_party"),
#         (try_begin),
# 		  (eq, ":encountered_party_template", "pt_village_farmers"),
# 		  (unlock_achievement, ACHIEVEMENT_HELP_HELP_IM_BEING_REPRESSED),
# 		(try_end),
#
#         (call_script, "script_calculate_renown_value"),
#         (call_script, "script_calculate_battle_advantage"),
#         (set_battle_advantage, reg0),
#         (set_party_battle_mode),
#         (try_begin),
#           (eq, "$g_encounter_type", enctype_fighting_against_village_raid),
#           (assign, "$g_village_raid_evil", 0),
#           (set_jump_mission,"mt_village_raid"),
#           (party_get_slot, ":scene_to_use", "$g_encounter_is_in_village", slot_castle_exterior),
#           (jump_to_scene, ":scene_to_use"),
#         (else_try),
#           (eq, "$g_encounter_type", enctype_catched_during_village_raid),
#           (assign, "$g_village_raid_evil", 0),
#           (set_jump_mission,"mt_village_raid"),
#           (party_get_slot, ":scene_to_use", "$g_encounter_is_in_village", slot_castle_exterior),
#           (jump_to_scene, ":scene_to_use"),
#         (else_try),
#           (set_jump_mission,"mt_lead_charge"),
#           (call_script, "script_setup_random_scene"),
#         (try_end),
#         (assign, "$g_next_menu", "mnu_simple_encounter"),
#         (jump_to_menu, "mnu_battle_debrief"),
#         (change_screen_mission),
#       ]),
#
#       ("encounter_order_attack",
#       [
#         (eq, "$encountered_party_friendly", 0),
#         (call_script, "script_party_count_members_with_full_health", "p_main_party"),(ge, reg0, 4),
#       ],
#       "Order your troops to attack without you.",
#       [
#         (jump_to_menu, "mnu_order_attack_begin"),
#         #(simulate_battle,3),
#       ]),
#
#       ("encounter_leave",[
#           (eq,"$cant_leave_encounter", 0),
#           ],"Leave.",[
#
# ###NPC companion changes begin
#               (try_begin),
#                   (eq, "$encountered_party_friendly", 0),
#                   (encountered_party_is_attacker),
#                   (call_script, "script_objectionable_action", tmt_aristocratic, "str_flee_battle"),
#               (try_end),
# ###NPC companion changes end
# #Troop commentary changes begin
#               (try_begin),
#                   (eq, "$encountered_party_friendly", 0),
# #                  (encountered_party_is_attacker),
#                   (party_get_num_companion_stacks, ":num_stacks", "p_encountered_party_backup"),
#                   (try_for_range, ":stack_no", 0, ":num_stacks"),
#                     (party_stack_get_troop_id,   ":stack_troop","p_encountered_party_backup",":stack_no"),
#                     (is_between, ":stack_troop", active_npcs_begin, active_npcs_end),
# 					(troop_slot_eq, ":stack_troop", slot_troop_occupation, slto_kingdom_hero),
#                     (store_troop_faction, ":victorious_faction", ":stack_troop"),
# #					(store_relation, ":relation_with_stack_troop", ":victorious_faction", "fac_player_faction"),
# #					(lt, ":relation_with_stack_troop", 0),
#                     (call_script, "script_add_log_entry", logent_player_retreated_from_lord, "trp_player",  -1, ":stack_troop", ":victorious_faction"),
#                   (try_end),
#               (try_end),
# #Troop commentary changes end
#           	(leave_encounter),(change_screen_return)]),
#       ("encounter_retreat",[
#          (eq,"$cant_leave_encounter", 1),
#          (call_script, "script_get_max_skill_of_player_party", "skl_tactics"),
#          (assign, ":max_skill", reg0),
#          (val_add, ":max_skill", 4),
#
#          (call_script, "script_party_count_members_with_full_health", "p_collective_enemy", 0),
#          (assign, ":enemy_party_strength", reg0),
#          (val_div, ":enemy_party_strength", 2),
#
#          (val_div, ":enemy_party_strength", ":max_skill"),
#          (val_max, ":enemy_party_strength", 1),
#
#          (call_script, "script_party_count_fit_regulars", "p_main_party"),
#          (assign, ":player_count", reg0),
#          (ge, ":player_count", ":enemy_party_strength"),
#          ],"Pull back, leaving some soldiers behind to cover your retreat.",[(jump_to_menu, "mnu_encounter_retreat_confirm"),]),
#
#       ("encounter_surrender",[
#          (eq,"$cant_leave_encounter", 1),
#           ],"Surrender.",[(assign,"$g_player_surrenders",1)]),
#     ]
#   ),
#   (
#     "encounter_retreat_confirm",0,
#     "As the party member with the highest tactics skill,\
#  ({reg2}), {reg3?you devise:{s3} devises} a plan that will allow you and your men to escape with your lives,\
#  but you'll have to leave {reg4} soldiers behind to stop the enemy from giving chase.",
#     "none",
#     [(call_script, "script_get_max_skill_of_player_party", "skl_tactics"),
#      (assign, ":max_skill", reg0),
#      (assign, ":max_skill_owner", reg1),
#      (assign, reg2, ":max_skill"),
#      (val_add, ":max_skill", 4),
#
#      (call_script, "script_party_count_members_with_full_health", "p_collective_enemy", 0),
#      (assign, ":enemy_party_strength", reg0),
#      (val_div, ":enemy_party_strength", 2),
#
#      (store_div, reg4, ":enemy_party_strength", ":max_skill"),
#      (val_max, reg4, 1),
#
#      (try_begin),
#        (eq, ":max_skill_owner", "trp_player"),
#        (assign, reg3, 1),
#      (else_try),
#        (assign, reg3, 0),
#        (str_store_troop_name, s3, ":max_skill_owner"),
#      (try_end),
#      ],
#     [
#       ("leave_behind",[],"Go on. The sacrifice of these men will save the rest.",
# 	  [
# 	    (assign, ":num_casualties", reg4),
# 		(try_for_range, ":unused", 0, ":num_casualties"),
# 		  (call_script, "script_cf_party_remove_random_regular_troop", "p_main_party"),
# 		  (assign, ":lost_troop", reg0),
# 		  (store_random_in_range, ":random_no", 0, 100),
# 		  (ge, ":random_no", 30),
# 		  (party_add_prisoners, "$g_encountered_party", ":lost_troop", 1),
# 		(try_end),
# 		(call_script, "script_change_player_party_morale", -20),
# 		(jump_to_menu, "mnu_encounter_retreat"),
#       ]),
#       ("dont_leave_behind",[],"No. We leave no one behind.",[(jump_to_menu, "mnu_simple_encounter"),]),
#     ]
#   ),
#   (
#     "encounter_retreat",0,
#     "You tell {reg4} of your troops to hold the enemy while you retreat with the rest of your party.",
#     "none",
#     [
#      ],
#     [
#       ("continue",[],"Continue...",
# 	  [
#         ###Troop commentary changes begin
#         (call_script, "script_objectionable_action", tmt_aristocratic, "str_flee_battle"),
#         (party_get_num_companion_stacks, ":num_stacks", "p_encountered_party_backup"),
#         (try_for_range, ":stack_no", 0, ":num_stacks"),
#           (party_stack_get_troop_id,   ":stack_troop","p_encountered_party_backup",":stack_no"),
#           (is_between, ":stack_troop", active_npcs_begin, active_npcs_end),
#           (troop_slot_eq, ":stack_troop", slot_troop_occupation, slto_kingdom_hero),
#           (store_troop_faction, ":victorious_faction", ":stack_troop"),
#           (call_script, "script_add_log_entry", logent_player_retreated_from_lord_cowardly, "trp_player",  -1, ":stack_troop", ":victorious_faction"),
#         (try_end),
#         ###Troop commentary changes end
#         (party_ignore_player, "$g_encountered_party", 1),
#         (leave_encounter),
# 		(change_screen_return)
#       ]),
#     ]
#   ),
#   (
#     "order_attack_begin",0,
#     "Your troops prepare to attack the enemy.",
#     "none",
#     [],
#     [
#       ("order_attack_begin",[],"Order the attack to begin.",
#       [
#         (party_get_template_id, ":encountered_party_template", "$g_encountered_party"),
#         (try_begin),
# 		  (eq, ":encountered_party_template", "pt_village_farmers"),
# 		  (unlock_achievement, ACHIEVEMENT_HELP_HELP_IM_BEING_REPRESSED),
# 		(try_end),
#
#         (assign, "$g_engaged_enemy", 1),
#         (jump_to_menu,"mnu_order_attack_2"),
#       ]),
#       ("call_back",[],"Call them back.",[(jump_to_menu,"mnu_simple_encounter")]),
#     ]
#   ),
#   (
#     "order_attack_2",mnf_disable_all_keys,
#     "{s4}^^Your casualties: {s8}^^Enemy casualties: {s9}",
#     "none",
#     [
#       (set_background_mesh, "mesh_pic_charge"),
#
#       (call_script, "script_party_calculate_strength", "p_main_party", 1), #exclude player
#       (assign, ":player_party_strength", reg0),
#
#       (call_script, "script_party_calculate_strength", "p_collective_enemy", 0),
#       (assign, ":enemy_party_strength", reg0),
#
#       (party_collect_attachments_to_party, "p_main_party", "p_collective_ally"),
#       (call_script, "script_party_calculate_strength", "p_collective_ally", 1), #exclude player
#       (assign, ":total_player_and_followers_strength", reg0),
#
#       (try_begin),
#         (le, ":total_player_and_followers_strength", ":enemy_party_strength"),
#         (assign, ":minimum_power", ":total_player_and_followers_strength"),
#       (else_try),
#         (assign, ":minimum_power", ":enemy_party_strength"),
#       (try_end),
#
#       (try_begin),
#         (le, ":minimum_power", 25),
#         (assign, ":division_constant", 1),
#       (else_try),
#         (le, ":minimum_power", 50),
#         (assign, ":division_constant", 2),
#       (else_try),
#         (le, ":minimum_power", 75),
#         (assign, ":division_constant", 3),
#       (else_try),
#         (le, ":minimum_power", 125),
#         (assign, ":division_constant", 4),
#       (else_try),
#         (le, ":minimum_power", 200),
#         (assign, ":division_constant", 5),
#       (else_try),
#         (le, ":minimum_power", 400),
#         (assign, ":division_constant", 6),
#       (else_try),
#         (le, ":minimum_power", 800),
#         (assign, ":division_constant", 7),
#       (else_try),
#         (le, ":minimum_power", 1600),
#         (assign, ":division_constant", 8),
#       (else_try),
#         (le, ":minimum_power", 3200),
#         (assign, ":division_constant", 9),
#       (else_try),
#         (le, ":minimum_power", 6400),
#         (assign, ":division_constant", 10),
#       (else_try),
#         (le, ":minimum_power", 12800),
#         (assign, ":division_constant", 11),
#       (else_try),
#         (le, ":minimum_power", 25600),
#         (assign, ":division_constant", 12),
#       (else_try),
#         (le, ":minimum_power", 51200),
#         (assign, ":division_constant", 13),
#       (else_try),
#         (le, ":minimum_power", 102400),
#         (assign, ":division_constant", 14),
#       (else_try),
#         (assign, ":division_constant", 15),
#       (try_end),
#
#       (val_div, ":player_party_strength", ":division_constant"), #1.126, ":division_constant" was 5 before
#       (val_max, ":player_party_strength", 1), #1.126
#       (val_div, ":enemy_party_strength", ":division_constant"), #1.126, ":division_constant" was 5 before
#       (val_max, ":enemy_party_strength", 1), #1.126
#       (val_div, ":total_player_and_followers_strength", ":division_constant"), #1.126, ":division_constant" was 5 before
#       (val_max, ":total_player_and_followers_strength", 1), #1.126
#
#       (store_mul, "$g_strength_contribution_of_player", ":player_party_strength", 100),
#       (val_div, "$g_strength_contribution_of_player", ":total_player_and_followers_strength"),
#
#       (inflict_casualties_to_party_group, "p_main_party", ":enemy_party_strength", "p_temp_casualties"),
#       (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
#       (str_store_string_reg, s8, s0),
#
#       (try_begin),
#         (ge, "$g_ally_party", 0),
#         (inflict_casualties_to_party_group, "$g_ally_party", ":enemy_party_strength", "p_temp_casualties"),
#         (str_store_string_reg, s8, s0),
#       (try_end),
#
#       (inflict_casualties_to_party_group, "$g_encountered_party", ":total_player_and_followers_strength", "p_temp_casualties"),
#
#       #ozan begin
#       (party_get_num_companion_stacks, ":num_stacks", "p_temp_casualties"),
#       (try_for_range, ":stack_no", 0, ":num_stacks"),
#         (party_stack_get_troop_id, ":stack_troop", "p_temp_casualties", ":stack_no"),
#         (try_begin),
#           (party_stack_get_size, ":stack_size", "p_temp_casualties", ":stack_no"),
#           (gt, ":stack_size", 0),
#           (party_add_members, "p_total_enemy_casualties", ":stack_troop", ":stack_size"), #addition_to_p_total_enemy_casualties
#           (party_stack_get_num_wounded, ":stack_wounded_size", "p_temp_casualties", ":stack_no"),
#           (gt, ":stack_wounded_size", 0),
#           (party_wound_members, "p_total_enemy_casualties", ":stack_troop", ":stack_wounded_size"),
#         (try_end),
#       (try_end),
#       #ozan end
#
#       (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
#       (str_store_string_reg, s9, s0),
#
#       (party_collect_attachments_to_party, "$g_encountered_party", "p_collective_enemy"),
#       (assign, "$no_soldiers_left", 0),
#       (try_begin),
#         (call_script, "script_party_count_members_with_full_health", "p_main_party"),
#         (assign, ":num_our_regulars_remaining", reg0),
#         (store_add, ":num_routed_us_plus_one", "$num_routed_us", 1),
#         (le, ":num_our_regulars_remaining", ":num_routed_us_plus_one"), #replaced for above line because we do not want routed agents to spawn again in next turn of battle.
#         (assign, "$no_soldiers_left", 1),
#         (str_store_string, s4, "str_order_attack_failure"),
#       (else_try),
#         (call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
#         (assign, ":num_enemy_regulars_remaining", reg0),
#         (this_or_next|le, ":num_enemy_regulars_remaining", 0),
#         (le, ":num_enemy_regulars_remaining", "$num_routed_enemies"), #replaced for above line because we do not want routed agents to spawn again in next turn of battle.
#         (assign, ":continue", 0),
#         (party_get_num_companion_stacks, ":party_num_stacks", "p_collective_enemy"),
#         (try_begin),
#           (eq, ":party_num_stacks", 0),
#           (assign, ":continue", 1),
#         (else_try),
#           (party_stack_get_troop_id, ":party_leader", "p_collective_enemy", 0),
#           (try_begin),
#             (neg|troop_is_hero, ":party_leader"),
#             (assign, ":continue", 1),
#           (else_try),
#             (troop_is_wounded, ":party_leader"),
#             (assign, ":continue", 1),
#           (try_end),
#         (try_end),
#         (eq, ":continue", 1),
#         (assign, "$g_battle_result", 1),
#         (assign, "$no_soldiers_left", 1),
#         (str_store_string, s4, "str_order_attack_success"),
#       (else_try),
#       (str_store_string, s4, "str_order_attack_continue"),
#     (try_end),
#     ],
#     [
#       ("order_attack_continue",[(eq, "$no_soldiers_left", 0)],"Order your soldiers to continue the attack.",[
#           (jump_to_menu,"mnu_order_attack_2"),
#           ]),
#       ("order_retreat",[(eq, "$no_soldiers_left", 0)],"Call your soldiers back.",[
#           (jump_to_menu,"mnu_simple_encounter"),
#           ]),
#       ("continue",[(eq, "$no_soldiers_left", 1)],"Continue...",[
#           (jump_to_menu,"mnu_simple_encounter"),
#           ]),
#     ]
#   ),
#
#   (
#     "battle_debrief",mnf_scale_picture|mnf_disable_all_keys,
#     "{s11}^^Your Casualties:{s8}{s10}^^Enemy Casualties:{s9}",
#     "none",
#     [
#      (try_begin),
#        (eq, "$g_battle_result", 1),
#        (call_script, "script_change_troop_renown", "trp_player", "$battle_renown_value"),
#
#        (try_begin),
#          (ge, "$g_encountered_party", 0),
#          (party_is_active, "$g_encountered_party"),
#          (party_get_template_id, ":encountered_party_template", "$g_encountered_party"),
#          (eq, ":encountered_party_template", "pt_kingdom_caravan_party"),
#
#          (get_achievement_stat, ":number_of_village_raids", ACHIEVEMENT_THE_BANDIT, 0),
#          (get_achievement_stat, ":number_of_caravan_raids", ACHIEVEMENT_THE_BANDIT, 1),
#          (val_add, ":number_of_caravan_raids", 1),
#          (set_achievement_stat, ACHIEVEMENT_THE_BANDIT, 1, ":number_of_caravan_raids"),
#
#          (try_begin),
#            (ge, ":number_of_village_raids", 3),
#            (ge, ":number_of_caravan_raids", 3),
#            (unlock_achievement, ACHIEVEMENT_THE_BANDIT),
#          (try_end),
#        (try_end),
#
#        (try_begin),
#          (party_get_current_terrain, ":cur_terrain", "p_main_party"),
#          (eq, ":cur_terrain", rt_snow),
#          (get_achievement_stat, ":number_of_victories_at_snowy_lands", ACHIEVEMENT_BEST_SERVED_COLD, 0),
#          (val_add, ":number_of_victories_at_snowy_lands", 1),
#          (set_achievement_stat, ACHIEVEMENT_BEST_SERVED_COLD, 0, ":number_of_victories_at_snowy_lands"),
#
#          (try_begin),
#            (eq, ":number_of_victories_at_snowy_lands", 10),
#            (unlock_achievement, ACHIEVEMENT_BEST_SERVED_COLD),
#          (try_end),
#        (try_end),
#
#        (try_begin),
#          (ge, "$g_enemy_party", 0),
#          (party_is_active, "$g_enemy_party"),
#          (party_stack_get_troop_id, ":stack_troop", "$g_enemy_party", 0),
#          (eq, ":stack_troop", "trp_mountain_bandit"),
#
#          (get_achievement_stat, ":number_of_victories_aganist_mountain_bandits", ACHIEVEMENT_MOUNTAIN_BLADE, 0),
#          (val_add, ":number_of_victories_aganist_mountain_bandits", 1),
#          (set_achievement_stat, ACHIEVEMENT_MOUNTAIN_BLADE, 0, ":number_of_victories_aganist_mountain_bandits"),
#
#          (try_begin),
#            (eq, ":number_of_victories_aganist_mountain_bandits", 10),
#            (unlock_achievement, ACHIEVEMENT_MOUNTAIN_BLADE),
#          (try_end),
#        (try_end),
#
#        (try_begin),
#          (is_between, "$g_ally_party", walled_centers_begin, walled_centers_end),
#          (unlock_achievement, ACHIEVEMENT_NONE_SHALL_PASS),
#        (try_end),
#
#        (try_begin),
#          (eq, "$g_joined_battle_to_help", 1),
#          (unlock_achievement, ACHIEVEMENT_GOOD_SAMARITAN),
#        (try_end),
#      (try_end),
#
#      (assign, "$g_joined_battle_to_help", 0),
#      (call_script, "script_count_casualties_and_adjust_morale"),#new
#      (call_script, "script_encounter_calculate_fit"),
#
#      (call_script, "script_party_count_fit_regulars", "p_main_party"),
#      (assign, "$playerparty_postbattle_regulars", reg0),
#
#      (try_begin),
#        (eq, "$g_battle_result", 1),
#        (eq, "$g_enemy_fit_for_battle", 0),
#        (str_store_string, s11, "@You were victorious!"),
# #       (play_track, "track_bogus"), #clear current track.
# #       (call_script, "script_music_set_situation_with_culture", mtf_sit_victorious),
#        (try_begin),
#          (gt, "$g_friend_fit_for_battle", 1),
#          (set_background_mesh, "mesh_pic_victory"),
#        (try_end),
#      (else_try),
#        (eq, "$g_battle_result", -1),
#        (ge, "$g_enemy_fit_for_battle",1),
#        (this_or_next|le, "$g_friend_fit_for_battle",0),
#        (le, "$playerparty_postbattle_regulars", 0),
#        (str_store_string, s11, "@Battle was lost. Your forces were utterly crushed."),
#        (set_background_mesh, "mesh_pic_defeat"),
#      (else_try),
#        (eq, "$g_battle_result", -1),
#        (str_store_string, s11, "@Your companions carry you away from the fighting."),
#        (troop_get_type, ":is_female", "trp_player"),
#        (try_begin),
#          (eq, ":is_female", 1),
#          (set_background_mesh, "mesh_pic_wounded_fem"),
#        (else_try),
#          (set_background_mesh, "mesh_pic_wounded"),
#        (try_end),
#      (else_try),
#        (eq, "$g_battle_result", 1),
#        (str_store_string, s11, "@You have defeated the enemy."),
#        (try_begin),
#          (gt, "$g_friend_fit_for_battle", 1),
#          (set_background_mesh, "mesh_pic_victory"),
#        (try_end),
#      (else_try),
#        (eq, "$g_battle_result", 0),
#        (str_store_string, s11, "@You have retreated from the fight."),
#      (try_end),
# #NPC companion changes begin
# ##check for excessive casualties, more forgiving if battle result is good
#      (try_begin),
#         (gt, "$playerparty_prebattle_regulars", 9),
#         (store_add, ":divisor", 3, "$g_battle_result"),
#         (store_div, ":half_of_prebattle_regulars", "$playerparty_prebattle_regulars", ":divisor"),
#         (lt, "$playerparty_postbattle_regulars", ":half_of_prebattle_regulars"),
#         (call_script, "script_objectionable_action", tmt_egalitarian, "str_excessive_casualties"),
#      (try_end),
# #NPC companion changes end
#
#      (call_script, "script_print_casualties_to_s0", "p_player_casualties", 0),
#      (str_store_string_reg, s8, s0),
#      (call_script, "script_print_casualties_to_s0", "p_enemy_casualties", 0),
#      (str_store_string_reg, s9, s0),
#      (str_clear, s10),
#      (try_begin),
#        (eq, "$any_allies_at_the_last_battle", 1),
#        (call_script, "script_print_casualties_to_s0", "p_ally_casualties", 0),
#        (str_store_string, s10, "@^^Ally Casualties:{s0}"),
#      (try_end),
#      ],
#     [
#       ("continue",[],"Continue...",[(jump_to_menu, "$g_next_menu"),]),
#     ]
#   ),
#
#
#
#   (
#     "total_victory", 0,
#     "You shouldn't be reading this... {s9}",
#     "none",
#     [
#         # We exploit the menu condition system below.
#         # The conditions should make sure that always another screen or menu is called.
#         (assign, ":break", 0),
#         (try_begin),
#           (eq, "$routed_party_added", 0), #new
#           (assign, "$routed_party_added", 1),
#
#            #add new party to map (routed_warriors)
#           (call_script, "script_add_routed_party"),
#         (end_try),
#
# 		(try_begin),
# 			(check_quest_active, "qst_track_down_bandits"),
# 			(neg|check_quest_succeeded, "qst_track_down_bandits"),
# 			(neg|check_quest_failed, "qst_track_down_bandits"),
#
# 			(quest_get_slot, ":quest_party", "qst_track_down_bandits", slot_quest_target_party),
# 			(party_is_active, ":quest_party"),
# 			(party_get_attached_to, ":quest_party_attached"),
# 			(this_or_next|eq, ":quest_party", "$g_enemy_party"),
# 				(eq, ":quest_party_attached", "$g_enemy_party"),
# 			(call_script, "script_succeed_quest", "qst_track_down_bandits"),
# 		(try_end),
#
# 		(try_begin),
# 			(gt, "$g_private_battle_with_troop", 0),
# 			(troop_slot_eq, "$g_private_battle_with_troop", slot_troop_leaded_party, "$g_encountered_party"),
# 			(assign, "$g_private_battle_with_troop", 0),
# 			(assign, "$g_disable_condescending_comments", 1),
# 		(try_end),
#
# 		#new - begin
#         (party_get_num_companion_stacks, ":num_stacks", "p_collective_enemy"),
#         (try_for_range, ":i_stack", 0, ":num_stacks"),
#           (party_stack_get_troop_id, ":stack_troop", "p_collective_enemy", ":i_stack"),
#           (is_between, ":stack_troop", lords_begin, lords_end),
#           (troop_is_wounded, ":stack_troop"),
#           (party_add_members, "p_total_enemy_casualties", ":stack_troop", 1),
#         (try_end),
#         #new - end
#
#         (try_begin),
#           # Talk to ally leader
#           (eq, "$thanked_by_ally_leader", 0),
#           (assign, "$thanked_by_ally_leader", 1),
#
#           (gt, "$g_ally_party", 0),
#           #(store_add, ":total_str_without_player", "$g_starting_strength_ally_party", "$g_starting_strength_enemy_party"),
#
#           (store_add, ":total_str_without_player", "$g_starting_strength_friends", "$g_starting_strength_enemy_party"),
#           (val_sub, ":total_str_without_player", "$g_starting_strength_main_party"),
#
#           (store_sub, ":ally_strength_without_player", "$g_starting_strength_friends", "$g_starting_strength_main_party"),
#
#           (store_mul, ":ally_advantage", ":ally_strength_without_player", 100),
#           (val_add, ":total_str_without_player", 1),
#           (val_div, ":ally_advantage", ":total_str_without_player"),
#           #Ally advantage=50  means battle was evenly matched
#
#           (store_sub, ":enemy_advantage", 100, ":ally_advantage"),
#
#           (store_mul, ":faction_reln_boost", ":enemy_advantage", "$g_starting_strength_enemy_party"),
#           (val_div, ":faction_reln_boost", 3000),
#           (val_min, ":faction_reln_boost", 4),
#
#           (store_mul, "$g_relation_boost", ":enemy_advantage", ":enemy_advantage"),
#           (val_div, "$g_relation_boost", 700),
#           (val_clamp, "$g_relation_boost", 0, 20),
#
#           (party_get_num_companion_stacks, ":num_ally_stacks", "$g_ally_party"),
#           (gt, ":num_ally_stacks", 0),
#           (store_faction_of_party, ":ally_faction","$g_ally_party"),
#           (call_script, "script_change_player_relation_with_faction", ":ally_faction", ":faction_reln_boost"),
#           (party_stack_get_troop_id, ":ally_leader", "$g_ally_party"),
#           (party_stack_get_troop_dna, ":ally_leader_dna", "$g_ally_party", 0),
#           (try_begin),
#             (troop_is_hero, ":ally_leader"),
#             (troop_get_slot, ":hero_relation", ":ally_leader", slot_troop_player_relation),
#             (assign, ":rel_boost", "$g_relation_boost"),
#             (try_begin),
#               (lt, ":hero_relation", -5),
#               (val_div, ":rel_boost", 3),
#             (try_end),
#             (call_script,"script_change_player_relation_with_troop", ":ally_leader", ":rel_boost"),
#           (try_end),
#           (assign, "$talk_context", tc_ally_thanks),
#           (call_script, "script_setup_troop_meeting", ":ally_leader", ":ally_leader_dna"),
#         (else_try),
#           # Talk to enemy leaders
#           (assign, ":break", 0),
#
#           (party_get_num_companion_stacks, ":num_stacks", "p_total_enemy_casualties"), #p_encountered changed to total_enemy_casualties
#           (try_for_range, ":stack_no", "$last_defeated_hero", ":num_stacks"), #May 31 bug note -- this now returns some heroes in victorious party as well as in the other party
#             (eq, ":break", 0),
#             (party_stack_get_troop_id, ":stack_troop", "p_total_enemy_casualties", ":stack_no"),
#             (party_stack_get_troop_dna, ":stack_troop_dna", "p_total_enemy_casualties", ":stack_no"),
#
#             (troop_is_hero, ":stack_troop"),
#
#             (store_troop_faction, ":defeated_faction", ":stack_troop"),
#             #steve post 0912 changes begin - removed, this is duplicated elsewhere in game menus
#             #(call_script, "script_add_log_entry", logent_lord_defeated_by_player, "trp_player",  -1, ":stack_troop", ":defeated_faction"),
#             (try_begin),
#    			  (store_relation, ":relation", ":defeated_faction", "fac_player_faction"),
# 			  (ge, ":relation", 0),
# 			  (str_store_troop_name, s4, ":stack_troop"),
#
# 			  (try_begin),
# 				(eq, "$cheat_mode", 1),
# 				(display_message, "@{!}{s4} skipped in p_total_enemy_casualties capture queue because is friendly"),
# 			  (try_end),
# 			(else_try),
#               (try_begin),
#                 (party_stack_get_troop_id, ":party_leader", "$g_encountered_party", 0),
#                 (is_between, ":party_leader", active_npcs_begin, active_npcs_end),
#                 (troop_slot_eq, ":party_leader", slot_troop_occupation, slto_kingdom_hero),
#                 (store_sub, ":kingdom_hero_id", ":party_leader", active_npcs_begin),
#                 (get_achievement_stat, ":was_he_defeated_player_before", ACHIEVEMENT_BARON_GOT_BACK, ":kingdom_hero_id"),
#                 (eq, ":was_he_defeated_player_before", 1),
#
#                 (unlock_achievement, ACHIEVEMENT_BARON_GOT_BACK),
#               (try_end),
#
#               (store_add, "$last_defeated_hero", ":stack_no", 1),
#               (call_script, "script_remove_troop_from_prison", ":stack_troop"),
#               (troop_set_slot, ":stack_troop", slot_troop_leaded_party, -1),
#
#               (call_script, "script_cf_check_hero_can_escape_from_player", ":stack_troop"),
#
#               (str_store_troop_name, s1, ":stack_troop"),
#               (str_store_faction_name, s3, ":defeated_faction"),
#               (str_store_string, s17, "@{s1} of {s3} managed to escape."),
#               (display_log_message, "@{!}{s17}"),
#               (jump_to_menu, "mnu_enemy_slipped_away"),
#               (assign, ":break", 1),
# 			(else_try),
#               (store_add, "$last_defeated_hero", ":stack_no", 1),
#               (call_script, "script_remove_troop_from_prison", ":stack_troop"),
#               (troop_set_slot, ":stack_troop", slot_troop_leaded_party, -1),
#
#               (assign, "$talk_context", tc_hero_defeated),
#
#               (call_script, "script_setup_troop_meeting", ":stack_troop", ":stack_troop_dna"),
#               (assign, ":break", 1),
#             (try_end),
#           (try_end),
#
#           (eq, ":break", 1),
#         (else_try),
#           # Talk to freed heroes
#           (assign, ":break", 0),
#           (party_get_num_prisoner_stacks, ":num_prisoner_stacks", "p_collective_enemy"),
#           (try_for_range, ":stack_no", "$last_freed_hero", ":num_prisoner_stacks"),
#             (eq, ":break", 0),
#             (party_prisoner_stack_get_troop_id, ":stack_troop", "p_collective_enemy", ":stack_no"),
#             (troop_is_hero, ":stack_troop"),
#             (party_prisoner_stack_get_troop_dna, ":stack_troop_dna", "p_collective_enemy", ":stack_no"),
#             (store_add, "$last_freed_hero", ":stack_no", 1),
#             (assign, "$talk_context", tc_hero_freed),
#             (call_script, "script_setup_troop_meeting", ":stack_troop", ":stack_troop_dna"),
#             (assign, ":break", 1),
#           (try_end),
#           (eq, ":break", 1),
#         (else_try),
#           (eq, "$capture_screen_shown", 0),
#           (assign, "$capture_screen_shown", 1),
#           (party_clear, "p_temp_party"),
#           (assign, "$g_move_heroes", 0),
#           #(call_script, "script_party_prisoners_add_party_companions", "p_temp_party", "p_collective_enemy"),
#
#           #p_total_enemy_casualties deki yarali askerler p_temp_party'e prisoner olarak eklenecek.
#           (call_script, "script_party_add_wounded_members_as_prisoners", "p_temp_party", "p_total_enemy_casualties"),
#
#           (call_script, "script_party_add_party_prisoners", "p_temp_party", "p_collective_enemy"),
#           (try_begin),
#             (call_script, "script_party_calculate_strength", "p_collective_friends_backup",0),
#             (assign,":total_initial_strength", reg(0)),
#             (gt, ":total_initial_strength", 0),
#             #(gt, "$g_ally_party", 0),
#             (call_script, "script_party_calculate_strength", "p_main_party_backup",0),
#             (assign,":player_party_initial_strength", reg(0)),
#             # move ally_party_initial_strength/(player_party_initial_strength + ally_party_initial_strength) prisoners to ally party.
#             # First we collect the share of prisoners of the ally party and distribute those among the allies.
#             (store_sub, ":ally_party_initial_strength", ":total_initial_strength", ":player_party_initial_strength"),
#
#             #(call_script, "script_party_calculate_strength", "p_ally_party_backup"),
#             #(assign,":ally_party_initial_strength", reg(0)),
#             #(store_add, ":total_initial_strength", ":player_party_initial_strength", ":ally_party_initial_strength"),
#             (store_mul, ":ally_share", ":ally_party_initial_strength", 1000),
#             (val_div, ":ally_share", ":total_initial_strength"),
#             (assign, "$pin_number", ":ally_share"), #we send this as a parameter to the script.
#             (party_clear, "p_temp_party_2"),
#             (call_script, "script_move_members_with_ratio", "p_temp_party", "p_temp_party_2"),
#
#             #TODO: This doesn't handle prisoners if our allies joined battle after us.
#             (try_begin),
#               (gt, "$g_ally_party", 0),
#               (distribute_party_among_party_group, "p_temp_party_2", "$g_ally_party"),
#             (try_end),
#             #next if there's anything left, we'll open up the party exchange screen and offer them to the player.
#           (try_end),
#           (party_get_num_companions, ":num_rescued_prisoners", "p_temp_party"),
#           (party_get_num_prisoners,  ":num_captured_enemies", "p_temp_party"),
#
#           (store_add, ":total_capture_size", ":num_rescued_prisoners", ":num_captured_enemies"),
#
#           (gt, ":total_capture_size", 0),
#           (change_screen_exchange_with_party, "p_temp_party"),
#         (else_try),
#           (eq, "$loot_screen_shown", 0),
#           (assign, "$loot_screen_shown", 1),
# #          (try_begin),
# #            (gt, "$g_ally_party", 0),
# #            (call_script, "script_party_add_party", "$g_ally_party", "p_temp_party"), #Add remaining prisoners to ally TODO: FIX it.
# #          (else_try),
# #            (party_get_num_attached_parties, ":num_quick_attachments", "p_main_party"),
# #            (gt, ":num_quick_attachments", 0),
# #            (party_get_attached_party_with_rank, ":helper_party", "p_main_party", 0),
# #            (call_script, "script_party_add_party", ":helper_party", "p_temp_party"), #Add remaining prisoners to our reinforcements
# #          (try_end),
#           (troop_clear_inventory, "trp_temp_troop"),
#           (call_script, "script_party_calculate_loot", "p_total_enemy_casualties"), #p_encountered_party_backup changed to total_enemy_casualties
#           (gt, reg0, 0),
#           (troop_sort_inventory, "trp_temp_troop"),
#           (change_screen_loot, "trp_temp_troop"),
#         (else_try),
#           #finished all
#           (try_begin),
#             (le, "$g_ally_party", 0),
#             (end_current_battle),
#           (try_end),
#           (call_script, "script_party_give_xp_and_gold", "p_total_enemy_casualties"), #p_encountered_party_backup changed to total_enemy_casualties
#           (try_begin),
#             (eq, "$g_enemy_party", 0),
#             (display_message,"str_error_string"),
#           (try_end),
#
# 		  (try_begin),
# 		    (party_is_active, "$g_ally_party"),
# 			(call_script, "script_battle_political_consequences", "$g_enemy_party", "$g_ally_party"),
# 		  (else_try),
# 			(call_script, "script_battle_political_consequences", "$g_enemy_party", "p_main_party"),
# 		  (try_end),
#
#           (call_script, "script_event_player_defeated_enemy_party", "$g_enemy_party"),
#           (call_script, "script_clear_party_group", "$g_enemy_party"),
#           (try_begin),
#             (eq, "$g_next_menu", -1),
#
#             #NPC companion changes begin
#             (call_script, "script_post_battle_personality_clash_check"),
#             #NPC companion changes end
#
#             #Post 0907 changes begin
#             (party_stack_get_troop_id, ":enemy_leader", "p_encountered_party_backup",0),
#             (try_begin),
#               (is_between, ":enemy_leader", active_npcs_begin, active_npcs_end),
#               (neg|is_between, "$g_encountered_party", centers_begin, centers_end),
#               (store_troop_faction, ":enemy_leader_faction", ":enemy_leader"),
#
#               (try_begin),
#                 (eq, "$g_ally_party", 0),
#                 (call_script, "script_add_log_entry", logent_lord_defeated_by_player, "trp_player",  -1, ":enemy_leader", ":enemy_leader_faction"),
#                 (try_begin),
#                   (eq, "$cheat_mode", 1),
#                   (display_message, "@{!}Victory comment. Player was alone"),
#                 (try_end),
#               (else_try),
#                 (ge, "$g_strength_contribution_of_player", 40),
#                 (call_script, "script_add_log_entry", logent_lord_defeated_by_player, "trp_player",  -1, ":enemy_leader", ":enemy_leader_faction"),
#                 (try_begin),
#                   (eq, "$cheat_mode", 1),
#                   (display_message, "@{!}Ordinary victory comment. The player provided at least 40 percent forces."),
#                 (try_end),
#               (else_try),
#                 (gt, "$g_starting_strength_enemy_party", 1000),
#                 (call_script, "script_get_closest_center", "p_main_party"),
#                 (assign, ":battle_of_where", reg0),
#                 (call_script, "script_add_log_entry", logent_player_participated_in_major_battle, "trp_player",  ":battle_of_where", -1, ":enemy_leader_faction"),
#                 (try_begin),
#                   (eq, "$cheat_mode", 1),
#                   (display_message, "@{!}Player participation comment. The enemy had at least 1k starting strength."),
#                 (try_end),
#               (else_try),
#                 (eq, "$cheat_mode", 1),
#                 (display_message, "@{!}No victory comment. The battle was small, and the player provided less than 40 percent of allied strength"),
#               (try_end),
#             (try_end),
#             #Post 0907 changes end
#             (val_add, "$g_total_victories", 1),
#             (leave_encounter),
#             (change_screen_return),
#           (else_try),
#             (try_begin), #my kingdom
#               #(change_screen_return),
#               (eq, "$g_next_menu", "mnu_castle_taken"),
#
#               (call_script, "script_add_log_entry", logent_castle_captured_by_player, "trp_player", "$g_encountered_party", -1, "$g_encountered_party_faction"),
#               (store_current_hours, ":hours"),
# 			  (faction_set_slot, "$players_kingdom", slot_faction_ai_last_decisive_event, ":hours"),
#
#               (try_begin), #player took a walled center while he is a vassal of npc kingdom.
#                 (is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
#                 (jump_to_menu, "$g_next_menu"),
#               (else_try), #player took a walled center while he is a vassal of rebels.
#                 (eq, "$players_kingdom", "fac_player_supporters_faction"),
#                 (assign, "$g_center_taken_by_player_faction", "$g_encountered_party"),
#                 (neg|faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
#                 (faction_get_slot, ":faction_leader", "fac_player_supporters_faction", slot_faction_leader),
#                 (change_screen_return),
#                 (start_map_conversation, ":faction_leader", -1),
#               (else_try), #player took a walled center for player's kingdom
#                 (neg|is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
#                 (assign, "$g_center_taken_by_player_faction", "$g_encountered_party"),
#                 (assign, "$talk_context", tc_give_center_to_fief),
#                 (change_screen_return),
#
#                 (assign, ":best_troop", "trp_swadian_sharpshooter"),
#                 (assign, ":maximum_troop_score", 0),
#
#                 (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
#                 (try_for_range, ":stack_no", 0, ":num_stacks"),
#                   (party_stack_get_troop_id, ":stack_troop", "p_main_party", ":stack_no"),
#                   (neq, ":stack_troop", "trp_player"),
#
#                   (party_stack_get_size, ":stack_size", "p_main_party", ":stack_no"),
#                   (party_stack_get_num_wounded, ":num_wounded", "p_main_party", ":stack_no"),
#                   (troop_get_slot, ":num_routed", "p_main_party", slot_troop_player_routed_agents),
#
#                   (assign, ":continue", 0),
#                   (try_begin),
#                     (neg|troop_is_hero, ":stack_troop"),
#                     (store_add, ":agents_which_cannot_speak", ":num_wounded", ":num_routed"),
#                     (gt, ":stack_size", ":agents_which_cannot_speak"),
#                     (assign, ":continue", 1),
#                   (else_try),
#                     (troop_is_hero, ":stack_troop"),
#                     (neg|troop_is_wounded, ":stack_troop"),
#                     (assign, ":continue", 1),
#                   (try_end),
#                   (eq, ":continue", 1),
#
#                   (try_begin),
#                     (troop_is_hero, ":stack_troop"),
#                     (troop_get_slot, ":troop_renown", ":stack_troop", slot_troop_renown),
#                     (store_mul, ":troop_score", ":troop_renown", 100),
#                     (val_add, ":troop_score", 1000),
#                   (else_try),
#                     (store_character_level, ":troop_level", ":stack_troop"),
#                     (assign, ":troop_score", ":troop_level"),
#                   (try_end),
#
#                   (try_begin),
#                     (gt, ":troop_score", ":maximum_troop_score"),
#                     (assign, ":maximum_troop_score", ":troop_score"),
#                     (assign, ":best_troop", ":stack_troop"),
#                     (party_stack_get_troop_dna, ":best_troop_dna", "p_main_party", ":stack_no"),
#                   (try_end),
#                 (try_end),
#
#                 (start_map_conversation, ":best_troop", ":best_troop_dna"),
#               (try_end),
#             (try_end),
#           (try_end),
#         (try_end),
#       ],
#     [
#       ("continue",[],"Continue...",[]),
#         ]
#   ),
#
#   (
#     "enemy_slipped_away",0,
#     "{s17}",
#     "none",
#     [],
#     [
#       ("continue",[],"Continue...",[(jump_to_menu,"mnu_total_victory")]),
#     ]
#   ),
#
#   (
#     "total_defeat",0,
#     "{!}You shouldn't be reading this...",
#     "none",
#     [
#         (play_track, "track_captured", 1),
#            # Free prisoners
#           (party_get_num_prisoner_stacks, ":num_prisoner_stacks","p_main_party"),
#           (try_for_range, ":stack_no", 0, ":num_prisoner_stacks"),
#             (party_prisoner_stack_get_troop_id, ":stack_troop","p_main_party",":stack_no"),
#             (troop_is_hero, ":stack_troop"),
#             (call_script, "script_remove_troop_from_prison", ":stack_troop"),
#           (try_end),
#
# 		  (try_begin),
# 		    (party_is_active, "$g_ally_party"),
# 			(call_script, "script_battle_political_consequences", "$g_ally_party", "$g_enemy_party"),
# 		  (else_try),
# 			(call_script, "script_battle_political_consequences", "p_main_party", "$g_enemy_party"),
# 		  (try_end),
#
#           (call_script, "script_loot_player_items", "$g_enemy_party"),
#
#           (assign, "$g_move_heroes", 0),
#           (party_clear, "p_temp_party"),
#           (call_script, "script_party_add_party_prisoners", "p_temp_party", "p_main_party"),
#           (call_script, "script_party_prisoners_add_party_companions", "p_temp_party", "p_main_party"),
#           (distribute_party_among_party_group, "p_temp_party", "$g_enemy_party"),
#
#           (assign, "$g_prison_heroes", 1),
#           (call_script, "script_party_remove_all_companions", "p_main_party"),
#           (assign, "$g_prison_heroes", 0),
#           (assign, "$g_move_heroes", 1),
#           (call_script, "script_party_remove_all_prisoners", "p_main_party"),
#
#           (val_add, "$g_total_defeats", 1),
#
#           (try_begin),
#             (neq, "$g_player_surrenders", 1),
#             (store_random_in_range, ":random_no", 0, 100),
#             (ge, ":random_no", "$g_player_luck"),
#             (jump_to_menu, "mnu_permanent_damage"),
#           (else_try),
#             (try_begin),
#               (eq, "$g_next_menu", -1),
#               (leave_encounter),
#               (change_screen_return),
#             (else_try),
#               (jump_to_menu, "$g_next_menu"),
#             (try_end),
#           (try_end),
#           (try_begin),
#             (gt, "$g_ally_party", 0),
#             (call_script, "script_party_wound_all_members", "$g_ally_party"),
#           (try_end),
#
# #Troop commentary changes begin
#           (party_get_num_companion_stacks, ":num_stacks", "p_encountered_party_backup"),
#           (try_for_range, ":stack_no", 0, ":num_stacks"),
#             (party_stack_get_troop_id,   ":stack_troop","p_encountered_party_backup",":stack_no"),
#             (is_between, ":stack_troop", active_npcs_begin, active_npcs_end),
# 			(troop_slot_eq, ":stack_troop", slot_troop_occupation, slto_kingdom_hero),
#             (store_troop_faction, ":victorious_faction", ":stack_troop"),
#             (call_script, "script_add_log_entry", logent_player_defeated_by_lord, "trp_player",  -1, ":stack_troop", ":victorious_faction"),
#           (try_end),
# #Troop commentary changes end
#
#       ],
#     []
#   ),
#
#   (
#     "permanent_damage",mnf_disable_all_keys,
#     "{s0}",
#     "none",
#     [
#       (assign, ":end_cond", 1),
#       (try_for_range, ":unused", 0, ":end_cond"),
#         (store_random_in_range, ":random_attribute", 0, 4),
#         (store_attribute_level, ":attr_level", "trp_player", ":random_attribute"),
#         (try_begin),
#           (gt, ":attr_level", 3),
#           (neq, ":random_attribute", ca_charisma),
#           (try_begin),
#             (eq, ":random_attribute", ca_strength),
#             (str_store_string, s0, "@Some of your tendons have been damaged in the battle. You lose 1 strength."),
#           (else_try),
#             (eq, ":random_attribute", ca_agility),
#             (str_store_string, s0, "@You took a nasty wound which will cause you to limp slightly even after it heals. You lose 1 agility."),
# ##          (else_try),
# ##            (eq, ":random_attribute", ca_charisma),
# ##            (str_store_string, s0, "@After the battle you are aghast to find that one of the terrible blows you suffered has left a deep, disfiguring scar on your face, horrifying those around you. Your charisma is reduced by 1."),
#           (else_try),
# ##            (eq, ":random_attribute", ca_intelligence),
#             (str_store_string, s0, "@You have trouble thinking straight after the battle, perhaps from a particularly hard hit to your head, and frequent headaches now plague your existence. Your intelligence is reduced by 1."),
#           (try_end),
#         (else_try),
#           (lt, ":end_cond", 200),
#           (val_add, ":end_cond", 1),
#         (try_end),
#       (try_end),
#       (try_begin),
#         (eq, ":end_cond", 200),
#         (try_begin),
#           (eq, "$g_next_menu", -1),
#           (leave_encounter),
#           (change_screen_return),
#         (else_try),
#           (jump_to_menu, "$g_next_menu"),
#         (try_end),
#       (else_try),
#         (troop_raise_attribute, "trp_player", ":random_attribute", -1),
#       (try_end),
#       ],
#     [
#       ("s0",
#        [
#          (store_random_in_range, ":random_no", 0, 4),
#          (try_begin),
#            (eq, ":random_no", 0),
#            (str_store_string, s0, "@Perhaps I'm getting unlucky..."),
#          (else_try),
#            (eq, ":random_no", 1),
#            (str_store_string, s0, "@Retirement is starting to sound better and better."),
#          (else_try),
#            (eq, ":random_no", 2),
#            (str_store_string, s0, "@No matter! I will persevere!"),
#          (else_try),
#            (eq, ":random_no", 3),
#            (troop_get_type, ":is_female", "trp_player"),
#            (try_begin),
#              (eq, ":is_female", 1),
#              (str_store_string, s0, "@What did I do to deserve this?"),
#            (else_try),
#              (str_store_string, s0, "@I suppose it'll make for a good story, at least..."),
#            (try_end),
#          (try_end),
#          ],
#        "{s0}",
#        [
#          (try_begin),
#            (eq, "$g_next_menu", -1),
#            (leave_encounter),
#            (change_screen_return),
#          (else_try),
#            (jump_to_menu, "$g_next_menu"),
#          (try_end),
#          ]),
#       ]
#   ),
#
#   (
#     "pre_join",0,
#     "You come across a battle between {s2} and {s1}. You decide to...",
#     "none",
#     [
#         (str_store_party_name, 1,"$g_encountered_party"),
#         (str_store_party_name, 2,"$g_encountered_party_2"),
#       ],
#     [
#       ("pre_join_help_attackers",[
#           (store_faction_of_party, ":attacker_faction", "$g_encountered_party_2"),
#           (store_relation, ":attacker_relation", ":attacker_faction", "fac_player_supporters_faction"),
#           (store_faction_of_party, ":defender_faction", "$g_encountered_party"),
#           (store_relation, ":defender_relation", ":defender_faction", "fac_player_supporters_faction"),
#           (ge, ":attacker_relation", 0),
#           (lt, ":defender_relation", 0),
#           ],
#           "Move in to help the {s2}.",[
#               (select_enemy,0),
#               (assign,"$g_enemy_party","$g_encountered_party"),
#               (assign,"$g_ally_party","$g_encountered_party_2"),
#               (jump_to_menu,"mnu_join_battle")]),
#       ("pre_join_help_defenders",[
#           (store_faction_of_party, ":attacker_faction", "$g_encountered_party_2"),
#           (store_relation, ":attacker_relation", ":attacker_faction", "fac_player_supporters_faction"),
#           (store_faction_of_party, ":defender_faction", "$g_encountered_party"),
#           (store_relation, ":defender_relation", ":defender_faction", "fac_player_supporters_faction"),
#           (ge, ":defender_relation", 0),
#           (lt, ":attacker_relation", 0),
#           ],
#           "Rush to the aid of the {s1}.",[
#               (select_enemy,1),
#               (assign,"$g_enemy_party","$g_encountered_party_2"),
#               (assign,"$g_ally_party","$g_encountered_party"),
#               (jump_to_menu,"mnu_join_battle")]),
#       ("pre_join_leave",[],"Don't get involved.",[(leave_encounter),(change_screen_return)]),
#     ]
#   ),
#
#   (
#     "join_battle",0,
#     "You are helping the {s2} against the {s1}. You have {reg10} troops fit for battle against the enemy's {reg11}.",
#     "none",
#     [
#         (str_store_party_name, 1,"$g_enemy_party"),
#         (str_store_party_name, 2,"$g_ally_party"),
#
#         (call_script, "script_encounter_calculate_fit"),
#
#         (try_begin),
#           (eq, "$new_encounter", 1),
#           (assign, "$new_encounter", 0),
#           (call_script, "script_encounter_init_variables"),
#         (else_try), #second or more turn
#           (eq, "$g_leave_encounter",1),
#           (change_screen_return),
#         (try_end),
#
#         (try_begin),
#           (call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
#           (assign, ":num_enemy_regulars_remaining", reg0),
#           (assign, ":enemy_finished",0),
#           (try_begin),
#             (eq, "$g_battle_result", 1),
#
#             (this_or_next|le, ":num_enemy_regulars_remaining", 0), #battle won
#             (le, ":num_enemy_regulars_remaining", "$num_routed_enemies"), #replaced for above line because we do not want routed agents to spawn again in next turn of battle.
#
#             (assign, ":enemy_finished",1),
#           (else_try),
#             (eq, "$g_engaged_enemy", 1),
#             (le, "$g_enemy_fit_for_battle",0),
#             (ge, "$g_friend_fit_for_battle",1),
#             (assign, ":enemy_finished",1),
#           (try_end),
#
#           (this_or_next|eq, ":enemy_finished",1),
#           (eq,"$g_enemy_surrenders",1),
#           (assign, "$g_next_menu", -1),
#           (jump_to_menu, "mnu_total_victory"),
#         (else_try),
#           (call_script, "script_party_count_members_with_full_health", "p_collective_friends"),
#           (assign, ":num_ally_regulars_remaining", reg0),
#           (assign, ":battle_lost", 0),
#           (try_begin),
#             (eq, "$g_battle_result", -1),
#
#             #(eq, ":num_ally_regulars_remaining", 0), #battle lost
#             (le, ":num_ally_regulars_remaining",  "$num_routed_allies"), #replaced for above line because we do not want routed agents to spawn again in next turn of battle.
#
#             (assign, ":battle_lost",1),
#           (try_end),
#
#           (this_or_next|eq, ":battle_lost",1),
#           (eq,"$g_player_surrenders",1),
#           (leave_encounter),
#           (change_screen_return),
#         (try_end),
#       ],
#     [
#       ("join_attack",
#       [
#         (neg|troop_is_wounded, "trp_player"),
#       ],
#       "Charge the enemy.",
#       [
#         (assign, "$g_joined_battle_to_help", 1),
#         (party_set_next_battle_simulation_time, "$g_encountered_party", -1),
#         (assign, "$g_battle_result", 0),
#         (call_script, "script_calculate_renown_value"),
#         (call_script, "script_calculate_battle_advantage"),
#         (set_battle_advantage, reg0),
#         (set_party_battle_mode),
#         (set_jump_mission,"mt_lead_charge"),
#         (call_script, "script_setup_random_scene"),
#         (assign, "$g_next_menu", "mnu_join_battle"),
#         (jump_to_menu, "mnu_battle_debrief"),
#         (change_screen_mission),
#       ]),
#
#       ("join_order_attack",
#       [
#         (call_script, "script_party_count_members_with_full_health", "p_main_party"),
#         (ge, reg0, 3),
#       ],
#       "Order your troops to attack with your allies while you stay back.",
#       [
#         (assign, "$g_joined_battle_to_help", 1),
#         (party_set_next_battle_simulation_time, "$g_encountered_party", -1),
#         (jump_to_menu,"mnu_join_order_attack"),
#       ]),
#
#       ("join_leave",[],"Leave.",
#       [
#         (try_begin),
#            (neg|troop_is_wounded, "trp_player"),
#            (call_script, "script_objectionable_action", tmt_aristocratic, "str_flee_battle"),
#            (party_stack_get_troop_id, ":enemy_leader","$g_enemy_party",0),
# 		   (is_between, ":enemy_leader", active_npcs_begin, active_npcs_end),
#            (call_script, "script_add_log_entry", logent_player_retreated_from_lord, "trp_player",  -1, ":enemy_leader", -1),
#         (try_end),
#
#         (leave_encounter),(change_screen_return)]),
#       ]),
#
#   (
#     "join_order_attack",mnf_disable_all_keys,
#     "{s4}^^Your casualties: {s8}^^Allies' casualties: {s9}^^Enemy casualties: {s10}",
#     "none",
#     [
#       (call_script, "script_party_calculate_strength", "p_main_party", 1), #skip player
#       (assign, ":player_party_strength", reg0),
#       (val_div, ":player_party_strength", 5),
#       (call_script, "script_party_calculate_strength", "p_collective_friends", 0),
#       (assign, ":friend_party_strength", reg0),
#       (val_div, ":friend_party_strength", 5),
#
#       (call_script, "script_party_calculate_strength", "p_collective_enemy", 0),
#       (assign, ":enemy_party_strength", reg0),
#       (val_div, ":enemy_party_strength", 5),
#
#       (try_begin),
#         (eq, ":friend_party_strength", 0),
#         (store_div, ":enemy_party_strength_for_p", ":enemy_party_strength", 2),
#       (else_try),
#         (assign, ":enemy_party_strength_for_p", ":enemy_party_strength"),
#         (val_mul, ":enemy_party_strength_for_p", ":player_party_strength"),
#         (val_div, ":enemy_party_strength_for_p", ":friend_party_strength"),
#       (try_end),
#
#       (val_sub, ":enemy_party_strength", ":enemy_party_strength_for_p"),
#       (inflict_casualties_to_party_group, "p_main_party", ":enemy_party_strength_for_p", "p_temp_casualties"),
#       (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
#       (str_store_string_reg, s8, s0),
#
#       (inflict_casualties_to_party_group, "$g_enemy_party", ":friend_party_strength", "p_temp_casualties"),
#
#       #ozan begin
#       (party_get_num_companion_stacks, ":num_stacks", "p_temp_casualties"),
#       (try_for_range, ":stack_no", 0, ":num_stacks"),
#         (party_stack_get_troop_id, ":stack_troop", "p_temp_casualties", ":stack_no"),
#         (try_begin),
#           (party_stack_get_size, ":stack_size", "p_temp_casualties", ":stack_no"),
#           (gt, ":stack_size", 0),
#           (party_add_members, "p_total_enemy_casualties", ":stack_troop", ":stack_size"), #addition_to_p_total_enemy_casualties
#           (party_stack_get_num_wounded, ":stack_wounded_size", "p_temp_casualties", ":stack_no"),
#           (gt, ":stack_wounded_size", 0),
#           (party_wound_members, "p_total_enemy_casualties", ":stack_troop", ":stack_wounded_size"),
#         (try_end),
#       (try_end),
#       #ozan end
#
#       (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
#       (str_store_string_reg, s10, s0),
#
#       (call_script, "script_collect_friendly_parties"),
#       #(party_collect_attachments_to_party, "$g_ally_party", "p_collective_ally"),
#
#       (inflict_casualties_to_party_group, "$g_ally_party", ":enemy_party_strength", "p_temp_casualties"),
#       (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
#       (str_store_string_reg, s9, s0),
#       (party_collect_attachments_to_party, "$g_enemy_party", "p_collective_enemy"),
#
#        #(assign, "$cant_leave_encounter", 0),
#        (assign, "$no_soldiers_left", 0),
#        (try_begin),
#          (call_script, "script_party_count_members_with_full_health","p_main_party"),
#          (assign, ":num_our_regulars_remaining", reg0),
#
#          #(le, ":num_our_regulars_remaining", 0),
#          (le, ":num_our_regulars_remaining", "$num_routed_us"), #replaced for above line because we do not want routed agents to spawn again in next turn of battle.
#
#          (assign, "$no_soldiers_left", 1),
#          (str_store_string, s4, "str_join_order_attack_failure"),
#        (else_try),
#          (call_script, "script_party_count_members_with_full_health","p_collective_enemy"),
#          (assign, ":num_enemy_regulars_remaining", reg0),
#
#          (this_or_next|le, ":num_enemy_regulars_remaining", 0),
#          (le, ":num_enemy_regulars_remaining", "$num_routed_enemies"), #replaced for above line because we do not want routed agents to spawn again in next turn of battle.
#
#          (assign, "$g_battle_result", 1),
#          (assign, "$no_soldiers_left", 1),
#          (str_store_string, s4, "str_join_order_attack_success"),
#        (else_try),
#          (str_store_string, s4, "str_join_order_attack_continue"),
#        (try_end),
#     ],
#     [
#       ("continue",[],"Continue...",
#       [
#         (jump_to_menu,"mnu_join_battle"),
#       ]),
#     ]
#   ),

  # (
  #   "town_trade",0,
  #   "You head towards the marketplace.",
  #   "none",
  #   [],
  #   [
  #     ("assess_prices",
  #      [
  #        (store_faction_of_party, ":current_town_faction", "$current_town"),
  #        (store_relation, ":reln", ":current_town_faction", "fac_player_supporters_faction"),
  #        (ge, ":reln", 0),
  #        ],
  #      "Assess the local prices.",
  #      [
  #          (jump_to_menu,"mnu_town_trade_assessment_begin"),
  #       ]),
  #     ("trade_with_arms_merchant",[(party_slot_ge, "$current_town", slot_town_weaponsmith, 1)],
  #      "Trade with the arms merchant.",
  #      [
  #          (party_get_slot, ":merchant_troop", "$current_town", slot_town_weaponsmith),
  #          (change_screen_trade, ":merchant_troop"),
  #       ]),
  #     ("trade_with_armor_merchant",[(party_slot_ge, "$current_town", slot_town_armorer, 1)],
  #      "Trade with the armor merchant.",
  #      [
  #          (party_get_slot, ":merchant_troop", "$current_town", slot_town_armorer),
  #          (change_screen_trade, ":merchant_troop"),
  #       ]),
  #     ("trade_with_horse_merchant",[(party_slot_ge, "$current_town", slot_town_horse_merchant, 1)],
  #      "Trade with the horse merchant.",
  #      [
  #          (party_get_slot, ":merchant_troop", "$current_town", slot_town_horse_merchant),
  #          (change_screen_trade, ":merchant_troop"),
  #       ]),
  #     ("trade_with_goods_merchant",[(party_slot_ge, "$current_town", slot_town_merchant, 1)],
  #      "Trade with the goods merchant.",
  #      [
  #          (party_get_slot, ":merchant_troop", "$current_town", slot_town_merchant),
  #          (change_screen_trade, ":merchant_troop"),
  #       ]),
  #     ("back_to_town_menu",[],"Head back.",
  #      [
  #          (jump_to_menu,"mnu_town"),
  #       ]),
  #   ]
  # ),













    (
    "debug_alert_from_s65",0,
    "DEBUG ALERT: {s65}",
    "none",
    [
    ],
    [
      ("continue",[],"Continue...",
       [
		(assign, "$debug_message_in_queue", 0),
        (change_screen_return),
        ]),
     ]
  ),
      
  (
    "auto_return_to_map",0,
    "stub",
    "none",
    [(change_screen_map)],
    []
  ),

 ]
