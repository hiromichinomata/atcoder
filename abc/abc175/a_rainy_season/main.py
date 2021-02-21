#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  s= list(map(str, input().strip().split()))[0]
  print(max(map(len, s.split('S'))))

main()
