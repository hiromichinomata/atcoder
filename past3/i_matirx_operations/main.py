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

def replace_column(arr, a, b):
  for i in range(len(arr)):
    aa = arr[i][a]
    ab = arr[i][b]
    arr[i][a] = ab
    arr[i][b] = aa

def transpose(arr):
  arr_new = copy.deepcopy(arr)
  for i in range(len(arr)):
    for j in range(len(arr)):
      arr_new[i][j] = arr[j][i]

  return arr_new

def print_matrix(arr, a, b):
  print(arr[a][b])

def main():
  n = int(input().strip())
  q = int(input().strip())
  a = defaultdict(list)
  for i in range(n):
    for j in range(n):
      a[i].append(n*i+j)

  for i in range(q):
    query = list(map(int, input().strip().split()))
    if query[0] == 1:
      replace_row(a, query[1]-1, query[2]-1)
    elif query[0] == 2:
      replace_column(a, query[1]-1, query[2]-1)
    elif query[0] == 3:
      a = transpose(a)
    elif query[0] == 4:
      print_matrix(a, query[1]-1, query[2]-1)

main()
