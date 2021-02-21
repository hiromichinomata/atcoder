#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  a, b = input().strip().split()
  a, b = int(a), round(float(b)*100)
  result = a * b //100
  print(result)

main()
