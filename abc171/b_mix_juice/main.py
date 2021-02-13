#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n,k = list(map(int, input().strip().split()))
  p= list(map(int,  input().strip().split()))
  result = 0
  p = sorted(p)
  for i in range(k):
    result += p[i]

  print(result)

main()
