from typing import Dict

from BaseClasses import Location
from .names.LevelNames import Earth, Jupiter, Mars, Mercury, Neptune, \
                              Pluto, Saturn, Sun, Uranus, Venus

class FlywrenchLocation(Location):
  game: str = "Flywrench"


# Pluto
LOCATION_PLUTO_NUM_LEVELS = 21
LOCATION_PLUTO_ID_START = 700
LOCATION_PLUTO_ID_END = LOCATION_PLUTO_ID_START + LOCATION_PLUTO_NUM_LEVELS

location_pluto_table: Dict[str, int] = {
    Pluto.INIT_WHITE       : LOCATION_PLUTO_ID_START,
    Pluto.INIT_RED         : LOCATION_PLUTO_ID_START + 1,
    Pluto.LNG_WHITE_RED    : LOCATION_PLUTO_ID_START + 2,
    Pluto.LNG_UP_WHITE_RED : LOCATION_PLUTO_ID_START + 3,
    Pluto.HL_1             : LOCATION_PLUTO_ID_START + 4,
    Pluto.HL_2             : LOCATION_PLUTO_ID_START + 5,
    Pluto.HL_3             : LOCATION_PLUTO_ID_START + 6,
    Pluto.HL_4             : LOCATION_PLUTO_ID_START + 7,
    Pluto.PS_REDUXYAR      : LOCATION_PLUTO_ID_START + 8,
    Pluto.PS_SAW           : LOCATION_PLUTO_ID_START + 9,
    Pluto.FRSY_1           : LOCATION_PLUTO_ID_START + 10,
    Pluto.FRSY_2           : LOCATION_PLUTO_ID_START + 11,
    Pluto.FRSY_3           : LOCATION_PLUTO_ID_START + 12,
    Pluto.FRSY_4           : LOCATION_PLUTO_ID_START + 13,
    Pluto.NT_RCORE         : LOCATION_PLUTO_ID_START + 14,
    Pluto.NT_RFREE         : LOCATION_PLUTO_ID_START + 15,
    Pluto.DK_SLIGHT        : LOCATION_PLUTO_ID_START + 16,
    Pluto.DK_FLX           : LOCATION_PLUTO_ID_START + 17,
    Pluto.DK_REDUXOKKO     : LOCATION_PLUTO_ID_START + 18,
    Pluto.DK_REDUXPERF     : LOCATION_PLUTO_ID_START + 19,
    Pluto.DK_REDUXSLAMMER  : LOCATION_PLUTO_ID_START + 20,
}

# Neptune
LOCATION_NEPTUNE_NUM_LEVELS = 21
LOCATION_NEPTUNE_ID_START = LOCATION_PLUTO_ID_END
LOCATION_NEPTUNE_ID_END = LOCATION_NEPTUNE_ID_START + LOCATION_NEPTUNE_NUM_LEVELS

location_neptune_table: Dict[str, int] = {
    Neptune.INIT_GREEN                : LOCATION_NEPTUNE_ID_START,
    Neptune.INIT_REFLECT              : LOCATION_NEPTUNE_ID_START + 1,
    Neptune.INIT_SPINRISE             : LOCATION_NEPTUNE_ID_START + 2,
    Neptune.N1_DROP_AND_ROLL          : LOCATION_NEPTUNE_ID_START + 3,
    Neptune.N1_REVERSE_ROLL_CAVE      : LOCATION_NEPTUNE_ID_START + 4,
    Neptune.N1_ROLL_BASKET            : LOCATION_NEPTUNE_ID_START + 5,
    Neptune.N2_RED_GREEN_WHITE_BASKET : LOCATION_NEPTUNE_ID_START + 6,
    Neptune.N2_GREEN_COMBO_CASTLE     : LOCATION_NEPTUNE_ID_START + 7,
    Neptune.CLM_1                     : LOCATION_NEPTUNE_ID_START + 8,
    Neptune.CLM_3                     : LOCATION_NEPTUNE_ID_START + 9,
    Neptune.CLM_4                     : LOCATION_NEPTUNE_ID_START + 10,
    Neptune.CLM_5                     : LOCATION_NEPTUNE_ID_START + 11,
    Neptune.BRST_WIRE                 : LOCATION_NEPTUNE_ID_START + 12,
    Neptune.BRST_POT                  : LOCATION_NEPTUNE_ID_START + 13,
    Neptune.BRST_ROW                  : LOCATION_NEPTUNE_ID_START + 14,
    Neptune.NXT_WATCH                 : LOCATION_NEPTUNE_ID_START + 15,
    Neptune.NXT_TENNIS                : LOCATION_NEPTUNE_ID_START + 16,
    Neptune.NXT_MAKO                  : LOCATION_NEPTUNE_ID_START + 17,
    Neptune.NXT_DOOR                  : LOCATION_NEPTUNE_ID_START + 18,
    Neptune.NXT_LATE                  : LOCATION_NEPTUNE_ID_START + 19,
    Neptune.NXT_BSS                   : LOCATION_NEPTUNE_ID_START + 20,
}

