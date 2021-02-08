#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n= list(map(int, input().strip().split()))[0] 
  count = 0
  for i in range(n):
    d,e= list(map(int, input().strip().split()))
    if d == e:
      count += 1
    else:
      count=0
    if count == 3:
      print('Yes')
      sys,exit()

  print('No')

main()
