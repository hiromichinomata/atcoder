#!/bin/python3

import sys
input = sys.stdin.readline
from statistics import mean

def main():
  n= list(map(int, input().strip().split()))[0]
  x= list(map(int, input().strip().split()))
  m = round(mean(x))
  result = 0
  for i in range(n):
    result += (x[i]-m)**2

  print(result)
main()
