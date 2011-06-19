import copy
import uuid

class Element(object):
    def __init__(self, *args, **kwds):
        self.__initial_properties__ = copy.deepcopy(self.__dict__)

class Vertex(Element):
    def __init__(self, obj=None, *args, **kwds):
        self.uuid = uuid.uuid4().hex
        self.obj = obj
        self._out = []
        self._outE = []
        self._in_ = []
        self._inE = []
        super(Vertex, self).__init__(*args, **kwds)

    def edgeto(self, to, weight=None):
        """
        Defines a relationship between two vertices.

        This is functionally equivalent to edgefrom, with the vertex instances
        reversed.  So:

        >>> e = u.edgeto(v)

        is equivalent to

        >>> e = v.edgefrom(u)
        """
        e = Edge(from_=self, to=to, weight=weight)

        # Bookkeeping
        self._out.append(to)
        self._outE.append(e)

        to._in_.append(self)
        to._inE.append(e)

        e._inV.append(to)
        e._outV.append(self)

        return e

    def edgefrom(self, from_, weight=None):
        """
        Defines a relationship between two vertices.

        Defines the reverse relationship that `edgeto` does
        """
        e = Edge(from_=from_, to=self, weight=weight)

        # Bookkeeping
        self._in_.append(from_)
        self._inE.append(e)

        from_._out.append(self)
        from_._outE.append(e)

        e._inV.append(self)
        e._outV.append(from_)

        return e

    def __rshift__(self, to):
        return self.edgeto(to)

    def __lshift__(self, from_):
        return self.edgefrom(from_)

    def out(self):
        return self._out
    def outE(self):
        return self._outE
    def in_(self):
        return self._in_
    def inE(self):
        return self._inE
    def both(self):
        return self._out + self._in_
    def bothE(self):
        return self._outE + self._inE

class Edge(Element):
    def __init__(self, from_, to, weight=None, *args, **kwds):
        self.from_ = from_
        self.to = to
        self.weight = weight
        self._inV = []
        self._outV = []
        super(Edge, self).__init__(*args, **kwds)

    def inV(self):
        return self._inV
    def outV(self):
        return self._outV


