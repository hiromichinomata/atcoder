#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  c = list(map(str, input().strip().split()))[0]
  if c[0] == c[1] == c[2]:
    print('Won')
  else:
    print('Lost')

main()
