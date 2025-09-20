# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

# TODO We need to add in the story blocks and placeholder screens
# The game starts here.

image intro_video = Movie(play="intro_video.ogv",  size=(1280,720), loop=True, xalign=0.10, yalign=0.10)

label start:

    # Stop any menu music (fade out) so it doesn't continue into gameplay.
    stop music fadeout 1.0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy
    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    # calls the intro intro_VideoS
    show intro_video behind eileen


    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
