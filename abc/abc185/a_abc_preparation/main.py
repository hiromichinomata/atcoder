#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  a = list(map(int, input().strip().split()))
  print(min(a))

main()
