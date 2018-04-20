#!/bin/python3

import os
import sys
import ast


# Complete the maximumEfficiency function below.
def maximumEfficiency(n, m):
    G = {}
    Glist = []
    for i in range(m):
        # O(n)
        kf = input().split()
        k, f = int(kf[0]), int(kf[1])
        g = input().split()
        G[repr(g)] = f
        #G[repr(g) + "*"] = k
    print(G)

    x = G.keys()
    print("x", x)
    GList = list(set().union(list(x)))
    print(GList)

    return 0

if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    result = maximumEfficiency(n, m)

    #print(str(result) + '\n')


'''
4 3
2 4z
1 2
2 5
1 3
3 10
2 3 4
'''
