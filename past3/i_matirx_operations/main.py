#!/bin/python3

import copy
import sys
input = sys.stdin.readline
from collections import defaultdict

def replace_column(convert_column, a, b):
  tmp_a = convert_column[a]
  tmp_b = convert_column[b]
  convert_column[a] = tmp_b
  convert_column[b] = tmp_a

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
  convert_column = []
  for i in range(n):
    convert_column.append(i)

  for i in range(n):
    for j in range(n):
      a[i].append(n*i+j)

  transpose = False
  for i in range(q):
    query = list(map(int, input().strip().split()))
    if query[0] == 1:
      if transpose:
        replace_column(convert_column, query[1]-1, query[2]-1)
      else:
        replace_row(a, query[1]-1, query[2]-1)
    elif query[0] == 2:
      if transpose:
        replace_row(a, query[1]-1, query[2]-1)
      else:
        replace_column(convert_column, query[1]-1, query[2]-1)
    elif query[0] == 3:
      transpose = not transpose
    elif query[0] == 4:
      if transpose:
        print_matrix(a, query[2]-1, convert_column[query[1]-1])
      else:
        print_matrix(a, query[1]-1, convert_column[query[2]-1])

main()
