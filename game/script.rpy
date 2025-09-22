# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

# TODO [ ] We need to add in the story blocks and placeholder screens
# The game starts here.

image intro_video = Movie(play="intro_video.ogv",  size=(1280,720), loop=True, xalign=0.10, yalign=0.10)

label start:

    # Stop any menu music (fade out) so it doesn't continue into gameplay.
    stop music fadeout 1.0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

# TODO [ ] We need to add in the main screen background

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

# TODO [ ] We need to add in a new main character, or sprite

    show eileen happy
    # These display lines of dialogue.

    e "You've created a new Ren'Py game." id start_a170b500

# TODO [ ] We need to find a better video, and have full view
    # calls the intro intro_VideoS
    show intro_video behind eileen


    e "Once you add a story, pictures, and music, you can release it to the world!"



# New Pre log Scence 01 use Michelle for e from luvvoice.com
    scene bg room
    with Dissolve(.5)
    pause .5
    scene bg room
    show e happy
    with Dissolve(.5)
    e "The story begins. Your choices will write your legend." id start_37d02c1f


# New Prolog Scence 02 use Michelle for e from luvvoice.com
    scene bg room
    with Dissolve(.5)
    pause .5
    scene bg room
    show e happy
    with Dissolve(.5)
    e "Among the shattered timbers of your ship, you find a single usable pistol and a canteen of fresh water. It's enough to keep going. A figure watches you from the treeline..." id start_5e0f0520


# New Pre log Scence 03 use Michelle for e from luvvoice.com
    scene bg room
    with Dissolve(.5)
    pause .5
    scene bg room
    show e happy
    with Dissolve(.5)
    e "The sea had not been kind.
Splintered beams jutted from the sand like broken ribs, the wreckage of your ship strewn across the cove in a jagged crescent. Smoke curled from the remains of the galley, mingling with the brine-heavy wind. The tide lapped hungrily at the debris, dragging away scraps of canvas and shattered crates like a scavenger with no face." id start_331130df



# New Pre log Scence 04 use Michelle for e from luvvoice.com
    scene bg room
    with Dissolve(.5)
    pause .5
    scene bg room
    show e happy
    with Dissolve(.5)
    e "You crawl from the wreckage, blood crusted on your temple, the taste of salt and ash thick on your tongue. Your boots squelch in the wet sand as you stagger upright, ribs aching with every breath. The world tilts, then steadies." id start_8fee8174



# New Pre log Scence 05 use Michelle for e from luvvoice.com
    scene bg room
    with Dissolve(.5)
    pause .5
    scene bg room
    show e happy
    with Dissolve(.5)
    e "Among the ruin, you find it: a single pistol, half-buried beneath a collapsed mast. The grip is scorched, the barrel dented—but the chamber holds one round. One chance. You sling it into your belt. Nearby, a canteen rolls against a broken spar. You snatch it up, shake it. Still full. Still clean.

Enough to keep going." id start_665085ed



# New Pre log Scence 06 use Michelle for e from luvvoice.com
    scene bg room
    with Dissolve(.5)
    pause .5
    scene bg room
    show e happy
    with Dissolve(.5)
    e "The jungle looms beyond the beach, a wall of tangled green and shadow. Vines hang like nooses from the canopy, and the air pulses with insect song. You feel it before you see it—eyes on you. A prickle at the base of your neck. You turn.
A figure stands just beyond the treeline.

Motionless. Watching." id start_e4317610


# New Pre log Scence 07 use Michelle for e from luvvoice.com
    scene bg room
    with Dissolve(.5)
    pause .5
    scene bg room
    show e happy
    with Dissolve(.5)
    e "Cloaked in mottled cloth, face obscured by a hood, they blend with the underbrush like a ghost stitched from leaves. No weapon visible. No threat made. But they do not move. Do not speak.
You grip the pistol. Your knuckles whiten.
The figure tilts its head.
Then vanishes.
Not into the jungle—but as if the jungle swallowed them whole." id start_a9cb0a9a


# New Pre log Scence 08 use Michelle for e from luvvoice.com
    scene bg room
    with Dissolve(.5)
    pause .5
    scene bg room
    show e happy
    with Dissolve(.5)
    e "You take a step forward. Then another. The trees seem to breathe around you, exhaling damp heat and the scent of decay. Somewhere deeper in the foliage, something howls—low and mournful. Not human.
You glance back at the wreckage. No sails. No crew. No way home.
Forward, then.
You tighten your grip on the canteen, adjust the pistol at your hip, and step into the green.
The jungle closes behind you." id start_42e2151c


    # This ends the game.
# TODO [ ] End of the game, not sure what we need here. (Eplilog) - credits


    return
