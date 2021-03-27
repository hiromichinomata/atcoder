#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n = list(map(int, input().strip().split()))[0]
  a = list(map(int, input().strip().split()))
  a = sorted(a)
  result = 0

  for i in range(n):

main()
