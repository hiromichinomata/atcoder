#!/bin/python3

import sys
input = sys.stdin.readline
from collections import defaultdict

def print_score(score, solved, n):
  result = 0
  for i in solved[n]:
    result += score[i]
  print(result)

def solve_problem(score, solved, n, m):
  solved[n].append(m)
  score[m] -= 1

def main():
  n, m, q = list(map(int, input().strip().split()))
  score = [n]*m
  solved = defaultdict(list)
  for i in range(q):
    query = list(map(int, input().strip().split()))
    if query[0] == 1:
      print_score(score, solved, query[1]-1)
    elif query[0] == 2:
      solve_problem(score, solved, query[1]-1, query[2]-1)

main()
