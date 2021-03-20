#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

def main():
	q, h, s, d = list(map(int, input().strip().split()))
	n = list(map(int, input().strip().split()))[0]
	min1 = min(4*q,2*h,s)
	min2 = min(min1*2, d)
	result = n // 2 * min2 + n % 2 * min1
	print(result)
	
main()
