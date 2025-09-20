# Building and running The Marooned's Folly (Ren'Py)

This document shows how to run the game from the Ren'Py SDK and how to build distributable packages. The instructions focus on Windows (PowerShell), with brief notes for macOS and Linux.

## Prerequisites

- Ren'Py SDK downloaded and extracted. You can download it from the Ren'Py website: [Ren'Py](https://www.renpy.org/).
- (Optional) Git if you want to pull the latest source or use version control: [Git downloads](https://git-scm.com/downloads).

## Run the game from the Ren'Py SDK (Windows PowerShell)

1. Open PowerShell.
2. Change to the Ren'Py SDK folder (where `renpy.exe` lives) or the SDK launcher folder:

   ```powershell
   cd "e:\renpy-8.4.1-sdk"
   ```

3. Launch the Ren'Py launcher and select this project, or run the project directly using the CLI:

   ```powershell
   # Show the projects and launcher UI
   & .\renpy.exe
   # OR run the project directly by passing the project directory name (folder with `game/`)
   & .\renpy.exe "e:\renpy-8.4.1-sdk\The-Marooneds-Folly"
   ```

4. The Ren'Py launcher opens. Click 'Launch Project' (or use the CLI command above) to start the game.

## Run quickly without the launcher (Python/CLI)

If you prefer running the game directly (fast, for development), run the project's `renpy.py` with the SDK's Python. This is useful for automated tests or headless runs.

```powershell
# From the SDK root (example)
python .\renpy.py launch "e:\renpy-8.4.1-sdk\The-Marooneds-Folly"
```

## Build distributables (Windows PowerShell)

1. Open PowerShell and change to the Ren'Py SDK root:

   ```powershell
   cd "e:\renpy-8.4.1-sdk"
   ```

2. Use the build command to create distributions (Windows, macOS, Linux). Replace <project-dir> with the path to the folder that contains `game/` (this repo):

   ```powershell
   # Example: build distributions for the project
   & .\renpy.exe build "e:\renpy-8.4.1-sdk\The-Marooneds-Folly"
   ```

3. When the build finishes, check the `dist/` subfolder inside the Ren'Py SDK root (or the `dist/` folder specified in the Ren'Py launcher) for platform-specific packages (zip/exe/dmg).

## Notes and tips

- Use the Ren'Py launcher GUI when you want visual control over translations, package name, or when adding icons.
- Windows: If `renpy.exe` doesn't run double-check that the SDK is the correct edition for your OS and that you have Visual C++ redistributables if needed.
- macOS/Linux: The Ren'Py launcher is similar. Use the provided `renpy.sh` or run the SDK with the SDK's Python (e.g., `./renpy.sh build /path/to/project`).
- For CI: you can run the renpy build CLI inside a CI job — ensure the CI runner has the SDK and required system packages. Consider caching the SDK between runs.
- Large assets: use .gitignore / Git LFS for very large files.

## Troubleshooting

- Game fails to start: check `game/log.txt`, `log.txt` in the repository root, and Ren'Py output in the launcher for Python errors or missing assets.
- Build errors: missing dependencies or permission issues; run the launcher once interactively to ensure all resources load correctly.

If you'd like, I can add a short PowerShell wrapper script (for example `tools/build.ps1`) to make these commands repeatable.
