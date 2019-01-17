#!/usr/bin/env python3
import sys
from ascii_graph import Pyasciigraph
fstr = open(sys.argv[1], "r").read()
print ("\n".join(line for line in Pyasciigraph().graph('letter frequency', [(c,fstr.count(c)) for c in "abcdefghijklmnopqrstuvwxyz"])))
