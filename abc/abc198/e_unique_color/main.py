#!/bin/python3

import sys
# input = sys.stdin.readline
from collections import defaultdict

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

visited = []
d = []

def visit(index, c, routes):
	count = 0
	global visited
	global d
	visited[index] = True
	for i in routes[index]:
		if not visited[i]:
			d[c[i]] += 1
			if d[c[i]] == 1:
				count += 1
				count += visit(i, c, routes)
	return count

def main():
	n = list(map(int, input().strip().split()))[0]
	c = list(map(int, input().strip().split()))
	routes = [[] for i in range(n)]
	for i in range(n-1):
		a, b = list(map(int, input().strip().split()))
		a -= 1
		b -= 1
		routes[a].append(b)
		routes[b].append(a)

	global d
	d = defaultdict(int)
	global visited
	visited = [False]*n
	result = visit(0, c, routes)
	print(result)

main()
