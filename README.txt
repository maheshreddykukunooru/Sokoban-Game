
## Format of input:

O - Obstacle

S - Storage

B - Block

R - Robot

'*' - Block on strage space

'.' - Robot on storage space

## How to compile and execute:

I have implemented all the algorithms in 6 different files, named bfs.py, dfs.py, greedy_manhattan.py, Astar_manhattan.py, greedyOwnHeuristic.py and Astar-ownHeuristic.py

	- python <program> is enough to run the program if user wants to give input manually** 
	
	After running the program, it asks to enter the intial configuration, where we should enter input in the above format and type an **extra line** after the input so that, the program understands that the input is done.


	Or if the input is stored in a file, we can also do

	 - python <program> < input.txt

	 For example, 

	 				----- python bfs.py < exampleInput.txt

**Note: input.txt also has to contain 2 new lines after the input**


bfs.py is commented neatly. As all the programs are almost similiar except the operations on queue and prioritizing the elements in queue using the heuristics, all the programs are not commented.



## Heuristic:

Intially, Greedy best first search and A* search are implemented using Manhattan distance between blocks and the nearest storage spaces. In this the distance from blocks to storage spaces is only considered. But consider a situation when there is a tie between the moves where this distance doesn't change i.e, the robot moves into an empty space without moving a block. In this case, we can prioritize the moves based on the distance from robot to all blocks. Using this we always move in a direction which is closer to blocks rather than moving away from them. This heuristic can come to rescue when there are many empty spaces where all the unnecessary moves into the empty spaces away from the blocks can be avoided. Also I considered another heuristic which is the number of storage spaces unoccupied at any time. It is also admissible as the probability of finding a solution from a position where almost all storage spaces are occupied is greater than vice versa. It's always better to consider a move which still has one unoccupied storage space among the 5 storage spaces rather than the one which has only one occupied.

	My heuristic funciton is a combination of all the above three, which is

		f(n) = Manhattan(box<->storages) + Distance(box<->robot) + storageSpacesLeft * 2;

	I have used 2* storageSpacesLeft to provide more weightage to storageSpacesLeft because it's always a lesser number compared to other two.

## Analysis:

BFS always returns an optimal solution as it checks for the solution level by level but it is slow.
DFS opens a node and continues among its children untill it reaches a leaf node, but it is sometimes fast but gives a longer path to reach solution.
Greedy Best first considers heuristic to move faster towards the goal, and thus it is faster.
A* is a combination of both BFS and greedy, so it outputs the optimal solution and is faster than BFS.

We'll analyze the run times and outputs for the following input:

###Input - 1

	OOOO
	OSROO
	OBBSO
	O B O
	O S O
	OO  O
	 OOOO

BFS: ['L', 'D', 'R', 'D', 'R', 'D', 'D', 'L', 'U', 'L', 'U', 'U', 'R', 'D']
Run time: 0.049024

DFS: ['L', 'D', 'R', 'D', 'R', 'D', 'D', 'L', 'U', 'L', 'U', 'U', 'R', 'D']
Run time: 0.121407

Greedy_manhattan: ['L', 'D', 'R', 'D', 'R', 'D', 'D', 'L', 'U', 'L', 'U', 'U', 'R', 'D']
Run time: 0.038888

A*_manhattan: ['L', 'D', 'R', 'D', 'R', 'D', 'D', 'L', 'U', 'L', 'U', 'U', 'R', 'D']
Run time: 0.051323

Greedy_OwnHeuristic: ['L', 'D', 'R', 'D', 'R', 'D', 'D', 'L', 'U', 'L', 'U', 'U', 'R', 'D']
Run time: 0.034194

A*_Ownheuristic: ['L', 'D', 'R', 'D', 'R', 'D', 'D', 'L', 'U', 'L', 'U', 'U', 'R', 'D']
Run time: 0.049421


We can observe that both Greedy search algorithms are faster as expected, in this case all the methods gave the same path to the solution.

###Input - 2 

	  OOOOOO
	OOOSO  O
	O    B OO
	O B R  SO
	OOO O OOO
	  OBO O
	  O  SO
	  OOOOO

BFS: ['R', 'D', 'D', 'D', 'L', 'L', 'U', 'U', 'U', 'U', 'L', 'L', 'D', 'R', 'R', 'R', 'R', 'R', 'U', 'U', 'L', 'D', 'D', 'D', 'D']
Run time: 33.390089

DFS: ['L', 'U', 'L', 'L', 'D', 'R', 'U', 'R', 'R', 'D', 'R', 'D', 'D', 'D', 'L', 'L', 'U', 'D', 'R', 'R', 'U', 'U', 'U', 'L', 'L', 'U', 'L', 'L', 'D', 'R', 'R', 'U', 'R', 'R', 'L', 'L', 'D', 'D', 'U', 'U', 'R', 'R', 'D', 'L', 'L', 'U', 'R', 'R', 'D', 'D', 'D', 'D', 'L', 'L', 'U', 'D', 'R', 'R', 'U', 'U', 'U', 'L', 'L', 'U', 'L', 'L', 'D', 'R', 'U', 'R', 'R', 'R', 'U', 'R', 'D', 'L', 'L', 'L', 'L', 'D', 'R', 'D', 'U', 'U', 'R', 'R', 'D', 'L', 'L', 'U', 'R', 'R', 'D', 'D', 'D', 'D', 'L', 'L', 'U', 'D', 'R', 'R', 'U', 'U', 'U', 'R', 'L', 'L', 'L', 'D', 'U', 'U', 'L', 'L', 'D', 'R', 'U', 'R', 'R', 'D', 'R', 'D', 'D', 'D', 'L', 'L', 'U', 'D', 'R', 'R', 'U', 'U', 'U', 'L', 'U', 'L', 'L', 'D', 'R', 'U', 'R', 'R', 'D', 'D', 'D', 'D', 'L', 'L', 'U', 'U', 'U', 'L', 'U', 'R', 'D', 'D', 'D', 'D', 'R', 'R', 'U', 'U', 'U', 'L', 'L', 'D', 'D', 'D', 'R', 'R', 'U', 'U', 'U', 'U', 'L', 'D', 'L', 'U', 'L', 'L', 'D', 'R', 'U', 'R', 'D', 'D', 'U', 'U', 'R', 'R', 'D', 'D', 'D', 'D', 'L', 'L', 'U', 'U', 'U', 'L', 'U', 'R', 'R', 'L', 'D', 'D', 'D', 'D', 'R', 'R', 'U', 'U', 'U', 'R', 'U', 'U', 'L', 'D', 'D', 'D', 'D']
Run time: 46.226894

