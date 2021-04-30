#!/bin/python3

import sys
# input = sys.stdin.readline
import math

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

def main():
	n = list(map(int, input().strip().split()))[0]
	a = list(map(int, input().strip().split()))
	if 1 in a:
		print('pairwise coprime')
		sys.exit()

	max_a = max(a)+1
	data = [0] * max_a
	for num in a:
		data[num] += 1

	max_result = 0
	for i in range(2, max_a):
		result = 0
		for j in range(i, max_a, i):
			if data[j] != 0:
				result += data[j]
				if result > 1:
					break
		max_result = max(result, max_result)

	if max_result == 1:
		print('pairwise coprime')
		sys.exit()

	result = a[0] 
	for i in range(1, n):
		result = math.gcd(result, a[i])
		if result == 1:
			break
	if result == 1:
		print('setwise coprime')
	else:
		print('not coprime')

main()
