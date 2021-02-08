#!/bin/python3

import sys
input = sys.stdin.readline
def main():
  a= list(map(str, input().strip().split()))[0]
  if 'a' <= a and a <= 'z':
    print('a')
  else:
    print('A')
main()
