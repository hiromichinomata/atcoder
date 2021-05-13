#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

def main():
	n = list(map(int, input().strip().split()))[0]
	a = list(map(int, input().strip().split()))
	data = [0] * 200
	
	for i in range(n):
		data[a[i] % 200] += 1
	result = 0
	for i in range(200):
		num = data[i]
		if num > 1:
			result += num * (num-1) // 2
	print(result)

main()
