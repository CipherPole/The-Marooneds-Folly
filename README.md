# The Marooned's Folly

A short README for this Ren'Py visual novel project. This repository contains the game's Ren'Py scripts, UI assets, audio, and localization.

## Overview

This repository contains the Ren'Py source for the game: scripts, UI artwork, audio, and localization files.

### Key folders

- `game/` — Ren'Py scripts (.rpy), translations, and other source files.
- `gui/`, `audio/`, `images/` — UI artwork, sounds, and image assets.

## Quick start (Windows PowerShell)

Prerequisites:
- Ren'Py: see the Ren'Py website: [Ren'Py](https://www.renpy.org/).
- Git: [Git downloads](https://git-scm.com/downloads).
- (Optional) GitHub CLI: [GitHub CLI](https://cli.github.com/).

Open PowerShell and run:

```powershell
cd "e:\renpy-8.4.1-sdk\The-Marooneds-Folly"
```

If this is a new repository, initialize and push to GitHub:

```powershell
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/<username>/<repository>.git
git branch -M main
git push -u origin main
```

Or create and push with the GitHub CLI:

```powershell
gh repo create <username>/<repository> --public --source=. --remote=origin --push
```

For detailed run and build instructions, see `docs/BUILD.md`.

## Collaboration

- Clone the repository: `git clone https://github.com/<username>/<repository>.git`.
- Keep `main` up to date: `git checkout main; git pull origin main`.
- Work in short-lived feature branches. Suggested naming:
  - `feature/<short-description>` for new features
  - `fix/<short-description>` for bugfixes
  - `wip/<topic>` for work-in-progress

Example feature flow (PowerShell):

```powershell
git checkout -b feature/my-feature
# make changes
git add .
git commit -m "Add: short description of change"
git push -u origin feature/my-feature
```

Open a Pull Request on GitHub and request reviews. Describe what changed, how to test, and link related issues.

## Automation in this repository

- Pushing a branch named `feature/**` will create a PR targeting `main` if one does not already exist.
- Applying the label `automerge` to a PR will trigger the auto-merge workflow (squash-merge) when checks and reviews pass.

If automation fails due to permission restrictions, a repository maintainer can add a Personal Access Token (PAT) with `repo` scope as a repository secret named `PR_TOKEN` to enable the workflows. See GitHub: [Create a personal access token](https://github.com/settings/tokens).

## Security & publishing notes

- Do not commit large built outputs or exported binaries. Add them to `.gitignore` or use Git LFS for large files.
- Never commit secrets, API keys, or credentials.

## Discord notifications

You can enable Discord notifications by adding a repository secret named `DISCORD_WEBHOOK` (Settings → Secrets and variables → Actions → New repository secret) and pasting the webhook URL as the value. The `discord-notify.yml` workflow will post updates when pushes or merges occur.

## What I can do next

- Commit this README change to your branch (I can do that for you).
- Expand the README with Ren'Py-specific run and build steps.
- Add a `CONTRIBUTING.md` with branch and PR guidelines.

If you'd like me to proceed, tell me which item above to run next and I will commit and push the change to the markdown-fixes branch so Super-Linter can re-run.


