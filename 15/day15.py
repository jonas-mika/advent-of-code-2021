from sys import stdin
from itu.algs4.fundamentals.stack import Stack
from itu.algs4.sorting.index_min_pq import IndexMinPQ
from itu.algs4.graphs.edge_weighted_digraph import EdgeWeightedDigraph
import math
import numpy as np

m = [[int(x) for x in line.strip()] for line in stdin.readlines()]

#xs, ys = len(m[0]), len(m)

XS, YS = len(m[0]), len(m)
m2 = [[0 for _ in range(XS*5)] for _ in range(YS*5)]

for y in range(YS * 5):
    for x in range(XS * 5):
        # copy original map
        if y < YS and x < XS:
            m2[y][x] = m[y][x]
        # build top tile row
        elif y < YS:
            m2[y][x] = m2[y][x-XS]+1 if m2[y][x-XS] < 9 else 1
        # copy from upper tile
        else:
            m2[y][x] = m2[y-YS][x]+1 if m2[y-YS][x] < 9 else 1

class DirectedEdge:
    def __init__(self, u, v, weight=1):
        self._u = u
        self._v = v
        self._weight = weight

    def from_vertex(self):
        return self._u

    def to_vertex(self):
        return self._v

    def weight(self):
        return self._weight

    def __lt__(self, other):
        if self.weight() < other.weight():
            return True
        return False

    def __repr__(self):
        return f"{self._u}->{self._v} {float(self._weight)}"


class DijkstraSP:
    def __init__(self, G, s=0):
        for e in G.edges():
            if e.weight() < 0:
                raise ValueError("edge {} has negative weight".format(e))
        self._dist_to = [math.inf] * G.V()
        self._edge_to = [None] * G.V()

        # initialise source distance to 0 by convention
        self._dist_to[s] = 0.0

        # initialising index min pq to keep track of vertices that are candidates for being relaxed next
        self._pq = IndexMinPQ(G.V())
        self._pq.insert(s, 0.0)

        # iterate until all vertices possibly reachable are reached
        while not self._pq.is_empty():
            v = self._pq.del_min()
            for e in G.adj(v):
                self._relax(e)

    def dist_to(self, v):
        return self._dist_to[v]

    def has_path_to(self, v):
        return self._dist_to[v] < float("inf")

    def path_to(self, v):
        if not self.has_path_to(v):
            return None
        path = Stack()
        e = self._edge_to[v]
        while e is not None:
            path.push(e)
            e = self._edge_to[e.from_vertex()]
        return path

    def _relax(self, e):
        v = e.from_vertex()
        w = e.to_vertex()
        if self._dist_to[w] > self._dist_to[v] + e.weight():
            self._dist_to[w] = self._dist_to[v] + e.weight()
            self._edge_to[w] = e
            if self._pq.contains(w):
                self._pq.decrease_key(w, self._dist_to[w])
            else:
                self._pq.insert(w, self._dist_to[w])

def neighbors(x, y, xs, ys):
    ns = []
    if y>0:
        ns.append((x,y-1))
    if y<ys-1:
        ns.append((x,y+1))
    if x>0:
        ns.append((x-1,y))
    if x<xs-1:
        ns.append((x+1,y))
    return ns

def coord_to_id(x, y, xs):
    return y * xs + x

def create_graph(m):
    xs, ys = len(m[0]), len(m)
    nn = xs*ys

    G = EdgeWeightedDigraph(nn)

    for y in range(ys):
        for x in range(xs):
            u = coord_to_id(x,y, xs)
            for n in neighbors(x, y, xs, ys):
                w = coord_to_id(n[0], n[1], xs)
                G.add_edge(DirectedEdge(u, w, m[n[1]][n[0]]))
    return G


def main():
    G = create_graph(m)
    G2 = create_graph(m2)
    
    spt = DijkstraSP(G, s=0)
    spt2 = DijkstraSP(G2, s=0)

    print(f'Part 1: {int(spt.dist_to(G.V()-1))}')
    print(f'Part 2: {int(spt2.dist_to(G2.V()-1))}')

if __name__ == '__main__':
    main()
