from heapq import heappush, heappop

def a_star(graph, start, goal, heuristic):
    open_set = []
    heappush(open_set, (0, start))

    g_cost = {start: 0}
    parent = {start: None}

    while open_set:
        current_f, current = heappop(open_set)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]

        for neighbor, cost in graph[current]:
            new_g = g_cost[current] + cost

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                f_cost = new_g + heuristic[neighbor]
                heappush(open_set, (f_cost, neighbor))
                parent[neighbor] = current

    return None

# Graph representation
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 1)],
    'E': [('G', 2)],
    'F': [('G', 1)],
    'G': []
}

# Heuristic values
heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 1,
    'G': 0
}

start = 'A'
goal = 'G'

path = a_star(graph, start, goal, heuristic)

print("Shortest Path:", path)
