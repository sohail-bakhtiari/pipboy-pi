import os
from data_models import LimbPosition, IconConfig
from items import ItemLoader, Inventory
from settings_secrets import *
import platform

#######################################################
# Load items from the items.ini file
#######################################################
loader = ItemLoader('modules/items.ini')
items = loader.load_items()

# ==================================================
# Constants (Modify only if program structure changes)
# ==================================================
TABS = ("STAT", "INV", "DATA", "MAP", "RADIO")
SUBTABS = {
    "STAT": ("STATUS", "SPECIAL", "PERKS"),
    "INV": ("WEAPONS", "APPAREL", "AID", "MISC", "JUNK", "MODS", "AMMO"),
    "DATA": ("QUESTS", "WORKSHOPS", "STATS", "SETTINGS")
}

# ==================================================
# User Configuration (Adjust these for setup/preferences)
# ==================================================


# ------------------
# General Settings
# ------------------

RASPI = True
SPEED = 1
GAME_ACCURATE_MODE = False
YEARS_ADDED = 263

# ------------------
# Screen Settings
# ------------------
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 480
FPS = 24
FULLSCREEN = True if RASPI else False 
BACKGROUND = (0, 0, 0)
PIP_BOY_LIGHT = (0, 255, 0)
PIP_BOY_MIDDLE = (0, 190, 0)
PIP_BOY_DARKER = (0, 127, 0)
PIP_BOY_DARK = (0, 63, 0)

# ------------------
# Audio Settings
# ------------------
SOUND_ON = True
VOLUME = 1
MUSIC_VOLUME = 1
SWITCH_SOUND_CHANCE = 70

# ------------------
# Visual Effects
# ------------------
SHOW_CRT = True
BLOOM_EFFECT = True
GLITCH_MOVE_CHANCE = 60
BOOT_SCREEN = False
RANDOM_GLITCHES = True
RANDOM_GLITCH_CHANCE = 0.5

# ------------------
# Path Configuration
# ------------------
from paths import *

# ------------------
# UI Layout
# ------------------
TAB_MARGIN = 20
TAB_VERTICAL_OFFSET = 0
TAB_VERTICAL_LINE_OFFSET = 10
TAB_HORIZONTAL_LINE_OFFSET =4
TAB_SCREEN_EDGE_LENGTH = 2
TAB_HORIZONTAL_LENGTH = TAB_HORIZONTAL_LINE_OFFSET // 1.1
TAB_BOTTOM_MARGIN = 2
BOTTOM_BAR_VERTICAL_MARGINS = 2
BOTTOM_BAR_HEIGHT = 18
BOTTOM_BAR_MARGIN = 5
TAB_SIDE_MARGIN = 0
SUBTAB_SPACING = 5
SUBTAB_VERTICAL_OFFSET = 1
LIST_TOP_MARGIN = 10

# ------------------
# Player Settings
# ------------------
PLAYER_NAME = "BestPi"
HP_MAX = 120
HP_CURRENT = 100
AP_MAX = 90
AP_CURRENT = 90
RADIATION_CURRENT = 10 # percentage of hp
LEVEL = 28
XP_CURRENT = 39
ADDICTED = False

DEFAULT_LIMB_DAMAGE = [70, 14, 69, 54, 28, 100]
CRIPPLED_THRESHOLD = 20
DAMAGED_THRESHOLD = 50
DEFAULT_STATS_DAMAGE = [
    IconConfig(STAT_TAB_RETICLE, 18),
    IconConfig(STAT_TAB_BOLT, 10)
]
DEFAULT_STATS_ARMOR = [
    IconConfig(STAT_TAB_SHIELD, 5),
    IconConfig(STAT_TAB_RADIATION, 10)
]
DEFAULT_SPECIAL_STATS = [2, 3, 2, 7, 3, 1, 0]
SPECIAL_STATS_BONUS = [0, 0, 0, 0, 0, 0, 0]

_inventory = Inventory()
_inventory.add_item(items['10mm Pistol'], 2)
_inventory.add_item(items['Fat Man'])
_inventory.add_item(items['Vault 111 Jumpsuit'])
_inventory.add_item(items['Road Leathers'], 3)
_inventory.add_item(items['Stimpak'], 5)
_inventory.add_item(items['RadAway'], 2)
_inventory.add_item(items['Nuka-Cola'], 3)
_inventory.add_item(items['Abraxo Cleaner'])
_inventory.add_item(items['Fusion Core'])
_inventory.add_item(items['.308 Round'], 10)
_inventory.add_item(items['Fusion Cell'], 25)
_inventory.add_item(items['10mm Round'], 37)
_inventory.add_item(items['Mini Nuke'])



for item in _inventory.get_all_items():
    for i in range(7):
        if "special_bonus" in item.__dict__:
            SPECIAL_STATS_BONUS[i] += item.special_bonus[i]

MAX_WEIGHT = 200 + (DEFAULT_SPECIAL_STATS[0] * 10)
CAPS = 1000

