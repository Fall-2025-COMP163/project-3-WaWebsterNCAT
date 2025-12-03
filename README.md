[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/wnCpjX4n)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=21902560&assignment_repo_type=AssignmentRepo)
# COMP 163: Project 3 - Quest Chronicles

**AI Usage: Free Use (with explanation requirement)**

## Overview

Build a complete modular RPG adventure game demonstrating mastery of **exceptions and modules**.

## Getting Started

### Step 1: Accept Assignment
1. Click the assignment link provided in Blackboard
2. Accept the assignment - this creates your personal repository
3. Clone your repository to your local machine:
```bash
git clone [your-personal-repo-url]
cd [repository-name]
```

### Step 2: Understand the Project Structure

Your repository contains:

```
quest_chronicles/
├── main.py                     # Game launcher (COMPLETE THIS)
├── character_manager.py        # Character creation/management (COMPLETE THIS)
├── inventory_system.py         # Item and equipment management (COMPLETE THIS)
├── quest_handler.py            # Quest system (COMPLETE THIS)
├── combat_system.py            # Battle mechanics (COMPLETE THIS)
├── game_data.py                # Data loading and validation (COMPLETE THIS)
├── custom_exceptions.py        # Exception definitions (PROVIDED)
├── data/
│   ├── quests.txt             # Quest definitions (PROVIDED)
│   ├── items.txt              # Item database (PROVIDED)
│   └── save_games/            # Player save files (created automatically)
├── tests/
│   ├── test_module_structure.py       # Module organization tests
│   ├── test_exception_handling.py     # Exception handling tests
│   └── test_game_integration.py       # Integration tests
└── README.md                   # This file
```

### Step 3: Development Workflow

```bash
# Work on one module at a time
# Test your code frequently

# Commit and push to see test results
git add .
git commit -m "Implement character_manager module"
git push origin main

# Check GitHub for test results (green checkmarks = passed!, red xs = at least 1 failed test case. Click the checkmark or x and then "Details" to see what test cases passed/failed)
```

## Core Requirements (60 Points)

### Critical Constraint
You may **only** use concepts covered through the **Exceptions and Modules** chapters. 

### 🎨 Creativity and Customization

This project encourages creativity! Here's what you can customize:

**✅ FULLY CUSTOMIZABLE:**
- **Character stats** - Adjust health, strength, magic for balance
- **Enemy stats** - Make enemies easier or harder
- **Special abilities** - Design unique abilities for each class
- **Additional enemies** - Add your own enemy types beyond the required three
- **Game mechanics** - Add status effects, combos, critical hits, etc.
- **Quest rewards** - Adjust XP and gold amounts
- **Item effects** - Create unique items with creative effects

**⚠️ REQUIRED (for testing):**
- **4 Character classes:** Warrior, Mage, Rogue, Cleric (names must match exactly)
- **3 Enemy types:** "goblin", "orc", "dragon" (must exist, stats flexible)
- **All module functions** - Must have the specified function signatures
- **Exception handling** - Must raise appropriate exceptions

**💡 CREATIVITY TIPS:**
1. Start with required features working
2. Add creative elements incrementally
3. Test after each addition
4. Be ready to explain your design choices in the interview
5. Bonus interview points for thoughtful, balanced customization!

**Example Creative Additions:**
- Vampire enemy that heals when attacking
- Warrior "Last Stand" ability that activates when health is low
- Poison status effect that deals damage over time
- Critical hit system based on character stats
- Rare "legendary" weapons with special effects

### Module 1: custom_exceptions.py (PROVIDED - 0 points to implement)

**This module is provided complete.** It defines all custom exceptions you'll use throughout the project.

### Module 2: game_data.py (10 points)

### Module 3: character_manager.py (15 points)

### Module 4: inventory_system.py (10 points)

### Module 5: quest_handler.py (10 points)

### Module 6: combat_system.py (10 points)

### Module 7: main.py (5 points)

## Automated Testing & Validation (60 Points)

## Interview Component (40 Points)

**Creativity Bonus** (up to 5 extra points on interview):
- Added 2+ custom enemy types beyond required three
- Designed unique and balanced special abilities
- Implemented creative game mechanics (status effects, advanced combat, etc.)
- Thoughtful stat balancing with clear reasoning

**Note:** Creativity is encouraged, but functionality comes first! A working game with required features scores higher than a broken game with lots of extras.

### Update README.md

Document your project with:

