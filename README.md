# PyGremlin

This is a project to create a graph library similar to (but not nearly as
powerful as) the [Gremlin](https://github.com/tinkerpop/gremlin/) project.

~~One aspect of the library I am experimenting with is not having a central
`Graph` class, and just using `Vertex`s and `Edge`s.  The reason behind this is that,
it is my understanding that a graph doesn't really have a 'beginning' or an
'end' like a lot of datastructures do (like lists), so potentially any node
in the graph could be a starting point for traversal algorithms.  I am still
researching this, but at this point I don't see a lot of point to having a
`Graph` class, it seems like it would just be a wrapper around 2 lists: a
list of all the `Vertex`s,and a list of all the `Edge`s.~~

To be semi-compatible with the Gremlin way of things, I am going to
include a `Graph` class. For now, it will probably remain optional, and
will probably be nothing more than a wrapper around a `Vertex` list and
an `Edge` list. My thinking is that eventually I am going to want to be
able to import and export GraphML graphs, and having a central `Graph`
class to do that in will probably be the most convenient.

Right now, the API does not includes Gremlin's nifty ``optional'' parenthesis.
I would like to say it was because Python doesn't support that, but really I just don't
have the necessary Python chops to pull this off right now.

So, for now, the API would look something like this:

    >>> myobj = {'name': 'Fred'}
    >>> myobj2 = {'name': 'Sally'}
    >>> myobj3 = {'name': 'Bob'}
    >>> # setting up the graph
    >>> 
    >>> t = Vertex(myobj)
    >>> u = Vertex(myobj2)
    >>> v = Vertex(myobj3)
    >>> 
    >>> e = t >> u
    >>> 
    >>> t.outE().inV().name
    {'Bob'}

