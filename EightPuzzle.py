import copy

# Time-Complexity  *f(n) = 9 *O(1)
def findPosOfBlank(state):
	for i in range(3):
		for j in range(3):
			if state[i][j] == 0:
				return (i,j)


def newStateAfterSwap(state, prevI, prevJ, newI, newJ):

	newState = copy.deepcopy(state)

	temp = newState[prevI][prevJ]

	newState[prevI][prevJ] = newState[newI][newJ]

	newState[newI][newJ] = temp

	return newState


def allNextStates(state):
	i = findPosOfBlank(state)[0]
	j = findPosOfBlank(state)[1]

	

	stateList = []

	#Top if i > 0
	if i > 0:
		stateList.append(newStateAfterSwap(state, i, j, i-1, j))
		

	#Left j >0
	if j > 0:
		stateList.append(newStateAfterSwap(state, i, j, i, j-1))
		
		
	#Right j < 2
	if j < 2:
		stateList.append(newStateAfterSwap(state, i, j, i, j +1))
		

	#Down i < 2
	if i < 2:
		stateList.append(newStateAfterSwap(state, i, j, i+1, j))
		




	return stateList



# Time-Complexity  *f(n) = 9 *O(1)
def isGoal(state, goalState):
	return state == goalState

#Creating a new path to push into Open
def createPath(popped, state):
	newPath = popped.append(state)
	return newPath