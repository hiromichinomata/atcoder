#!/bin/python3

import sys
input = sys.stdin.readline

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

def main():
	t = list(map(int, input().strip().split()))[0]
	for _ in range(t):
		n2, n3, n4 = list(map(int, input().strip().split()))

		m3 = min(n3 // 2, n4)
		n3 -= m3 * 2
		n4 -= m3

		m3_2 = min(n3 // 2, n2 // 2)
		n3 -= m3_2 * 2
		n2 -= m3_2 * 2

		m4 = min(n4 // 2, n2)
		n4 -= m4 * 2
		n2 -= m4

		m4_2 = min(n4, n2*3)
		n4 -= m4_2
		n2 -= m4_2 * 3

		m2 = n2 // 5

		print(m2+m3+m3_2+m4+m4_2)

main()

# 2 * 5 = 10
# 2 * 2 + 3 * 2 = 10
# 3 * 2 + 4 * 1 = 10
# 2 * 1 + 4 * 2 = 10
# 2 * 3 + 4 * 1 = 10
