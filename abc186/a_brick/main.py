#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n, w = list(map(int, input().strip().split()))
  print(n//w)

main()
