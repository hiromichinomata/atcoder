#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n = list(map(int, input().strip().split()))[0]
  a = list(map(int, input().strip().split()))

  result = 0
  past_count = 0
  for i in range(2, 1001):
    count = 0
    for j in a:
      if j % i == 0:
        count += 1

    if count > past_count:
      result = i
      past_count = count

  print(result)

main()
