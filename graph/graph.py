import copy
import uuid

class Element(object):
    def __init__(self, *args, **kwds):
        self.__initial_properties__ = copy.deepcopy(self.__dict__)

class Vertex(Element):
    def __init__(self, obj=None, *args, **kwds):
        self.id = uuid.uuid4().hex
        self.obj = obj
        super(Vertex, self).__init__(*args, **kwds)

    def edgeto(self, to, weight=None):
        return Edge(from_=self, to=to, weight=weight)

    def edgefrom(self, from_, weight=None):
        return Edge(from_=from_, to=self, weight=weight)

    def __rshift__(self, to):
        return self.edgeto(to)

    def __lshift__(self, from_):
        return self.edgefrom(from_)

class Edge(Element):
    def __init__(self, from_, to, weight=None, *args, **kwds):
        self.from_ = from_
        self.to = to
        self.weight = weight
        super(Edge, self).__init__(*args, **kwds)

