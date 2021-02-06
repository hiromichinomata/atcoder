#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  h, w = list(map(int, input().strip().split()))
  s = []
  for _ in range(h):
    st = list(map(str, input().strip().split()))
    s.append(st)

  print(s)

main()
