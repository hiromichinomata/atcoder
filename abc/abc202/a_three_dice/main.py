#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

def main():
	nums = list(map(int, input().strip().split()))
	result = 21 - sum(nums)
	print(result)

main()
