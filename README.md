
# The Marooned's Folly

A short, clear README for this Ren'Py visual novel project. The repository contains the game's Ren'Py scripts, UI assets, audio, and localization.

Overview
- `game/` — Ren'Py scripts (.rpy), translation files, and other source assets used by the engine.
- `gui/`, `audio/`, `images/` — artwork and media used by the project.

Quick start (Windows PowerShell)
1. Install Git if needed: https://git-scm.com/downloads
2. Open PowerShell and change to the project folder:

```powershell
cd "e:\renpy-8.4.1-sdk\The-Marooneds-Folly"
```

3. If this is a new repository, initialize and push to GitHub:

```powershell
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/<username>/<repo>.git
git branch -M main
git push -u origin main
```

Or create & push with the GitHub CLI:

```powershell
gh repo create <username>/<repo> --public --source=. --remote=origin --push
```

Run & build (details)
- For detailed run and build instructions see `docs/BUILD.md`. It includes PowerShell commands to launch the game from the Ren'Py SDK and to build distributables.

Collaboration
- Clone the repo: `git clone https://github.com/<username>/<repo>.git`
- Keep `main` up to date: `git checkout main ; git pull origin main`
- Work in short-lived feature branches. Recommended naming:
   - `feature/<short-description>` for new features
   - `fix/<short-description>` for bug fixes
   - `wip/<topic>` for work-in-progress

Example feature flow (PowerShell):

```powershell
git checkout -b feature/my-feature
# make changes
git add .
git commit -m "Add: short description of change"
git push -u origin feature/my-feature
```

- Open a Pull Request on GitHub and request reviews. Describe what changed, how to test, and link related issues.

Automation in this repository
- Pushing a branch named `feature/**` will automatically create a PR targeting `main` if one does not already exist.
- Applying the label `automerge` to a PR will trigger the auto-merge workflow (squash-merge) when checks and reviews pass.
- If automation fails due to permission restrictions, a maintainer can add a Personal Access Token (PAT) with `repo` scope as a repository secret named `PR_TOKEN` to enable the workflows.

Security & publishing notes
- Don't commit large compiled outputs or exported binaries. Add them to `.gitignore` or use Git LFS for big files.
- Never commit secrets, API keys, or credentials. Grep `game/options.rpy` and other config files if you're unsure.

Help & next steps
- I added `docs/BUILD.md` with step-by-step run/build steps.
- I can also add a `CONTRIBUTING.md` (branch/PR guidelines and automation notes) if you'd like — or open a PR that commits these updates for you.

Thank you for contributing — open an issue or a draft PR if you want guidance on where to start.

