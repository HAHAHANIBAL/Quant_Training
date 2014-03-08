#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc

#quick implementation of heapsort
import time


class sort:
    def __init__(self,A,count):
        self.A=A
        self.count=count


def heapify(A,count):
    start=(count-2)/2
    while start>=0:
        siftdown(A,start,count-1)
        start-=1


def siftdown(A,start,end):
    root=start
    while (root*2+1)<=end:
        child=root*2+1
        swap=root

        if A[swap]<A[child]:
            swap=child
        if child+1<=end and A[swap]<A[child+1]:
            swap=child+1
        if swap!=root:
            temp=A[root]
            A[root]=A[swap]
            A[swap]=temp
            root=swap
        else:
            return A


def heapsort(A,count):
    heapify(A,count)
    end=count-1
    while end>0:
        temp=A[end]
        A[end]=A[0]
        A[0]=temp
        end-=1
        siftdown(A,0,end)

start_time=time.time()
A=[7,1,9,2,6,8,5,2,4]
count=len(A)
heapsort(A,count)
print A,'\n',time.time()-start_time,'seconds'



