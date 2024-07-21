import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


### ЗАВДАННЯ 1 ###


# Створення графу
G = nx.Graph()

# Додавання вершин та ребер
G.add_edge('Аліса', 'Микола', weight=4)
G.add_edge('Микола', 'Олег', weight=2)
G.add_edge('Олег', 'Богдан', weight=5)
G.add_edge('Богдан', 'Юля', weight=1)
G.add_edge('Юля', 'Аліса', weight=3)
G.add_edge('Аліса', 'Олег', weight=6)
G.add_edge('Микола', 'Юля', weight=7)

# Візуалізація графу
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold', edge_color='gray')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title('Соціальна мережа')
plt.show()

# Аналіз основних характеристик
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = dict(G.degree())

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print(f"Ступені вершин: {degrees}")



### ЗАВДАННЯ 2 ###

def dfs_recursive(graph, vertex, visited=None):
  if visited is None:
    visited = set()
  visited.add(vertex)
  print(vertex, end=' ')
  for neighbor in graph[vertex]:
    if neighbor not in visited:
      dfs_recursive(graph, neighbor, visited)

dfs_path = dfs_recursive(G, 'Микола')
print(f"{dfs_path}")

def bfs_recursive(graph, queue, visited=None):
  if visited is None:
    visited = set()
  if not queue:
    return
  vertex = queue.popleft()
  if vertex not in visited:
    print(vertex, end=" ")
    visited.add(vertex)
    queue.extend(set(graph[vertex]) - visited)
  bfs_recursive(graph, queue, visited)

bfs_path = bfs_recursive(G, deque(['Микола']))
print(f"{bfs_path}")

"""
Пояснення результатів:

-- DFS (Depth-First Search): 
Алгоритм DFS досліджує граф углиб, тобто намагається пройти якомога глибше в графі, 
перш ніж повертатися і досліджувати інші гілки. 
Це може призвести до знаходження довших шляхів, оскільки DFS не обов'язково знаходить найкоротший шлях.

-- BFS (Breadth-First Search):
Алгоритм BFS досліджує граф ушир, тобто досліджує всі сусідні вершини на поточному рівні, 
перш ніж переходити до наступного рівня. 
Це гарантує знаходження найкоротшого шляху в незваженому графі.

"""


### ЗАВДАННЯ 3 ###

def dijkstra_shortest_path(graph, start, end):
  try:
    path = nx.shortest_path(graph, source=start, target=end, weight='weight')
    length = nx.shortest_path_length(graph, source=start, target=end, weight='weight')
    return path, length
  except nx.NetworkXNoPath:
    return None, float('inf')

# Знаходження найкоротших шляхів між всіма парами вершин
for start_node in G.nodes():
  for end_node in G.nodes():
    if start_node != end_node:
      path, length = dijkstra_shortest_path(G, start_node, end_node)
      print(f"Найкоротший шлях від {start_node} до {end_node}: {path} з довжиною {length}")