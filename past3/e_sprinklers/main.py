#!/bin/python3

import sys
input = sys.stdin.readline
from collections import defaultdict

def print_color(c, x):
  print(c[x])

def launch_sprinkler(c, vdict, x):
  for i in vdict[x]:
    c[i] = c[x]

def change_color(c, x, y):
  c[x] = y

def main():
  n, m, q = list(map(int, input().strip().split()))
  vdict = defaultdict(list)
  for i in range(m):
    u, v = list(map(int, input().strip().split()))
    vdict[u-1].append(v-1)
    vdict[v-1].append(u-1)
  c = list(map(int, input().strip().split()))

  for i in range(q):
    query = list(map(int, input().strip().split()))
    if query[0] == 1:
      print_color(c, query[1]-1)
      launch_sprinkler(c, vdict, query[1]-1)
    elif query[0] == 2:
      print_color(c, query[1]-1)
      change_color(c, query[1]-1, query[2])

main()
