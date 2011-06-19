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

