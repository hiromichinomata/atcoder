#!/bin/python3
# python3.8

import sys
input = sys.stdin.readline
import math

def main():
  l = int(input().strip())
  n = l - 1 
  print(math.comb(n, 11))

main()
