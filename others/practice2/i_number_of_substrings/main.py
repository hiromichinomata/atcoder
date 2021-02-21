#!/bin/python3

import sys
input = sys.stdin.readline
from atcoder.string import suffix_array ,lcp_array

def main():
  s = list(map(str, input().strip().split()))[0]
  sa = suffix_array(s)
  result = len(sa) * (len(sa) + 1)//2
  for i in lcp_array(s, sa):
    result -= i
  print(result)

main()
