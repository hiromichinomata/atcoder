#!/bin/python3

import sys
input = sys.stdin.readline
from collections import defaultdict

# n: 頂点数
# g[v] = {(w, cost)}:
#     頂点vから遷移可能な頂点(w)とそのコスト(cost)
# s: 始点の頂点

from heapq import heappush, heappop
INF = float("inf")

def dijkstra(n, g, s):
    dist = [INF] * n
    que = [(0, s)]
    dist[s] = 0
    while que:
        c, v = heappop(que)
        if dist[v] < c:
            continue
        for t, cost in g[v]:
            if dist[v] + cost < dist[t]:
                dist[t] = dist[v] + cost
                heappush(que, (dist[t], t))
    return dist

def main():
  n, l = list(map(int, input().strip().split()))
  x = list(map(int, input().strip().split()))
  t = list(map(int, input().strip().split()))

  board = [0] * (l+5)
  for i in x:
    board[i] = 1

  g = defaultdict(list)
  for i in range(l):
    for j in range(3):
      if j == 1:
        pos = i+1
        cost = t[0]
      elif j == 2:
        pos = i+2
        cost = t[0] + t[1]
      else:
        pos = i+4
        cost = t[0] + t[1] * 3

      if board[i] == 1:
        cost += t[2]
      g[i].append((pos, cost))

  start = 0
  dist = dijkstra(l+5, g, start)
  end = l
  result = dist[end]
  print(result)

main()
