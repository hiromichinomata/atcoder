#!/bin/python3

import sys
# input = sys.stdin.readline
import math

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

def main():
	n = list(map(int, input().strip().split()))[0]
	a = list(map(int, input().strip().split()))
	max_a = max(a)
	count = [0] * (max_a+1)
	for num in a:
		for i in range(num, max_a+1, num):
			count[i] += 1
	result = 0
	for num in a:
		if count[num] == 1:
			result += 1
	print(result)

main()
