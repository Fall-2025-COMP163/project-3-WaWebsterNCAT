"""
COMP 163 - Project 3: Quest Chronicles
Game Data Module - Starter Code

Name: [Will Webster]

AI Usage: [Document any AI assistance used]

Handles loading, validating, and creating default quests and items.
"""

import os
from custom_exceptions import (
    InvalidDataFormatError,
    MissingDataFileError,
    CorruptedDataError
)

# ============================================================================ #
# DATA LOADING FUNCTIONS
# ============================================================================ #

def load_quests(filename="data/quests.txt"):
    """Load quest data from file and return as a dictionary."""
    if not os.path.exists(filename):
        raise MissingDataFileError(f"{filename} not found.")
    
    quests = {}
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
        
        # Split lines into blocks (each quest separated by blank line)
        block = []
        for line in lines:
            if line == "":
                if block:
                    quest = parse_quest_block(block)
                    quests[quest["quest_id"]] = quest
                    block = []
            else:
                block.append(line)
        if block:  # Last block
            quest = parse_quest_block(block)
            quests[quest["quest_id"]] = quest

    except InvalidDataFormatError:
        raise
    except Exception as e:
        raise CorruptedDataError(f"Error reading quests file: {e}")
    
    return quests


def load_items(filename="data/items.txt"):
    """Load item data from file and return as a dictionary."""
    if not os.path.exists(filename):
        raise MissingDataFileError(f"{filename} not found.")
    
    items = {}
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
        
        block = []
        for line in lines:
            if line == "":
                if block:
                    item = parse_item_block(block)
                    items[item["item_id"]] = item
                    block = []
            else:
                block.append(line)
        if block:
            item = parse_item_block(block)
            items[item["item_id"]] = item

    except InvalidDataFormatError:
        raise
    except Exception as e:
        raise CorruptedDataError(f"Error reading items file: {e}")
    
    return items


# ============================================================================ #
# VALIDATION FUNCTIONS
# ============================================================================ #

def validate_quest_data(quest_dict):
    required_fields = [
        "quest_id", "title", "description",
        "reward_xp", "reward_gold", "required_level", "prerequisite"
    ]
    for key in required_fields:
        if key not in quest_dict:
            raise InvalidDataFormatError(f"Missing quest field: {key}")
    # Validate numeric fields
    for key in ["reward_xp", "reward_gold", "required_level"]:
        if not isinstance(quest_dict[key], int):
            raise InvalidDataFormatError(f"{key} must be an integer")
    return True


def validate_item_data(item_dict):
    required_fields = ["item_id", "name", "type", "effect", "cost", "description"]
    valid_types = ["weapon", "armor", "consumable"]
    
    for key in required_fields:
        if key not in item_dict:
            raise InvalidDataFormatError(f"Missing item field: {key}")
    
    if item_dict["type"] not in valid_types:
        raise InvalidDataFormatError(f"Invalid item type: {item_dict['type']}")
    
    if not isinstance(item_dict["cost"], int):
        raise InvalidDataFormatError("Cost must be an integer")
    
    if not isinstance(item_dict["effect"], dict):
        raise InvalidDataFormatError("Effect must be a dictionary")
    
    return True


# ============================================================================ #
# DEFAULT DATA FILE CREATION
# ============================================================================ #

def create_default_data_files():
    """Create default quests.txt and items.txt if they do not exist."""
    os.makedirs("data", exist_ok=True)
    
    default_quests = [
        {
            "quest_id": "quest_1",
            "title": "Beginner's Luck",
            "description": "Complete your first quest",
            "reward_xp": 100,
            "reward_gold": 50,
            "required_level": 1,
            "prerequisite": "NONE"
        }
    ]
    
    default_items = [
        {
            "item_id": "item_1",
            "name": "Rusty Sword",
            "type": "weapon",
            "effect": {"strength": 5},
            "cost": 100,
            "description": "An old sword with minimal damage."
        }
    ]
    
    quests_file = "data/quests.txt"
    items_file = "data/items.txt"
    
    if not os.path.exists(quests_file):
        try:
            with open(quests_file, "w", encoding="utf-8") as f:
                for quest in default_quests:
                    for k, v in quest.items():
                        f.write(f"{k.upper()}: {v}\n")
                    f.write("\n")
        except Exception as e:
            raise CorruptedDataError(f"Error creating quests file: {e}")
    
    if not os.path.exists(items_file):
        try:
            with open(items_file, "w", encoding="utf-8") as f:
                for item in default_items:
                    for k, v in item.items():
                        if k == "effect":
                            effect_str = ",".join(f"{stat}:{val}" for stat, val in v.items())
                            f.write(f"EFFECT: {effect_str}\n")
                        else:
                            f.write(f"{k.upper()}: {v}\n")
                    f.write("\n")
        except Exception as e:
            raise CorruptedDataError(f"Error creating items file: {e}")


# ============================================================================ #
# PARSING HELPERS
# ============================================================================ #

def parse_quest_block(lines):
    quest = {}
    try:
        for line in lines:
            if ": " not in line:
                continue
            key, val = line.split(": ", 1)
            key = key.lower()
            val = val.strip()
            if key in ["reward_xp", "reward_gold", "required_level"]:
                quest[key] = int(val)
            else:
                quest[key] = val
        validate_quest_data(quest)
        return quest
    except Exception as e:
        raise InvalidDataFormatError(f"Failed to parse quest: {e}")


def parse_item_block(lines):
    item = {}
    try:
        for line in lines:
            if ": " not in line:
                continue
            key, val = line.split(": ", 1)
            key = key.lower()
            val = val.strip()
            if key == "cost":
                item[key] = int(val)
            elif key == "effect":
                effect = {}
                parts = val.split(",")
                for part in parts:
                    stat, amount = part.split(":")
                    effect[stat.strip()] = int(amount.strip())
                item[key] = effect
            else:
                item[key] = val
        validate_item_data(item)
        return item
    except Exception as e:
        raise InvalidDataFormatError(f"Failed to parse item: {e}")


# ============================================================================ #
# TESTING
# ============================================================================ #

if __name__ == "__main__":
    print("=== GAME DATA MODULE TEST ===")
    create_default_data_files()
    
    try:
        quests = load_quests()
        print(f"Loaded {len(quests)} quests: {list(quests.keys())}")
    except Exception as e:
        print(f"Quests load error: {e}")
    
    try:
        items = load_items()
        print(f"Loaded {len(items)} items: {list(items.keys())}")
    except Exception as e:
        print(f"Items load error: {e}")

