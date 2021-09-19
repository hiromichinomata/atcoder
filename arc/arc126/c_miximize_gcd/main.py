#!/bin/python3

import sys
input = sys.stdin.readline
import math

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

def main():
	n, k = list(map(int, input().strip().split()))
	a = list(map(int, input().strip().split()))
	result = a[0]
	for i in range(1, n):
		result = math.gcd(result, a[i])
		if result == 0:
			break

	start_gcd = k // n + 1
	result += start_gcd

	print(result)

main()
