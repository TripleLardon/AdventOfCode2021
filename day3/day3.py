#!/bin/python3
# -*- coding: UTF-8 -*-

import collections as c

input = open("input","r")
lines = list(map(lambda x: x[:-1],input.readlines()))

lenLine = len(lines[0])

def getInvertTab(tab):
    pos = []
    for l in range(lenLine):
        pos.append("")
    for line in tab:
        for i in range(lenLine):
            pos[i]+=line[i]
    return pos
 
print(getInvertTab(lines))



gamma = ""
for b in pos:
    b0 = b.count('0')
    b1 = b.count('1')
    gamma += '0' if b0>b1 else '1'

epsilon = ""

for b in gamma:
    epsilon += '0' if int(b) else '1'

part1 = int(gamma,2) * int(epsilon,2)

print("Part 1: ",part1)

