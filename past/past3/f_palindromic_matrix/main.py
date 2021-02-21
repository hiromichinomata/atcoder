#!/bin/python3

import sys
input = sys.stdin.readline
from collections import defaultdict

def main():
  n = int(input().strip())
  a = []
  for i in range(n):
    a.append(set(list(input().strip())))

  s = []
  for i in range(n//2):
    common = list(a[i] & a[-i-1])
    if len(common) > 0:
      s.append(common[0])
    else:
      print(-1)
      sys.exit()

  if n % 2 == 0:
    print(''.join(s + s[::-1]))
  else:
    print(''.join(s + [list(a[n//2])[0]] + s[::-1]))

main()
