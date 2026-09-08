# BFW Wegweiser

Indoor navigation system prototype designed to assist routing within the BFW facility.

## Architecture

The repository adopts a two-tier architecture separating data preparation from presentation:

- [src/](src/): Python graph compiler defining coordinates, weights, and precomputing route data.
- [web/](web/): Static client displaying the floor plan and rendering route overlays in the browser.

## Workspace Layout

```text
wegweiser/
├── .gitignore
├── README.md
├── docs/
│   ├── adr_directory_structure.md
│   ├── current_state.md
│   ├── devlog.md
│   ├── environment_snapshot.md
│   └── temp_branch_strategy.md
├── src/
│   ├── main.py
│   └── test_main.py
└── web/
    ├── assets/
    │   └── Grundriss_mit_Knotenpunkten.png
    ├── index.html
    ├── script.js
    └── style.css
```
