#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n, m = list(map(int, input().strip().split()))
  a = list(map(int, input().strip().split()))
  a = set(a)
  a = sorted(list(a))
  for i in range(len(a)):
    if i != a[i]:
      print(i)
      sys.exit()
  print(a[-1]+1)

main()
