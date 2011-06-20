import string

from nose.tools import *
from unittest import TestCase

from graph.graph import Edge, Vertex

def ishex(s):
    return all(c in string.hexdigits for c in s)

class GraphTests(TestCase):
    def testVertexUUID(self):
        """Every vertex should get created with a uuid4().hex"""
        v = Vertex()
        self.assertTrue(ishex(v.uuid))

    def testVertexInitWithProperties(self):
        """
        Set initial properties for the vertex. These are application-specific,
        not tied to any of our implementation details
        """
        t = Vertex(name="my name is t")

        self.assertEqual(t.name, "my name is t")

    def testVertexCantOverwriteOurProperties(self):
        """
        We want to make sure the user can't set a property on an Edge or Vertex
        that would overwrite something we need"""
        with self.assertRaises(AttributeError):
            Vertex(uuid="if this gets set, baaad!")


    def testVertexEdgeTo(self):
        """Connect 2 Vertices with an edge"""
        u = Vertex()
        v = Vertex()

        e = u.edgeto(v)

        self.assertIsInstance(e, Edge)
        self.assertEqual(e.from_, u)
        self.assertEqual(e.to, v)

    def testVertexEdgeToWithWeight(self):
        """Connect 2 Vertices with an edge, and give the edge a weight"""
        u = Vertex()
        v = Vertex()

        e = u.edgeto(v, weight=5)

        self.assertEqual(e.weight, 5)

    def testVertexEdgeFrom(self):
        """Connect 2 Vertices with an edge"""
        u = Vertex()
        v = Vertex()

        e = u.edgefrom(v)

        self.assertIsInstance(e, Edge)
        self.assertEqual(e.from_, v)
        self.assertEqual(e.to, u)

    def testVertexEdgeFromWithWeight(self):
        """Connect 2 Vertices with an edge, and give the edge a weight"""
        u = Vertex()
        v = Vertex()

        e = u.edgefrom(v, weight=5)

        self.assertEqual(e.weight, 5)

    def testVertexToShorthand(self):
        """
        Shorthand for connecting 2 vertices. Cannot easily specify edge weight
        """
        u = Vertex()
        v = Vertex()

        e = u >> v

        self.assertIsInstance(e, Edge)
        self.assertEqual(e.from_, u)
        self.assertEqual(e.to, v)

    def testVertexFromShorthand(self):
        """
        Shorthand for connecting 2 vertices. Cannot easily specify edge weight
        """
        u = Vertex()
        v = Vertex()

        e = u << v

        self.assertIsInstance(e, Edge)
        self.assertEqual(e.from_, v)
        self.assertEqual(e.to, u)

    # Abandoning this for now, til I get a better idea of how I'm going to do
    # this
    #def testVertexMultipleShorthandAssignments(self):
        #"""
        #Shorthand for joining unlimited nodes. Should return tuple of edges
        #"""
        #t = Vertex()
        #u = Vertex()
        #v = Vertex()

        #e1, e2 = t >> u << v

        #self.assertIsInstance(e1, Edge)
        #self.assertEqual(e1.outV(), [t])
        #self.assertEqual(e1.inV(), [u])
        #self.assertIsInstance(e2, Edge)
        #self.assertEqual(e2.outV(), [v])
        #self.assertEqual(e2.inV(), [u])

    def testVertexOut(self):
        """
        Vertex().out() should ret a list of the vertices that are 'out' from it
        """
        u = Vertex()
        v = Vertex()

        e = u >> v

        self.assertEqual(u.out(), [v])

    def testVertexOutE(self):
        """
        Vertex().outE() should ret a list of the edges that go 'out' from it
        """
        u = Vertex()
        v = Vertex()

        e = u >> v

        self.assertEqual(u.outE(), [e])


    def testVertexIn(self):
        """
        Vertex().in() should ret a list of the vertices that come 'in' to it
        """
        u = Vertex()
        v = Vertex()
        e = u >> v

        self.assertEqual(v.in_(), [u])

    def testVertexInE(self):
        """
        Vertex().inE() should ret a list of the edges that come 'in' to it
        """
        u = Vertex()
        v = Vertex()

        e = u >> v

        self.assertEqual(v.inE(), [e])

    def testVertexBoth(self):
        """
        Vertex().both() should ret a list of all adjacent vertices
        """
        t = Vertex()
        u = Vertex()
        v = Vertex()

        e1 = t >> u
        e2 = u >> v

        self.assertEqual(u.both(), [v, t])


    def testVertexBothE(self):
        """
        Vertex().bothE() should ret a list of all 'connected' edges
        """
        t = Vertex()
        u = Vertex()
        v = Vertex()

        e1 = t >> u
        e2 = u >> v
        self.assertEqual(u.bothE(), [e2, e1])


    def testEdgeInV(self):
        """
        Edge().inV() should ret a list of the vertices that the edge goes into
        """
        t = Vertex()
        u = Vertex()
        e = t >> u
        self.assertEqual(e.inV(), [u])


    def testEdgeOutV(self):
        """
        Edge().outV() should ret a list of the vertices the edge goes out of
        """
        t = Vertex()
        u = Vertex()
        e = t >> u
        self.assertEqual(e.outV(), [t])

    def testChainingSelectors(self):
        """Chain {in,out}{_,E,V} calls together"""
        t = Vertex()
        u = Vertex()
        e = t >> u

        # >>> t.outE()
        # [e]
        # >>> e.inV()
        # [u]
        should_be_u = t.outE().inV()

        self.assertEqual(should_be_u, [u])


    def testChainingSelectorsWithAttributeAccess(self):
        """
        Chain selectors together and request an attribute at the end of the chain
        """
        t = Vertex()
        u = Vertex()
        u.name = "I am U"

        e = t >> u

        should_be_i_am_u = t.outE().inV().name
        self.assertEqual(should_be_i_am_u, ["I am U"])

    def testChainingSelectorsWithAttributeMultiple(self):
        """
        Chain selectors together, and get a list of attributes
        """
        t = Vertex()
        u = Vertex()
        v = Vertex()
        t.name = "_t"
        u.name = "_u"
        v.name = "_v"

        e1 = t >> v
        e2 = u >> v

        result = t.out().in_().name
        self.assertEqual(result, ["_t", "_u"])

    def testSelectorWithFilter(self):
        """
        Selectors take optional keyword arguments as filters
        """
        t = Vertex(name="_t", value=1)
        u = Vertex(name="_u", value=3)
        v = Vertex(name="_v", value=5)

        e1 = t >> u
        e2 = t >> v

        result = t.out(value=5)
        self.assertEqual(result, [v])


