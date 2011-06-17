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
        self.assertTrue(ishex(v.id))

    def testVertexEdgeTo(self):
        """Connect 2 Vertices with an edge"""
        u = Vertex()
        v = Vertex()

        e = u.edgeto(v)

        self.assertIsInstance(e, Edge)

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

    def testVertexEdgeFromWithWeight(self):
        """Connect 2 Vertices with an edge, and give the edge a weight"""
        u = Vertex()
        v = Vertex()

        e = u.edgefrom(v, weight=5)

        self.assertEqual(e.weight, 5)

