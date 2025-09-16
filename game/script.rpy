# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

# Player name variable with a default value.
default player_name = "Player"

init python:
    import random


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

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

    # This ends the game.

    return


label combat:

    # Simple stats
    $ player_hp = 30
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
