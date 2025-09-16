# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

# Player name variable with a default value.
default player_name = "Player"


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

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
