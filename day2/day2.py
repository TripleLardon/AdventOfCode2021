#!/bin/python3
# -*- coding: UTF-8 -*-

input = open("input","r")
lines = input.readlines()

pos = 0
depth = 0
for line in lines:
    do = line[:-3]
    n = int(line[-2])
    if do == "forward":
        pos += n
    elif do == "down":
        depth += n
    elif do == "up":
        depth -= n

part1 = pos*depth

print("Part1: ",part1)


pos = 0
depth = 0
aim = 0
for line in lines:
    do = line[:-3]
    n = int(line[-2])
    if do == "forward":
        pos += n
        depth += aim*n
    elif do == "down":
        aim += n
    elif do == "up":
        aim -= n

part2 = pos*depth
print("Part2: ",part2)