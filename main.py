#!/usr/bin/python
#------------------------------------------------------------------------------
"""
Graph Experiments
"""
#------------------------------------------------------------------------------

import graph

#------------------------------------------------------------------------------

def main():
  """create a graph"""
  g = graph.Graph('stuff')

  n0 = graph.Node('A')
  n1 = graph.Node('B')
  n2 = graph.Node('C')

  e0 = graph.Edge('AB', n0, n1)
  e1 = graph.Edge('BC', n1, n2)
  e2 = graph.Edge('AC', n0, n2)

  g.add_edge(e0)
  g.add_edge(e1)
  g.add_edge(e2)

  print g

main()

#------------------------------------------------------------------------------
