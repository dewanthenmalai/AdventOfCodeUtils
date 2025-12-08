import math
import itertools
from scipy.cluster.hierarchy import DisjointSet

class Edge_3D:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.length = math.sqrt((v1.x-v2.x)**2 + (v1.y-v2.y)**2 + (v1.z-v2.z)**2)

class Vertex_3D:
    def __init__(self,v):
        self.x = v[0]
        self.y = v[1]
        self.z = v[2]

def get_edges_3d(vertices):
    edges = []
    for v1,v2 in itertools.combinations(vertices,2):
        edges.append(Edge_3D(v1,v2))
    return edges

def modified_kruskal_3d(vertex_list, iterations):
    vertices = [Vertex_3D([int(i) for i in l.split(",")]) for l in vertex_list]
    edges = get_edges_3d(vertices)
    forest = DisjointSet(vertices)
    for i in range(iterations):
        edge = min(edges, key=lambda e: e.length)
        edges.remove(edge)
        forest.merge(edge.v1, edge.v2)
    return forest

def last_edge_kruskal_3d(vertex_list):
    vertices = [Vertex_3D([int(i) for i in l.split(",")]) for l in vertex_list]
    edges = get_edges_3d(vertices)
    forest = DisjointSet(vertices)
    last_edge = None
    edge_set = set()
    for edge in sorted(edges,key=lambda e: e.length):
        if not forest.connected(edge.v1, edge.v2):
            edge_set |= {edge}
            last_edge = edge
            forest.merge(edge.v1, edge.v2)
    return last_edge


def kruskal_3d(vertex_list):
    vertices = [Vertex_3D([int(i) for i in l.split(",")]) for l in vertex_list]
    edges = get_edges_3d(vertices)
    forest = DisjointSet(vertices)
    edge_set = set()
    for edge in sorted(edges,key=lambda e: e.length):
        if not forest.connected(edge.v1, edge.v2):
            edge_set |= {edge}
            forest.merge(edge.v1, edge.v2)
    return edge_set
