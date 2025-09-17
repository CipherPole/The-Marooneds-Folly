# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

# Player name variable with a default value.
default player_name = "Player"

# Player attributes and equipment defaults
default player_stats = {
    'HP': 30,
    'STR': 6,
    'DEF': 4,
    'AGI': 5,
}

default player_equipment = {
    'Weapon': 'Rusty Sword',
    'Armor': 'Worn Tunic',
    'Accessory': 'Lucky Coin',
}

# Keep an immutable base for recalculation when equipment changes
default player_base_stats = {
    'HP': 30,
    'STR': 6,
    'DEF': 4,
    'AGI': 5,
}

# An inventory of period-appropriate (circa 1650) weapons and equipment.
# Each item has a type, a name, a modifiers dict, and an owned flag.
default inventory = [
    { 'type': 'Weapon', 'name': 'Rapier', 'mod': {'STR': 2, 'AGI': 1}, 'owned': True, 'desc': 'A light thrusting sword, common for duels.' },
    { 'type': 'Weapon', 'name': 'Broadsword', 'mod': {'STR': 3, 'AGI': -1}, 'owned': True, 'desc': 'A heavy cutting sword favored by soldiers.' },
    { 'type': 'Weapon', 'name': 'Cutlass', 'mod': {'STR': 2, 'AGI': 0}, 'owned': True, 'desc': 'A short, sturdy blade useful in close combat.' },
    { 'type': 'Weapon', 'name': 'Matchlock Musket', 'mod': {'STR': 4, 'AGI': -2, 'DEF': -1}, 'owned': False, 'desc': 'A slow-firing firearm; powerful but cumbersome.' },
    { 'type': 'Weapon', 'name': 'Pike', 'mod': {'STR': 3, 'AGI': -2}, 'owned': False, 'desc': 'A long pole weapon effective against cavalry.' },

    { 'type': 'Armor', 'name': 'Worn Tunic', 'mod': {'DEF': 0}, 'owned': True, 'desc': 'Simple cloth clothing offering no protection.' },
    { 'type': 'Armor', 'name': 'Leather Jerkin', 'mod': {'DEF': 1, 'AGI': 0}, 'owned': True, 'desc': 'Padded leather offering light protection.' },
    { 'type': 'Armor', 'name': 'Brigandine', 'mod': {'DEF': 3, 'AGI': -1}, 'owned': False, 'desc': 'Layered plates riveted inside fabric for solid defense.' },
    { 'type': 'Armor', 'name': 'Breastplate', 'mod': {'DEF': 4, 'AGI': -2}, 'owned': False, 'desc': 'Solid metal plate protecting the torso.' },

    { 'type': 'Accessory', 'name': 'Lucky Coin', 'mod': {'AGI': 1}, 'owned': True, 'desc': 'A small charm believed to bring fortune.' },
    { 'type': 'Accessory', 'name': 'Powder Horn', 'mod': {'STR': 1}, 'owned': False, 'desc': 'Used to carry powder; useful if you use a musket.' },
    { 'type': 'Accessory', 'name': 'Signet Ring', 'mod': {'DEF': 0}, 'owned': True, 'desc': 'A decorative ring, some say it grants resolve.' },
]

init python:
    import renpy

    def find_item_by_name(name):
        for it in inventory:
            if it['name'] == name:
                return it
        return None

    def recalc_player_stats():
        # Start from the base stats
        new = dict(player_base_stats)
        # Apply currently equipped items' modifiers
        for slot, iname in player_equipment.items():
            it = find_item_by_name(iname)
            if it and 'mod' in it:
                for k, v in it['mod'].items():
                    new[k] = new.get(k, 0) + v
        # Update the mutable player_stats mapping in-place
        for k in new:
            player_stats[k] = new[k]

    def equip_item(item_name):
        it = find_item_by_name(item_name)
        if not it:
            return
        # Only allow equipping items the player owns
        if not it.get('owned', False):
            renpy.notify("You don't own that item.")
            return
        player_equipment[it['type']] = it['name']
        recalc_player_stats()
        renpy.notify(f"Equipped {it['name']}.")


init python:
    import random


# The game starts here.

init python:
    # Simple GitHub 'main' branch update checker.
    # This uses urllib so no extra dependencies are required.
    import json, urllib.request, urllib.error

    REPO_OWNER = 'CipherPole'
    REPO_NAME = 'The-Marooneds-Folly'
    GITHUB_COMMITS_API = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/commits/main'

    def fetch_main_sha():
        """Return (sha, html_url) of latest commit on main or (None, None) on error."""
        try:
            req = urllib.request.Request(GITHUB_COMMITS_API, headers={'User-Agent': 'RenPy Update Checker'})
            with urllib.request.urlopen(req, timeout=5) as resp:
                data = json.load(resp)
            sha = data.get('sha')
            html_url = data.get('html_url')
            return sha, html_url
        except Exception:
            # Network errors or rate limits will be silently ignored here.
            return None, None


