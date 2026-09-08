
import os
from collections import deque

import matplotlib.pyplot as plt


# -----------------------------
# 1. Definition der Grunddaten
# -----------------------------
# Hier werden alle Knoten und Zielpunkte mit ihren x/y-Koordinaten gespeichert.
# Diese Koordinaten werden später für die grafische Darstellung des Pfads verwendet.

start_point = (675, 400)

nodes = {
    "knoten_1": (680, 318),  # Flur nach Eingang
    "knoten_2": (556, 314),  # Aufenthalt
    "knoten_3": (488, 354),  # vor dem Speisesaal
    "knoten_4": (327, 349),  # vor den Aufzügen
    "knoten_nord": (624, 185),
}

checkpoints = {
    "ost_1": (769, 330),
    "ost_2": (880, 340),
    "nord_1": (511, 185),
    "nord_2": (777, 176),
    "nord_west_1": (163, 82),
    "west_1": (165, 349),
    "west_2": (96, 348),
    "sued_west": (255, 485),
}

# Verbindungsliste: jeder Eintrag beschreibt einen Abschnitt zwischen zwei Punkten.
# Diese Abschnitte bilden die Kanten des Graphen.
# Example: "connection9": ["knoten_3", "knoten_4"] bedeutet, dass es einen
# begehbaren Weg von knoten_3 nach knoten_4 gibt.
connections = {
    "connection1": ["startpunkt", "knoten_1"],
    "connection2": ["knoten_1", "ost_1"],
    "connection3": ["ost_1", "ost_2"],
    "connection4": ["knoten_1", "knoten_2"],
    "connection5": ["knoten_2", "knoten_nord"],
    "connection6": ["knoten_nord", "nord_1"],
    "connection7": ["knoten_nord", "nord_2"],
    "connection8": ["knoten_2", "knoten_3"],
    "connection9": ["knoten_3", "knoten_4"],
    "connection10": ["knoten_4", "nord_west_1"],
    "connection11": ["knoten_4", "west_1"],
    "connection12": ["knoten_4", "sued_west"],
    "connection13": ["west_1", "west_2"],
}


# ------------------------------------------------
# 2. Graph-Aufbau: Erstelle eine Adjazenzliste
# ------------------------------------------------
def build_graph(connections: dict[str, list[str]]):
    """Erzeuge aus den Verbindungsabschnitten einen Graphen."""
    graph = {}

    # Jede Verbindung ist eine Liste mit zwei Elementen: [startpunkt, endpunkt].
    for connection in connections.values():
        point_a = connection[0]  # erster Endpunkt des Abschnitts
        point_b = connection[1]  # zweiter Endpunkt des Abschnitts

        # Stelle sicher, dass beide Punkte als Knoten im Graphen existieren.
        if point_a not in graph:
            graph[point_a] = []
        if point_b not in graph:
            graph[point_b] = []

        # Füge die Verbindung in beide Richtungen hinzu.
        # Der Graph ist ungerichtet: von point_a kann man zu point_b und umgekehrt.
        graph[point_a].append(point_b)
        graph[point_b].append(point_a)

    return graph


# ------------------------------------------------
# 3. Pfadfindung: Breitensuche (BFS)
# ------------------------------------------------
def find_path(graph: dict[str, list[str]], start: str, goal: str):
    """Finde einen Pfad vom Startpunkt zum Ziel im Graphen."""
    visited = set()  # bereits besuchte Knoten

    # Die Queue enthält Tupel (aktueller Knoten, bisheriger Pfad).
    queue = deque([(start, [start])])
    visited.add(start)

    while queue:
        current, path = queue.popleft()

        # Wenn der aktuelle Knoten das Ziel ist, haben wir einen Weg gefunden.
        if current == goal:
            return path

        # Untersuche alle Nachbarn des aktuellen Knotens.
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)

                # Erzeuge den neuen Pfad für den Nachbarn anhand des aktuellen Pfads.
                queue.append((neighbor, path + [neighbor]))

    # Wenn die Queue leer ist und kein Ziel gefunden wurde, gibt es keinen Pfad.
    return None


# ------------------------------------------------
# 4. Karte laden
# ------------------------------------------------
def load_map():
    """Lade das Bild des Grundrisses aus dem aktuellen Verzeichnis."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(base_dir, "Grundriss_mit_Knotenpunkten.png")
    try:
        return plt.imread(image_path)
    except FileNotFoundError:
        print("Fehler: Kartenbild nicht gefunden.")
        raise SystemExit(1)


# ------------------------------------------------
# 5. Pfad zeichnen
# ------------------------------------------------
def draw_path(map_image, path: list[str], point_coordinates: dict[str, tuple[int, int]]):
    """Zeichne den gefundenen Weg auf die Karte."""
    if not path or len(path) < 2:
        return

    coords = []
    for point in path:
        # Nur Punkte berücksichtigen, die auch Koordinaten haben.
        if point in point_coordinates:
            coords.append(point_coordinates[point])

    if len(coords) < 2:
        return

    xs = [x for x, _ in coords]
    ys = [y for _, y in coords]

    plt.figure(figsize=(10, 8))
    plt.imshow(map_image)
    plt.plot(xs, ys, color="red", linewidth=2.5)
    plt.scatter(xs, ys, color="red", zorder=3)
    plt.axis("off")
    plt.show()


# ------------------------------------------------
# 6. Hauptprogramm
# ------------------------------------------------
def main():
    user_input = input("Geben Sie bitte den Zielpunkt ein (ost_1, ost_2, nord_1, nord_2, nord_west_1, west_1, west_2, sued_west):__ ")

    # Lade den Hintergrundplan als Bild.
    map_image = load_map()

    # Graph bauen
    graph = build_graph(connections)

    # Nutzer-Eingabe nehmen
    target = user_input.strip()

    if target not in checkpoints:
        print(f"Fehler: '{target}' ist kein gültiger Zielpunkt.")
        raise SystemExit(1)

    # Pfad finden
    path = find_path(graph, "startpunkt", target)

    # Kombiniere die Koordinaten aller bekannten Punkte in ein Dictionary.
    point_coordinates = {**nodes, **checkpoints, "startpunkt": start_point}

    print(f"Pfad: {path}")

    if path is None:
        print("Kein Pfad gefunden.")
        return

    # Zeichne den Pfad auf die geladene Karte.
    draw_path(map_image, path, point_coordinates)


if __name__ == "__main__":
    main()


