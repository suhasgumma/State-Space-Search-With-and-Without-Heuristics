import math

#Priority Queue using Heaps
class PriorityQueue():
	def __init__(self):
		self.data = []

	def swap(self, present, parent):
		temp = self.data[present]
		self.data[present] = self.data[parent]
		self.data[parent] = temp


	def isEmpty(self):
		return len(self.data) == 0

	def enqueue(self, path, manhattanDistance):
		self.data.append({"path": path, "manhattanDistance": manhattanDistance})
		self.bubbleUp()

	def dequeue(self):
		self.swap(0, len(self.data)-1)
		popped = self.data.pop()
		self.sinkDown()
		return popped

	def bubbleUp(self):
		present = (len(self.data))-1
		parent = math.floor((present-1)/2)

		if(parent < 0):
			return


		while self.data[parent]["manhattanDistance"] > self.data[present]["manhattanDistance"]:
			self.swap(present, parent)
			present = parent
			parent = math.floor((present-1)/2)
			if parent < 0:
				break






	def sinkDown(self):
		minimum = 0
		present = 0

		if len(self.data) < 2:
			return

		if len(self.data) == 2:
			if self.data[0]["manhattanDistance"] > self.data[1]["manhattanDistance"]:
				self.swap(0,1)
			return

		
		left = (2 * present) + 1
		right = (2 * present) + 2

		while self.data[present]["manhattanDistance"] > self.data[left]["manhattanDistance"] or self.data[present]["manhattanDistance"] > self.data[right]["manhattanDistance"]:
			if self.data[left]["manhattanDistance"] == min(self.data[left]["manhattanDistance"], self.data[right]["manhattanDistance"]):
				minimum = left
			else:
				minimum = right

			self.swap(present, minimum)

			present = minimum
			left = (2 * present) + 1
			right = (2 * present) + 2

			if left >= len(self.data):
				return

			if right >= len(self.data):
				if self.data[present]["manhattanDistance"] > self.data[left]["manhattanDistance"]:
					self.swap(present, left)
				return



# Pqueue = PriorityQueue()

# Pqueue.enqueue(23,11)
# Pqueue.enqueue(12,12)
# Pqueue.enqueue(2,4)
# Pqueue.enqueue(24,6)

# print(Pqueue.data)

# print(Pqueue.dequeue())
# print(Pqueue.dequeue())
# print(Pqueue.dequeue())
# print(Pqueue.dequeue())
