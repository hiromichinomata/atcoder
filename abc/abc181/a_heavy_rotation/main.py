#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n = list(map(int, input().strip().split()))[0]
  if n % 2 == 0:
    print('White')
  else:
    print('Black')

main()
