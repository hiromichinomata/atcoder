#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  t= list(map(int, input().strip().split()))[0]
  if t >= 30:
    print('Yes')
  else:
    print('No')
main()
