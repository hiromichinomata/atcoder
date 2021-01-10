#!/bin/python3

import sys
input = sys.stdin.readline
from collections import defaultdict

def main():
  n = int(input().strip())
  d1 = defaultdict(int)
  s = []
  for _ in range(n):
    st = input().strip()
    s.append(st)
  s = list(set(s))
  for i in range(len(s)):
    st = s[i]
    tmp = ''
    if st[0] == '!':
      tmp = st[1:]
      d1[tmp] += 1
      if d1[tmp] == 2:
        print(tmp)
        sys.exit()
    else:
      tmp = st
      d1[tmp] += 1
      if d1[tmp] == 2:
        print(tmp)
        sys.exit()

  print('satisfiable')

main()
