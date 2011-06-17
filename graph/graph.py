import uuid

class Vertex(object):
    def __init__(self, *args, **kwds):
        self.id = uuid.uuid4().hex

