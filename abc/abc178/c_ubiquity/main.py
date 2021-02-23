#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n = list(map(int, input().strip().split()))[0]
  result = 10**n - 9**n - 9**n + 8**n
  result %= (10**9 + 7)
  print(result)

main()
