#!/bin/python3
# -*- coding: UTF-8 -*-

input = open("input","r")
lines = input.readlines()
lines = list(map(lambda s: int(s[:-1]),lines))

last = lines[0]
part1 = 0

for line in lines[1:]:
    if(line >  last):
        part1+=1
    last = line

print("Part1:", part1)

last = lines[:3]
part2 = 0
for line in lines[3:]:
    if sum(last[1:])+line > sum(last):
        part2+=1
    last.append(line)
    last.pop(0)

print("Part2", part2)