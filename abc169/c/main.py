#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  a, b = list(map(float, input().strip().split()))
  result = int(a * b)
  print(result)

main()
