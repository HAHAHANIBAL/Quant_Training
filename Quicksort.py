#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc

#quick implementation of quicksort
#this is in-place quicksort

import time


def partition(A,left,right,pivotindex):
    pivotvalue=A[pivotindex]
    A[pivotindex]=A[right]
    A[right]=pivotvalue
    storeindex=left
    for i in range(left,right):
        if A[i]<=pivotvalue:
            temp=A[i]
            A[i]=A[storeindex]
            A[storeindex]=temp
            storeindex+=1
    temp=A[right]
    A[right]=A[storeindex]
    A[storeindex]=temp
    return storeindex


def quicksort(A,left,right):
    if left<right:
        pivotindex=(left+right)/2
        pivotnewindex=partition(A,left,right,pivotindex)
        quicksort(A,left,pivotnewindex-1)
        quicksort(A,pivotnewindex+1,right)

start_time=time.time()
A=[7,1,9,2,6,8,5,2,4]
left=0
right=len(A)-1
quicksort(A,left,right)
print A,'\n',time.time()-start_time,'seconds'





