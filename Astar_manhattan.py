import collections
from multiprocessing import Queue
from Queue import PriorityQueue
import copy

board=[]
maxLength=0

boxRobot=[]
wallsStorageSpaces=[]
possibleMoves = {'U':[-1,0], 'R':[0,1],'D':[1,0],'L':[0,-1]}

maxRowLength = 0	
lines=0
print "Enter the board configuration:\n\n"
while(1):
	line =raw_input()
	if line!="":
		lines+=1
		board.append(line)
		if len(line)>maxRowLength:
			maxRowLength=len(line)
	else:
		break	

import time
time_start = time.clock()
for i in range(0,lines):
	boxRobot.append([])
	wallsStorageSpaces.append([])
	for j in range(0,maxRowLength):
		boxRobot[-1].append('-')
		wallsStorageSpaces[-1].append('-')

for i in range(0,len(board)):
	if len(board[i])<maxRowLength:
		for j in range(len(board[i]),maxRowLength):
			board[i]+='O'

for i in range(0,len(board)):
	for j in range(0,maxRowLength):
		if board[i][j]=='B' or board[i][j]=='R':
			boxRobot[i][j]=board[i][j]
			wallsStorageSpaces[i][j]=' '
		elif board[i][j]=='S' or board[i][j]=='O':
			wallsStorageSpaces[i][j] = board[i][j]
			boxRobot[i][j] = ' '
		elif board[i][j]==' ':
			boxRobot[i][j] = ' '
			wallsStorageSpaces[i][j]=' '
		elif board[i][j] == '*':
			boxRobot[i][j] = 'B'
			wallsStorageSpaces[i][j] = 'S'
		elif board[i][j] == '.':
			boxRobot[i][j] = 'R'
			wallsStorageSpaces[i][j] = 'S'

storages = []
for i in range(0,lines):
	for j in range(0,maxRowLength):
		if wallsStorageSpaces[i][j]=='S':
			storages.append([i,j])

# print storages
def manhattan(state):
	distance = 0
	for i in range(0,lines):
		for j in range(0,maxRowLength):
			if state[i][j] == 'B':
				temp= 9999999
				for storage in storages:
					distanceToNearest = abs(storage[0]-i)+abs(storage[1]-j)
					if temp > distanceToNearest:
						temp = distanceToNearest
				# print i,j,temp
				distance+=temp
	return distance

print "Solving using A star with Manhattan as heuristic\n"

movesList=[]
visitedMoves=[]

queue = PriorityQueue()
source = [boxRobot,movesList]
if boxRobot not in visitedMoves:
	visitedMoves.append(boxRobot)
queue.put((manhattan(boxRobot),source))
robot_x = -1
robot_y = -1
completed = 0

while not queue.empty() and completed==0:
	temp = queue.get()
	curPosition = temp[1][0]
	movesTillNow = temp[1][1]
	stepsTillNow= len(movesTillNow)
	for i in range(0,lines):
		for j in range(0,maxRowLength):
			if curPosition[i][j]=='R':
				robot_y = j
				robot_x = i
				break
		else:
			continue
		break

	for key in possibleMoves:
		robotNew_x = robot_x+possibleMoves[key][0]
		robotNew_y = robot_y+possibleMoves[key][1] 
		curPositionCopy = copy.deepcopy(curPosition)
		movesTillNowCopy = copy.deepcopy(movesTillNow)

		if curPositionCopy[robotNew_x][robotNew_y] == 'B':
			boxNew_x = robotNew_x + possibleMoves[key][0]
			boxNew_y = robotNew_y + possibleMoves[key][1]
			if curPositionCopy[boxNew_x][boxNew_y]=='B' or wallsStorageSpaces[boxNew_x][boxNew_y]=='O':
				continue
			else:
				curPositionCopy[boxNew_x][boxNew_y]='B'
				curPositionCopy[robotNew_x][robotNew_y] = 'R'
				curPositionCopy[robot_x][robot_y] = ' '
				if curPositionCopy not in visitedMoves:
					matches= 0
					for k in range(0,lines):
						for l in range(0,maxRowLength):
							if wallsStorageSpaces[k][l]=='S':
								if curPositionCopy[k][l]!='B':
									matches=1
					movesTillNowCopy.append(key)
					if matches == 0:
						completed = 1
						print movesTillNowCopy
					else:
						queue.put((manhattan(curPositionCopy)+stepsTillNow,[curPositionCopy,movesTillNowCopy]))
						visitedMoves.append(curPositionCopy)
		else:
			if wallsStorageSpaces[robotNew_x][robotNew_y]=='O' or curPositionCopy[robotNew_x][robotNew_y]!=' ':
				continue
			else:
				curPositionCopy[robotNew_x][robotNew_y]='R'
				curPositionCopy[robot_x][robot_y]=' '
				if curPositionCopy not in visitedMoves:
					movesTillNowCopy.append(key)
					queue.put((manhattan(curPositionCopy)+stepsTillNow,[curPositionCopy,movesTillNowCopy]))
					visitedMoves.append(curPositionCopy)

if completed==0:
	print "Can't make it"

time_end = time.clock()
print "Run time: "+str(time_end - time_start)