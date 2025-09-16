# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


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

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

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
        e "Heads up — there's a new update on the project's main branch."
        menu:
            "Open changelist in browser":
                $ renpy.open_url(remote_url)
            "Ignore for now":
                pass
    elif remote_sha and not last_sha:
        # First time seeing a SHA; store it.
        $ renpy.say(None, "Update check complete.")

    python:
        try:
            if remote_sha:
                with open(".last_main_sha", "w") as f:
                    f.write(remote_sha)
        except Exception:
            pass

    # This ends the game.

    return
