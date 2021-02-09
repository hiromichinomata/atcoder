#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n = list(map(int, input().strip().split()))[0]
  if n% 9==0:
    print('Yes')
  else:
    print('No')

main()
