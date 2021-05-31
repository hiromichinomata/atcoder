#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

def main():
	n = list(map(int, input().strip().split()))[0]
	a = list(map(int, input().strip().split()))
	max_a = 0
	result = 0
	sum_a = 0
	
	for i in range(n):
		prev_max = max_a
		max_a = max(a[i], max_a)
		sum_a += a[i]
		result += i * (max_a - prev_max) + sum_a + max_a
		print(result)

main()
