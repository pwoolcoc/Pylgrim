import uuid

class Vertex(object):
    def __init__(self, *args, **kwds):
        self.id = uuid.uuid4().hex

    def edgeto(self, to, weight=None):
        return Edge(from_=self, to=to, weight=weight)

    def edgefrom(self, from_, weight=None):
        return Edge(from_=from_, to=self, weight=weight)

    def __rshift__(self, to):
        return self.edgeto(to)

    def __lshift__(self, from_):
        return self.edgefrom(from_)

class Edge(object):
    def __init__(self, from_, to, weight=None, *args, **kwds):
        self.from_ = from_
        self.to = to
        self.weight = weight