# Uranus
LOCATION_URANUS_NUM_LEVELS = 25
LOCATION_URANUS_ID_START = LOCATION_NEPTUNE_ID_END
LOCATION_URANUS_ID_END = LOCATION_URANUS_ID_START + LOCATION_URANUS_NUM_LEVELS

location_uranus_table: Dict[str, int] = {
    Uranus.INIT_PINK        : LOCATION_URANUS_ID_START,
    Uranus.UT1_CALL1        : LOCATION_URANUS_ID_START + 1,
    Uranus.UT1_CALL2        : LOCATION_URANUS_ID_START + 2,
    Uranus.UT1_CALL3        : LOCATION_URANUS_ID_START + 3,
    Uranus.TGT_CHAMBER      : LOCATION_URANUS_ID_START + 4,
    Uranus.TGT_CAVERNS      : LOCATION_URANUS_ID_START + 5,
    Uranus.TGT_SIDESTRAFE   : LOCATION_URANUS_ID_START + 6,
    Uranus.TGT_SLAMJAM2     : LOCATION_URANUS_ID_START + 7,
    Uranus.MLT_DOWN2        : LOCATION_URANUS_ID_START + 8,
    Uranus.MLT_SLAMJAM1     : LOCATION_URANUS_ID_START + 9,
    Uranus.MLT_SPIKES       : LOCATION_URANUS_ID_START + 10,
    Uranus.MTRD_CHAMBERBOSS : LOCATION_URANUS_ID_START + 11,
    Uranus.MTRD_OVERWORLD   : LOCATION_URANUS_ID_START + 12,
    Uranus.MTRD_POWERUP     : LOCATION_URANUS_ID_START + 13,
    Uranus.MTRD_SPACEPIRATE : LOCATION_URANUS_ID_START + 14,
    Uranus.FLT_GLIDE        : LOCATION_URANUS_ID_START + 15,
    Uranus.FLT_DRIFT        : LOCATION_URANUS_ID_START + 16,
    Uranus.FLT_CARE         : LOCATION_URANUS_ID_START + 17,
    Uranus.FLT_FALLING      : LOCATION_URANUS_ID_START + 18,
    Uranus.FLT_LIFT         : LOCATION_URANUS_ID_START + 19,
    Uranus.GUM_FOOT         : LOCATION_URANUS_ID_START + 20,
    Uranus.GUM_MOLD         : LOCATION_URANUS_ID_START + 21,
    Uranus.GUM_BONES        : LOCATION_URANUS_ID_START + 22,
    Uranus.GUM_FLAM         : LOCATION_URANUS_ID_START + 23,
    Uranus.GUM_FLIM         : LOCATION_URANUS_ID_START + 24,
}

# Saturn
LOCATION_SATURN_NUM_LEVELS = 18
LOCATION_SATURN_ID_START = LOCATION_URANUS_ID_END
LOCATION_SATURN_ID_END = LOCATION_SATURN_ID_START + LOCATION_SATURN_NUM_LEVELS

