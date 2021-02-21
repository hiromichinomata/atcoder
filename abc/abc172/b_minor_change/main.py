#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  s = list(map(str, input().strip().split()))[0]
  t = list(map(str, input().strip().split()))[0]
  result = 0
  for i in range(len(s)):
    if s[i] != t[i]:
      result += 1

  print(result)

main()
