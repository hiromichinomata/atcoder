#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

def main():
	n = list(map(int, input().strip().split()))[0]
	d = [0] * (10**5+1)
	a = list(map(int, input().strip().split()))
	for i in range(n):
		d[a[i]] += 1
	q = list(map(int, input().strip().split()))[0]
	result = sum(a)
	for _ in range(q):
		b, c = list(map(int, input().strip().split()))
		result -= d[b] * b
		result += d[b] * c
		d[c] += d[b]
		d[b] = 0
		print(result)

main()
