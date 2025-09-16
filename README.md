# The Marooned's Folly

This repository contains a Ren'Py visual novel project.

What's included
- game/ - Ren'Py scripts, assets, and localization.
- gui/, audio/, images/ - project assets used by the game.

Notes before publishing
- Do NOT commit large build outputs (use .gitignore).
- Do NOT commit personal secrets or API keys. Check `game/options.rpy` or other files for any hard-coded credentials.

Getting started with Git & GitHub (Windows PowerShell)
1. Install Git if you don't have it: https://git-scm.com/downloads
2. Open PowerShell and run:

```powershell
cd "e:\Project-Priates\RenPy\The Marooneds Folly"
git init
git add .
git commit -m "Initial commit"
```

3. Create a new repository on GitHub (https://github.com/new).
4. Add the remote and push (replace URL with your repo):

```powershell
git remote add origin https://github.com/<username>/<repo>.git
git branch -M main
git push -u origin main
```

If you prefer to use the GitHub CLI (gh), you can run:

```powershell
gh repo create <username>/<repo> --public --source=. --remote=origin --push
```

If you want, I can initialize the repo and make the first commit for you, or walk you through creating the GitHub repo and pushing. What would you like me to do next?