Greedy_manhattan: ['R', 'D', 'D', 'D', 'L', 'L', 'U', 'U', 'U', 'U', 'D', 'D', 'D', 'D', 'R', 'R', 'U', 'U', 'U', 'R', 'U', 'L', 'D', 'D', 'D', 'D', 'L', 'L', 'U', 'U', 'U', 'U', 'L', 'L', 'D', 'R', 'R', 'R', 'R', 'R', 'L', 'D', 'D', 'D', 'L', 'L', 'U', 'U', 'U', 'U', 'R', 'D', 'R', 'R', 'U', 'U', 'L', 'D', 'D', 'D', 'D']
Run time: 5.665106

A*_manhattan: ['R', 'D', 'D', 'D', 'L', 'L', 'U', 'U', 'U', 'U', 'L', 'L', 'D', 'R', 'R', 'R', 'R', 'R', 'U', 'U', 'L', 'D', 'D', 'D', 'D']
Run time: 7.050841

Greedy_OwnHeuristic: ['U', 'R', 'D', 'L', 'L', 'U', 'L', 'L', 'D', 'R', 'R', 'U', 'R', 'R', 'D', 'D', 'D', 'D', 'L', 'L', 'U', 'U', 'U', 'U', 'D', 'R', 'U', 'R', 'U', 'R', 'D', 'L', 'D', 'R', 'L', 'D', 'D']
Run time: 1.75507

A*_Ownheuristic: ['R', 'D', 'D', 'D', 'L', 'L', 'U', 'U', 'U', 'U', 'L', 'L', 'D', 'R', 'R', 'R', 'R', 'R', 'U', 'U', 'L', 'D', 'D', 'D', 'D']
Run time: 4.733036


In this case also, Greedy methods are faster than the others, and we can clearly see that my heuristic is faster than using just the manhattan distance.
We can also observe that DFS gave a longer path as output.

###Input - 3:

	OOOOOOO
	O     O
	O     O
	OS O  O
	OS BB O
	OSBB  O
	OSO  RO
	OOOOOOO


DFS: ['L', 'U', 'U', 'L', 'L', 'U', 'L', 'D', 'D', 'U', 'U', 'U', 'U', 'R', 'R', 'D', 'R', 'D', 'D', 'R', 'D', 'D', 'L', 'L', 'U', 'L', 'U', 'L', 'U', 'U', 'U', 'R', 'R', 'D', 'R', 'D', 'D', 'L', 'L', 'D', 'R', 'D', 'R', 'U', 'L', 'L', 'U', 'U', 'L', 'U', 'U', 'R', 'R', 'D', 'R', 'D', 'D', 'R', 'D', 'L', 'D', 'L', 'U', 'L', 'U', 'U', 'L', 'U', 'U', 'R', 'R', 'D', 'R', 'D', 'D', 'L', 'D', 'L', 'U', 'U', 'L', 'U', 'U', 'R', 'R', 'D', 'L', 'U', 'L', 'D']
Run time: 30.057636


Greedy_manhattan: ['L', 'U', 'U', 'L', 'L', 'R', 'R', 'D', 'D', 'L', 'U', 'R', 'U', 'L', 'D', 'D', 'R', 'R', 'U', 'U', 'U', 'U', 'L', 'D', 'D', 'R', 'D', 'L', 'U', 'U', 'U', 'L', 'L', 'D', 'L', 'D', 'D', 'U', 'U', 'R', 'U', 'R', 'R', 'D', 'D', 'D', 'D', 'L', 'U', 'L', 'U', 'D', 'R', 'R', 'U', 'L', 'L', 'U', 'D', 'D', 'R', 'R', 'U', 'U', 'U', 'L', 'L', 'U', 'L', 'D']
Run time: 6.214863

Greedy_ownHeuristic: ['L', 'U', 'U', 'L', 'L', 'U', 'L', 'D', 'D', 'U', 'R', 'R', 'R', 'D', 'D', 'L', 'U', 'L', 'R', 'R', 'U', 'L', 'L', 'U', 'U', 'R', 'R', 'D', 'D', 'L', 'D', 'D', 'R', 'U', 'R', 'U', 'L', 'L', 'D', 'L', 'U', 'U', 'L', 'U', 'R', 'D', 'D', 'R', 'R', 'U', 'U', 'L', 'L', 'U', 'L', 'D']
Run time: 0.511531

For the above input, only three algorithms gave ouput, but BFS and A* algorithms runs forever in finding the solution. The reason for this may be due to the number of empty spaces, where there are many moves where the robot tries to move away from the blocks most of the time. 













