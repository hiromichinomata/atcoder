#!/bin/python3

import sys
input = sys.stdin.readline
from collections import defaultdict
from collections import deque

def add_last(s, c, x):
  s.append((c,x))

def print_del(s, d):
  count_dict = defaultdict(int)

  while len(s) > 0 and d > 0:
    v = s.popleft()
    c, x = v

    if x > d:
      count_dict[c] += d
      x -= d
      d -= d
      s.appendleft((c, x))
    else:
      count_dict[c] += x
      d -= x

  result = 0
  for key in count_dict.keys():
    count = count_dict[key]
    result += count**2
  print(result)

def main():
  q = int(input().strip())
  s = deque()
  for i in range(q):
    query = input().strip().split()
    query[0] = int(query[0])
    if query[0] == 1:
      query[2] = int(query[2])
    else:
      query[1] = int(query[1])

    if query[0] == 1:
      add_last(s, query[1], query[2])
    else:
      print_del(s, query[1])

main()
