#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

def main():
	n = list(map(int, input().strip().split()))[0]
	a = [0]*n
	c = [[] for i in range(n)]
	for i in range(n):
		c[i] = list(map(int, input().strip().split()))
		a[i] = c[i][0]
	min_a = min(a)
	a = list(map(lambda x: x - min_a, a))
	b = list(map(lambda x: x - min(c[0]), c[0]))
	if a[0] + b[0] > c[0][0]:
		print('No')
		sys.exit()
	diff = c[0][0] - a[0] - b[0]
	b = list(map(lambda x: x + diff, b))
	for i in range(n):
		for j in range(n):
			if a[i] + b[j] != c[i][j]:
				print('No')
				sys.exit()
	print('Yes')
	print(' '.join(map(str, a)))
	print(' '.join(map(str, b)))


main()
