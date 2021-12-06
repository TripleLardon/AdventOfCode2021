#!/bin/python3
# -*- coding: UTF-8 -*-

import collections as c

input = open("input","r")
lines = input.readlines()

pos = []
for l in lines[0][:-1]:
    pos.append("")

print(pos)


for line in lines:
    line = line[:-1]
    for i in range(len(line)):
        pos[i]+=line[i]

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