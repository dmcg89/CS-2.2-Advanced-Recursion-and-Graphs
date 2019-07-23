from graph import Vertex, Graph
# from queue import Queue

# class Vert(Vertex):
#     def __init__(self, vertex, visited = False, distance = 9999):
#         Vertex.__init__(self, vertex)
#         self.visited = visited
#         self.distance = distance
#         self.path = []


def bfs(graph, from_vertex, to_vertex):
    queue = []
    source = graph.get_vertex(from_vertex)
    source.distance = 0
    source.path.append(source.id)
    queue.append(source.id)
    for neighbor in source.neighbors:
        queue.append(neighbor.id)
    while queue:
        u = queue.pop(0)
        vert_u = graph.get_vertex(u)
        vert_u.visited = True
        print(queue)
        for vert_v in vert_u.neighbors:
            if vert_v.visited == False:
                queue.append(vert_v.id)
                if vert_v.distance > vert_u.distance + 1:
                    vert_v.distance = vert_u.distance + 1
                    vert_u.path.append(vert_v.id)

    # while queue:
    #     source = queue.pop(0)
    #     source.visited = True
g = Graph()

# Add your friends
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_vertex(5)
g.add_vertex(6)
g.add_vertex(7)

g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(1, 4)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 7)
# print(bfs(g, 1, 4))
bfs(g, 1, 4)
curr_vert = g.get_vertex(1)
print('path')
print(curr_vert.path)
print('here')
# for key in g.vert_dict:
#     curr_vert = g.get_vertex(key)
#     print(curr_vert.distance)
# if __name__ == "__main__":
    
#     # Challenge 1: Create the graph

#     g = Graph()

#     # Add your friends
#     g.add_vertex(1)
#     g.add_vertex(2)
#     g.add_vertex(3)
#     g.add_vertex(4)
#     # g.add_vertex("Friend 5")
#     # g.add_vertex("Friend 6")
#     # g.add_vertex("Friend 7")
#     # g.add_vertex("Friend 8")
#     # g.add_vertex("Friend 9")
#     # g.add_vertex("Friend 10")

#     # ...  add all 10 including you ...

#     # Add connections (non weighted edges for now)
#     g.add_edge(1, 2)
#     g.add_edge(2, 3)
#     g.add_edge(3, 4)
#     # g.add_edge("Friend 4", "Friend 5")
#     # g.add_edge("Friend 5", "Friend 6")
#     # g.add_edge("Friend 7", "Friend 8")
#     # g.add_edge("Friend 8", "Friend 9")
#     # g.add_edge("Friend 9", "Friend 10")

#     # Challenge 1: Output the vertices & edges
#     # Print vertices
#     print(bfs(g, 1, 4))
#     print("The vertices are: ", g.get_vertices(), "\n")

#     print("The edges are: ")
#     for v in g:
#         for w in v.get_neighbors():
#             print("( %s , %s )" % (v.get_id(), w.get_id()))
