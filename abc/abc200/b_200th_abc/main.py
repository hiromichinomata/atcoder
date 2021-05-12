#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

def main():
	n, k = list(map(int, input().strip().split()))
	for i in range(k):
		if n % 200 == 0:
			n //= 200
		else:
			n = 1000*n+200
	print(n)

main()
