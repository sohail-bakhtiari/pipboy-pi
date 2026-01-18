
# Fonts
MAIN_FONT_PATH = "fonts/RobotoCondensed-Bold.ttf"
ROBOTO_BOLD_PATH = "fonts/Roboto-Bold.ttf"
ROBOTO_PATH = "fonts/Roboto-Regular.ttf"
ROBOTO_CONDENSED_PATH = "fonts/RobotoCondensed-Regular.ttf"
ROBOTO_CONDENSED_BOLD_PATH = "fonts/RobotoCondensed-Bold.ttf"
TECH_MONO_FONT_PATH = "fonts/TechMono.ttf"

# Images
CRT_OVERLAY = "images/overlay.png"
BLOOM_OVERLAY = "images/dirt.png"
SCANLINE_OVERLAY = "images/scanline.png"
SCANLINES_OVERLAY = "images/scanlines.png"
CRT_STATIC = "images/static"
BOOT_THUMBS = "images/boot"
STAT_TAB_BODY_BASE_FOLDER = "images/stats/body"
STAT_TAB_BODY_SVG_BASE_FOLDER = "images/svgs/vaultboy_body"

STAT_TAB_HEADS = {
    "normal" : "images/svgs/vaultboy_body/heads/normal.svg",
    "damaged" : "images/svgs/vaultboy_body/heads/damaged.svg",
    "addicted" : "images/svgs/vaultboy_body/heads/addicted.svg",
    "radiated" : "images/svgs/vaultboy_body/heads/radiated.svg",
    "crippled" : "images/svgs/vaultboy_body/heads/crippled.svg",
    "addicted_crippled" : "images/svgs/vaultboy_body/heads/addicted_crippled.svg",
    "radiated_crippled" : "images/svgs/vaultboy_body/heads/radiated_crippled.svg",
}

STAT_TAB_GUN = "images/stats/gun.png"
STAT_TAB_ARMOUR = "images/stats/helmet.png"
STAT_TAB_RETICLE = "images/stats/reticle.png"
STAT_TAB_SHIELD = "images/stats/shield.png"
STAT_TAB_RADIATION = "images/stats/radiation.png"
STAT_TAB_BOLT = "images/stats/bolt.png"
SPECIAL_BASE_FOLDER = "images/stats/special"
WEIGHT_ICON = "images/svgs/weight.svg"
CAPS_ICON = "images/svgs/caps.svg"
GUN_ICON = "images/svgs/gun.svg"
ARMOR_ICON = "images/svgs/helmet.svg"
AMMO_ICON = "images/svgs/ammo.svg"
DEFENSE_ICON = "images/svgs/shield.svg"
TIME_ICON = "images/svgs/time.svg"

DAMAGE_TYPES_ICONS = {
    "energy_dmg": "images/svgs/damage_types/bolt.svg",
    "radiation_dmg": "images/svgs/damage_types/radiation.svg",
    "physical_dmg": "images/svgs/damage_types/physical.svg",
    "fire_dmg": "images/svgs/damage_types/fire.svg",
    "acid_dmg": "images/svgs/damage_types/acid.svg",
}

ITEMS_BASE_FOLDER = "../objs/items"

COMMONWEALTH_MAP = "images/worldmap/CompanionWorldMap.png"
COMMONWEALTH_MAP_MARKERS = "images/worldmap/WorldMapMarkers.png"

MAP_ICONS_BASE_FOLDER = "images/svgs/map_markers_processed"



# Sounds
BOOT_SOUND_A = "sounds/pipboy/BootSequence/UI_PipBoy_BootSequence_A.ogg"
BOOT_SOUND_B = "sounds/pipboy/BootSequence/UI_PipBoy_BootSequence_B.ogg"
BOOT_SOUND_C = "sounds/pipboy/BootSequence/UI_PipBoy_BootSequence_C.ogg"
BACKGROUND_HUM = "sounds/pipboy/UI_PipBoy_Hum_LP.ogg"
BUZZ_SOUND_BASE_FOLDER = "sounds/pipboy/BurstStatic"
RADIO_BASE_FOLDER = "sounds/radio"
RADIO_TURN_ON_SOUND = "sounds/pipboy/Radio/UI_PipBoy_Radio_On.ogg"
RADIO_TURN_OFF_SOUND = "sounds/pipboy/Radio/UI_PipBoy_Radio_Off.ogg"
DCR_INTERMISSIONS_BASE_FOLDER = "sounds/radio/DCR_intermissions"
RADIO_STATIC_BURSTS_BASE_FOLDER = "sounds/pipboy/Radio/StaticBursts"
ROTARY_HORIZONTAL_1 = "sounds/pipboy/RotaryHorizontal/UI_PipBoy_RotaryHorizontal_01.ogg"
ROTARY_HORIZONTAL_2 = "sounds/pipboy/RotaryHorizontal/UI_PipBoy_RotaryHorizontal_02.ogg"
ROTARY_VERTICAL_1 = "sounds/pipboy/RotaryVertical/UI_PipBoy_RotaryVertical_01.ogg"
ROTARY_VERTICAL_2 = "sounds/pipboy/RotaryVertical/UI_PipBoy_RotaryVertical_02.ogg"
OK_SOUND = "sounds/pipboy/UI_PipBoy_OK.ogg"
SPECIAL_SOUNDS = "sounds/pipboy/PerkMenu/SPECIAL"



# Misc
MAP_CACHE = "../cache/maps"
MAP_PLACES_CACHE = "../cache/places"
MAP_RENDERED_CACHE = "../cache/rendered_maps"
STAT_TAB_OFFSET_INI = "positions.ini"


