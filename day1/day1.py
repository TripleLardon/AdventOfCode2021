#!/bin/python3
# -*- coding: UTF-8 -*-

input = open("input","r")
lines = input.readlines()

last = int(lines[0])
part1 = 0

for line in lines[1:]:
    line = int(line)
    if(line >  last):
        part1+=1
    last = line

print("part1: ",part1)