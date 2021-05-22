#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

def main():
	k = list(map(int, input().strip().split()))[0]
	result = 0
	for i in range(1, k+1):
		for j in range(1, k+1):
			if i * j > k:
				break
			result += k // (i*j)
	print(result)

main()
