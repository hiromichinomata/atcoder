#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
  sys.stdin=open('input1.txt')

def main():
  s = list(map(str, input().strip().split()))[0]
  t = list(map(str, input().strip().split()))[0]

  result = float('inf')
  for i in range(len(s)-len(t)+1):
    count = 0
    for j in range(len(t)):
      if s[i+j] != t[j]:
        count += 1
    result = min(result, count)

  print(result)

main()
