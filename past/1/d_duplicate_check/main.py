#!/bin/python3

import sys

n = int(input().strip())

arr = []
for i in range(n):
  arr.append(int(input().strip()))
arr = sorted(arr)

missing = -1
for i in range(n):
  if i+1 != arr[i]:
    missing = i+1
    break

prev = -1
duplicate = -1
for i in range(n):
  if prev == arr[i]:
    duplicate = arr[i]
    break
  prev = arr[i]

if missing == -1:
  print("Correct")
else:
  print(str(duplicate) + " " + str(missing))
