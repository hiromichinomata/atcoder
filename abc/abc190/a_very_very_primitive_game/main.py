#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  a,b,c = list(map(int, input().strip().split()))
  while True:
    if c == 0:
      a -= 1
      c = 1
      if a < 0:
        print('Aoki')
        sys.exit()
    else:
      b -= 1
      c = 0
      if b < 0:
        print('Takahashi')
        sys.exit()

main()
