#!/bin/python3

import sys
input = sys.stdin.readline
import math

def main():
  a = list(map(int, input().strip().split()))[0]
  b = list(map(int, input().strip().split()))[0]
  c = list(map(int, input().strip().split()))[0]
  d = list(map(int, input().strip().split()))[0]
  e = list(map(int, input().strip().split()))[0]
  foods = [a, b, c, d, e]

  result = 0
  for e in foods:
    result += round(math.ceil(e/10))*10

  last_digit = 10
  for e in filter(lambda x: x%10 != 0, foods):
    last_digit = min(last_digit, e%10)

  result += -10 + last_digit

  print(result)

main()
