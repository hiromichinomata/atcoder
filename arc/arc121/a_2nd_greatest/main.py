#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

def main():
	n = list(map(int, input().strip().split()))[0]
	houses = [[] for i in range(n)]
	for i in range(n):
		x, y = list(map(int, input().strip().split()))
		houses[i] = [x, y, i]
	x_houses = sorted(houses)
	candidates = set()
	for i in [0, 1, -2, -1]:
		candidates.add(x_houses[i][2])
	y_houses  = sorted(houses, key=lambda x: x[1])
	for i in [0, 1, -2, -1]:
		candidates.add(y_houses[i][2])
	candidates = sorted(list(candidates))
	result = []
	for ci in range(len(candidates)-1):
		for cj in range(ci+1, len(candidates)):
			i = candidates[ci]
			j = candidates[cj]
			v = max(abs(houses[i][0]-houses[j][0]), abs(houses[i][1]-houses[j][1]))
			result.append(v)
	print(sorted(result)[-2])

main()

