#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

def main():
	n, x, m = list(map(int, input().strip().split()))
	data = [0] * (10**5+1)
	data[x] = 1
	start = end = 1
	orig_x = x
	for i in range(2, n+1):
		x = x**2 % m
		if data[x] != 0:
			start = x
			end = i
			break
		else:
			data[x] = i
	result = x = orig_x
	for i in range(2, start):
		x = x**2 % m
		result += x
	num = 0
	for i in range(start, end):
		x = x**2 % m
		num += x
	if start < end:
		result += (n-start)//(end-start)*num
	else:
		end += 1
	for i in range(end, n+1):
		x = x**2 % m
		result += x
	print(result)

main()
