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

## Collaboration

If you'd like to co-develop with others, here are the basic commands and workflow your collaborators can use to start working with this repository.

Clone the repository (one-time):

```powershell
git clone https://github.com/<username>/<repo>.git
cd "<repo>"
```

Get the latest changes from main:

```powershell
git checkout main
git pull origin main
```

Create and push a feature branch:

```powershell
git checkout -b feature/<short-description>
# make changes, then:
git add .
git commit -m "Short description of change"
git push -u origin feature/<short-description>
```

Open a Pull Request on GitHub to merge changes into `main`. Use PRs for review and testing before merging.

If the repository is private, invite collaborators under Settings → Manage access. For very large binary assets, consider Git LFS (ask if you need help setting it up).

## Automation: auto-PR and auto-merge

This repository includes two GitHub Actions workflows to streamline collaboration:

- `auto-create-pr.yml`: when anyone pushes to a branch matching `feature/**`, a pull request will be automatically created targeting `main` (if one doesn't already exist).
- `auto-merge-pr.yml`: when a pull request is labeled `automerge`, the PR will be automatically merged using squash merge.

How to use:
- Push your changes to a branch named `feature/<something>`.
- A PR will be created automatically. Review it on GitHub.
- If everything looks good, add the label `automerge` to the PR and the workflow will merge it.

Security and notes:
- The workflows use the built-in `GITHUB_TOKEN`. This token has limited permissions and cannot create or manage secrets. Review workflow logs and PRs before merging automatically.
- If you want stricter rules (e.g., require approvals, CI checks), update the workflow or add branch protection rules in GitHub Settings.

If you see the error "GitHub Actions is not permitted to create or approve pull requests", GitHub is preventing the built-in `GITHUB_TOKEN` from creating PRs or merging. To fix this, create a Personal Access Token (PAT) with repo scope and add it as a repository secret named `PR_TOKEN`:

1. Create a PAT: https://github.com/settings/tokens/new — enable `repo` (or at least `public_repo` for public repos).
2. In your GitHub repository: Settings → Secrets and variables → Actions → New repository secret.
	- Name: PR_TOKEN
	- Value: (paste your PAT)

With `PR_TOKEN` set, the workflows will use that token to create and merge PRs.

### Discord notifications

You can receive repository notifications in Discord. To enable this, add a repository secret named `DISCORD_WEBHOOK` (Settings → Secrets and variables → Actions → New repository secret) and paste the webhook URL as the value.

The repository includes a workflow `discord-notify.yml` which will post messages to that webhook when:
- a push happens on any branch (reports branch, author and commit link)
- a pull request is merged (reports title, author, merged by, and PR link)

Note: For security, add the webhook as a secret rather than placing it directly in the repo. If you'd like, I can add the webhook secret for you if you paste the webhook here (but keep in mind chat is not a secure channel; it's safer to add it manually in the GitHub UI).


