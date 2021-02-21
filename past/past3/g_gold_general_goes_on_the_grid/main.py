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
  n, x, y = list(map(int, input().strip().split()))
  x = x + 210
  y = y + 210
  weight = [[1] * 420 for i in range(420)]
  move = [(1,1), (0,1), (-1,1), (1,0), (-1,0), (0,-1)]

  for i in range(n):
    a, b = list(map(int, input().strip().split()))
    a += 210
    b += 210
    weight[a][b] = 10000

  g = defaultdict(list)
  for i in range(5, 415):
    for j in range(5, 415):
      for a,b in move:
        pos = 420*(i+a)+j+b
        cost = weight[i+a][j+b]
        g[420*i+j].append((pos, cost))

  start = 420*210+210
  dist = dijkstra(1700*1700, g, start)
  end = 420*x+y
  result = dist[end]
  if result >= 10000:
    print(-1)
  else:
    print(result)

main()