Automation (what's included)
- Pushing a branch named `feature/**` will create a PR automatically.
- Label a PR `automerge` to have it automatically squash-merged.

Security & publishing notes
- Do not commit large build outputs or exported binaries. Add them to `.gitignore`.
- Do not commit secrets or API keys. Search `game/options.rpy` and other config files for hard-coded credentials.

If GitHub Actions cannot create or merge PRs because of permission restrictions, add a Personal Access Token (PAT) named `PR_TOKEN` in repository secrets:
1. Create a PAT with `repo` scope: https://github.com/settings/tokens/new
2. In GitHub: Settings → Secrets and variables → Actions → New repository secret
   - Name: `PR_TOKEN`
   - Value: (paste your PAT)

What I can do next
- Commit this README update to your branch.
- Add Ren'Py run/build instructions to the README.
- Create a `CONTRIBUTING.md` with branch and PR guidelines.

Which would you like me to do next?
1. Install Git if needed: https://git-scm.com/downloads
2. Open PowerShell and go to the project folder:

```powershell
cd "e:\renpy-8.4.1-sdk\The-Marooneds-Folly"
```

3. If this is a new repo, initialize and push to GitHub:

```powershell
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/<username>/<repo>.git
git branch -M main
git push -u origin main
```

Or create & push with the GitHub CLI:

```powershell
gh repo create <username>/<repo> --public --source=. --remote=origin --push
```

Collaboration basics
- Clone: `git clone https://github.com/<username>/<repo>.git`
- Update main: `git checkout main ; git pull origin main`
- Create a feature branch and push:

```powershell
git checkout -b feature/my-feature
# make changes
git add .
git commit -m "Add my feature"
git push -u origin feature/my-feature
```

- Open a Pull Request on GitHub and request reviews before merging.

Automation in this repo
- Pushing a branch named `feature/**` will automatically create a PR targeting `main`.
- Label a PR `automerge` to automatically squash-merge it.

Security & publishing notes
- Don't commit large build outputs or exported binaries. Add them to `.gitignore`.
- Don't commit secrets or API keys. Search `game/options.rpy` and other config files for hard-coded credentials.

If automatic PR creation or merging fails due to permissions, add a Personal Access Token (PAT) named `PR_TOKEN` in repository secrets:

1. Create a PAT with `repo` scope: https://github.com/settings/tokens/new
2. In GitHub: Settings → Secrets and variables → Actions → New repository secret
   - Name: `PR_TOKEN`
   - Value: (paste your PAT)

Next steps I can do for you
- Commit this README change to your branch.
- Expand the README with Ren'Py development & build instructions.
- Add a `CONTRIBUTING.md` with branch and PR conventions.

Tell me which you'd like next.
# The Marooned's Folly

A short, clear README for the Ren'Py project. This repository contains the game's source scripts, assets, and localization used by Ren'Py.

What you'll find
- `game/` — Ren'Py scripts (.rpy), translations, and other game source files.
- `gui/`, `audio/`, `images/` — UI art, sounds, and images.

Quick start (Windows PowerShell)
1. Install Git if needed: https://git-scm.com/downloads
2. Open PowerShell and go to the project folder:

```powershell
cd "e:\renpy-8.4.1-sdk\The-Marooneds-Folly"
```

3. If this is a new repo, initialize and push to GitHub:

```powershell
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/<username>/<repo>.git
git branch -M main
git push -u origin main
```

Or create & push with GitHub CLI:

```powershell
gh repo create <username>/<repo> --public --source=. --remote=origin --push
```

Collaboration basics
- Clone: `git clone https://github.com/<username>/<repo>.git`
- Update main: `git checkout main ; git pull origin main`
- Work on a feature branch and push:

```powershell
git checkout -b feature/my-feature
# make changes
git add .
git commit -m "Add my feature"
git push -u origin feature/my-feature
```

- Open a Pull Request on GitHub and request reviews before merging.

Automation in this repo
- Pushing a `feature/**` branch will automatically create a PR targeting `main`.
- Label a PR `automerge` to automatically squash-merge it.

Security & publishing notes
- Don't commit large build outputs or exported binaries. Add them to `.gitignore`.
- Don't commit secrets or API keys. Search `game/options.rpy` and other files for hard-coded credentials.

If automatic PR creation or merging fails due to permissions, add a Personal Access Token (PAT) named `PR_TOKEN` in repository secrets:

1. Create a PAT with `repo` scope: https://github.com/settings/tokens/new
2. In GitHub: Settings → Secrets and variables → Actions → New repository secret
   - Name: `PR_TOKEN`
   - Value: (paste your PAT)

Next steps I can help with
- Commit this README change to your branch.
- Expand the README with Ren'Py run/build instructions.
- Add a `CONTRIBUTING.md` with branch and PR rules.

Tell me which you'd like next.
# The Marooned's Folly

A short, clear README for the Ren'Py visual novel project.

Overview
- This repository contains the game's Ren'Py source: scripts, assets, and localization.

Key folders
- `game/` — Ren'Py scripts (.rpy), translations, and other source files.
- `gui/`, `audio/`, `images/` — UI art, sounds, and image assets.

Quick start (Windows PowerShell)
1. Install Git if needed: https://git-scm.com/downloads
2. Open PowerShell and go to the project folder:

```powershell
cd "e:\renpy-8.4.1-sdk\The-Marooneds-Folly"
```

3. If this is a new repository, initialize and push to GitHub:

```powershell
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/<username>/<repo>.git
git branch -M main
git push -u origin main
```

Alternative: create and push with GitHub CLI:

```powershell
gh repo create <username>/<repo> --public --source=. --remote=origin --push
```

Collaboration basics
- Clone: `git clone https://github.com/<username>/<repo>.git`
- Update main: `git checkout main ; git pull origin main`
- Create a feature branch and push:

```powershell
git checkout -b feature/my-feature
# make changes
git add .
git commit -m "Add my feature"
git push -u origin feature/my-feature
```

- Open a Pull Request on GitHub and request reviews before merging.

Automation in this repo
- Pushing a branch named `feature/**` triggers a workflow that creates a PR targeting `main`.
- Label a PR `automerge` to automatically squash-merge it.

Security & publishing notes
- Do not commit large build outputs or exported binaries. Add them to `.gitignore`.
- Do not commit secrets or API keys. Search `game/options.rpy` and other config files for hard-coded credentials.

If automatic PR creation or merging fails due to permissions, add a Personal Access Token (PAT) named `PR_TOKEN` in repository secrets:

1. Create a PAT with `repo` scope: https://github.com/settings/tokens/new
2. In GitHub: Settings → Secrets and variables → Actions → New repository secret
   - Name: `PR_TOKEN`
   - Value: (paste your PAT)

Next actions I can do for you
- Commit this README change to your branch (I can run that for you).
- Expand the README with Ren'Py-specific run and build steps.
- Add a `CONTRIBUTING.md` with branch/PR guidelines.

Which of the above would you like next?
# The Marooned's Folly

A short, clear README for the Ren'Py visual novel project.

Overview
- This repository contains the game's Ren'Py source: scripts, assets, and localization.

Key folders
- `game/` — Ren'Py scripts (.rpy), translations, and other source files.
- `gui/`, `audio/`, `images/` — UI art, sounds, and image assets.

Quick start (Windows PowerShell)
1. Install Git if needed: https://git-scm.com/downloads
2. Open PowerShell and go to the project folder:

```powershell
cd "e:\renpy-8.4.1-sdk\The-Marooneds-Folly"
```

3. If this is a new repository, initialize and push to GitHub:

```powershell
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/<username>/<repo>.git
git branch -M main
git push -u origin main
```

Alternative: create and push with GitHub CLI:

```powershell
gh repo create <username>/<repo> --public --source=. --remote=origin --push
```

Collaboration basics
- Clone: `git clone https://github.com/<username>/<repo>.git`
- Update main: `git checkout main ; git pull origin main`
- Create a feature branch and push:

```powershell
git checkout -b feature/my-feature
# make changes
git add .
git commit -m "Add my feature"
git push -u origin feature/my-feature
```

- Open a Pull Request on GitHub and request reviews before merging.

Automation in this repo
- Pushing a branch named `feature/**` triggers a workflow that creates a PR targeting `main`.
- Label a PR `automerge` to automatically squash-merge it.

Security & publishing notes
- Do not commit large build outputs or exported binaries. Add them to `.gitignore`.
- Do not commit secrets or API keys. Search `game/options.rpy` and other config files for hard-coded credentials.

If automatic PR creation or merging fails due to permissions, add a Personal Access Token (PAT) named `PR_TOKEN` in repository secrets:

1. Create a PAT with `repo` scope: https://github.com/settings/tokens/new
2. In GitHub: Settings → Secrets and variables → Actions → New repository secret
   - Name: `PR_TOKEN`
   - Value: (paste your PAT)

Next actions I can do for you
- Commit this README change to your branch (I can run that for you).
- Expand the README with Ren'Py-specific run and build steps.
- Add a `CONTRIBUTING.md` with branch/PR guidelines.

Which of the above would you like next?
# The Marooned's Folly

A short, clear README for the Ren'Py visual novel project.

Overview
- This repository contains the game's Ren'Py source: scripts, assets, and localization.

Key folders
- `game/` — Ren'Py scripts (.rpy), translations, and other source files.
- `gui/`, `audio/`, `images/` — UI art, sounds, and image assets.

Quick start (Windows PowerShell)
1. Install Git if needed: https://git-scm.com/downloads
2. Open PowerShell and go to the project folder:

```powershell
cd "e:\renpy-8.4.1-sdk\The-Marooneds-Folly"
```

3. If this is a new repository, initialize and push to GitHub:

```powershell
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/<username>/<repo>.git
git branch -M main
git push -u origin main
```

Alternative: create and push with GitHub CLI:

```powershell
gh repo create <username>/<repo> --public --source=. --remote=origin --push
```

Collaboration basics
- Clone: `git clone https://github.com/<username>/<repo>.git`
- Update main: `git checkout main ; git pull origin main`
- Create a feature branch and push:

```powershell
git checkout -b feature/my-feature
# make changes
git add .
git commit -m "Add my feature"
git push -u origin feature/my-feature
```

- Open a Pull Request on GitHub and request reviews before merging.

Automation in this repo
- Pushing a branch named `feature/**` triggers a workflow that creates a PR targeting `main`.
- Label a PR `automerge` to automatically squash-merge it.

Security & publishing notes
- Do not commit large build outputs or exported binaries. Add them to `.gitignore`.
- Do not commit secrets or API keys. Search `game/options.rpy` and other config files for hard-coded credentials.

If automatic PR creation or merging fails due to permissions, add a Personal Access Token (PAT) named `PR_TOKEN` in repository secrets:

1. Create a PAT with `repo` scope: https://github.com/settings/tokens/new
2. In GitHub: Settings → Secrets and variables → Actions → New repository secret
   - Name: `PR_TOKEN`
   - Value: (paste your PAT)

Next actions I can do for you
- Commit this README change to your branch (I can run that for you).
- Expand the README with Ren'Py-specific run and build steps.
- Add a `CONTRIBUTING.md` with branch/PR guidelines.

Which of the above would you like next?
# The Marooned's Folly

A short, clear README for the Ren'Py visual novel project.

Overview
- This repository contains the game's Ren'Py source: scripts, assets, and localization.

Key folders
- `game/` — Ren'Py scripts (.rpy), translations, and other source files.
- `gui/`, `audio/`, `images/` — UI art, sounds, and image assets.

Quick start (Windows PowerShell)
1. Install Git if needed: https://git-scm.com/downloads
2. Open PowerShell and go to the project folder:

```powershell
cd "e:\renpy-8.4.1-sdk\The-Marooneds-Folly"
```

3. If this is a new repository, initialize and push to GitHub:

```powershell
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/<username>/<repo>.git
git branch -M main
git push -u origin main
```

Alternative: create and push with GitHub CLI:

```powershell
gh repo create <username>/<repo> --public --source=. --remote=origin --push
```

Collaboration basics
- Clone: `git clone https://github.com/<username>/<repo>.git`
- Update main: `git checkout main ; git pull origin main`
- Create a feature branch and push:

```powershell
git checkout -b feature/my-feature
# make changes
git add .
git commit -m "Add my feature"
git push -u origin feature/my-feature
```

- Open a Pull Request on GitHub and request reviews before merging.

Automation in this repo
- Pushing a branch named `feature/**` triggers a workflow that creates a PR targeting `main`.
- Label a PR `automerge` to automatically squash-merge it.

Security & publishing notes
- Do not commit large build outputs or exported binaries. Add them to `.gitignore`.
- Do not commit secrets or API keys. Search `game/options.rpy` and other config files for hard-coded credentials.

If automatic PR creation or merging fails due to permissions, add a Personal Access Token (PAT) named `PR_TOKEN` in repository secrets:

1. Create a PAT with `repo` scope: https://github.com/settings/tokens/new
2. In GitHub: Settings → Secrets and variables → Actions → New repository secret
   - Name: `PR_TOKEN`
   - Value: (paste your PAT)

Next actions I can do for you
- Commit this README change to your branch (I can run that for you).
- Expand the README with Ren'Py-specific run and build steps.
- Add a `CONTRIBUTING.md` with branch/PR guidelines.

Which of the above would you like next?
# The Marooned's Folly

This repository contains the source for a Ren'Py visual novel: scripts, assets, and localization.

Overview
- `game/`: Ren'Py scripts (.rpy), translations, and other game source files.
- `gui/`, `audio/`, `images/`: UI art, sounds, and images.

Quick start (PowerShell)
1. Install Git if needed: https://git-scm.com/downloads
2. Open PowerShell and change to this folder:

```powershell
cd "e:\renpy-8.4.1-sdk\The-Marooneds-Folly"
```

3. If you're creating a new remote repo, initialize and push:

```powershell
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/<username>/<repo>.git
git branch -M main
git push -u origin main
```

Or use GitHub CLI to create & push in one step:

```powershell
gh repo create <username>/<repo> --public --source=. --remote=origin --push
```

Collaboration essentials
- Clone: `git clone https://github.com/<username>/<repo>.git`
- Keep main updated: `git checkout main ; git pull origin main`
- Work in feature branches:

```powershell
git checkout -b feature/short-description
# make changes
git add .
git commit -m "Short description"
git push -u origin feature/short-description
```

- Open a Pull Request on GitHub for review before merging.

Automation (what's included)
- Pushing a branch named `feature/**` will create a PR automatically.
- Label a PR `automerge` to have it automatically squash-merged.

Security & publishing notes
- Do not commit large build outputs or exported binaries. Add them to `.gitignore`.
- Do not commit secrets or API keys. Search `game/options.rpy` and other config files for hard-coded credentials.

If GitHub Actions cannot create or merge PRs because of permission restrictions, add a Personal Access Token (PAT) named `PR_TOKEN` in repository secrets:
1. Create a PAT with `repo` scope: https://github.com/settings/tokens/new
2. In GitHub: Settings → Secrets and variables → Actions → New repository secret
   - Name: `PR_TOKEN`
   - Value: (paste your PAT)

What I can do next
- Commit this README update to your branch.
- Add Ren'Py run/build instructions to the README.
- Create a `CONTRIBUTING.md` with branch and PR guidelines.

Which would you like me to do next?


