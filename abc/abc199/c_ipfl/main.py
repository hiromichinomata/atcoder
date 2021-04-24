#!/bin/python3
# pypy3

import sys
input = sys.stdin.readline

def main():
  n = list(map(int, input().strip().split()))[0]
  s = list(map(str, input().strip().split()))[0]
  s_f = [c for c in s[:n]]
  s_b = [c for c in s[n:]]
  q = list(map(int, input().strip().split()))[0]
  for i in range(q):
    t, a, b = list(map(int, input().strip().split()))
    if t == 1:
      a -= 1
      b -= 1

      if a < n and b < n:
        s_f[a], s_f[b] = s_f[b], s_f[a]
      elif a < n and b >= n:
        s_f[a], s_b[b-n] = s_b[b-n], s_f[a]
      elif a >= n and b < n:
        s_b[a-n], s_f[b] = s_f[b], s_b[a-n]
      elif a >= n and b >= n:
        s_b[a-n], s_b[b-n] = s_b[b-n], s_b[a-n]
    else:
      s_f, s_b = s_b, s_f

  s = s_f + s_b
  print(''.join(s))

main()
