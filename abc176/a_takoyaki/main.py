#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n, x, t= list(map(int, input().strip().split()))
  answer =0
  while n >0:
    n -= x
    answer += t

  print(answer)

main()
