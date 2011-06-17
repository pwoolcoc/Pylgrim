import string

from nose.tools import *
from unittest import TestCase

from graph.graph import Vertex

def ishex(s):
    return all(c in string.hexdigits for c in s)

class GraphTests(TestCase):
    def testVertexUUID(self):
        """Every vertex should get created with a uuid4().hex"""
        v = Vertex()
        self.assertTrue(ishex(v.id))

