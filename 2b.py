from queue import PriorityQueue

# Graph representation
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# Heuristic values
heuristic = {
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 7,
    'E': 3,
    'F': 6,
    'G': 0
}

def best_first_search(start, goal):
    visited = set()
    pq = PriorityQueue()

    pq.put((heuristic[start], start))

    while not pq.empty():
        h, node = pq.get()

        if node in visited:
            continue

        print(node, end=" ")
        visited.add(node)

        if node == goal:
            print("\nGoal Reached!")
            return

        for neighbor in graph[node]:
            if neighbor not in visited:
                pq.put((heuristic[neighbor], neighbor))

    print("\nGoal Not Found!")

# Driver Code
start_node = 'A'
goal_node = 'G'

print("Best First Search Traversal:")
best_first_search(start_node, goal_node)
