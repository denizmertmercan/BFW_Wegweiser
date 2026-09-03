
import os
import matplotlib.pyplot as plt
from collections import deque

start_point = (675, 400)

nodes = {
    
    "knoten_1": (680, 318),#nach osten oder knoten_2
    "knoten_2": (556, 314),#nach norden oder westen
    "knoten_3": (624, 185),#nord_1 oder nord_2
    "knoten_4": (327, 349)#nach nord_west,west oder sued_west
}

checkpoints = {
    
    "ost_1": (769, 330),
    "ost_2": (880, 340),
    
    "nord_1": (511, 185),
    "nord_2": (777, 176),

    "nord_west_1": (163, 82),

    "west_1": (165, 349),
    "west_2": (96, 394),

    "sued_west": (255, 485)

}

connections = {
    
    "connection1": ["startpunkt", "knoten_1"],

    "connection2": ["knoten_1", "ost_1"],
    "connection3": ["ost_1", "ost_2"],

    "connection4": ["knoten_1", "knoten_2"],
    "connection5": ["knoten_2", "knoten_3"],
    "connection6": ["knoten_3", "nord_1"],
    "connection7": ["knoten_3", "nord_2"],

    "connection8": ["knoten_2", "knoten_4"],
    "connection9": ["knoten_4", "nord_west_1"],
    "connection10": ["knoten_4", "west_1"],
    "connection11": ["knoten_4", "sued_west"],

    "connection12": ["west_1", "west_2"]

}

# 1. Baue aus connections eine Adjazenzliste
def build_graph(connections: dict[str, list[str]]):
    graph = {}
    for connection in connections.values():
        point_a = connection[0]
        point_b = connection[1]
        
        # Beide Richtungen hinzufügen (weil Wege bidirektional sind)
        if point_a not in graph:
            graph[point_a] = []
        if point_b not in graph:
            graph[point_b] = []
        
        graph[point_a].append(point_b)
        graph[point_b].append(point_a)
        

    
    return graph
    
# 2. Suche den Pfad (BFS = Breitensuche)
def find_path(graph: dict[str, list[str]], start: str, goal: str):
    visited = set()
    queue = deque([(start, [start])])
    visited.add(start)
    
    while queue:
        current, path = queue.popleft()
        
        if current == goal:
            return path
        
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return None  # Kein Pfad gefunden


def main():
    user_input = input("Geben Sie bitte den Zielpunkt ein (ost_1, ost_2, nord_1, nord_2, nord_west_1, west_1, west_2, sued_west):__ ")

    script_dir = os.path.dirname(os.path.abspath(__file__))
    try:
        map_image = plt.imread(os.path.join(script_dir, "Grundriss_mit_Knotenpunkten.png"))
    except FileNotFoundError:
        print("Fehler: Kartenbild nicht gefunden.")
        raise SystemExit(1)

    plt.imshow(map_image)
    plt.axis("off")
    plt.show()

    # Graph bauen
    graph = build_graph(connections)

    # Nutzer-Eingabe nehmen
    target = user_input.strip()

    if target not in checkpoints:
        print(f"Fehler: '{target}' ist kein gültiger Zielpunkt.")
        raise SystemExit(1)

    # Pfad finden
    path = find_path(graph, "startpunkt", target)

    print(f"Pfad: {path}")


if __name__ == "__main__":
    main()


