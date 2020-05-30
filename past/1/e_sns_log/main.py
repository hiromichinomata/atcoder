#!/bin/python3

import copy
import sys

n, q = list(map(int, input().strip().split()))

f = [[0] * (n+1) for i in range(n+1)]

def follow(i, j):
  f[i][j] = 1

def follow_back(i):
  for j in range(1, n+1):
    if f[j][i] == 1:
      f[i][j] = 1

def follow_follow(i):
  f_prev = copy.deepcopy(f)
  for j in range(1, n+1):
    if f_prev[i][j] == 1:
      for k in range(1, n+1):
        if f_prev[j][k] == 1:
          f[i][k] = 1

for i in range(q):
  inst = list(map(int, input().strip().split()))
  if inst[0] == 1:
    follow(inst[1], inst[2])
  elif inst[0] == 2:
    follow_back(inst[1])
  elif inst[0] == 3:
    follow_follow(inst[1])

for i in range(1, n+1):
  f[i][i] = 0

result = []
for i in range(1, n+1):
  item = ""
  for j in range(1, n+1):
    if f[i][j] == 1:
      item += "Y"
    elif f[i][j] == 0:
      item += "N"

  result.append(item)

for i in result:
  print(i)