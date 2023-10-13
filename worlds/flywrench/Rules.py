from BaseClasses import MultiWorld
from .Regions import connect_flywrench_regions, MENU_REGION

from .names.LevelNames import Earth, Jupiter, Mars, Mercury, Neptune, \
                              Pluto, Saturn, Sun, Uranus, Venus


# Defines all rules for a particular player's Flywrench world.
# This should set up and handle the connection of regions and setting
# up any of the rules that restrict access to areas of the game
#
# NOTE: Currently all locations are open, but in the future we can
#       do things like make planet access an unlockable thing found
#       in other player worlds and other funky rulesets.
#

def set_flywrench_rules(world: MultiWorld, player: int):
    # In a vanilla game, the menu allows access to all planets in unlock everything mode
    # TODO: Handle normal planet level restrictions
    connect_flywrench_regions(world, player, MENU_REGION, Pluto.NAME)
    connect_flywrench_regions(world, player, MENU_REGION, Neptune.NAME)
    connect_flywrench_regions(world, player, MENU_REGION, Uranus.NAME)
    connect_flywrench_regions(world, player, MENU_REGION, Saturn.NAME)
    connect_flywrench_regions(world, player, MENU_REGION, Jupiter.NAME)
    connect_flywrench_regions(world, player, MENU_REGION, Mars.NAME)
    connect_flywrench_regions(world, player, MENU_REGION, Earth.NAME)
    connect_flywrench_regions(world, player, MENU_REGION, Venus.NAME)
    connect_flywrench_regions(world, player, MENU_REGION, Mercury.NAME)
    connect_flywrench_regions(world, player, MENU_REGION, Sun.NAME)
