#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

def main():
	n = list(map(int, input().strip().split()))[0]
	data = [0] * n
	for i in range(n):
		s, p = list(map(str, input().strip().split()))
		data[i] = [s, -int(p), i+1]
	data = sorted(data)
	for i in range(n):
		print(data[i][2])

main()
