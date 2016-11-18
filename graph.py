#------------------------------------------------------------------------------
"""
Graph Class
"""
#------------------------------------------------------------------------------

class Error(Exception):
  """base class for exceptions in this module"""
  pass

#------------------------------------------------------------------------------

node_uuid = 0

def get_node_id():
  """return a uuid for the node"""
  global node_uuid
  x = node_uuid
  node_uuid += 1
  return x

class NodeError(Error):
  """Node Errors"""
  def __init__(self, msg):
    self.msg = msg

class Node(object):
  """node object"""

  def __init__(self):
    """create a node"""
    self.id = get_node_id()
    self.name = 'n%d' % self.id

#------------------------------------------------------------------------------

edge_uuid = 0

def get_edge_id():
  """return a uuid for the edge"""
  global edge_uuid
  x = edge_uuid
  edge_uuid += 1
  return x

class EdgeError(Error):
  """Edge Errors"""
  def __init__(self, msg):
    self.msg = msg

class Edge(object):
  """edge object"""

  def __init__(self, n0, n1):
    """create an edge: n0 to n1"""
    self.id = get_edge_id()
    self.name = 'e%d' % self.id
    self.n0 = n0
    self.n1 = n1

#------------------------------------------------------------------------------

graph_uuid = 0

def get_graph_id():
  """return a uuid for the graph"""
  global graph_uuid
  x = graph_uuid
  graph_uuid += 1
  return x

class Graph(object):
  """graph object"""

  def __init__(self):
    """create an empty graph"""
    self.id = get_graph_id()
    self.name = 'g%d' % self.id
    self.nodes = {}
    self.edges = {}

  def merge(self, g):
    """merge graph g with this graph"""
    for e in g.edges.itervalues():
      self.add_edge(e)
    for n in g.nodes.itervalues():
      if not self.nodes.has_key(n.name):
        self.add_node(n)

  def add_node(self, node):
    """add a node to the graph"""
    if self.nodes.has_key(node.name):
      raise NodeError('node %s is already in the graph' % node.name)
    self.nodes[node.name] = node

  def add_edge(self, edge):
    """add an edge to the graph"""
    if self.edges.has_key(edge.name):
      raise EdgeError('edge %s is already in the graph' % edge.name)
    self.edges[edge.name] = edge
    # add the nodes if they aren't in the graph
    if not self.nodes.has_key(edge.n0.name):
      self.add_node(edge.n0)
    if not self.nodes.has_key(edge.n1.name):
      self.add_node(edge.n1)

  def gv_str(self):
    """return a graphviz graph description"""
    s = []
    s.append('digraph %s {' % self.name)
    for _,node in self.nodes.iteritems():
      s.append('  %s;' % node.name)
    for _,edge in self.edges.iteritems():
      s.append('  %s->%s;' % (edge.n0.name, edge.n1.name))
    s.append('}')
    return '\n'.join(s)

#------------------------------------------------------------------------------
