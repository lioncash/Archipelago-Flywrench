from enum import StrEnum, unique


# Name IDs for everything in the game that needs one. Also used for building up
# the location tables without open-coding string names all over the place.

@unique
class Pluto(StrEnum):
    NAME = "Pluto"

    INIT_WHITE       = "Pluto: INIT_WHITE"
    INIT_RED         = "Pluto: INIT_RED"
    LNG_WHITE_RED    = "Pluto: LNG_WHITE_RED"
    LNG_UP_WHITE_RED = "Pluto: LNG_UP_WHITE_RED"
    HL_1             = "Pluto: HL_1"
    HL_2             = "Pluto: HL_2"
    HL_3             = "Pluto: HL_3"
    HL_4             = "Pluto: HL_4"
    PS_REDUXYAR      = "Pluto: PS_REDUXYAR"
    PS_SAW           = "Pluto: PS_SAW"
    FRSY_1           = "Pluto: FRSY_1"
    FRSY_2           = "Pluto: FRSY_2"
    FRSY_3           = "Pluto: FRSY_3"
    FRSY_4           = "Pluto: FRSY_4"
    NT_RCORE         = "Pluto: NT_RCORE"
    NT_RFREE         = "Pluto: NT_RFREE"
    DK_SLIGHT        = "Pluto: DK_SLIGHT"
    DK_FLX           = "Pluto: DK_FLX"
    DK_REDUXOKKO     = "Pluto: DK_REDUXOKKO"
    DK_REDUXPERF     = "Pluto: DK_REDUXPERF"
    DK_REDUXSLAMMER  = "Pluto: DK_REDUXSLAMMER"


@unique
class Neptune(StrEnum):
    NAME = "Neptune"

    INIT_GREEN                = "Neptune: INIT_GREEN"
    INIT_REFLECT              = "Neptune: INIT_REFLECT"
    INIT_SPINRISE             = "Neptune: INIT_SPINRISE"
    N1_DROP_AND_ROLL          = "Neptune: N1_DROP_AND_ROLL"
    N1_REVERSE_ROLL_CAVE      = "Neptune: N1_REVERSE_ROLL_CAVE"
    N1_ROLL_BASKET            = "Neptune: N1_ROLL_BASKET"
    N2_RED_GREEN_WHITE_BASKET = "Neptune: N2_RED_GREEN_WHITE_BASKET"
    N2_GREEN_COMBO_CASTLE     = "Neptune: N2_GREEN_COMBO_CASTLE"
    CLM_1                     = "Neptune: CLM_1"
    # Not a typo they literally skip CLM_2
    CLM_3                     = "Neptune: CLM_3"
    CLM_4                     = "Neptune: CLM_4"
    CLM_5                     = "Neptune: CLM_5"
    BRST_WIRE                 = "Neptune: BRST_WIRE"
    BRST_POT                  = "Neptune: BRST_POT"
    BRST_ROW                  = "Neptune: BRST_ROW"
    NXT_WATCH                 = "Neptune: NXT_WATCH"
    NXT_TENNIS                = "Neptune: NXT_TENNIS"
    NXT_MAKO                  = "Neptune: NXT_MAKO"
    NXT_DOOR                  = "Neptune: NXT_DOOR"
    NXT_LATE                  = "Neptune: NXT_LATE"
    NXT_BSS                   = "Neptune: NXT_BSS"


@unique
class Uranus(StrEnum):
    NAME = "Uranus"

    INIT_PINK        = "Uranus: INIT_PINK"
    UT1_CALL1        = "Uranus: UT1_CALL1"
    UT1_CALL2        = "Uranus: UT1_CALL2"
    UT1_CALL3        = "Uranus: UT1_CALL3"
    TGT_CHAMBER      = "Uranus: TGT_CHAMBER"
    TGT_CAVERNS      = "Uranus: TGT_CAVERNS"
    TGT_SIDESTRAFE   = "Uranus: TGT_SIDESTRAFE"
    TGT_SLAMJAM2     = "Uranus: TGT_SLAMJAM2"
    MLT_DOWN2        = "Uranus: MLT_DOWN2"
    MLT_SLAMJAM1     = "Uranus: MLT_SLAMJAM1"
    MLT_SPIKES       = "Uranus: MLT_SPIKES"
    MTRD_CHAMBERBOSS = "Uranus: MTRD_CHAMBERBOSS"
    MTRD_OVERWORLD   = "Uranus: MTRD_OVERWORLD"
    MTRD_POWERUP     = "Uranus: MTRD_POWERUP"
    MTRD_SPACEPIRATE = "Uranus: MTRD_SPACEPIRATE"
    FLT_GLIDE        = "Uranus: FLT_GLIDE"
    FLT_DRIFT        = "Uranus: FLT_DRIFT"
    FLT_CARE         = "Uranus: FLT_CARE"
    FLT_FALLING      = "Uranus: FLT_FALLING"
    FLT_LIFT         = "Uranus: FLT_LIFT"
    GUM_FOOT         = "Uranus: GUM_FOOT"
    GUM_MOLD         = "Uranus: GUM_MOLD"
    GUM_BONES        = "Uranus: GUM_BONES"
    GUM_FLAM         = "Uranus: GUM_FLAM"
    GUM_FLIM         = "Uranus: GUM_FLIM"