TOTAL_AMMO = {}
for item in _inventory.get_all_items():
    if item.category == 'Ammo':
        if item.name in TOTAL_AMMO:
            TOTAL_AMMO[item.name] += 1
        else:
            TOTAL_AMMO[item.name] = 1
            
# ------------------
# Stat Tab Settings
# ------------------
# Status subtab
CONDITIONBOY_SCALE = 4
CONDITIONBOY_OFFSET = 12
LIMB_POSITIONS = [
    LimbPosition(0, 10, 'head'),
    LimbPosition(-50, 50, 'left_arm'),
    LimbPosition(50, 50, 'right_arm'),
    LimbPosition(-50, 95, 'left_leg'),
    LimbPosition(50, 95, 'right_leg'),
    LimbPosition(0, 130, 'torso')
]
DAMAGE_ARMOUR_MARGIN_SMALL = 2
DAMAGE_ARMOUR_ICON_SMALL_SIZE = 0.5
DAMAGE_ARMOUR_MARGIN_BIG = 8
DAMAGE_ARMOUR_ICON_BIG_SIZE = 0.45
DAMAGE_ARMOUR_ICON_ABSOLUTE_SIZE = 11.5
DAMAGE_ARMOUR_ICON_MARGIN = 7
LIMB_DAMAGE_WIDTH = 20

# Special subtab
SPECIAL = ("Strength", "Perception", "Endurance", "Charisma", "Intelligence", "Agility", "Luck")
SPECIAL_IMAGE_SCALE = 0.45
SPECIAL_DESCRIPTIONS = [
    "Strength is a measure of your raw physical power. It affects how much you can carry, and the damage of all melee attacks.",
    "Perception is your environmental awareness and 'sixth sense', and affects weapon accuracy in V.A.T.S.",
    "Endurance is a measure of your overall physical fitness. It affect your total Health and the Action Point drain from sprinting.",
    "Charisma is your ability to charm and convince others. It affects your success to persuade in dialogue and prices when you barter.",
    "Intelligence is a measure of your overall metal acuity, and affects the number of Experience Points earned",
    "Agility is a measure of your overall fitnesse and reflexes. It affects the number of Action Points in V.A.T.S. and your ability to sneak",
    "Luck is a measure of your general good fortune, and affects the recharge rate of Critical Hits, and the chances of finding better items."
]

# ------------------
# Inventory Tab Settings
# ------------------
MAX_CARRY_WEIGHT = 150
GRID_BOTTOM_MARGIN = 0
GRID_RIGHT_MARGIN = 35
GRID_LEFT_MARGIN = 5
TURNTABLE_LEFT_MARGIN = 15

# ------------------
# Radio Tab Settings
# ------------------
RADIO_STATION_MARGIN = 10
RADIO_STATION_TEXT_MARGIN = 10
RADIO_STATION_SELECTION_MARGIN = 6
RADIO_STATION_SELECTION_DOT_SIZE = 4
RADIO_WAVE_POINTS = 12
RADIO_WAVE_VARIANCE = 5
RADIO_WAVE_SMOOTHING = 0.5
RADIO_WAVE_MAX = 10
RADIO_WAVE_MIN = 2
RADIO_WAVE_VISUALIZER_X_OFFSET = 10
RADIO_WAVE_VISUALIZER_Y_OFFSET = 10
RADIO_WAVE_VISUALIZER_SIZE_OFFSET = 50
RADIO_WAVE_VISUALIZER_GRID_LINES = 15
RADIO_WAVE_BATCH_SIZE = 5
RADIO_WAVE_SMOOTHING_FACTOR = 0.05
INTERMISSION_FREQUENCY = 50

# ------------------
# Map Tab Settings
# ------------------
FAKE_LOCATION = "Commonwealth"
SHOW_ALL_MARKERS = True
MAP_ZOOM_SPEED = 0.2
MAP_MOVE_SPEED = 30
MIN_MAP_ZOOM = 1.5
INITIAL_MAP_ZOOM = 1
MARKER_SCALE_MIN = 0.5
MARKER_SCALE_MAX = 1.5
MAP_EDGES_OFFSET = 5
MAP_SIZE = 1024
EXTRA_MAP_SIZE = 100
LOGO_SIZE = 7.3
MAP_ZOOM = 12
MAP_ICON_SIZE = 30
MAP_PLACES_ZOOM = 20000
MAP_MIN_NODE_DISTANCE = 200

MAP_TYPE_PRIORITY = {
    "town": 50,
    "police": 5,
    "village": 50,
    "ruins": 20,
    "base": 10,
    "bunker": 40,
    "hamlet": 10,
    "farmland": 10,
    "lake": 6,
    "bridge": 6,
    "industrial": 9,
}

OSM_KEYS = (
    "place",
    "water",
    "historic",
    "landuse",
    "military",
    "man_made",
    "amenity",
)
    

MAP_TILE_SIZE = 512


if os.path.exists("modules/user_config.py"):
    from user_config import *
    

