#!/bin/python3

import sys
from itertools import product

n = int(input().strip())
a = [[0] * (n) for i in range(n)]

for i in range(0, n-1):
  s = list(map(int, input().strip().split()))
  a[i] = [0]*(i+1) + s

result = -float("INF")
for candidate in product([0, 1, 2], repeat=n):
  happiness = 0
  for i in range(n-1):
    for j in range(i+1, n):
      if candidate[i] == candidate[j]:
        happiness += a[i][j]
  result = max(result, happiness)

print(result)
