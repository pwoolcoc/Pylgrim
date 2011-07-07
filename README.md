# Pilgrim

This is a project to create a graph library similar to (but not nearly as
powerful as) the [Gremlin](https://github.com/tinkerpop/gremlin/) project.

When I first started the project, I had hoped to *not* include a central
`Graph` class, and just work directly with the vertices and edges. I
have conceded that this plan will limit my options down the line a bit,
so I am adding a central `Graph` class, and the API show below will be
changing.

So, for now, the API looks something like this:

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

After I'm done with the main `Graph` class, the query/filter API will be
very similar, but building and managing the graph itself will be done
through the `Graph` class.

