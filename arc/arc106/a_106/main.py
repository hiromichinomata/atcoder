#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
  sys.stdin=open('input1.txt')

def main():
  n = list(map(int, input().strip().split()))[0]
  for i in range(1, 50):
    for j in range(1, 50):
      if 3**i + 5**j == n:
        print(f'{i} {j}')
        sys.exit()
  print(-1)

main()
