#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  d,t,s = list(map(int, input().strip().split()))
  if d/s <= t:
    print("Yes")
  else:
    print("No")

main()
