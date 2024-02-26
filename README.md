# Artificial Intelligence

Implement a Wumpus World Agent using python:
There is an agent who can move in n x n grid (one step at a time). Cells can have wampus, pit, Gold, or nothing. Smell around the wumpus and breeze around the pit. The agent will be killed if he enters the wampus cell. The agent can kill a wampus if he shoots an arrow (provided the wumpus is in the adjacent cell faced by the agent). The objective of the agent is to get the Gold (not to kill wumpus). Following are the rules.
1. Let number of pit be p where p >= 0 as per the setting of environment. The agent did not know the value of p.
2. Let number of wumpus be w where w >= 0 as per the setting of environment. The agent did not know the
value of w.
3. Let number of arrow be m where m >= w as per the setting of environment. The agent can see the value of m.
4. Agent can move in a cell adjacent to its current location (one cell only). Only horizontal and vertical movement
is allowed. No diagonal movement. Any attempt to get down the nxn grid (corner moves) gives him a bump, and he remains in the same cell.
5. Cost of actions
Attempt to move up, down, left, right -1
Shoot arrow -10
Grab Gold 150
6. Agent is always in cell (1,1) at the beginning. No pit or wumpus in the cell (1,1)
7. Agent dies if it enters a cell of live wumpus (Game over). Dead wumpus disappears. Wumpus screams after being hit by an arrow, and the same can be heard by the agent using the sensor.
8. Agent entering in pit gets stuck. This is again Game over.
9. There is only one gold.
10. Environment is static.
11. Agent can move using GO up/down/left/right
12. Agent can focus arrow by SHOOT up/down/left/right

1.1 Logistic
1. Write code in PYTHON. It should run on version 3 and above without any errors.
2. Code should take a file as a parameter to set the environment (say \env1.txt").
- First line specifies the size of the grid (if the grid is 25 x 25 first line is 25).
- Second line specifies the number of arrows (say 3).
- Every subsequent line specifies one pit/gold or wumpus location.

  "p 2 5" specifies a pit at (2,5) location

  "w 3 7" specifies a wumpus at (3,7) location

  "g 8 4" specifies a GOLD at (8,4) location

A valid environment file is as below.

20

5

p 5 5

w 2 2

p 4 2

p 6 2

g 10 5

w 6 3

w 9 9

p 11 3

Here agent is in 20 x 20 tile with 5 arrows. There are 4 pits and 3 wumpuses. Gold is at (10,5)

3. Code should output the moves taken by the agent
