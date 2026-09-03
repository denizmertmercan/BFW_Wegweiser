# Devlog

Running log of notable changes and the reasoning behind them. Complements commit
messages with slightly more context. Each entry is headed by timestamp and
contributor initials. Entries don't map 1:1 to commits. Ordered most recent
first. Covers changes made after forking; upstream history predates this log.

## 2026-09-03 09:19 - DM

Added type hints to `build_graph`/`find_path` parameters — the minimum
needed for Pylance's Basic type-checking mode to catch call-site type
mismatches. Return types and local variables are already inferred
automatically by Pylance, so left unannotated to keep the change minimal.
Earlier attempt annotated the whole file (module-level data, return types,
locals); reverted in favor of this minimal version so the import-removal,
debug-cleanup, and type-hint changes could each land as their own commit.

Commits: `285931a`

## 2026-09-03 09:15 - DM

Removed obsolete debug print statements from `main()`
(`print(user_input)`, `print(os.getcwd())`, `print(os.listdir())`). These
were leftover artifacts from debugging the original hardcoded image-path
bug and served no purpose for the end user once the path was fixed.

Commits: `1b87f1b`

## 2026-09-03 09:14 - DM

Removed a redundant `deque` import inside `find_path()` — it was already
imported at module level, so the inner import was dead duplication left
over from earlier iterations. No behavior change.

Commits: `4c570d8`

## 2026-09-03 08:26 - DM

Established the project's language convention and renamed all German
identifiers to English accordingly: identifiers, code structure, commit
messages, and docs stay English; comments and user-facing strings stay
German for the course's German-speaking audience. Graph node label
*values* (e.g. `"knoten_1"`, `"startpunkt"`, `"ost_1"`) were deliberately
left German too — they share one namespace with user-typed checkpoint
names (which must stay German), so keeping the whole namespace uniform
avoided a worse, mixed-language graph. Renamed: `startpunkt`→`start_point`,
`knotenpunkte`→`nodes`, `verbindungen`→`connections` (incl. its
`verbindungN`→`connectionN` keys), `nutzer_eingabe`→`user_input`,
`punkt_a`/`punkt_b`→`point_a`/`point_b`, `karte`→`map_image`, `ziel`→
`target`, `weg`→`path`.

Commits: `1c0fa7a`

## 2026-09-02 14:04 - DM

Added `__pycache__` to `.gitignore`. The folder was generated as a side
effect of testing `import main` (to verify the `__main__` guard below
doesn't trigger side effects on import) and showed up as untracked —
Python's compiled bytecode cache should never be version-controlled.

Commits: `cc82513`

## 2026-09-02 14:01 - DM

Wrapped executable script logic in a `main()` function guarded by
`if __name__ == "__main__":`. Previously, every line (input prompt, image
loading, pathfinding) executed immediately at module load, so importing
`main.py` from elsewhere would trigger all of it as a side effect. Data
and function definitions stay at module level; only the runtime logic
moved into `main()`. No behavior change — verified with a piped-input
test run and an `import main` test.

Commits: `3c907c1`

## 2026-09-02 13:50 - DM

Added validation for the user's checkpoint input. Previously, an invalid
target string caused `find_path` to silently return `None`, printing
`Pfad: None` with no explanation. Now checks the input against
`checkpoints` and prints a clear German error message before exiting.

Commits: `1914d74`

## 2026-09-02 13:45 - DM

Added error handling around `plt.imread()`. A missing or renamed map
image previously crashed with an unhandled traceback; now fails with a
clear German error message instead.

Commits: `46990aa`

## 2026-09-02 13:41 - DM

Fixed the hardcoded absolute path to `Grundriss_mit_Knotenpunkten.png`
(originally pointing to the original author's local machine path,
`E:\TN_Daten\Schmitz\Code_Projekts\...`), which broke the script for any
other contributor. Now resolved relative to the script's own directory
via `__file__`, independent of the caller's working directory.

Commits: `5d26c44`

## 2026-09-02 13:18 - DM

Added `images/` to `.gitignore`. While deciding where the map image
should live, it was briefly moved into an `images/` subfolder and then
back to the project root (kept at root, since it's a required runtime
asset, consistent with the original author's layout). Along the way, an
unrelated `images/` folder containing personal photos appeared in the
working directory (likely synced in from elsewhere) — excluded via
`.gitignore` rather than tracked.

Commits: `bcae946`

## 2026-09-01 14:02 - DM

Updated the environment snapshot doc after upgrading `pip`/`setuptools`/
`wheel` globally and creating the project's `.venv` with `matplotlib`
installed. Reformatted the table into Global vs. Project venv sections.

Commits: `2089dd8`

## 2026-09-01 13:47 - DM

Added `.venv/` to `.gitignore` after creating the project's virtual
environment, so it isn't accidentally committed.

Commits: `8cee102`

## 2026-09-01 13:41 - DM

Created `docs/environment_snapshot.md` to record installed tool versions
(Python, pip, Git, VS Code, PowerShell) at project setup time, for
reproducibility and onboarding as a new contributor to the fork.

Commits: `365a2b4`
