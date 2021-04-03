#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
  sys.stdin=open('input1.txt')

def main():
  n, m = list(map(int, input().strip().split()))
  h = list(map(int, input().strip().split()))
  w = list(map(int, input().strip().split()))
  print(h)

main()
