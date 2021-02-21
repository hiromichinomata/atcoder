#!/bin/python3

import sys
input = sys.stdin.readline
from decimal import Decimal

def main():
  a, b = list(map(Decimal, input().strip().split()))
  print(int(a*b))

main()
