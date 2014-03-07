#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc

#Use Babyloninan (aka simplified Newton's) to solve square root

from math import log10
from math import ceil
from math import floor
from math import sqrt

number=70000
num_digit=int(ceil(log10(number)))
print num_digit

#determine the start point, reduce calculation time
start=int(10**floor(num_digit/2))

#Babylonian algorithm
for i in range(0,num_digit):
    print start
    start=(start+number/start)/2

#compare to the original
print sqrt(number)