from BaseClasses import MultiWorld, Region, Entrance
from .Locations import FlywrenchLocation, location_table, location_pluto_table, location_neptune_table, \
                       location_uranus_table, location_saturn_table, location_jupiter_table, location_mars_table, \
                       location_earth_table, location_venus_table, location_mercury_table, location_sun_table

from .names.LevelNames import Earth, Jupiter, Mars, Mercury, Neptune, \
                              Pluto, Saturn, Sun, Uranus, Venus

# The main region that all the levels connect to
MENU_REGION = "Menu"


# Creates a defined region for Flywrench using the given location table
def create_region(name: str, player: int, world: MultiWorld, region_location_table) -> Region:
    region = Region(name, player, world)
    region.locations += \
        [FlywrenchLocation(player, loc_name, location_table[loc_name], region) for loc_name in region_location_table]
    return region


# Connects a source region to a given target region and optionally adds an access rule
# governing whether a player is allowed to enter the target region from the source region.
def connect_flywrench_regions(world: MultiWorld, player: int, source: str, target: str, rule=None):
    source_region = world.get_region(source, player)
    target_region = world.get_region(target, player)

    connection = Entrance(player, '', source_region)
    if rule:
        connection.access_rule = rule

    source_region.exits.append(connection)
    connection.connect(target_region)


def create_flywrench_regions(world: MultiWorld, player: int):
    world.regions.append(Region(MENU_REGION, player, world, "Main Menu/Level Select"))

    # Create individual planet regions
    world.regions.append(create_region(Pluto.NAME, player, world, location_pluto_table))
    world.regions.append(create_region(Neptune.NAME, player, world, location_neptune_table))
    world.regions.append(create_region(Uranus.NAME, player, world, location_uranus_table))
    world.regions.append(create_region(Saturn.NAME, player, world, location_saturn_table))
    world.regions.append(create_region(Jupiter.NAME, player, world, location_jupiter_table))
    world.regions.append(create_region(Mars.NAME, player, world, location_mars_table))
    world.regions.append(create_region(Earth.NAME, player, world, location_earth_table))
    world.regions.append(create_region(Venus.NAME, player, world, location_venus_table))
    world.regions.append(create_region(Mercury.NAME, player, world, location_mercury_table))
    world.regions.append(create_region(Sun.NAME, player, world, location_sun_table))
