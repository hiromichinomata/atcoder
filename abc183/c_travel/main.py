#!/bin/python3
# pypy3

import sys
input = sys.stdin.readline
from itertools import permutations

def main():
  n, k = list(map(int, input().strip().split()))
  t = []
  for _ in range(n):
    tt = list(map(int, input().strip().split()))
    t.append(tt)

  l = [i for i in range(1, n)]
  result = 0
  for lt in permutations(l):
    path = [0] + list(lt)
    score = 0
    for pi in range(len(path)-1):
      score += t[path[pi]][path[pi+1]]
    score += t[path[-1]][path[0]]
    if score == k:
      result += 1

  print(result)

main()
