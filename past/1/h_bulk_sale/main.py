#!/bin/python3

import copy
import sys

n = int(input().strip())
c = list(map(int, input().strip().split()))
q = int(input().strip())
result = 0

def single_sell(x, a):
  global result
  if c[x] - a < 0:
    return
  else:
    result += a
    c[x] -= a

def set_sell(a):
  global result

  for i in range(0, len(c), 2):
    if c[i] - a < 0:
      return

  for i in range(0, len(c), 2):
    result += a
    c[i] -= a

def all_sell(a):
  global result

  for i in range(len(c)):
    if c[i] - a < 0:
      return

  for i in range(len(c)):
    result += a
    c[i] -= a

for i in range(q):
  query = list(map(int, input().strip().split()))
  if query[0] == 1:
    single_sell(query[1]-1, query[2])
  elif query[0] == 2:
    set_sell(query[1])
  elif query[0] == 3:
    all_sell(query[1])

print(result)
