# Contributing to The Marooned's Folly

Thank you for helping improve the game! This document describes the recommended workflow, branch naming, pull request (PR) process, and how the repository's automation behaves.

Basics

- Fork or clone the repository and create a branch for each separate change.
- Keep changes small and focused. One feature or bugfix per branch/PR.

Branch naming

- Use this pattern for feature branches: `feature/<short-description>`
- For fixes/bugs: `fix/<short-description>`
- For experiments or spikes: `wip/<topic>`

Workflow (recommended)

1. Update your local main: `git checkout main ; git pull origin main`
2. Create a branch: `git checkout -b feature/my-feature`
3. Make changes and run the game locally (see `docs/BUILD.md`).
4. Commit with a clear message: `git add . ; git commit -m "Short summary: what and why"`
5. Push: `git push -u origin feature/my-feature`
6. Open a Pull Request on GitHub targeting `main`.

Pull request guidelines

- Include a short description of the change and the motivation.
- Link any related issues (if applicable).
- Provide testing notes: how to run and what to verify.
- Request reviewers and wait for at least one approving review before merging.

Automation & auto-PR behavior

- If you push a branch named `feature/**`, a GitHub Actions workflow will automatically create a PR targeting `main` if one doesn't exist. This makes iteration faster for small features.
- Labeling a PR with `automerge` will cause the auto-merge workflow to squash-merge the PR once requirements (reviews, checks) pass.

When automation might fail

- The workflows use the built-in `GITHUB_TOKEN` by default, which may be restricted by organization or repository settings. If automatic PR creation or merging fails, a repository secret named `PR_TOKEN` (a Personal Access Token with `repo` scope) can be added by a maintainer to enable the automation.

Code style & testing

- Keep code and scripts readable. There are no formal linters configured in this repository; run manual checks when appropriate.
- Test your changes by launching the game locally and verifying the affected scenes or features.

Adding assets

- Keep large binary assets out of the main git history. Use Git LFS for very large files or provide download links in the repository.

Maintainers

- Maintainers will review incoming PRs and merge when ready. If you're a maintainer and want to change the automation or branch protections, update the `.github/workflows/` files and repository branch protection rules.

Thanks for contributing! If you're unsure about where to start, open an issue or a draft PR and ask for guidance.
# Contributing to The Marooned's Folly

Thank you for helping improve the game! This document describes the recommended workflow, branch naming, pull request (PR) process, and how the repository's automation behaves.

Basics
- Fork or clone the repository and create a branch for each separate change.
- Keep changes small and focused. One feature or bugfix per branch/PR.

Branch naming
- Use this pattern for feature branches: `feature/<short-description>`
- For fixes/bugs: `fix/<short-description>`
- For experiments or spikes: `wip/<topic>`

Workflow (recommended)
1. Update your local main: `git checkout main ; git pull origin main`
2. Create a branch: `git checkout -b feature/my-feature`
3. Make changes and run the game locally (see `docs/BUILD.md`).
4. Commit with a clear message: `git add . ; git commit -m "Short summary: what and why"`
5. Push: `git push -u origin feature/my-feature`
6. Open a Pull Request on GitHub targeting `main`.

Pull request guidelines
- Include a short description of the change and the motivation.
- Link any related issues (if applicable).
- Provide testing notes: how to run and what to verify.
- Request reviewers and wait for at least one approving review before merging.

Automation & auto-PR behavior
- If you push a branch named `feature/**`, a GitHub Actions workflow will automatically create a PR targeting `main` if one doesn't exist. This makes iteration faster for small features.
- Labeling a PR with `automerge` will cause the auto-merge workflow to squash-merge the PR once requirements (reviews, checks) pass.

When automation might fail
- The workflows use the builtin `GITHUB_TOKEN` by default, which may be restricted by organization or repo settings. If automatic PR creation or merging fails, a repository secret named `PR_TOKEN` (a Personal Access Token with `repo` scope) can be added by a maintainer to enable the automation.

Code style & testing
- Keep code and scripts readable. There are no formal linters configured in this repo; run manual checks when appropriate.
- Test your changes by launching the game locally and verifying the affected scenes or features.

Adding assets
- Keep large binary assets out of the main git history. Use Git LFS for very large files or provide download links in the repo.

Maintainers
- Maintainers will review incoming PRs and merge when ready. If you're a maintainer and want to change the automation or branch protections, update the `.github/workflows/` files and repository branch protection rules.

Thanks for contributing! If you're unsure about where to start, open an issue or a draft PR and ask for guidance.
