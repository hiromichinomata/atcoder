#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  a, b = list(map(int, input().strip().split()))
  result = (a - b) * 100 / a
  print(result)

main()
