[Sokoban](https://en.wikipedia.org/wiki/Sokoban) is a puzzle game where the player has to move boxes into storage locations with some obstacles in between. You can play online version of the game [here](http://www.game-sokoban.com/).
### Input Format

O - Obstacle  
S - Storage  
B - Block  
R - Robot

"*****" - Block on strage space  
"**.**" - Robot on storage space

### How to compile and execute

I have implemented all the algorithms in 6 different files, named bfs.py, dfs.py, greedy_manhattan.py, Astar_manhattan.py, greedyOwnHeuristic.py and Astar-ownHeuristic.py

	if user wants to give input manually  
	python bfs.py

An **extra line** should bee provided after the input configuration is typed in so that, the program understands that the input is done. You can look at the *exampleInput.txt* to know how to give the input.


	Or if the input is stored in a file, we can even do
	python bfs.py < exampleInput.txt

**Note: input.txt also has to contain 2 new lines after the input**

### Heuristic:

* Greedy best first search and A* search are implemented using Manhattan distance between blocks and the nearest storage spaces. In this the distance from blocks to storage spaces is only considered.

	In addition to the above, I now consider the following for the algorithm to work better
* Distance of robot and boxes and
* Number of storage spaces left at any time


		f(n) = Manhattan(box - storages) + Distance(box - robot) + storageSpacesLeft * 2;

		I have used 2* storageSpacesLeft to provide more weightage to storageSpacesLeft because  
		it's always a lesser number compared to other two.

### Analysis:

* BFS always returns an optimal solution as it checks for the solution level by level but it is slow.
* DFS opens a node and continues among its children till it reaches a leaf node, but it is sometimes fast but gives a longer path to reach solution.
* Greedy Best first considers heuristic to move faster towards the goal, and thus it is faster but it doesn't always provide the best solution
* A* is a combination of both BFS and greedy, so it outputs the optimal solution and is faster than BFS.

For some inputs mentioned in *Inputs.txt*, not all algorithms implemented returned a solution such as  BFS and A* algorithms runs forever in finding the solution. The reason for this may be due to the number of empty spaces, where there are many moves where the robot tries to move away from the blocks most of the time. And even we can reduce the time by crossing the tunnel once entered as explained [here](http://sokobano.de/wiki/index.php?title=Solver).
