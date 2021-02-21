#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n= list(map(int, input().strip().split()))[0]
  x= list(map(int, input().strip().split()))
  m = sum([abs(i) for i in x])
  print(m)
  y= sum([i**2for i in x])**0.5
  print(y)
  c = max([abs(i) for i in x])
  print(c)

main()
