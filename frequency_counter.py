#!/usr/bin/env python3
import sys
import ascii_graph
if len(sys.argv) == 3:
    s = open(sys.argv[1]).read()
    c = open(sys.argv[2]).read()
    sl = [a for a in sorted([(a,s.count(a)) for a in "abcdefghijklmnopqrstuvwxyz"], key=lambda x: x[1], reverse=True)]
    cl = [a for a in sorted([(a,c.count(a)) for a in "abcdefghijklmnopqrstuvwxyz"], key=lambda x: x[1], reverse=True)]
    st = sum(a for i, a in sl)
    ct = sum(a for i, a in cl)
    sp = [(l,a, a / st * 100) for l,a in sl]
    cp = [(l,a, a / ct * 100) for l,a in cl]
    print("\n".join(l for l in ascii_graph.Pyasciigraph().graph('Task 1:letter frequency', sl))+"\nTask 2: breaking the cipher\n"+"\n".join("{0} is {1} - match {2:0.2f}%".format(cp[i][0], sp[i][0], 100-abs(cp[i][2] - sp[i][2])) for i in range(len(sp))))
else:
    print("usage: {} <source text> <cipher text>".format(sys.argv[0]))