location_saturn_table: Dict[str, int] = {
    Saturn.INIT_WHEEL         : LOCATION_SATURN_ID_START,
    Saturn.ST1_DROP_THRU_PINK : LOCATION_SATURN_ID_START + 1,
    Saturn.ST1_DOWNDOUBLES    : LOCATION_SATURN_ID_START + 2,
    Saturn.ST1_GREEN_WHEEL    : LOCATION_SATURN_ID_START + 3,
    Saturn.ST1_PINWHEELSWAG2  : LOCATION_SATURN_ID_START + 4,
    Saturn.ST2_GEARBOX        : LOCATION_SATURN_ID_START + 5,
    Saturn.ST2_MIIKONG        : LOCATION_SATURN_ID_START + 6,
    Saturn.WTG1_DOUBLEDOOR    : LOCATION_SATURN_ID_START + 7,
    Saturn.WTG1_SPLITTER      : LOCATION_SATURN_ID_START + 8,
    Saturn.RLX_SPINNER        : LOCATION_SATURN_ID_START + 9,
    Saturn.RLX_SAVIOUR        : LOCATION_SATURN_ID_START + 10,
    Saturn.RLX_BOUNCE         : LOCATION_SATURN_ID_START + 11,
    Saturn.RLX_KEY            : LOCATION_SATURN_ID_START + 12,
    Saturn.WTG2_TRAFFICJAM    : LOCATION_SATURN_ID_START + 13,
    Saturn.WTG2_TWOCHAMBERS   : LOCATION_SATURN_ID_START + 14,
    Saturn.WTG2_WACKATTACK    : LOCATION_SATURN_ID_START + 15,
    Saturn.WTG2_BRASH         : LOCATION_SATURN_ID_START + 16,
    Saturn.WTG2_REDACTED      : LOCATION_SATURN_ID_START + 17,
}

# Jupiter (musical banger alert)
LOCATION_JUPITER_NUM_LEVELS = 20
LOCATION_JUPITER_ID_START = LOCATION_SATURN_ID_END
LOCATION_JUPITER_ID_END = LOCATION_JUPITER_ID_START + LOCATION_JUPITER_NUM_LEVELS

location_jupiter_table: Dict[str, int] = {
    Jupiter.INIT_GRAV     : LOCATION_JUPITER_ID_START,
    Jupiter.JT1_HEAVY_SKY : LOCATION_JUPITER_ID_START + 1,
    Jupiter.TRNS_DRINK    : LOCATION_JUPITER_ID_START + 2,
    Jupiter.TRNS_MASH     : LOCATION_JUPITER_ID_START + 3,
    Jupiter.TRNS_STTIN    : LOCATION_JUPITER_ID_START + 4,
    Jupiter.TRNS_HOP      : LOCATION_JUPITER_ID_START + 5,
    Jupiter.KLE_ENABLER   : LOCATION_JUPITER_ID_START + 6,
    Jupiter.KLE_VEGGIES   : LOCATION_JUPITER_ID_START + 7,
    Jupiter.KLE_FIREFIRE  : LOCATION_JUPITER_ID_START + 8,
    Jupiter.PAX_MALAZZO   : LOCATION_JUPITER_ID_START + 9,
    Jupiter.PAX_SALMON    : LOCATION_JUPITER_ID_START + 10,
    Jupiter.PAX_ATHOUGHTZ : LOCATION_JUPITER_ID_START + 11,
    Jupiter.PAX_MFA       : LOCATION_JUPITER_ID_START + 12,
    Jupiter.PTH_BENCH     : LOCATION_JUPITER_ID_START + 13,
    Jupiter.PTH_PLATE     : LOCATION_JUPITER_ID_START + 14,
    Jupiter.PTH_RAWR      : LOCATION_JUPITER_ID_START + 15,
    Jupiter.PTH_PROBOND   : LOCATION_JUPITER_ID_START + 16,
    Jupiter.WND_WIND      : LOCATION_JUPITER_ID_START + 17,
    Jupiter.WND_TRAILS    : LOCATION_JUPITER_ID_START + 18,
    Jupiter.WND_TREETOPS  : LOCATION_JUPITER_ID_START + 19,
}

# Mars
LOCATION_MARS_NUM_LEVELS = 18
LOCATION_MARS_ID_START = LOCATION_JUPITER_ID_END
LOCATION_MARS_ID_END = LOCATION_MARS_ID_START + LOCATION_MARS_NUM_LEVELS

