#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  a= list(map(int, input().strip().split()))[0]
  print(a+a**2+a**3)
main()
