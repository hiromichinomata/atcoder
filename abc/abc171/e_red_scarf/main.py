#!/bin/python3

import sys
# input = sys.stdin.readline
import math

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

def main():
	n = list(map(int, input().strip().split()))[0]
	a = list(map(int, input().strip().split()))
	a_sum = 0

	for i in range(n):
		a_sum ^= a[i]
	result = [0] * n
	for i in range(n):
		result[i] = a_sum ^ a[i]
	result = map(str, result)
	print(' '.join(result))

main()
