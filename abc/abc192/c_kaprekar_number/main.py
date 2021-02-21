#!/bin/python3

import sys
input = sys.stdin.readline

def g1x(x):
  return int(''.join(sorted([char for char in str(x)], reverse=True)))

def g2x(x):
  return int(''.join(sorted([char for char in str(x)])))

def fx(x):
  return g1x(x) - g2x(x)


def main():
  n, k = list(map(int, input().strip().split()))
  a = n
  for i in range(k):
    a = fx(a)

  print(a)

main()
