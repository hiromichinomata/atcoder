#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  a, b = list(map(int, input().strip().split()))
  result = a * 2 + 100 - b
  print(result)

main()
