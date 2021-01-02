#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  a, b = list(map(int, input().strip().split()))
  s_a = 0
  s_b = 0
  for i in str(a):
    s_a += int(i)
  for i in str(b):
    s_b += int(i)
  if s_b > s_a:
    print(s_b)
  else:
    print(s_a)

main()
