#!/usr/bin/env python3
import sys
from ascii_graph import Pyasciigraph

if len(sys.argv) != 3:
    print("usage: {} <source text> <cipher text>".format(sys.argv[0]))
    sys.exit(1)

src = open(sys.argv[1], "r").read()
cnt = open(sys.argv[2], "r").read()

src_lettercounts = [(c,src.count(c)) for c in "abcdefghijklmnopqrstuvwxyz"]
cnt_lettercounts = [(c,cnt.count(c)) for c in "abcdefghijklmnopqrstuvwxyz"]

print("\n".join(l for l in Pyasciigraph().graph('Task 1:letter frequency', src_lettercounts)))

src_total = sum(c for i, c in src_lettercounts)
cnt_total = sum(c for i, c in cnt_lettercounts)

src_percents = [(l,c, c / src_total * 100) for l,c in sorted(src_lettercounts, key=lambda x: x[1], reverse=True)]
cnt_percents = [(l,c, c / cnt_total * 100) for l,c in sorted(cnt_lettercounts, key=lambda x: x[1], reverse=True)]

print("Task 2: breaking the cipher")

for i in range(len(src_percents)):
    print("{0} likely {1} - match {2:0.2f}%".format(cnt_percents[i][0], src_percents[i][0], 100-abs(cnt_percents[i][2] - src_percents[i][2])))

