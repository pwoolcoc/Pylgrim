import copy
import itertools
import uuid

from itertools import chain

class ElementList(list):
    """
    ElementList is just a thin wrapper around the builtin `list` class. It's
    only purpose is to forward function calls to it's members.  That way, my
    `Vertex` and `Edge` classes can receive the traversal selectors when they
    are chained together.

    Let's say we have this graph:

    +---+   e1    +---+   e2    +---+
    | n | - - - > | o | - - - > | p |
    +---+         +---+         +---+
                    |
                    |    e3     +---+
                    + - - - - > | q |
                                +---+

    If we call this:

        >>> n.outE()
        ElementList(e1)

    So chaining calls together like this:

        >>> n.outE().inV()

    We would actually be like doing this:

        >>> f = n.outE()
        >>> f.inV()        # where f is an instance of ElementList, not Edge...

    Since this won't work, I make ElementList call the missing function on all
    it's members, consolidating the results into one single (new) ElementList.
    So,

        >>> o.outE()   # ==> ElementList(e2, e3)
        >>> # and
        >>> o.outE().inV()  # ==> ElementList(p, q)

    Because in this case, both e2.inV() and e3.inV() get called, and the
    results get put into one single ElementList.

    (Note that calling Vertex().outE().inV() is functionally the same as
    calling Vertex().out(). The latter should be used for efficiency, but the
    is used here for examples so we only have to construct graphs consisting of
    a few nodes.
    """
    def __getattr__(self, name):
        _callable = all([
                callable(getattr(x, name))
                for x in self
                if hasattr(x, name)
                ])

        # if the attribute is callable, create and return the function.
        # if not, collect the attributes into a list and return it

        if _callable:
            def callme(*args, **kwds):
                r = [
                        getattr(x, name)(*args, **kwds)
                        for x in self
                        if hasattr(x, name)]

                return ElementList( chain.from_iterable(r) )
            return callme
        else:
            r = [getattr(x, name) for x in self if hasattr(x, name)]
            return ElementList(r)

class Element(object):
    def __init__(self, *args, **kwds):
        for k, v in kwds.items():
            if not hasattr(self, k):
                setattr(self, k, v)
            else:
                raise AttributeError(
                        "You cannot overrite {0} on {1}".format(k, self))

    def matches(self, _list, **kwds):
        results = [
                elem
                for (elem, key) in itertools.product(_list, kwds)
                if getattr(elem, key) == kwds.get(key)]

        return ElementList(results)

class Vertex(Element):
    def __init__(self, obj=None, *args, **kwds):
        self.uuid = uuid.uuid4().hex
        self.obj = obj
        self._out = ElementList()
        self._outE = ElementList()
        self._in_ = ElementList()
        self._inE = ElementList()
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

    def out(self, **kwds):
        if kwds:
            return self.matches(self._out, **kwds)
        return self._out

    def outE(self, **kwds):
        if kwds:
            return []
        return self._outE
    def in_(self, **kwds):
        if kwds:
            return []
        return self._in_
    def inE(self, **kwds):
        if kwds:
            return []
        return self._inE
    def both(self, **kwds):
        if kwds:
            return []
        return self._out + self._in_
    def bothE(self, **kwds):
        if kwds:
            return []
        return self._outE + self._inE

class Edge(Element):
    def __init__(self, from_, to, weight=None, *args, **kwds):
        self.from_ = from_
        self.to = to
        self.weight = weight
        self._inV = ElementList()
        self._outV = ElementList()
        super(Edge, self).__init__(*args, **kwds)

    def inV(self, **kwds):
        return self._inV
    def outV(self, **kwds):
        return self._outV


