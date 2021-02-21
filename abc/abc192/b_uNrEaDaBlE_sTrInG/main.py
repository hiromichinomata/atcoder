#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  s = list(map(str, input().strip().split()))[0]

  for i in range(len(s)):
    c = s[i]
    if i % 2 == 0:
      if c == c.upper():
        print('No')
        sys.exit()
    else:
      if c == c.lower():
        print('No')
        sys.exit()

  print('Yes')

main()
