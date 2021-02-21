#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n= list(map(int, input().strip().split()))[0]
  print(-n%1000)
main()
