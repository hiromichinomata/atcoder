#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  a = list(map(int, input().strip().split()))
  a = sorted(a)
  if a[0] - a[1] == a[1] - a[2]:
    print('Yes')
  else:
    print('No')

main()
