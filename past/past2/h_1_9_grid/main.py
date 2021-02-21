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
  n, m = list(map(int, input().strip().split()))
  a = []
  d = defaultdict(int)

  for i in range(n):
    a.append(list(input().strip()))

  for line in a:
    for c in line:
        if c != 'S' and c != 'G':
            d[c] = 1

  if len(d.keys()) < 9:
      print(-1)
      sys.exit()

  g = defaultdict(list)
  edge_dict = defaultdict(list)
  flow = list('S123456789G')

  for i in range(n):
    for j in range(m):
      edge_dict[a[i][j]].append((i,j))

  for c_i in range(len(flow)-1):
    for i1, j1 in edge_dict[ flow[c_i] ]:
      for i2, j2 in edge_dict[ flow[c_i+1] ]:
        cost = abs(i1-i2) + abs(j1-j2)
        g[i1*m+j1].append((i2*m+j2, cost))

  e = edge_dict["S"][0]
  start = e[0] * m + e[1]
  e = edge_dict["G"][0]
  end = e[0] * m + e[1]

  dist = dijkstra(n*m, g, start)
  print(dist[end])

main()
