import json
import os
from typing import Any, Dict

from .Items import item_table, FlywrenchItem, create_flywrench_item, create_flywrench_items
from .Locations import location_table, FlywrenchLocation
from .Options import flywrench_options
from .Rules import set_flywrench_rules
from .Regions import create_flywrench_regions
from BaseClasses import ItemClassification, Tutorial
from ..AutoWorld import World, WebWorld


class FlywrenchWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Flywrench for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Lioncache"]
    )]


class FlywrenchWorld(World):
    """
    A frenetic action game made by Messhof LLC featuring a little white bar-shaped ship that hurdles through
    space in order to reach the sun. Features a killer soundtrack, a large difficulty curve near the game and
    allows for very fast completion once mastery over the controls is achieved.
    """

    game = "Flywrench"
    web = FlywrenchWeb()

    data_version = 1
    required_client_version = (0, 4, 2)

    item_name_to_id = item_table
    location_name_to_id = location_table

    option_definitions = flywrench_options

    topology_present = True

    def generate_early(self):
        # Currently unused, but here in the event options get fleshed out over time.
        pass

    def create_regions(self):
        create_flywrench_regions(self.multiworld, self.player)

    def create_item(self, name: str) -> FlywrenchItem:
        # Currently assume all created items are filler (because they are. we only have space dust)
        return create_flywrench_item(name, ItemClassification.filler,  self.player)

    def create_items(self):
        create_flywrench_items(self.multiworld, self.player)

    def set_rules(self):
        set_flywrench_rules(self.multiworld, self.player)

    def fill_slot_data(self) -> Dict[str, Any]:
        # Fill in if we ever need custom slot data. For now this is unused.
        return {}

    def generate_output(self, output_directory: str):
        if self.multiworld.players != 1:
            return
        data = {
            "slot_data": self.fill_slot_data(),
            "location_to_item":
                {self.location_name_to_id[i.name] : item_table[i.item.name] for i in self.multiworld.get_locations()},
            "data_package": {
                "data": {
                    "games": {
                        self.game: {
                            "item_name_to_id": self.item_name_to_id,
                            "location_name_to_id": self.location_name_to_id
                        }
                    }
                }
            }
        }
        filename = f"{self.multiworld.get_out_file_name_base(self.player)}.apflywrench"
        with open(os.path.join(output_directory, filename), 'w') as f:
            json.dump(data, f)

    def modify_multidata(self, multidata):
        pass

    # TODO: Flesh out other stuff
