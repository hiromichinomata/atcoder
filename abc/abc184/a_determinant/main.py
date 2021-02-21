#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  a, b = list(map(int, input().strip().split()))
  c, d = list(map(int, input().strip().split()))

  print(a*d-b*c)

main()
