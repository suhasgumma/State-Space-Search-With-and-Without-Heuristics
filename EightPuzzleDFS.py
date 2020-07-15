import EightPuzzle
import copy

def DFS(Start, Goal):
	visited = []

	opened = [[Start]]

	count = 0


	while len(opened) > 0:

		count += 1
		print(count)

		successors = []

		popped = opened.pop()

		statePopped = popped[len(popped)-1]

		print(statePopped)

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
			opened.append(path)

		


	return "Goal State Not Found"



Start = [[2,8,3], [1,6,4], [7,0,5]]

Goal = [[3,6,4], [2,0,1], [5,7,8]]



list1 = DFS(Start, Goal)






