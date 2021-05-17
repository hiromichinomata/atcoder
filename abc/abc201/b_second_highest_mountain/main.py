#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n = list(map(int, input().strip().split()))[0]
  data = []
  for i in range(n):
    s, t = list(map(str, input().strip().split()))
    t = int(t)
    data.append([t, s])

  data = sorted(data)
  print(data[-2][1])

main()
