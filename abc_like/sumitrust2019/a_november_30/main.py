#!/bin/python3

import sys
input = sys.stdin.readline
import math

def main():
  m1, d1 = list(map(int, input().split()))
  m2, d2 = list(map(int, input().split()))
  if d2 != 1:
    print('0')
  else:
    print('1')

main()