1. **Module Architecture:** Explain your module organization:

The project is organized into independent modules, each responsible for a core system within the Quest Chronicles RPG. This modular architecture ensures separation of concerns, easier debugging, and clear organization:

main.py
Acts as the central game launcher. It loads game data, initializes modules, and provides a simple user interface to create characters, start quests, and engage in combat.

character_manager.py
Handles character creation, loading, saving, leveling, stat updates, and gold management. Characters are stored as dictionaries for simplicity and easy serialization.

inventory_system.py
Implements item storage, equipment handling, and consumable usage. Supports adding/removing items, equipping gear, and applying item effects.

quest_handler.py
Manages quest acceptance, validation, prerequisite checking, and marking quests as completed. Ensures characters meet minimum level and prerequisite quest requirements.

combat_system.py
Controls turn-based combat, enemy generation, attack resolution, and reward distribution. Supports the required enemies (goblin, orc, dragon) with customizable stats.

game_data.py
Loads and validates quest and item data from the /data directory. Ensures data files exist, are correctly formatted, and contain required fields.

custom_exceptions.py
Contains all custom exception classes used for validation and error handling throughout the project (provided).

data/
Stores quests.txt, items.txt, and auto-generated player save files.

This structure ensures each module handles a single responsibility, and the entire game passes data cleanly between components.

2. **Exception Strategy:** Describe when/why you raise specific exceptions: Custom exceptions are used throughout the game to ensure clear error reporting and consistent validation:

MissingDataFileError
Raised when quests or items files do not exist.

InvalidDataFormatError
Raised when a data file exists but has missing keys, incorrect types, or malformed JSON.

CorruptedDataError
Raised when a file cannot be read or parsed due to unexpected errors.

InvalidCharacterClassError
Raised during character creation if the class name does not match the required four classes.

InvalidSaveDataError / SaveFileCorruptedError
Raised when loading a save file that is missing required fields or is improperly formatted.

CharacterDeadError
Raised when attempting actions (e.g., combat) with a character at 0 HP.

QuestRequirementsNotMetError
Raised if a character tries to accept a quest without meeting level or prerequisite requirements.

ItemNotFoundError / InventoryEmptyError
Raised when accessing or using items that do not exist.

This strategy ensures failures are explicit, easy to diagnose, and predictable for testing and integration modules.
3. **Design Choices:** Justify major decisions: Several key decisions were made to balance simplicity, clarity, and test requirements:
Dictionary-based game objects
Characters, quests, items, and enemies are stored as dictionaries instead of custom classes. This keeps the project aligned with material covered in class and simplifies JSON serialization.
Modular organization
Each core system has its own file, enabling isolated testing, clearer logic, and simpler debugging.
Predictable function signatures
All functions match required signatures from the assignment tests. This ensures compatibility with the autograder and expected integration behavior. Flexible enemy and item stats: Required enemies (goblin, orc, dragon) exist, but their stats are customizable to allow creative balancing and future extensions. Safe file operations: Load, save, and validation procedures are wrapped in exceptions to prevent undefined behavior or silent failures. Incremental expansion, Optional creative mechanics (e.g., critical hits, abilities) were designed to layer on top of a working core system so they do not break required features.

4. **AI Usage:** Detail what AI assistance you used: AI assistance was used in the following ways: Reviewing error messages from tests and identifying missing or incorrect function signatures. Helping design consistent validation logic for quests, items, and character data. Assisting with refactoring code to ensure proper exception handling. Drafting explanatory comments and improving code organization for readability. Producing documentation text (such as this README section) for clarity and completeness. All logic was reviewed and tested manually to ensure understanding of every component.
5. **How to Play:** Instructions for running the game: Create a new character using one of four classes: Warrior, Mage, Rogue, Cleric. Begin quests, battle enemies, and earn XP and gold. Use items, equip weapons and armor, and level up your character. Save and load progress from automatically created files in data/save_games/.The game is designed to be simple, text-based, and modular—perfect for experimentation and creative expansion.

### What to Submit:

1. **GitHub Repository:** Your completed multi-module project
2. **Interview:** Complete 10-minute explanation session
3. **README:** Updated documentation

## Protected Files Warning

⚠️ **IMPORTANT: Test Integrity**

Test files are provided for your learning but are protected. Modifying test files constitutes academic dishonesty and will result in:

- Automatic zero on the project
- Academic integrity investigation

You can view tests to understand requirements, but any modifications will be automatically detected.
