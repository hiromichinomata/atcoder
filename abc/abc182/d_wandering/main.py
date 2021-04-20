#!/bin/python3

import sys
# input = sys.stdin.readline
import math

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

def main():
	n = list(map(int, input().strip().split()))[0]
	a = list(map(int, input().strip().split()))
	pos = [0] * (n+1)
	tmp = 0
	pos_max = [0] * (n+1)
	tmp_max = 0
	for i in range(1, n+1):
		tmp += a[i-1]
		pos[i] = pos[i-1]+tmp
		tmp_max = max(tmp_max, tmp)
		pos_max[i] = tmp_max
	result = 0
	for i in range(n):
		result = max(result, pos[i], pos[i]+pos_max[i+1])

	print(result)

main()