def get_static_map_url(size, logo_size, apikey, lon, lat, zoom):
    return (
        f"https://maps.geoapify.com/v1/staticmap?style=osm-bright&width={size}&height={size + logo_size}&center=lonlat:{lon},{lat}&zoom={zoom}&scale=1&"
        f"styleCustomization=background:%23585858|landcover-glacier:none|landuse-residential:none|landuse-commercial:none|landuse-industrial:none|"
        f"park:none|park-outline:none|landuse-cemetery:none|landuse-hospital:none|landuse-school:none|landuse-railway:none|landcover-wood:none|"
        f"landcover-grass:none|landcover-grass-park:none|waterway_tunnel:none|waterway-other:none|waterway-stream-canal:none|waterway-river:none|"
        f"water-offset:%23292929|water:%23000000|water-pattern:none|landcover-ice-shelf:none|building:none|building-top:none|tunnel-service-track-casing:none|"
        f"tunnel-minor-casing:none|tunnel-secondary-tertiary-casing:none|tunnel-trunk-primary-casing:none|tunnel-motorway-casing:none|tunnel-path:none|"
        f"tunnel-service-track:none|tunnel-minor:none|tunnel-secondary-tertiary:none|tunnel-trunk-primary:none|tunnel-motorway:none|tunnel-railway:none|"
        f"ferry:none|aeroway-taxiway-casing:none|aeroway-runway-casing:none|aeroway-area:none|aeroway-taxiway:none|aeroway-runway:none|highway-area:none|"
        f"highway-motorway-link-casing:none|highway-link-casing:none|highway-minor-casing:none|highway-secondary-tertiary-casing:none|highway-primary-casing:none|"
        f"highway-trunk-casing:none|highway-motorway-casing:none|highway-path:none|highway-motorway-link:none|highway-link:none|highway-minor:%23868686|"
        f"highway-secondary-tertiary:%23868686|highway-primary:%23868686|highway-trunk:%23868686|highway-motorway:%23868686|railway-transit:none|"
        f"railway-transit-hatching:none|railway-service:none|railway-service-hatching:none|railway:none|railway-hatching:none|bridge-motorway-link-casing:none|"
        f"bridge-link-casing:none|bridge-secondary-tertiary-casing:none|bridge-trunk-primary-casing:none|bridge-motorway-casing:none|bridge-path-casing:none|"
        f"bridge-path:%23868686|bridge-motorway-link:%23868686|bridge-link:%23868686|bridge-secondary-tertiary:%23868686|bridge-trunk-primary:%23868686|"
        f"bridge-motorway:%23868686|bridge-railway:none|bridge-railway-hatching:none|cablecar:none|cablecar-dash:none|boundary-land-level-4:none|"
        f"boundary-land-level-2:none|boundary-land-disputed:none|boundary-water:none|waterway-name:none|water-name-lakeline:none|water-name-ocean:none|"
        f"water-name-other:none|poi-level-3:none|poi-level-2:none|poi-level-1:none|poi-railway:none|road_oneway:none|road_oneway_opposite:none|"
        f"highway-name-path:none|highway-name-minor:none|highway-name-major:none|highway-shield:none|highway-shield-us-interstate:none|highway-shield-us-other:none|"
        f"airport-label-major:none|place-other:none|place-village:none|place-town:none|place-city:none|place-city-capital:none|place-country-other:none|"
        f"place-country-3:none|place-country-2:none|place-country-1:none|place-continent:none&apiKey={apikey}"
    )



OVERPASS_URL = "https://overpass-api.de/api/interpreter"    
    
def get_places_map_url(radius, lat, lon):
    # Define the different queries to be run. You can easily add more queries here.
    queries = [
        # Settlements
        'node["place"~"city|town|village|hamlet"](around:{radius},{lat},{lon});',
        'way["place"~"city|town|village|hamlet"](around:{radius},{lat},{lon});',
        'relation["place"~"city|town|village|hamlet"](around:{radius},{lat},{lon});',

        # Lakes
        'node["water"="lake"](around:{radius},{lat},{lon});',
        'way["water"="lake"](around:{radius},{lat},{lon});',
        'relation["water"="lake"](around:{radius},{lat},{lon});',

        # Ruins
        'node["historic"="ruins"](around:{radius},{lat},{lon});',
        'way["historic"="ruins"](around:{radius},{lat},{lon});',
        'relation["historic"="ruins"](around:{radius},{lat},{lon});',

        # Industrial areas
        'node["landuse"~"industrial|farmland"](around:{radius},{lat},{lon});',
        'way["landuse"~"industrial|farmland"](around:{radius},{lat},{lon});',
        'relation["landuse"~"industrial|farmland"](around:{radius},{lat},{lon});',

        # Military facilities
        'node["military"~"base|bunker"](around:{radius},{lat},{lon});',
        'way["military"~"base|bunker"](around:{radius},{lat},{lon});',
        'relation["military"~"base|bunker"](around:{radius},{lat},{lon});',

        # Man made bunkers and bridges
        'node["man_made"~"bunker|bridge"](around:{radius},{lat},{lon});',
        'way["man_made"~"bunker|bridge"](around:{radius},{lat},{lon});',
        'relation["man_made"~"bunker|bridge"](around:{radius},{lat},{lon});',
        
        # Amenities
        'node["amenity"~"police"](around:{radius},{lat},{lon});',
        'way["amenity"~"police"](around:{radius},{lat},{lon});',
        'relation["amenity"~"police"](around:{radius},{lat},{lon});',
        

    ]
    # Fill in the parameters and join the queries
    query_body = "\n".join(queries).format(radius=radius, lat=lat, lon=lon)
    return f"""
    [out:json][timeout:25];
    (
    {query_body}
    );
    out center;
    """