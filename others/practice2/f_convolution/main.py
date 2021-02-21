#!/bin/python3

import sys
input = sys.stdin.readline
from atcoder.convolution import convolution

def main():
  n, m = list(map(int, input().strip().split()))
  a = list(map(int, input().strip().split()))
  b = list(map(int, input().strip().split()))

  result = convolution(998244353,a,b)
  print(' '.join(map(str, result)))

main()
