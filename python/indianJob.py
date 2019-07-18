#!/bin/python3

import os
import sys

#
# Complete the indianJob function below.
#
def indianJob(g, arr):
    n = len(arr)-1
    slot1,slot2 = [[],[]]

    if sum(arr)/2>g:
        return 'NO'

    arr = sorted(arr)
    def fill(slot1,slot2,c,g):
        if sum(slot1)>g or sum(slot2)>g:
            return False
        if sum(slot1)<=g and sum(slot2)<=g and c==0:
            return True
        return fill(slot1+[arr[c-1]],slot2,c-1,g) or fill(slot1,slot2+[arr[c-1]],c-1,g)

    if fill(slot1+[arr[n]],slot2,n,g) or fill(slot1,slot2+[arr[n]],n,g):
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ng = input().split()
        n = int(ng[0])
        g = int(ng[1])
        arr = list(map(int, input().rstrip().split()))
        result = indianJob(g,arr)

        fptr.write(result + '\n')

    fptr.close()

