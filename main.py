#!/usr/bin/python
#------------------------------------------------------------------------------
"""
Graph Experiments
"""
#------------------------------------------------------------------------------

import graph

#------------------------------------------------------------------------------

def star_graph(n):
  """generate star graph n"""
  g = graph.Graph()
  ni = graph.Node()
  for i in xrange(n):
    n = graph.Node()
    e = graph.Edge(ni, n)
    g.add_edge(e)
  return g

#------------------------------------------------------------------------------

def main():
  """create a graph"""

  g = graph.Graph()
  for k in range(5):
    gs = star_graph(10)
    g.merge(gs)

  print g.gv_str()

main()

#------------------------------------------------------------------------------
