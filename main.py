#!/usr/bin/python
#------------------------------------------------------------------------------
"""
Graph Experiments
"""
#------------------------------------------------------------------------------

import graph

#------------------------------------------------------------------------------

def star_graph(n):
  """generate start graph n"""
  g = graph.Graph('s%d' % n)
  ni = graph.Node('i')
  for i in xrange(n):
    n = graph.Node('e%d' % i)
    e = graph.Edge('i_to_e%d' % i , ni, n)
    g.add_edge(e)
  return g

#------------------------------------------------------------------------------

def main():
  """create a graph"""
  g = star_graph(10)
  print g

main()

#------------------------------------------------------------------------------
