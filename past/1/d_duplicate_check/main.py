#!/bin/python3

import sys

n = int(input().strip())

arr = [0] * (n+1)
for i in range(n):
  tmp = int(input().strip())
  arr[tmp] += 1

missing = -1
duplicate = -1
for i in range(1, n+1):
  if arr[i] == 0:
    missing = i
  elif arr[i] > 1:
    duplicate = i

  if missing != -1 and duplicate != -1:
    break

if missing == -1:
  print("Correct")
else:
  print(str(duplicate) + " " + str(missing))
