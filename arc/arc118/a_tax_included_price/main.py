#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

def main():
	t, n = list(map(int, input().strip().split()))
	count = 0
	ngs = []
	for i in range(1, 100+t):
		num = i*(100+t)//100
		if num < 100+t:
			ngs.append(num)
	oks = [i for i in range(1, 100+t) if i not in ngs]
	l = len(oks)
	result = ((n-1)//l) * (100+t) + oks[(n-1)%l]
	print(result)
main()