@unique
class Saturn(StrEnum):
    NAME = "Saturn"

    INIT_WHEEL         = "Saturn: INIT_WHEEL"
    ST1_DROP_THRU_PINK = "Saturn: ST1_DROP_THRU_PINK"
    ST1_DOWNDOUBLES    = "Saturn: ST1_DOWNDOUBLES"
    ST1_GREEN_WHEEL    = "Saturn: ST1_GREEN_WHEEL"
    ST1_PINWHEELSWAG2  = "Saturn: ST1_PINWHEELSWAG2"
    ST2_GEARBOX        = "Saturn: ST2_GEARBOX"
    ST2_MIIKONG        = "Saturn: ST2_MIIKONG"
    WTG1_DOUBLEDOOR    = "Saturn: WTG1_DOUBLEDOOR"
    WTG1_SPLITTER      = "Saturn: WTG1_SPLITTER"
    RLX_SPINNER        = "Saturn: RLX_SPINNER"
    RLX_SAVIOUR        = "Saturn: RLX_SAVIOUR"
    RLX_BOUNCE         = "Saturn: RLX_BOUNCE"
    RLX_KEY            = "Saturn: RLX_KEY"
    WTG2_TRAFFICJAM    = "Saturn: WTG2_TRAFFICJAM"
    WTG2_TWOCHAMBERS   = "Saturn: WTG2_TWOCHAMBERS"
    WTG2_WACKATTACK    = "Saturn: WTG2_WACKATTACK"
    WTG2_BRASH         = "Saturn: WTG2_BRASH"
    WTG2_REDACTED      = "Saturn: WTG2_REDACTED"


@unique
class Jupiter(StrEnum):
    NAME = "Jupiter"

    INIT_GRAV     = "Jupiter: INIT_GRAV"
    JT1_HEAVY_SKY = "Jupiter: JT1_HEAVY_SKY"
    TRNS_DRINK    = "Jupiter: TRNS_DRINK"
    TRNS_MASH     = "Jupiter: TRNS_MASH"
    TRNS_STTIN    = "Jupiter: TRNS_STTIN"
    TRNS_HOP      = "Jupiter: TRNS_HOP"
    KLE_ENABLER   = "Jupiter: KLE_ENABLER"
    KLE_VEGGIES   = "Jupiter: KLE_VEGGIES"
    KLE_FIREFIRE  = "Jupiter: KLE_FIREFIRE"
    PAX_MALAZZO   = "Jupiter: PAX_MALAZZO"
    PAX_SALMON    = "Jupiter: PAX_SALMON"
    PAX_ATHOUGHTZ = "Jupiter: PAX_ATHOUGHTZ"
    PAX_MFA       = "Jupiter: PAX_MFA"
    PTH_BENCH     = "Jupiter: PTH_BENCH"
    PTH_PLATE     = "Jupiter: PTH_PLATE"
    PTH_RAWR      = "Jupiter: PTH_RAWR"
    PTH_PROBOND   = "Jupiter: PTH_PROBOND"
    WND_WIND      = "Jupiter: WND_WIND"
    WND_TRAILS    = "Jupiter: WND_TRAILS"
    WND_TREETOPS  = "Jupiter: WND_TREETOPS"


@unique
class Mars(StrEnum):
    NAME = "Mars"

    INIT_TURRET  = "Mars: INIT_TURRET"
    BWL_SCHEDDER = "Mars: BWL_SCHEDDER"
    BWL_CHEESE   = "Mars: BWL_CHEESE"
    BWL_MAC      = "Mars: BWL_MAC"
    BWL_PIKE     = "Mars: BWL_PIKE"
    BWL_SCOOP2   = "Mars: BWL_SCOOP2"
    BWL_DUCKFACE = "Mars: BWL_DUCKFACE"
    MLW_BULLET1  = "Mars: MLW_BULLET1"
    MLW_POWROOM  = "Mars: MLW_POWROOM"
    MLW_ROLLEM   = "Mars: MLW_ROLLEM"
    MLW_PAD      = "Mars: MLW_PAD"
    HLMT_PANTS   = "Mars: HLMT_PANTS"
    HLMT_ZOMBIE  = "Mars: HLMT_ZOMBIE"
    HLMT_EXPO    = "Mars: HLMT_EXPO"
    HLMT_PZ      = "Mars: HLMT_PZ"
    MM_BOND      = "Mars: MM_BOND"
    MM_ESCAPE    = "Mars: MM_ESCAPE"
    MM_CLIMB     = "Mars: MM_CLIMB"


