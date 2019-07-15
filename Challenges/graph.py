#!python

""" Vertex Class
A helper class for the Graph class that defines vertices and vertex neighbors.
"""


class Vertex(object):

    def __init__(self, vertex):
        """initialize a vertex and its neighbors

        neighbors: set of vertices adjacent to self,
        stored in a dictionary with key = vertex,
        value = weight of edge between self and neighbor.
        """
        self.id = vertex
        self.neighbors = {}

    def add_neighbor(self, vertex, weight=0):
        """add a neighbor along a weighted edge"""
        #  check if vertex is already a neighbor
        if vertex in self.neighbors:
            raise ValueError('Item exists in neighbor: {}'.format(vertex))
        #  if not, add vertex to neighbors and assign weight.
        else:
            self.neighbors[vertex] = weight
            # return self.neighbors


    def __str__(self):
        """output the list of neighbors of this vertex"""
        return str(self.id) + " adjancent to " + str([x.id for x in self.neighbors])

    def get_neighbors(self):
        """return the neighbors of this vertex"""
        #  return the neighbors
        return self.neighbors.keys()

    def get_id(self):
        """return the id of this vertex"""
        return self.id

    def get_edge_weight(self, vertex):
        """return the weight of this edge"""
        #  return the weight of the edge from this vertex to the given vertex.
        return self.neighbors.values()


""" Graph Class
A class demonstrating the essential
facts and functionalities of graphs.
"""


class Graph:
    def __init__(self):
        """ initializes a graph object with an empty dictionary.
        """
        self.vert_dict = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        """add a new vertex object to the graph with
        the given key and return the vertex
        """
        #  increment the number of vertices
        self.num_vertices += 1
        #  create a new vertex
        new_vertex = Vertex(key)
        #  add the new vertex to the vertex list
        self.vert_dict[key] = new_vertex
        #  return the new vertex
        # return self

    def get_vertex(self, key):
        """return the vertex if it exists"""
        #  return the vertex if it is in the graph
        if key in self.vert_dict:
            return key
        raise ValueError('Vertex not found: {}'.format(key))

    def add_edge(self, key1, key2, cost=0):
        """add an edge from vertex f to vertex t with a cost
        """
        # if either vertex is not in the graph,
        # add it - or return an error (choice is up to you).
        if key1 not in self.vert_dict or key2 not in self.vert_dict:
            raise ValueError('One of the vertices not in graph')
            # if both vertices in the graph, add the
            # edge by making t a neighbor of f
        else:
            # and using the addNeighbor method of the Vertex class.
            # Hint: the vertex f is stored in self.vertList[f].
            self.vert_dict[key1].add_neighbor(self.vert_dict[key2])


    def get_vertices(self):
        """return all the vertices in the graph"""
        return self.vert_dict.keys()

    def __iter__(self):
        """iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.vert_dict.values())


# Driver code


