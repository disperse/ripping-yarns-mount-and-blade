# -*- coding: cp1254 -*-
from header_common import *
from header_dialogs import *
from header_operations import *
from header_parties import *
from header_item_modifiers import *
from header_skills import *
from header_triggers import *
from ID_troops import *
from ID_party_templates import *

from module_constants import *


####################################################################################################################
# During a dialog, the dialog lines are scanned from top to bottom.
# If the dialog-line is spoken by the player, all the matching lines are displayed for the player to pick from.
# If the dialog-line is spoken by another, the first (top-most) matching line is selected.
#
#  Each dialog line contains the following fields:
# 1) Dialogue partner: This should match the person player is talking to.
#    Usually this is a troop-id.
#    You can also use a party-template-id by appending '|party_tpl' to this field.
#    Use the constant 'anyone' if you'd like the line to match anybody.
#    Appending '|plyr' to this field means that the actual line is spoken by the player
#    Appending '|other(troop_id)' means that this line is spoken by a third person on the scene.
#       (You must make sure that this third person is present on the scene)
#
# 2) Starting dialog-state:
#    During a dialog there's always an active Dialog-state.
#    A dialog-line's starting dialog state must be the same as the active dialog state, for the line to be a possible candidate.
#    If the dialog is started by meeting a party on the map, initially, the active dialog state is "start"
#    If the dialog is started by speaking to an NPC in a town, initially, the active dialog state is "start"
#    If the dialog is started by helping a party defeat another party, initially, the active dialog state is "party_relieved"
#    If the dialog is started by liberating a prisoner, initially, the active dialog state is "prisoner_liberated"
#    If the dialog is started by defeating a party led by a hero, initially, the active dialog state is "enemy_defeated"
#    If the dialog is started by a trigger, initially, the active dialog state is "event_triggered"
# 3) Conditions block (list): This must be a valid operation block. See header_operations.py for reference.  
# 4) Dialog Text (string):
# 5) Ending dialog-state:
#    If a dialog line is picked, the active dialog-state will become the picked line's ending dialog-state.
# 6) Consequences block (list): This must be a valid operation block. See header_operations.py for reference.
# 7) Voice-over (string): sound filename for the voice over. Leave here empty for no voice over
####################################################################################################################

