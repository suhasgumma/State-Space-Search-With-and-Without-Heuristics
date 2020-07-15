#Contains Priority Queue
import EightPuzzle_heuristic_manhattanDistance1
import copy
import EightPuzzle

#Tested and Working
def manhattan_distance(start,goal):
	#store in dict so that I dont need to loop again and again for getting manhattan Distance

	startDict = {}

	manhattanDistance = 0


	for i in range(0,3):
		for j in range(0,3):
			startDict[start[i][j]] = (i,j)
	for x in range(0,3):
		for y in range(0,3):
			p,q = startDict[goal[x][y]]

			manhattanDistance += abs(p-x) + abs(q-y)

	return manhattanDistance

def heuristic_using_manhattan_distance(Start,Goal):
	visited = []

	count = 0

	opened = EightPuzzle_heuristic_manhattanDistance1.PriorityQueue()

	opened.enqueue([Start],manhattan_distance(Start,Goal))

	while not opened.isEmpty():

		count +=1 
		print(count)
		successors = []
		dequeued = opened.dequeue()
		path = dequeued["path"]
		state = path[len(path)-1]

		print(state)

		if state == Goal:
			return path

		print(state)

		visited.append(state)

		allPossibleNextStates = EightPuzzle.allNextStates(state)


		for states in allPossibleNextStates:
			if states not in visited:
				successors.append(states)
				visited.append(states)

		for successor in successors:
			paths = copy.deepcopy(path)
			paths.append(successor)
			opened.enqueue(paths,manhattan_distance(successor, Goal))

	return "State Not Found"


Start = [[2,8,3], [1,6,4], [7,0,5]]

Goal = [[3,6,4], [2,0,1], [5,7,8]]



list1 = heuristic_using_manhattan_distance(Start, Goal)

print("******")

for q in list1:
	print(q)




