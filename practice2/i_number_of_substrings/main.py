#!/bin/python3

import sys
input = sys.stdin.readline
from atcoder.string import z_algorithm

def main():
  s = list(map(str, input().strip().split()))[0]
  print(z_algorithm(s))

main()
