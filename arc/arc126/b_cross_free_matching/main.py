#!/bin/python3

import sys
input = sys.stdin.readline

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

def main():
	n, m = list(map(int, input().strip().split()))
	lines_0 = [0]*m
	lines_1 = [0]*m
	for i in range(m):
		a, b = list(map(int, input().strip().split()))
		a -= 1
		b -= 1
		lines_0[i] = [a, b]
		lines_1[i] = [b, a]

	lines_0 = sorted(lines_0, key=lambda x: x[0]+x[1])
	lines_1 = sorted(lines_1, key=lambda x: x[0]+x[1])

	result_0 = 0
	x = -1
	y = -1
	for i in range(m):
		a, b = lines_0[i]
		if x < a and y < b:
			x = a
			y = b
			result_0 += 1

	result_1 = 0
	x = -1
	y = -1
	for i in range(m):
		a, b = lines_1[i]
		if x < a and y < b:
			x = a
			y = b
			result_1 += 1

	result = max(result_0, result_1)
	print(result)

main()
