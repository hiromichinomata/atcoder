#!/bin/python3

import sys
input = sys.stdin.readline
def main():
  n= list(map(int, input().strip().split()))[0]
  result = 0
  for i in range(n):
    a,b= list(map(int, input().strip().split()))
    result += (a+b)*(b-a+1)/2

  print(round(result))
main()
