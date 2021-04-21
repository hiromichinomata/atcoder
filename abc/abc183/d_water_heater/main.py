#!/bin/python3

import sys
# input = sys.stdin.readline
import math

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

def main():
	n, w = list(map(int, input().strip().split()))
	data = [0] * (2*10**5+1)
	for i in range(n):
		s, t, p = list(map(int, input().strip().split()))
		data[s] += p
		data[t] -= p
	cur = 0
	for i in range(len(data)):
		cur += data[i]
		if cur > w:
			print('No')
			sys.exit()
	print('Yes')

main()
