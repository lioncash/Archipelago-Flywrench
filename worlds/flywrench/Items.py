from typing import Dict
from BaseClasses import Item, ItemClassification, MultiWorld
from .names.ItemNames import ITEM_SPACE_DUST

# The only real "item" is beating the level, thus 'Space Dust'
# Currently a junk item; this needs to be fleshed out a little more.
# TODO: We should be able to randomize the ability to play certain planets.
#       but for now, this gets things off the ground
item_table: Dict[str, int] = {
    ITEM_SPACE_DUST: 800
}


class FlywrenchItem(Item):
    game: str = "Flywrench"


# Creates a particular Flywrench item identified by a name.
def create_flywrench_item(name: str, classification: ItemClassification, player: int) -> FlywrenchItem:
    item_id = item_table[name]
    return FlywrenchItem(name, classification, item_id, player)


# Creates all the items for a particular flywrench world instance.
def create_flywrench_items(multiworld: MultiWorld, player: int):
    # Every level needs to be beaten to beat Flywrench, so every level has one check.
    multiworld.itempool += [create_flywrench_item(ITEM_SPACE_DUST, ItemClassification.filler, player)
                            for _ in multiworld.get_locations()]
