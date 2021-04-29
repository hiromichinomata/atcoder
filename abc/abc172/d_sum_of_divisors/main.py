#!/bin/python3
# pypy3

import sys
# input = sys.stdin.readline
import math

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

def main():
	n = list(map(int, input().strip().split()))[0]
	data = [0] * (n+1)
	for i in range(1, n+1):
		for j in range(i, n+1, i):
			data[j] += 1
	result = 0
	for i in range(1, n+1):
		result += i *  data[i]
	print(result)

main()
