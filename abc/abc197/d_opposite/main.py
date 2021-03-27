#!/bin/python3

import sys
input = sys.stdin.readline
import math
import numpy as np

def main():
  n = list(map(int, input().strip().split()))[0]
  x0, y0 = list(map(int, input().strip().split()))
  xo, yo = list(map(int, input().strip().split()))
  mx = (x0 + xo)/2
  my = (y0 + yo)/2
  x = x0 - mx
  y = y0 - my
  rad = 2 * math.pi/n
  cos = np.cos(rad)
  sin = np.sin(rad)
  rx = (x * cos) -  (y * sin) + mx
  ry = (x * sin) + (y * cos) + my
  print(" ".join([str(rx), str(ry)]))

main()
