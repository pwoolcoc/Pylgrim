# PyGremlin

This is a project to create a graph library similar to (but not nearly as
powerful as) the [Gremlin](https://github.com/tinkerpop/gremlin/) project.

To be semi-compatible with the Gremlin way of things, I am going to
include a `Graph` class. For now, it will probably remain optional, and
will probably be nothing more than a wrapper around a `Vertex` list and
an `Edge` list. My thinking is that eventually I am going to want to be
able to import and export GraphML graphs, and having a central `Graph`
class to do that in will probably be the most convenient.

~~Right now, the API does not includes Gremlin's nifty ``optional'' parenthesis.
I would like to say it was because Python doesn't support that, but really I just don't
have the necessary Python chops to pull this off right now.~~

So, for now, the API would look something like this:

    >>> # instantiate some vertices
    >>> 
    >>> t = Vertex(name="Fred")
    >>> u = Vertex(name="Bob")
    >>> 
    >>> # set a relationship between some vertices
    >>> e = t >> u
    >>> 
    >>> # query the graph
    >>> t.outE().inV().name
    {'Bob'}
    >>> 
    >>> # this query could also be made like this:
    >>> t.out().name
    {'Bob'}

You can also add filters to queries:

    >>> # instantiate some vertices
    >>> 
    >>> t = Vertex(tag="head")
    >>> u = Vertex(tag="title")
    >>> v = Vertex(tag="p", class_="bold")
    >>> w = Vertex(tag="section", class_="bold")
    >>> 
    >>> # set a relationship between the vertices
    >>> e1 = t >> u
    >>> e2 = t >> v
    >>> e3 = t >> w
    >>> 
    >>> # query the graph
    >>> t.out(class_="bold").tag
    {'section', 'p'}

