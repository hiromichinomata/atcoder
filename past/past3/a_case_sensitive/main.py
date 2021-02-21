#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  s = input().strip()
  t = input().strip()
  if s == t:
    print("same")
  elif s.lower() == t.lower():
    print("case-insensitive")
  else:
    print("different")

main()
