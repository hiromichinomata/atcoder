#!/bin/python3

import sys
sys.setrecursionlimit(100000)
# input = sys.stdin.readline

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

dp = []

def solve(num, n):
	global dp
	if num == 3:
		return 1
	result = 0
	for i in range(3, num+1-3):
		if dp[i] == -1:
			dp[i] = solve(i, n)
		result += dp[i]
	return (result +1) % (10**9+7)

def main():
	n = list(map(int, input().strip().split()))[0]
	if n < 3:
		print(0)
		sys.exit()
	global  dp
	dp = [-1]*(n+1)
	result = solve(n, n)
	print(result)

main()
