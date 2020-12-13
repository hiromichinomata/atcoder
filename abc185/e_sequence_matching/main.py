#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n, m = list(map(int, input().strip().split()))
  a = list(map(int, input().strip().split()))
  b = list(map(int, input().strip().split()))

  print(a*d-b*c)

main()
