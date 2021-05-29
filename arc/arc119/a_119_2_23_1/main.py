#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

def main():
	n = list(map(int, input().strip().split()))[0]
	result = float('inf')
	for b in range(n):
		num = 2**b
		if num > n:
			break
		a = n // num
		c = n - a * num
		result =  min(result, a+b+c)
	print(result)

main()
