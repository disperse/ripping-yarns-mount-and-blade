from header_common import *
from header_operations import *
from header_parties import *
from header_items import *
from header_skills import *
from header_triggers import *
from header_troops import *
from header_music import *

from module_constants import *

####################################################################################################################
# Simple triggers are the alternative to old style triggers. They do not preserve state, and thus simpler to maintain.
#
#  Each simple trigger contains the following fields:
# 1) Check interval: How frequently this trigger will be checked
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference. 
####################################################################################################################



simple_triggers = [
    # Updating player icon in every frame
    (0,
     [(troop_get_inventory_slot, ":cur_horse", "trp_player", 8), #horse slot
      (assign, ":new_icon", -1),
      (try_begin),
      (eq, "$g_player_icon_state", pis_normal),
      (try_begin),
      (ge, ":cur_horse", 0),
      (assign, ":new_icon", "icon_player_horseman"),
      (else_try),
      (assign, ":new_icon", "icon_player"),
      (try_end),
      (else_try),
      (eq, "$g_player_icon_state", pis_camping),
      (assign, ":new_icon", "icon_camp"),
      (else_try),
      (eq, "$g_player_icon_state", pis_ship),
      (assign, ":new_icon", "icon_ship"),
      (try_end),
      (neq, ":new_icon", "$g_player_party_icon"),
      (assign, "$g_player_party_icon", ":new_icon"),
      (party_set_icon, "p_main_party", ":new_icon"),
      ]),
    (24,
     []),
    (24,
     []),
    (24,
     []),
    (24,
     []),
    (24,
     []),
    (24,
     []),
    (24,
     []),
    (24,
     []),
    (24,
     []),
]