label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    # The "scene" statement also clears away any characters or

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # Ask the player for their name before dialogue starts.
    $ player_name_input = renpy.input("What's your name?", default=player_name)
    # Simple sanitization: strip whitespace and prevent empty names.
    $ player_name_input = player_name_input.strip()
    if player_name_input == "":
        $ player_name = player_name
    else:
        $ player_name = player_name_input

    # These display lines of dialogue. Eileen will use the entered name.

    e "Nice to meet you, [player_name]."

    e "You've created a new Ren'Py game, [player_name]."

    e "Once you add a story, pictures, and music, you can release it to the world, [player_name]!"

    # After Eileen speaks, let the player choose whether to investigate.
    menu:
        "Investigate the noise":
            e "Alright, let's check it out. Stay close, [player_name]."
            jump combat

        "Ignore it and continue":
            e "Maybe it's nothing. Let's keep going."
            # Continue the story here (falls through to return)

    # Check for updates on GitHub main branch and notify if different.
    python:
        try:
            remote_sha, remote_url = fetch_main_sha()
        except Exception:
            remote_sha, remote_url = None, None

        last_sha = None
        try:
            with open(".last_main_sha", "r") as f:
                last_sha = f.read().strip()
        except Exception:
            last_sha = None

    if remote_sha and last_sha and remote_sha != last_sha:
        # Non-blocking notification. Players can click the notification to open the URL.
        $ renpy.notify("Update available: click to view changelist")
        # Provide a clickable link in the log for convenience.
        $ renpy.open_url(remote_url)  # This will open immediately; if you'd prefer not to open automatically, remove this line.
    elif remote_sha and not last_sha:
        # First time seeing a SHA; store it quietly.
        pass

    python:
        try:
            if remote_sha:
                with open(".last_main_sha", "w") as f:
                    f.write(remote_sha)
        except Exception:
            pass

    # This ends the game.

    return


label combat:
    # Prepare the player and show the preparation screen
    call combat_prep

    # Simple stats (start from player_stats so values carry over)
    $ player_hp = player_stats['HP']
    $ enemy_hp = 20
    $ enemy_name = "Skulking Raider"

    scene bg room
    show eileen angry

    e "Wait... did you hear that, [player_name]? Something's coming..."

    "A wild [enemy_name] appears!"

    label combat_loop:
        "Player HP: [player_hp]    [enemy_name] HP: [enemy_hp]"

        menu:
            "Attack":
                $ dmg = random.randint(4,8)
                $ enemy_hp -= dmg
                "You attack the [enemy_name] for [dmg] damage."
                if enemy_hp <= 0:
                    jump combat_win
                # Enemy retaliates
                $ edmg = random.randint(3,7)
                $ player_hp -= edmg
                "The [enemy_name] strikes back for [edmg] damage."
                if player_hp <= 0:
                    jump combat_lose
                jump combat_loop

            "Defend":
                $ reduced = random.randint(1,4)
                $ edmg = max(0, random.randint(3,7) - reduced)
                $ player_hp -= edmg
                "You brace yourself and reduce incoming damage by [reduced]."
                "The [enemy_name] deals [edmg] damage."
                if player_hp <= 0:
                    jump combat_lose
                jump combat_loop

            "Run":
                $ chance = random.random()
                if chance < 0.5:
                    "You fail to escape! The [enemy_name] attacks."
                    $ edmg = random.randint(3,7)
                    $ player_hp -= edmg
                    if player_hp <= 0:
                        jump combat_lose
                    jump combat_loop
                else:
                    "You successfully escape the encounter."
                    jump combat_end

    label combat_win:
        "You defeated the [enemy_name]!"
        $ reward = random.randint(5,12)
        "You find [reward] gold on the foe."
        jump combat_end

    label combat_lose:
        "You collapse from your wounds..."
        scene black
        centered "You have been defeated."
        return

    label combat_end:
        show eileen normal
        e "That was close, [player_name]. Are you alright?"
        return


label combat_prep:
    # Display a simple preparation screen showing player attributes and equipment.
    scene bg room
    show eileen normal

    e "Prepare yourself, [player_name]. Here are your current stats:"

    # Display stats
    "HP: [player_stats['HP']]  STR: [player_stats['STR']]  DEF: [player_stats['DEF']]  AGI: [player_stats['AGI']]"

    e "Equipped: [player_equipment['Weapon']], [player_equipment['Armor']], [player_equipment['Accessory']]"

    menu:
        "Ready - enter the fight":
            e "Let's do this!"
            return

        "Adjust equipment (not implemented)":
            e "You'll have to check your inventory later."
            return
