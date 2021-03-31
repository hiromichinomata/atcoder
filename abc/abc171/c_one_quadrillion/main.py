#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n = list(map(int, input().strip().split()))[0]
  ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

  result = ''
  while n > 0:
    n -= 1
    # print(ALPHABET[n % 26])
    result = ALPHABET[n % 26] + result
    print(result)
    n //= 26

  print(result)

main()
