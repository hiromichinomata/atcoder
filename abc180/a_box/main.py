#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n, a,b = list(map(int, input().strip().split()))
  print(n-a+b)

main()
