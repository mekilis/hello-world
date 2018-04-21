#!/bin/python3

import os
import sys
import ast
import itertools as it


# Complete the maximumEfficiency function below.
def maximumEfficiency(n, m):
    G = {}
    Glist = () # should be a tuple
    #fl = open('demo.txt', 'r')
    #line = fl.readline() #discard
    for i in range(m):
        # O(n)
        kf = input().split()
        k, f = int(kf[0]), int(kf[1])
        g = [int(j) for j in input().split()]
        key = repr(g)
        if key in G:
            G[key] += f
        else:
            G[key] = f
        #print(g)
        #print(repr(g))
        #G[repr(g) + "*"] = k
    #print(G)

    gkeys = G.keys()
    gkeys = list(gkeys)
    #print("gkeys", gkeys)
    Keys = []
    for i in range(len(gkeys)):
        Keys.append(ast.literal_eval(gkeys[i]))
    #print(Keys)
    Glist = tuple(set().union(*Keys))
    Gset = set(Glist)
    #print(Glist)

    # code begins
    #Map = {} # prevent duplicates
    maxi = 0
    for i in range(len(Glist)):
        gl = list(it.combinations(Glist, i+1))
        #print(gl)
        # O(n^2)
        for j in range(len(gl)):
            summ = 0
            g_left = list(gl[j])
            if len(g_left) == 0:
                continue
            g_left_set = set(g_left)
            # remove common
            g_right = list(set.union(g_left_set, Gset) - set.intersection(g_left_set, Gset))
            if len(g_right) == 0:
                continue
            #print(g_left, g_right)
            left, right = repr(g_left), repr(g_right)

            # O(n^3) terrible
            items = G.items()
            for k, v in items:
                kk = ast.literal_eval(k)
                #print("...", k, kk, v)
                #print(type(k), type(kk))
                if set(kk).issubset(g_left):
                    summ += v
                if set(kk).issubset(g_right):
                    summ += v
            
            '''if left in G:
                summ += G[left]
            if right in G:
                summ += G[right]'''
            if summ > maxi:
                maxi = summ
            #(summ, maxi)
            
    #fl.close()

    return maxi

if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    result = maximumEfficiency(n, m)

    print(str(result) + '\n')


'''
4 3
2 4z
1 2
2 5
1 3
3 10
2 3 4
'''
