#!/usr/bin/env python3
import sys
from ascii_graph import Pyasciigraph
f=open(sys.argv[1], "r").read()
print("\n".join(l for l in Pyasciigraph().graph('letter frequency', [(c,f.count(c)) for c in "abcdefghijklmnopqrstuvwxyz"])))
