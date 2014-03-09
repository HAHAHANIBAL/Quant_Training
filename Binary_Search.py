#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc

#quick implementation of binary search in Python
#deferred detection of equality
import math

def midpoint(num1,num2):
    return num1+(num2-num1)/2


def binary_search(A,key,min,max):
    if max<min:
        return "no such value"
    else:
        mid=midpoint(min,max)
        if A[mid]>key:
            return binary_search(A,key,min,mid-1)
        elif A[mid]<key:
            return binary_search(A,key,mid+1,max)
        else:
            return mid


#this is just a demo, use heapsort to sort out the array first and then use binary search
A=[1,2,3,4,5,6,7,8,19]
min=0
max=len(A)+1
key=19

print "The position in the array is:", binary_search(A,key,min,max)
