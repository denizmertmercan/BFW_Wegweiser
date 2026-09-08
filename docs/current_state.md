# current state of affairs

Based on the provided context, the project situation and architectural direction can be summarized as follows:

Environment baseline: The environment is stabilized with Python 3.14.7, an isolated virtual environment, and passing tests in test_main.py.
Architecture shift: Rather than running a live backend server or duplicating pathfinding algorithms across Python and JavaScript, the project adopts an offline compiler and static viewer model documented in docs/adr.md.
Python responsibility: Python acts as an offline build tool. It defines coordinates, computes edge weights (such as Euclidean pixel distances plus potential stair or door penalties), evaluates optimal paths via Dijkstra or precomputed next-hop tables, and exports a standalone static artifact (such as a data.json file).
JavaScript responsibility: The frontend (adapted from Janus's UI work) functions strictly as a presentation layer. It fetches the precomputed JSON, populates user search suggestions, retrieves the route directly from lookup tables, and renders the SVG path onto the floor plan without running any graph traversal logic.
Scalability and maintenance: This separation avoids logic drift between languages, eliminates server hosting requirements for both kiosk and mobile phases, and permits future extensions (such as multi-floor routing or separate analytics collection) without altering the frontend rendering mechanics.
