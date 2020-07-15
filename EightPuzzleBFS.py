import EightPuzzle
import copy
import queue

def BFS(Start, Goal):
	visited = []

	opened = queue.Queue()
	opened.put([Start])

	count = 0


	while not opened.empty():

		successors = []

		popped = opened.get()

		statePopped = popped[len(popped)-1]

		count+=1

		# print(statePopped)
		# print(count)

		if statePopped == Goal:
			return popped

		visited.append(statePopped)

		allPossibleNextStates = EightPuzzle.allNextStates(statePopped)


		for state in allPossibleNextStates:
			if state not in visited:
				successors.append(state)
				visited.append(state)

		for successor in successors:
			path = copy.deepcopy(popped)
			path.append(successor)
			opened.put(path)

		


	return "Goal State Not Found"


Start = [[2,8,3], [1,6,4], [7,0,5]]

Goal = [[2,8,0], [3,1,4], [7,6,5]]

list1 = BFS(Start, Goal)

for x in list1:
	print(x)

