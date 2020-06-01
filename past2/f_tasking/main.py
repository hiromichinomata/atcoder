#!/bin/python3

import sys
input = sys.stdin.readline
from collections import deque
from queue import PriorityQueue

class MaxPriorityQueue:
  def __init__(self):
    self.queue = PriorityQueue()

  def put(self, item):
    self.queue.put((-item, item))
    return item

  def get(self):
    tmp = self.queue.get()
    return tmp[1]

  def empty(self):
    return self.queue.empty()

def main():
  n = int(input().strip())
  tasks = []
  task_queue = MaxPriorityQueue()
  result = 0

  for i in range(n):
    a, b = list(map(int, input().strip().split()))
    tasks.append((a,b))

  tasks = deque(sorted(tasks, key=lambda x: x[0]))
  for i in range(n):
    while len(tasks) > 0 and tasks[0][0] <= i+1:
      task_queue.put(tasks.popleft()[1])

    result += task_queue.get()
    print(result)

main()
