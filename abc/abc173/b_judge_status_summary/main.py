#!/bin/python3

import sys
input = sys.stdin.readline
from collections import defaultdict

def main():
  d = defaultdict(int)
  n = list(map(int, input().strip().split()))[0]
  for i in range(n):
    s = list(map(str, input().strip().split()))[0]
    d[s] += 1

  print('AC x '+ str(d["AC"]))
  print('WA x ' +str(d["WA"]))
  print('TLE x ' +str(d["TLE"]))
  print('RE x ' +str(d["RE"]))

main()