dialogs = [
#   [anyone ,"start", [(store_conversation_troop, "$g_talk_troop"),
#                      (store_conversation_agent, "$g_talk_agent"),
#                      (store_troop_faction, "$g_talk_troop_faction", "$g_talk_troop"),
# #                     (troop_get_slot, "$g_talk_troop_relation", "$g_talk_troop", slot_troop_player_relation),
#                      (call_script, "script_troop_get_player_relation", "$g_talk_troop"),
#                      (assign, "$g_talk_troop_relation", reg0),
#
# 					 #This may be different way to handle persuasion, which might be a little more transparent to the player in its effects
# 					 #Persuasion will affect the player's relation with the other character -- but only for 1 on 1 conversations
# 					 (store_skill_level, ":persuasion", "skl_persuasion", "trp_player"),
# 					 (assign, "$g_talk_troop_effective_relation", "$g_talk_troop_relation"),
# 					 (val_add, "$g_talk_troop_effective_relation", ":persuasion"),
# 					 (try_begin),
# 						(gt, "$g_talk_troop_effective_relation", 0),
# 						(store_add, ":persuasion_modifier", 10, ":persuasion"),
# 						(val_mul, "$g_talk_troop_effective_relation", ":persuasion_modifier"),
# 						(val_div, "$g_talk_troop_effective_relation", 10),
# 					 (else_try),
# 						(lt, "$g_talk_troop_effective_relation", 0),
# 						(store_sub, ":persuasion_modifier", 20, ":persuasion"),
# 						(val_mul, "$g_talk_troop_effective_relation", ":persuasion_modifier"),
# 						(val_div, "$g_talk_troop_effective_relation", 20),
# 					 (try_end),
# 					 (val_clamp, "$g_talk_troop_effective_relation", -100, 101),
# 					 (try_begin),
# 						(eq, "$cheat_mode", 1),
# 						(assign, reg3, "$g_talk_troop_effective_relation"),
# 						(display_message, "str_test_effective_relation_=_reg3"),
# 					 (try_end),
#
#                      (try_begin),
#                        (this_or_next|is_between, "$g_talk_troop", village_elders_begin, village_elders_end),
#                        (is_between, "$g_talk_troop", mayors_begin, mayors_end),
#                        (party_get_slot, "$g_talk_troop_relation", "$current_town", slot_center_player_relation),
#                      (try_end),
#                      (store_relation, "$g_talk_troop_faction_relation", "$g_talk_troop_faction", "fac_player_faction"),
#
#                      (assign, "$g_talk_troop_party", "$g_encountered_party"),
#                      (try_begin),
#                        (troop_slot_ge, "$g_talk_troop", slot_troop_leaded_party, 1),
#                        (troop_get_slot, "$g_talk_troop_party", "$g_talk_troop", slot_troop_leaded_party),
#                      (try_end),
#
# #                     (assign, "$g_talk_troop_kingdom_relation", 0),
# #                     (try_begin),
# #                       (gt, "$players_kingdom", 0),
# #                       (store_relation, "$g_talk_troop_kingdom_relation", "$g_talk_troop_faction", "$players_kingdom"),
# #                     (try_end),
#
#
#
#                      (store_current_hours, "$g_current_hours"),
#                      (troop_get_slot, "$g_talk_troop_last_talk_time", "$g_talk_troop", slot_troop_last_talk_time),
#                      (troop_set_slot, "$g_talk_troop", slot_troop_last_talk_time, "$g_current_hours"),
#                      (store_sub, "$g_time_since_last_talk","$g_current_hours","$g_talk_troop_last_talk_time"),
#                      (troop_get_slot, "$g_talk_troop_met", "$g_talk_troop", slot_troop_met),
# 					 (val_min, "$g_talk_troop_met", 1), #the global variable goes no higher than one
# 					 (try_begin),
# 					    (troop_slot_eq, "$g_talk_troop", slot_troop_met, 0),
# 						(troop_set_slot, "$g_talk_troop", slot_troop_met, 1),
#
# 						#Possible later activations of notes
# 						(try_begin),
# 							(is_between, "$g_talk_troop", kingdom_ladies_begin, kingdom_ladies_end),
# 						(try_end),
#
# 					 (try_end),
#
#                      (try_begin),
# #                       (this_or_next|eq, "$talk_context", tc_party_encounter),
# #                       (this_or_next|eq, "$talk_context", tc_castle_commander),
#                        (call_script, "script_party_calculate_strength", "p_collective_enemy",0),
#                        (assign, "$g_enemy_strength", reg0),
#                        (call_script, "script_party_calculate_strength", "p_main_party",0),
#                        (assign, "$g_ally_strength", reg0),
#                        (store_mul, "$g_strength_ratio", "$g_ally_strength", 100),
# 					   (assign, ":enemy_strength", "$g_enemy_strength"), #these two lines added to avoid div by zero error
# 					   (val_max, ":enemy_strength", 1),
#                        (val_div, "$g_strength_ratio", ":enemy_strength"),
#                      (try_end),
#
#                      (assign, "$g_comment_found", 0),
#
# 					 (assign, "$g_comment_has_rejoinder", 0),
# 					 (assign, "$g_romantic_comment_made", 0),
# 					 (assign, "$skip_lord_assumes_argument", 0), #a lord pre-empts a player's issue, ie, when the player is conducting a rebellion
# 					 (assign, "$bypass_female_vassal_explanation", 0),
# 					 (assign, "$g_done_wedding_comment", 0),
#
# #					 (assign, "$g_time_to_spare", 0),
#
#
#                      (try_begin),
#                        (troop_is_hero, "$g_talk_troop"),
#                        (talk_info_show, 1),
#                        (call_script, "script_setup_talk_info"),
#                      (try_end),
#
# 					 (assign, "$g_last_comment_copied_to_s42", 0),
#                      (try_begin),
#                        (troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_hero),
#                        (call_script, "script_get_relevant_comment_to_s42"),
#                        (assign, "$g_comment_found", reg0),
#                      (try_end),
#
#                      (troop_get_type, reg65, "$g_talk_troop"),
#                      (try_begin),
#                        (faction_slot_eq,"$g_talk_troop_faction",slot_faction_leader,"$g_talk_troop"),
#                        (str_store_string,s64,"@{reg65?my Lady:my Lord}"), #bug fix
#                        (str_store_string,s65,"@{reg65?my Lady:my Lord}"),
#                        (str_store_string,s66,"@{reg65?My Lady:My Lord}"),
#                        (str_store_string,s67,"@{reg65?My Lady:My Lord}"), #bug fix
#                      (else_try),
#                        (str_store_string,s64,"@{reg65?madame:sir}"), #bug fix
#                        (str_store_string,s65,"@{reg65?madame:sir}"),
#                        (str_store_string,s66,"@{reg65?Madame:Sir}"),
#                        (str_store_string,s67,"@{reg65?Madame:Sir}"), #bug fix
#                      (try_end),
#
# 					 (try_begin),
# 						(gt, "$cheat_mode", 0),
# 						(assign, reg4, "$talk_context"),
# 						(display_message, "@{!}DEBUG -- Talk context: {reg4}"),
# 					 (try_end),
#
# 					 (try_begin),
# 						(gt, "$cheat_mode", 0),
# 						(assign, reg4, "$g_time_since_last_talk"),
# 						(display_message, "@{!}DEBUG -- Time since last talk: {reg4}"),
# 					 (try_end),
#
#
# 					 (try_begin),
# 						(eq, "$cheat_mode", 0),
# 						(store_partner_quest, ":quest"),
# 						(ge, ":quest", 0),
# 						(str_store_quest_name, s4, ":quest"),
#
# 					 (try_end),
#
#                      (eq, 1, 0)],
#    "{!}Warning: This line is never displayed. It is just for storing conversation variables.", "close_window", []],
]
