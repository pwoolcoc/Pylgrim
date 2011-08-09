
import pylgrim.graphml
from pylgrim.element import Edge, ElementList, Vertex

class Graph(object):
    def __init__(self):
        self._V = ElementList()
        self._E = ElementList()

    @property
    def V(self):
        return _V

    @property
    def E(self):
        return _E

    def v(self, idx, **kwds):
        return _V[idx]

    def e(self, idx, **kwds):
        return _E[idx]

    def addvertex(self, obj=None, label=None, *args, **kwds):
        v = Vertex(obj, label, *args, **kwds)
        self._V.append(v)
        v.idx(len(self._V) - 1)
        return v

    def addedge(self, from_, to, weight=None, label=None, *args, **kwds):
        e = from_.edgeto(to, weight=weight, label=label)
        self._E.append(e)
        e.idx(len(self._E) - 1)
        return e

    @staticmethod
    def loadgraphml(self, file_):
        v, e = graphml.parse(file_)
        g = Graph(v, e)

    def savegraphml(self):
        return graphml.save(self)

