#!/bin/python3

import copy
import sys
input = sys.stdin.readline

def str_to_i(s):
  if s[0] == 'B':
    return -int(s[1])
  else:
    return int(s[0])-1

def main():
  s, t = list(map(str_to_i, input().strip().split()))

  print(abs(t-s))

main()