location_mars_table: Dict[str, int] = {
    Mars.INIT_TURRET  : LOCATION_MARS_ID_START,
    Mars.BWL_SCHEDDER : LOCATION_MARS_ID_START + 1,
    Mars.BWL_CHEESE   : LOCATION_MARS_ID_START + 2,
    Mars.BWL_MAC      : LOCATION_MARS_ID_START + 3,
    Mars.BWL_PIKE     : LOCATION_MARS_ID_START + 4,
    Mars.BWL_SCOOP2   : LOCATION_MARS_ID_START + 5,
    Mars.BWL_DUCKFACE : LOCATION_MARS_ID_START + 6,
    Mars.MLW_BULLET1  : LOCATION_MARS_ID_START + 7,
    Mars.MLW_POWROOM  : LOCATION_MARS_ID_START + 8,
    Mars.MLW_ROLLEM   : LOCATION_MARS_ID_START + 9,
    Mars.MLW_PAD      : LOCATION_MARS_ID_START + 10,
    Mars.HLMT_PANTS   : LOCATION_MARS_ID_START + 11,
    Mars.HLMT_ZOMBIE  : LOCATION_MARS_ID_START + 12,
    Mars.HLMT_EXPO    : LOCATION_MARS_ID_START + 13,
    Mars.HLMT_PZ      : LOCATION_MARS_ID_START + 14,
    Mars.MM_BOND      : LOCATION_MARS_ID_START + 15,
    Mars.MM_ESCAPE    : LOCATION_MARS_ID_START + 16,
    Mars.MM_CLIMB     : LOCATION_MARS_ID_START + 17,
}

# Earth
LOCATION_EARTH_NUM_LEVELS = 19
LOCATION_EARTH_ID_START = LOCATION_MARS_ID_END
LOCATION_EARTH_ID_END = LOCATION_EARTH_ID_START + LOCATION_EARTH_NUM_LEVELS

location_earth_table: Dict[str, int] = {
    Earth.INIT_SWITCH     : LOCATION_EARTH_ID_START,
    Earth.PLL_GRAVITY     : LOCATION_EARTH_ID_START + 1,
    Earth.PLL_PINK        : LOCATION_EARTH_ID_START + 2,
    Earth.PLL_TURRET      : LOCATION_EARTH_ID_START + 3,
    Earth.ET1_HOPP        : LOCATION_EARTH_ID_START + 4,
    Earth.ET1_POCKET      : LOCATION_EARTH_ID_START + 5,
    Earth.ENDN_START      : LOCATION_EARTH_ID_START + 6,
    Earth.ENDN_SPOOPY     : LOCATION_EARTH_ID_START + 7,
    Earth.ENDN_FRIDGE     : LOCATION_EARTH_ID_START + 8,
    Earth.ENDN_HARVEST    : LOCATION_EARTH_ID_START + 9,
    Earth.ENDN_FRANNY     : LOCATION_EARTH_ID_START + 10,
    Earth.ENDN_ZOOEY      : LOCATION_EARTH_ID_START + 11,
    Earth.ENDN_HELL       : LOCATION_EARTH_ID_START + 12,
    Earth.ENDN_PURGATORY  : LOCATION_EARTH_ID_START + 13,
    Earth.JKD_REHAB       : LOCATION_EARTH_ID_START + 14,
    Earth.JKD_FUARK       : LOCATION_EARTH_ID_START + 15,
    Earth.JKD_SUPERSUPPER : LOCATION_EARTH_ID_START + 16,
    Earth.EMLW_DOWN       : LOCATION_EARTH_ID_START + 17,
    Earth.EMLW_CANNONBALL : LOCATION_EARTH_ID_START + 18,
}

# Venus
LOCATION_VENUS_NUM_LEVELS = 23
LOCATION_VENUS_ID_START = LOCATION_EARTH_ID_END
LOCATION_VENUS_ID_END = LOCATION_VENUS_ID_START + LOCATION_VENUS_NUM_LEVELS

