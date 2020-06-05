#!/bin/python3

import copy
import sys
input = sys.stdin.readline
from collections import defaultdict

def replace_row(arr, a, b):
  aa = arr[a]
  ab = arr[b]
  arr[a] = ab
  arr[b] = aa

def print_matrix(arr, a, b):
  print(arr[a][b])

def main():
  n = int(input().strip())
  q = int(input().strip())
  a = defaultdict(list)
  convert = []
  for i in range(n):
    convert.append(i)

  for i in range(n):
    for j in range(n):
      a[i].append(n*i+j)

  transpose = False
  for i in range(q):
    query = list(map(int, input().strip().split()))
    if query[0] == 1:
      if transpose:
        x = query[1]-1
        y = query[2]-1
        tmp_x = convert[x]
        tmp_y = convert[y]
        convert[x] = tmp_y
        convert[y] = tmp_x
      else:
        replace_row(a, query[1]-1, query[2]-1)
    elif query[0] == 2:
      if transpose:
        replace_row(a, query[1]-1, query[2]-1)
      else:
        x = query[1]-1
        y = query[2]-1
        tmp_x = convert[x]
        tmp_y = convert[y]
        convert[x] = tmp_y
        convert[y] = tmp_x
    elif query[0] == 3:
      transpose = not transpose
    elif query[0] == 4:
      if transpose:
        print_matrix(a, query[2]-1, convert[query[1]-1])
      else:
        print_matrix(a, query[1]-1, convert[query[2]-1])

main()
