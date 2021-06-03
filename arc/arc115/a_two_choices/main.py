#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

def main():
	n,m = list(map(int, input().strip().split()))
	data = [0,0]
	for i in range(n):
		s = list(map(str, input().strip().split()))[0]
		count = 0
		for j in range(m):
			count += int(s[j])
		data[count%2] += 1
	result = data[0] * data[1]
	print(result)

main()
