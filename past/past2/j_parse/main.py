#!/bin/python3

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def calc(s, level=0):
  if len(s) == 0:
    return ''
  if '(' not in s:
    if level == 1:
      return s + s[::-1]
    else:
      return s

  lcount = rcount = 0
  start = end = -float('INF')
  for i in range(len(s)):
    if s[i] == '(':
      lcount += 1
      if lcount == 1:
        start = i
    if s[i] == ')':
      rcount +=1
      if lcount == rcount:
        end = i
        break

  middle = s[start+1:end]
  result = calc(s[0:start])
  result += calc(middle, 1)
  result += calc(s[end+1:])
  if level == 0:
    return result
  else:
    return result + result [::-1]

def main():
  s = input().strip()
  print(calc(s))

main()
