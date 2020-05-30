#!/bin/python3

import sys

n = int(input().strip())
a = []
for i in range(n):
  tmp = int(input().strip())
  a.append(tmp)

prev = a[0]
for i in range(1, n):
  diff = a[i] - prev

  if diff == 0:
    print("stay")
  elif diff > 0:
    print("up " + str(diff))
  else:
    print("down " + str(-diff))

  prev = a[i]