location_venus_table: Dict[str, int] = {
    Venus.INIT_MOV     : LOCATION_VENUS_ID_START,
    Venus.CRL_FLAS     : LOCATION_VENUS_ID_START + 1,
    Venus.CRL_OVERFLOW : LOCATION_VENUS_ID_START + 2,
    Venus.CRL_POPPBOCH : LOCATION_VENUS_ID_START + 3,
    Venus.CRL_MLKIT    : LOCATION_VENUS_ID_START + 4,
    Venus.CRL_SEWERS   : LOCATION_VENUS_ID_START + 5,
    Venus.CRL_DRAINAGE : LOCATION_VENUS_ID_START + 6,
    Venus.MVT_GRINDER  : LOCATION_VENUS_ID_START + 7,
    Venus.MVT_BIG_BOX  : LOCATION_VENUS_ID_START + 8,
    Venus.MVT_BENDER   : LOCATION_VENUS_ID_START + 9,
    Venus.IMP_POET     : LOCATION_VENUS_ID_START + 10,
    Venus.IMP_GUARD    : LOCATION_VENUS_ID_START + 11,
    Venus.IMP_SLAT     : LOCATION_VENUS_ID_START + 12,
    Venus.IMP_CROWN    : LOCATION_VENUS_ID_START + 13,
    Venus.IMP_STEPS    : LOCATION_VENUS_ID_START + 14,
    Venus.DST_VILLAIN  : LOCATION_VENUS_ID_START + 15,
    Venus.DST_FEEBLE   : LOCATION_VENUS_ID_START + 16,
    Venus.DST_HOFFMAN  : LOCATION_VENUS_ID_START + 17,
    Venus.DST_JACKET   : LOCATION_VENUS_ID_START + 18,
    Venus.DST_SAMUS    : LOCATION_VENUS_ID_START + 19,
    Venus.HY_BASERACE  : LOCATION_VENUS_ID_START + 20,
    Venus.HY_HIGHJUMP  : LOCATION_VENUS_ID_START + 21,
    Venus.HY_ROCKET    : LOCATION_VENUS_ID_START + 22,
}

# Mercury
LOCATION_MERCURY_NUM_LEVELS = 21
LOCATION_MERCURY_ID_START = LOCATION_VENUS_ID_END
LOCATION_MERCURY_ID_END = LOCATION_MERCURY_ID_START + LOCATION_MERCURY_NUM_LEVELS

location_mercury_table: Dict[str, int] = {
    Mercury.INIT_REV           : LOCATION_MERCURY_ID_START,
    Mercury.MCY1_PRECIPICE     : LOCATION_MERCURY_ID_START + 1,
    Mercury.MCY1_LONGHAUL      : LOCATION_MERCURY_ID_START + 2,
    Mercury.MCY1_SKISLOPE      : LOCATION_MERCURY_ID_START + 3,
    Mercury.MCY1_THREEPIECETUX : LOCATION_MERCURY_ID_START + 4,
    Mercury.MCY1_BIRDS         : LOCATION_MERCURY_ID_START + 5,
    Mercury.MCY1_BLUESQUARE    : LOCATION_MERCURY_ID_START + 6,
    Mercury.MCY1_BDIAMOND      : LOCATION_MERCURY_ID_START + 7,
    Mercury.MCY1_SLICKRICK     : LOCATION_MERCURY_ID_START + 8,
    Mercury.MCY1_SLICKPICNIC   : LOCATION_MERCURY_ID_START + 9,
    Mercury.MCY1_TRINITY       : LOCATION_MERCURY_ID_START + 10,
    Mercury.MCY1_TOGETHERNESS  : LOCATION_MERCURY_ID_START + 11,
    Mercury.MCY1_PRESENCE      : LOCATION_MERCURY_ID_START + 12,
    Mercury.MCY1_GOODY         : LOCATION_MERCURY_ID_START + 13,
    Mercury.INIT2_REV          : LOCATION_MERCURY_ID_START + 14,
    Mercury.MCY2_RATS          : LOCATION_MERCURY_ID_START + 15,
    Mercury.MCY2_IMPLANT       : LOCATION_MERCURY_ID_START + 16,
    Mercury.MCY2_GLITCHCITY    : LOCATION_MERCURY_ID_START + 17,
    Mercury.MCY2_VIRIDIAN      : LOCATION_MERCURY_ID_START + 18,
    Mercury.MCY2_KESTREL       : LOCATION_MERCURY_ID_START + 19,
    Mercury.MCY2_IMPACT        : LOCATION_MERCURY_ID_START + 20,
}

# Sun
# Only 1 level but provide constants for consistency's sake
LOCATION_SUN_NUM_LEVELS = 1
LOCATION_SUN_ID_START = LOCATION_MERCURY_ID_END
LOCATION_SUN_ID_END = LOCATION_SUN_ID_START + LOCATION_SUN_NUM_LEVELS

location_sun_table: Dict[str, int] = {
    Sun.INIT_ICARUS: LOCATION_SUN_ID_START,
}

# Main location table
location_table: Dict[str, int] = {
    **location_pluto_table,
    **location_neptune_table,
    **location_uranus_table,
    **location_saturn_table,
    **location_jupiter_table,
    **location_mars_table,
    **location_earth_table,
    **location_venus_table,
    **location_mercury_table,
    **location_sun_table,
}