@unique
class Earth(StrEnum):
    NAME = "Earth"

    INIT_SWITCH     = "Earth: INIT_SWITCH"
    PLL_GRAVITY     = "Earth: PLL_GRAVITY"
    PLL_PINK        = "Earth: PLL_PINK"
    PLL_TURRET      = "Earth: PLL_TURRET"
    ET1_HOPP        = "Earth: ET1_HOPP"
    ET1_POCKET      = "Earth: ET1_POCKET"
    ENDN_START      = "Earth: ENDN_START"
    ENDN_SPOOPY     = "Earth: ENDN_SPOOPY"
    ENDN_FRIDGE     = "Earth: ENDN_FRIDGE"
    ENDN_HARVEST    = "Earth: ENDN_HARVEST"
    ENDN_FRANNY     = "Earth: ENDN_FRANNY"
    ENDN_ZOOEY      = "Earth: ENDN_ZOOEY"
    ENDN_HELL       = "Earth: ENDN_HELL"
    ENDN_PURGATORY  = "Earth: ENDN_PURGATORY"
    JKD_REHAB       = "Earth: JKD_REHAB"
    JKD_FUARK       = "Earth: JKD_FUARK"
    JKD_SUPERSUPPER = "Earth: JKD_SUPERSUPPER"
    EMLW_DOWN       = "Earth: EMLW_DOWN"
    EMLW_CANNONBALL = "Earth: EMLW_CANNONBALL"


@unique
class Venus(StrEnum):
    NAME = "Venus"

    INIT_MOV     = "Venus: INIT_MOV"
    CRL_FLAS     = "Venus: CRL_FLAS"
    CRL_OVERFLOW = "Venus: CRL_OVERFLOW"
    CRL_POPPBOCH = "Venus: CRL_POPPBOCH"
    CRL_MLKIT    = "Venus: CRL_MLKIT"
    CRL_SEWERS   = "Venus: CRL_SEWERS"
    CRL_DRAINAGE = "Venus: CRL_DRAINAGE"
    MVT_GRINDER  = "Venus: MVT_GRINDER"
    MVT_BIG_BOX  = "Venus: MVT_BIG_BOX"
    MVT_BENDER   = "Venus: MVT_BENDER"
    IMP_POET     = "Venus: IMP_POET"
    IMP_GUARD    = "Venus: IMP_GUARD"
    IMP_SLAT     = "Venus: IMP_SLAT"
    IMP_CROWN    = "Venus: IMP_CROWN"
    IMP_STEPS    = "Venus: IMP_STEPS"
    DST_VILLAIN  = "Venus: DST_VILLAIN"
    DST_FEEBLE   = "Venus: DST_FEEBLE"
    DST_HOFFMAN  = "Venus: DST_HOFFMAN"
    DST_JACKET   = "Venus: DST_JACKET"
    DST_SAMUS    = "Venus: DST_SAMUS"
    HY_BASERACE  = "Venus: HY_BASERACE"
    HY_HIGHJUMP  = "Venus: HY_HIGHJUMP"
    HY_ROCKET    = "Venus: HY_ROCKET"


@unique
class Mercury(StrEnum):
    NAME = "Mercury"

    INIT_REV           = "Mercury: INIT_REV"
    MCY1_PRECIPICE     = "Mercury: MCY1_PRECIPICE"
    MCY1_LONGHAUL      = "Mercury: MCY1_LONGHAUL"
    MCY1_SKISLOPE      = "Mercury: MCY1_SKISLOPE"
    MCY1_THREEPIECETUX = "Mercury: MCY1_THREEPIECETUX"
    MCY1_BIRDS         = "Mercury: MCY1_BIRDS"
    MCY1_BLUESQUARE    = "Mercury: MCY1_BLUESQUARE"
    MCY1_BDIAMOND      = "Mercury: MCY1_BDIAMOND"
    MCY1_SLICKRICK     = "Mercury: MCY1_SLICKRICK"
    MCY1_SLICKPICNIC   = "Mercury: MCY1_SLICKPICNIC"
    MCY1_TRINITY       = "Mercury: MCY1_TRINITY"
    MCY1_TOGETHERNESS  = "Mercury: MCY1_TOGETHERNESS"
    MCY1_PRESENCE      = "Mercury: MCY1_PRESENCE"
    MCY1_GOODY         = "Mercury: MCY1_GOODY"
    INIT2_REV          = "Mercury: INIT2_REV"
    MCY2_RATS          = "Mercury: MCY2_RATS"
    MCY2_IMPLANT       = "Mercury: MCY2_IMPLANT"
    MCY2_GLITCHCITY    = "Mercury: MCY2_GLITCHCITY"
    MCY2_VIRIDIAN      = "Mercury: MCY2_VIRIDIAN"
    MCY2_KESTREL       = "Mercury: MCY2_KESTREL"
    MCY2_IMPACT        = "Mercury: MCY2_IMPACT"


@unique
class Sun(StrEnum):
    NAME = "Sun"
    INIT_ICARUS = "Sun: INIT_ICARUS"
