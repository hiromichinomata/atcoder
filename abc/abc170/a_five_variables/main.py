#!/bin/python3

import sys
input = sys.stdin.readline
def main():
  x= list(map(int, input().strip().split()))
  for i in range(len(x)):
    if x[i] ==0:
      print(i+1)
      sys.exit()

main()
