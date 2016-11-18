#------------------------------------------------------------------------------
"""
Graph Class
"""
#------------------------------------------------------------------------------

class Error(Exception):
  """base class for exceptions in this module"""
  pass


#------------------------------------------------------------------------------

class NodeError(Error):
  """Node Errors"""
  def __init__(self, msg):
    self.msg = msg

class Node(object):
  """node object"""
  def __init__(self, name):
    self.name = name

#------------------------------------------------------------------------------

class EdgeError(Error):
  """Edge Errors"""
  def __init__(self, msg):
    self.msg = msg

class Edge(object):
  """edge object"""
  def __init__(self, name, n0, n1):
    self.name = name
    self.n0 = n0
    self.n1 = n1

#------------------------------------------------------------------------------

class Graph(object):
  """graph object"""
  def __init__(self, name):
    self.name = name
    self.nodes = {}
    self.edges = {}

  def add_node(self, node):
    """add a node to the graph"""
    if self.nodes.has_key(node.name):
      raise NodeError('node of this name already in graph')
    self.nodes[node.name] = node

  def add_edge(self, edge):
    """add an edge to the graph"""
    if self.edges.has_key(edge.name):
      raise EdgeError('edge of this name already in graph')
    self.edges[edge.name] = edge
    # add the nodes if they aren't in the graph
    if not self.nodes.has_key(edge.n0.name):
      self.add_node(edge.n0)
    if not self.nodes.has_key(edge.n1.name):
      self.add_node(edge.n1)

  def __str__(self):
    """output a graphviz graph description"""
    s = []
    s.append('digraph "%s" {' % self.name)
    for _,node in self.nodes.iteritems():
      s.append('  "%s";' % node.name)
    for _,edge in self.edges.iteritems():
      s.append('  "%s"->"%s";' % (edge.n0.name, edge.n1.name))
    s.append('}')
    return '\n'.join(s)

#------------------------------------------------------------------------------
