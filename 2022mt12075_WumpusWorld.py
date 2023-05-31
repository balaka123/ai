# This is Python code for AI Assignment #1 (Wumpus World)

# To execute the program type:
# python 2022mt12075_WumpusWorld.py <inputfile_name>

import sys

# Argument verification
argLen = len(sys.argv)
if argLen != 2:
    print("Arguments not passed correctly")
    exit(1)
else:
    envFile = sys.argv[1]

# Arguments passed
print("Name of Input File:", envFile)


# def varInit():


class cellDef:

    def __init__(self, row, col):             # Cell location allocation
        self.row = int(row)
        self.col = int(col)


# Enlist the adjacent cells : possible next move
def findAdjcell(row, col):
    if 0 < row < (gridSize - 1) and 0 < col < (gridSize - 1):
        adjList.append(cellDef(row + 1, col))                   # up
        adjList.append(cellDef(row - 1, col))                   # down
        adjList.append(cellDef(row, col - 1))                   # left
        adjList.append(cellDef(row, col + 1))                   # right
    elif row == 0 and col == 0:
        adjList.append(cellDef(row + 1, col))                   # up
        adjList.append(cellDef(row, col + 1))                   # right
    elif row == 0 and 0 < col < (gridSize - 1):
        adjList.append(cellDef(row + 1, col))                   # up
        adjList.append(cellDef(row, col - 1))                   # left
        adjList.append(cellDef(row, col + 1))                   # right
    elif row == 0 and col == (gridSize - 1):
        adjList.append(cellDef(row + 1, col))                   # up
        adjList.append(cellDef(row, col - 1))                   # left
    elif 0 < row < (gridSize - 1) and col == 0:
        adjList.append(cellDef(row + 1, col))                   # up
        adjList.append(cellDef(row - 1, col))                   # down
        adjList.append(cellDef(row, col + 1))                   # right
    elif row == (gridSize - 1) and col == 0:
        adjList.append(cellDef(row - 1, col))                   # down
        adjList.append(cellDef(row, col + 1))                   # right
    elif row == (gridSize - 1) and 0 < col < (gridSize - 1):
        adjList.append(cellDef(row - 1, col))                   # down
        adjList.append(cellDef(row, col - 1))                   # left
        adjList.append(cellDef(row, col + 1))                   # right
    elif row == (gridSize - 1) and col == (gridSize - 1):
        adjList.append(cellDef(row - 1, col))                   # down
        adjList.append(cellDef(row, col - 1))                   # left
    elif 0 < row < (gridSize - 1) and col == (gridSize - 1):
        adjList.append(cellDef(row + 1, col))                   # up
        adjList.append(cellDef(row - 1, col))                   # down
        adjList.append(cellDef(row, col - 1))                   # left


# Process the Env file provided as parameter
def processEnvFile():
    file = open(envFile)
    content = file.readlines()

    lineCnt = len(content)
    # print("line count of file: " + str(len(content)))

    if lineCnt < 3:
        print("Please check and correct the environment file")
        exit(1)

    global gridSize, arrowCnt, pendingArrowCnt, arrowShot

    gridSize = int(content[0])
    arrowCnt = int(content[1])
    pendingArrowCnt = []
    pendingArrowCnt.insert(0, str(arrowCnt))
    arrowShot = []
    arrowShot.insert(0, '0')

    global maxWumpusCnt, foundWumpusCnt, killedWumpusCnt
    maxWumpusCnt = arrowCnt
    foundWumpusCnt = []
    foundWumpusCnt.insert(0, '0')
    killedWumpusCnt = []
    killedWumpusCnt.insert(0, '0')

    print("Size of the grid is: " + str(gridSize) + str(" X ") + str(gridSize))
    print("Number of arrows available initially is: " + str(arrowCnt))

    rows, cols = (gridSize, gridSize)
    global gridArr, pitArr, breezeArr, wumpusArr, stenchArr, visitedArr, okArr, screamArr
    gridArr = [[0 for i in range(cols)] for j in range(rows)]
    pitArr = [[0 for i in range(cols)] for j in range(rows)]
    breezeArr = [[0 for i in range(cols)] for j in range(rows)]
    wumpusArr = [[0 for i in range(cols)] for j in range(rows)]
    stenchArr = [[0 for i in range(cols)] for j in range(rows)]
    visitedArr = [[0 for i in range(cols)] for j in range(rows)]
    # goldGlitterArr = [[0 for i in range(cols)] for j in range(rows)]
    okArr = [[0 for i in range(cols)] for j in range(rows)]
    screamArr = [[0 for i in range(cols)] for j in range(rows)]

    global goldLoc, pitList, wumpusList
    goldCnt = 0
    # pitCnt = 0
    # wumpusCnt = 0
    goldLoc = []
    pitList = []
    wumpusList = []

    for i in range(2, lineCnt):
        word = content[i].split(" ")
        # print(word[0])
        if (word[0] != 'p' and word[0] != 'w' and word[0] != 'g'):
            print("Environment file have input values other than wumpus, pit, gold")
            exit(1)
        else:
            if word[0] == 'g':
                if goldCnt == 0:
                    rn = int(word[1]) - 1
                    cn = int(word[2]) - 1
                    # goldLoc.append(cellDef(word[1], word[2]))
                    goldLoc.append(cellDef(rn, cn))
                    gridArr[goldLoc[0].row][goldLoc[0].col] = 3
                    print("Location of the gold: " + str(goldLoc[0].row + 1) + " " + str(goldLoc[0].col + 1))
                    goldCnt = goldCnt + 1
                else:
                    print("There could be only one location for Gold, please fix the env file")
                    exit(1)
            elif word[0] == 'p':
                # pitCnt = pitCnt + 1
                rn = int(word[1]) - 1
                cn = int(word[2]) - 1
                # pitList.append(cellDef(word[1], word[2]))
                pitList.append(cellDef(rn, cn))
                # gridArr[pitList[len(pitList) - 1].row][pitList[len(pitList) - 1].col] = 1
            elif word[0] == 'w':
                # wumpusCnt = wumpusCnt + 1
                rn = int(word[1]) - 1
                cn = int(word[2]) - 1
                # wumpusList.append(cellDef(word[1], word[2]))
                wumpusList.append(cellDef(rn, cn))
                gridArr[wumpusList[len(wumpusList) - 1].row][wumpusList[len(wumpusList) - 1].col] = 2
    # Marking gridArr : 1 = pit, 2 = wumpus, 3 = gold
    print("Location of the pits are: ")
    if len(pitList) == 0:
        print("There is no pit mentioned in the env file")
    for obj in pitList:
        # print(str(obj.row), str(obj.col))
        print(str(obj.row + 1), str(obj.col + 1))
        gridArr[obj.row][obj.col] = 1
        if obj.row == 0 and obj.col == 0:
            print("There should not be any pit in cell [1,1]. Please fix the input file.")
            exit(1)
    print("Location of the wumpus are: ")
    if len(wumpusList) == 0:
        print("There is no wumpus mentioned in the env file")
    for obj in wumpusList:
        # print(str(obj.row), str(obj.col))
        print(str(obj.row + 1), str(obj.col + 1))
        gridArr[obj.row][obj.col] = 2
        if obj.row == 0 and obj.col == 0:
            print("There should not be any wumpus in cell [1,1]. Please fix the input file.")
            exit(1)
    if len(wumpusList) > maxWumpusCnt:
        print("Wumpus count should be <= arrow count. Please fix the input file.")
        exit(1)

    # print("Grid Array marked with pit=1, wumpus=2, gold=3 ===> ")
    # for row in gridArr:
    # print(row)


# Marking the adjacent cell of pit with 1 for breeze in breezeArr
# and the adjacent cell of wumpus with 1 for stench in stenchArr
def setBreezeStench():
    # print("Setting up breezeArr")
    for obj in pitList:
        findAdjcell(obj.row, obj.col)
        for obj1 in adjList:
            breezeArr[obj1.row][obj1.col] = 1
            # print(breezeArr[obj1.row][obj1.col])
        adjList.clear()

    # for row in breezeArr:
    # print(row)

    # print("Setting up stenchArr")
    for obj in wumpusList:
        findAdjcell(obj.row, obj.col)
        for obj1 in adjList:
            stenchArr[obj1.row][obj1.col] = 1
            # print(stenchArr[obj1.row][obj1.col])
        adjList.clear()

    # for row in stenchArr:
    # print(row)


# Processing the information/environment after stepping in on any new cell
# wumpusArr : 1 = wumpus is there; 2 = wumpus may be there; 3 = no wumpus
# pitArr : 1 = pit is there; 2 = pit may be there; 3 = no pit
def setEnv(currRow, currCol):
    if gridArr[currRow][currCol] == 1:
        print("#############################")
        print("GAME OVER --- YOU ENTER A PIT")
        print("#############################")
        stepsTaken = len(agentLoc) - 1
        finalScore = (stepsTaken * -1) + (int(arrowShot[0]) * -10)
        print("The path followed : ")
        for obj in agentLoc:
            print(str("[") + str(obj.row + 1) + str(",") + str(obj.col + 1) + str("]"), end=" ")
        print("\nNumber of steps taken before getting stuck in PIT: " + str(stepsTaken))
        print("Number of arrow shot: " + str(arrowShot[0]))
        print("Final Score: " + str(finalScore))
        exit(1)
    elif gridArr[currRow][currCol] == 2:
        print("####################################")
        print("GAME OVER --- YOU ENCOUNTER A WUMPUS")
        print("####################################")
        stepsTaken = len(agentLoc) - 1
        finalScore = (stepsTaken * -1) + (int(arrowShot[0]) * -10)
        print("The path followed : ")
        for obj in agentLoc:
            print(str("[") + str(obj.row + 1) + str(",") + str(obj.col + 1) + str("]"), end=" ")
        print("\nNumber of steps taken before getting killed by Wumpus: " + str(stepsTaken))
        print("Number of arrow shot: " + str(arrowShot[0]))
        print("Final Score: " + str(finalScore))
        exit(1)
    elif gridArr[currRow][currCol] == 3:
        # calculate balPoint and print
        print("############################")
        print("YOU WON --- YOU GRAB THE GOLD")
        print("############################")
        stepsTaken = len(agentLoc) - 1
        finalScore = (stepsTaken * -1) + (int(arrowShot[0]) * -10) + 150
        print("The path followed : ")
        for obj in agentLoc:
            print(str("[") + str(obj.row + 1) + str(",") + str(obj.col + 1) + str("]"), end=" ")
        print("\nNumber of steps taken to grab the GOLD: " + str(stepsTaken))
        print("Number of arrow shot: " + str(arrowShot[0]))
        print("Final Score: " + str(finalScore))
        # print(movesTaken)
        exit(0)
    else:
        findAdjcell(currRow, currCol)
        if breezeArr[currRow][currCol] == 0 and stenchArr[currRow][currCol] == 0:
            # findAdjcell(currRow, currCol)
            for obj2 in adjList:
                okArr[obj2.row][obj2.col] = 1
                pitArr[obj2.row][obj2.col] = 3
                wumpusArr[obj2.row][obj2.col] = 3
        elif breezeArr[currRow][currCol] == 1 and stenchArr[currRow][currCol] == 0:
            # findAdjcell(currRow, currCol)
            for obj2 in adjList:
                if pitArr[obj2.row][obj2.col] == 0:
                    pitArr[obj2.row][obj2.col] = 2
                wumpusArr[obj2.row][obj2.col] = 3
        elif breezeArr[currRow][currCol] == 0 and stenchArr[currRow][currCol] == 1:
            # findAdjcell(currRow, currCol)
            for obj2 in adjList:
                pitArr[obj2.row][obj2.col] = 3
                if wumpusArr[obj2.row][obj2.col] == 0:
                    wumpusArr[obj2.row][obj2.col] = 2
        elif breezeArr[currRow][currCol] == 1 and stenchArr[currRow][currCol] == 1:
            # findAdjcell(currRow, currCol)
            for obj2 in adjList:
                if pitArr[obj2.row][obj2.col] == 0:
                    pitArr[obj2.row][obj2.col] = 2
                if wumpusArr[obj2.row][obj2.col] == 0:
                    wumpusArr[obj2.row][obj2.col] = 2
        list1 = []
        for i in range(len(adjList)):
            list1.append(i)
        for adjCnt in range(len(adjList)):
            list2 = [adjCnt]
            list3 = []
            for elem in list1:
                if elem not in list2:
                    list3.append(elem)
            pitNCnt = 0
            wumpusNCnt = 0
            for elem1 in range(len(list3)):
                if pitArr[adjList[elem1].row][adjList[elem1].col] == 3:
                    pitNCnt = pitNCnt + 1
                if wumpusArr[adjList[elem1].row][adjList[elem1].col] == 3:
                    wumpusNCnt = wumpusNCnt + 1
            if pitNCnt == len(list3):
                if pitArr[adjList[adjCnt].row][adjList[adjCnt].col] in [0, 2]:
                    pitArr[adjList[adjCnt].row][adjList[adjCnt].col] = 1
            if wumpusNCnt == len(list3):
                if wumpusArr[adjList[adjCnt].row][adjList[adjCnt].col] in [0, 2] \
                        and int(foundWumpusCnt[0]) < maxWumpusCnt:
                    wumpusArr[adjList[adjCnt].row][adjList[adjCnt].col] = 1
                    uwc = int(foundWumpusCnt[0]) + 1
                    foundWumpusCnt.insert(0, str(uwc))
        for obj2 in adjList:
            if pitArr[obj2.row][obj2.col] == 3 and wumpusArr[obj2.row][obj2.col] == 3:
                okArr[obj2.row][obj2.col] = 1
        adjList.clear()

    # print("gridArr")
    # for row in gridArr:
        # print(row)
    # print("okArr")
    # for row in okArr:
        # print(row)
    # print("pitArr")
    # for row in pitArr:
        # print(row)
    # print("wumpusArr")
    # for row in wumpusArr:
        # print(row)


# Getting the location of the cell forward(UP) as per current direction, also check for bump
def findFrd(currRow, currCol):
    if agentFace[0] == 'N':
        # print("checking currCol frd:" + str(currCol))
        if currRow == gridSize - 1:
            noFrd.insert(0, '1')
        else:
            if 0 <= currRow + 1 < gridSize:
                frdLoc.insert(0, (cellDef(currRow + 1, currCol)))
    elif agentFace[0] == 'S':
        if currRow == 0:
            noFrd.insert(0, '1')
        else:
            if 0 <= currRow - 1 < gridSize:
                frdLoc.insert(0, (cellDef(currRow - 1, currCol)))
    elif agentFace[0] == 'E':
        if currCol == gridSize - 1:
            noFrd.insert(0, '1')
        else:
            if 0 <= currCol + 1 < gridSize:
                frdLoc.insert(0, (cellDef(currRow, currCol + 1)))
    elif agentFace[0] == 'W':
        if currCol == 0:
            noFrd.insert(0, '1')
        else:
            if 0 <= currCol - 1 < gridSize:
                frdLoc.insert(0, (cellDef(currRow, currCol - 1)))


# Getting the location/direction of the cell at left as per current direction, also check for bump
def findLeft(currRow, currCol):
    if agentFace[0] == 'N':
        # print("checking currCol left:" + str(currCol))
        if currCol == 0:
            noLeft.insert(0, '1')
        else:
            if 0 <= currCol - 1 < gridSize:
                leftLoc.insert(0, (cellDef(currRow, currCol - 1)))
                agentFaceNew.insert(0, 'W')
    elif agentFace[0] == 'S':
        if currCol == gridSize - 1:
            noLeft.insert(0, '1')
        else:
            if 0 <= currCol + 1 < gridSize:
                leftLoc.insert(0, (cellDef(currRow, currCol + 1)))
                agentFaceNew.insert(0, 'E')
    elif agentFace[0] == 'E':
        if currRow == gridSize - 1:
            noLeft.insert(0, '1')
        else:
            if 0 <= currRow + 1 < gridSize:
                leftLoc.insert(0, (cellDef(currRow + 1, currCol)))
                agentFaceNew.insert(0, 'N')
    elif agentFace[0] == 'W':
        if currRow == 0:
            noLeft.insert(0, '1')
        else:
            if 0 <= currRow - 1 < gridSize:
                leftLoc.insert(0, (cellDef(currRow - 1, currCol)))
                agentFaceNew.insert(0, 'S')


# Getting the location/direction of the cell at right as per current direction, also check for bump
def findRight(currRow, currCol):
    if agentFace[0] == 'N':
        # print("checking currCol right:" + str(currCol))
        if currCol == gridSize - 1:
            noRight.insert(0, '1')
        else:
            if 0 <= currCol + 1 < gridSize:
                rightLoc.insert(0, (cellDef(currRow, currCol + 1)))
                agentFaceNew.insert(0, 'E')
    elif agentFace[0] == 'S':
        if currCol == 0:
            noRight.insert(0, '1')
        else:
            if 0 <= currCol - 1 < gridSize:
                rightLoc.insert(0, (cellDef(currRow, currCol - 1)))
                agentFaceNew.insert(0, 'W')
    elif agentFace[0] == 'E':
        if currRow == 0:
            noRight.insert(0, '1')
        else:
            if 0 <= currRow - 1 < gridSize:
                rightLoc.insert(0, (cellDef(currRow - 1, currCol)))
                agentFaceNew.insert(0, 'S')
    elif agentFace[0] == 'W':
        if currRow == gridSize - 1:
            noRight.insert(0, '1')
        else:
            if 0 <= currRow + 1 < gridSize:
                rightLoc.insert(0, (cellDef(currRow + 1, currCol)))
                agentFaceNew.insert(0, 'N')


# Set the scream for adjacent cell if arrow kill the wumpus
def shootArrow(srow, scol):
    pc = int(pendingArrowCnt[0]) - 1
    pendingArrowCnt.insert(0, str(pc))
    ac = int(arrowShot[0]) + 1
    arrowShot.insert(0, str(ac))  # stores the number of arrow shot
    print("Shooting Arrow")
    if gridArr[srow][scol] == 2:
        if int(pendingArrowCnt[0]) > 0:
            findAdjcell(srow, scol)
            for obj in adjList:
                screamArr[obj.row][obj.col] = 1
            adjList.clear()
            # pc = int(pendingArrowCnt[0]) - 1
            # pendingArrowCnt.insert(0, str(pc))
            # ac = int(arrowShot[0]) + 1
            # arrowShot.insert(0, str(ac))                        # stores the number of arrow shot
        else:
            print("Cannot kill Wumpus as do not have arrow left")


# Checking from which cell and at which direction arrow needs to be shot
# after getting blocked from all the directions
def checkForShoot(currRow, currCol):
    noShoot = 0
    findFrd(currRow, currCol)
    if noFrd[0] == '1':
        noFrd.insert(0, '0')
        # noSafeMove = 1
        noShoot = 1
    else:
        if okArr[frdLoc[0].row][frdLoc[0].col] == 1:
            currRow = frdLoc[0].row
            currCol = frdLoc[0].col
            # agentFace.insert(0, agentFaceNew[0])
            agentLoc.append(cellDef(currRow, currCol))
            visitedArr[currRow][currCol] = visitedArr[currRow][currCol] + 1
            # visitedList.append(cellDef(currRow, currCol))
            # setEnv(currRow, currCol)
            checkForShoot(currRow, currCol)
        else:
            if pitArr[frdLoc[0].row][frdLoc[0].col] in [0, 3] \
                    and wumpusArr[frdLoc[0].row][frdLoc[0].col] in [0, 3]:
                currRow = frdLoc[0].row
                currCol = frdLoc[0].col
                # agentFace.insert(0, agentFaceNew[0])
                agentLoc.append(cellDef(currRow, currCol))
                visitedArr[currRow][currCol] = visitedArr[currRow][currCol] + 1
                # visitedList.append(cellDef(currRow, currCol))
                # setEnv(currRow, currCol)
                checkForShoot(currRow, currCol)
            else:
                if pitArr[frdLoc[0].row][frdLoc[0].col] == 1:
                    print("Skipping for Pit")
                    noShoot = 1
                else:
                    if wumpusArr[frdLoc[0].row][frdLoc[0].col] in [1, 2]:
                        # print("Will Shoot #1")
                        shootArrow(frdLoc[0].row, frdLoc[0].col)
                        if screamArr[currRow][currCol] == 1:
                            wc = int(killedWumpusCnt[0]) + 1
                            killedWumpusCnt.insert(0, str(wc))
                            print("Wumpus Killed # : " + str(killedWumpusCnt[0]))
                            okArr[frdLoc[0].row][frdLoc[0].col] = 1
                            wumpusArr[frdLoc[0].row][frdLoc[0].col] = 3
                            gridArr[frdLoc[0].row][frdLoc[0].col] = 0
                        currRow = frdLoc[0].row
                        currCol = frdLoc[0].col
                        agentLoc.append(cellDef(currRow, currCol))
                        visitedArr[currRow][currCol] = visitedArr[currRow][currCol] + 1
                        visitedList.append(cellDef(currRow, currCol))
                        setEnv(currRow, currCol)
                        nextMove(currRow, currCol)
                    else:
                        noShoot = 1
    if noShoot == 1:
        noShoot = 0
        # print("will start left shooting")
        findLeft(currRow, currCol)
        if noLeft[0] == '1':
            noLeft.insert(0, '0')
            # noSafeMove = 1
            noShoot = 1
        else:
            if (okArr[leftLoc[0].row][leftLoc[0].col] == 1):
                currRow = leftLoc[0].row
                currCol = leftLoc[0].col
                agentFace.insert(0, agentFaceNew[0])
                agentLoc.append(cellDef(currRow, currCol))
                visitedArr[currRow][currCol] = visitedArr[currRow][currCol] + 1
                # visitedList.append(cellDef(currRow, currCol))
                # setEnv(currRow, currCol)
                checkForShoot(currRow, currCol)
            else:
                if pitArr[leftLoc[0].row][leftLoc[0].col] in [0, 3] \
                        and wumpusArr[leftLoc[0].row][leftLoc[0].col] in [0, 3]:
                    currRow = leftLoc[0].row
                    currCol = leftLoc[0].col
                    agentFace.insert(0, agentFaceNew[0])
                    agentLoc.append(cellDef(currRow, currCol))
                    visitedArr[currRow][currCol] = visitedArr[currRow][currCol] + 1
                    # visitedList.append(cellDef(currRow, currCol))
                    # setEnv(currRow, currCol)
                    checkForShoot(currRow, currCol)
                else:
                    if pitArr[leftLoc[0].row][leftLoc[0].col] == 1:
                        print("Skipping for Pit")
                        noShoot = 1
                    else:
                        if wumpusArr[leftLoc[0].row][leftLoc[0].col] in [1, 2]:
                            # print("Will Shoot #2")
                            shootArrow(leftLoc[0].row, leftLoc[0].col)
                            if screamArr[currRow][currCol] == 1:
                                wc = int(killedWumpusCnt[0]) + 1
                                killedWumpusCnt.insert(0, str(wc))
                                print("Wumpus Killed # : " + str(killedWumpusCnt[0]))
                            currRow = leftLoc[0].row
                            currCol = leftLoc[0].col
                            agentFace.insert(0, agentFaceNew[0])
                            agentLoc.append(cellDef(currRow, currCol))
                            visitedArr[currRow][currCol] = visitedArr[currRow][currCol] + 1
                            visitedList.append(cellDef(currRow, currCol))
                            setEnv(currRow, currCol)
                            nextMove(currRow, currCol)
                        else:
                            noShoot = 1
    if noShoot == 1:
        noShoot = 0
        # print("will start right shooting")
        findRight(currRow, currCol)
        if noRight[0] == '1':
            noRight.insert(0, '0')
            # noSafeMove = 1
            noShoot = 1
        else:
            if (okArr[rightLoc[0].row][rightLoc[0].col] == 1):
                currRow = rightLoc[0].row
                currCol = rightLoc[0].col
                agentFace.insert(0, agentFaceNew[0])
                agentLoc.append(cellDef(currRow, currCol))
                visitedArr[currRow][currCol] = visitedArr[currRow][currCol] + 1
                # visitedList.append(cellDef(currRow, currCol))
                # setEnv(currRow, currCol)
                checkForShoot(currRow, currCol)
            else:
                if pitArr[rightLoc[0].row][rightLoc[0].col] in [0, 3] \
                        and wumpusArr[rightLoc[0].row][rightLoc[0].col] in [0, 3]:
                    currRow = rightLoc[0].row
                    currCol = rightLoc[0].col
                    agentFace.insert(0, agentFaceNew[0])
                    agentLoc.append(cellDef(currRow, currCol))
                    visitedArr[currRow][currCol] = visitedArr[currRow][currCol] + 1
                    # visitedList.append(cellDef(currRow, currCol))
                    # setEnv(currRow, currCol)
                    checkForShoot(currRow, currCol)
                else:
                    if pitArr[rightLoc[0].row][rightLoc[0].col] == 1:
                        print("Skipping for Pit")
                        noShoot = 1
                    else:
                        if wumpusArr[rightLoc[0].row][rightLoc[0].col] in [1, 2]:
                            # print("Will Shoot #3")
                            shootArrow(rightLoc[0].row, rightLoc[0].col)
                            if screamArr[currRow][currCol] == 1:
                                wc = int(killedWumpusCnt[0]) + 1
                                killedWumpusCnt.insert(0, str(wc))
                                print("Wumpus Killed # : " + str(killedWumpusCnt[0]))
                            currRow = rightLoc[0].row
                            currCol = rightLoc[0].col
                            agentFace.insert(0, agentFaceNew[0])
                            agentLoc.append(cellDef(currRow, currCol))
                            visitedArr[currRow][currCol] = visitedArr[currRow][currCol] + 1
                            visitedList.append(cellDef(currRow, currCol))
                            setEnv(currRow, currCol)
                            nextMove(currRow, currCol)
                        else:
                            noShoot = 1
    if noShoot == 1:
        # print("Blocked in the cell: " + str(currRow + 1) + " " + str(currCol + 1))
        findFrd(currRow, currCol)
        if noFrd[0] == '1':
            noFrd.insert(0, '0')
        else:
            currRow = frdLoc[0].row
            currCol = frdLoc[0].col
            agentLoc.append(cellDef(currRow, currCol))
            visitedArr[currRow][currCol] = visitedArr[currRow][currCol] + 1
            visitedList.append(cellDef(currRow, currCol))
            setEnv(currRow, currCol)
            nextMove(currRow, currCol)
        findLeft(currRow, currCol)
        if noLeft[0] == '1':
            noLeft.insert(0, '0')
        else:
            currRow = leftLoc[0].row
            currCol = leftLoc[0].col
            agentFace.insert(0, agentFaceNew[0])
            agentLoc.append(cellDef(currRow, currCol))
            visitedArr[currRow][currCol] = visitedArr[currRow][currCol] + 1
            visitedList.append(cellDef(currRow, currCol))
            setEnv(currRow, currCol)
            nextMove(currRow, currCol)
        findRight(currRow, currCol)
        if noRight[0] == '1':
            noRight.insert(0, '0')
        else:
            currRow = rightLoc[0].row
            currCol = rightLoc[0].col
            agentFace.insert(0, agentFaceNew[0])
            agentLoc.append(cellDef(currRow, currCol))
            visitedArr[currRow][currCol] = visitedArr[currRow][currCol] + 1
            visitedList.append(cellDef(currRow, currCol))
            setEnv(currRow, currCol)
            nextMove(currRow, currCol)


# Moving back once getting blocked - when no forward/left/right move are safe
def moveBack(currRow, currCol):
    # print("Inside moveBack:" + str(currRow) + " " + str(currCol))
    # print(len(visitedList))
    visitedList.pop(len(visitedList) - 1)
    l = len(visitedList) - 1
    # print("inside moveBack ::: " + str(l))
    # visitedList(l).row
    # visitedList(l).col
    if l >= 0:
        backLoc.insert(0, (cellDef(visitedList[l].row, visitedList[l].col)))
    else:
        # print("Initiate shooting")
        checkForShoot(currRow, currCol)


# Checking which direction to move next
def nextMove(currRow, currCol):
    noSafeMove = 0
    # Processing for Forward Cell
    findFrd(currRow, currCol)
    # fl = len(frdLoc) - 1
    # print("Afer frw move :::: " + str(currRow) + " " + str(currCol))
    # for row in okArr:
        # print(row)
    # print(okArr[frdLoc[0].row][frdLoc[0].col])
    if noFrd[0] == '1':
        noFrd.insert(0, '0')
        noSafeMove = 1
    else:
        if visitedArr[frdLoc[0].row][frdLoc[0].col] != 0:
            noSafeMove = 1
        else:
            if okArr[frdLoc[0].row][frdLoc[0].col] == 1:
                currRow = frdLoc[0].row
                currCol = frdLoc[0].col
                # agentFace.insert(0, agentFaceNew[0])
                # print("Inside FrdMove 1 : " + str(currRow) + str(" ") + str(currCol))
                agentLoc.append(cellDef(currRow, currCol))
                visitedArr[currRow][currCol] = 1
                visitedList.append(cellDef(currRow, currCol))
                setEnv(currRow, currCol)
                nextMove(currRow, currCol)
            elif okArr[frdLoc[0].row][frdLoc[0].col] == 0:
                # print("Inside 2 pit and wumpus ")
                # print(pitArr[frdLoc[0].row][frdLoc[0].col])
                # print(wumpusArr[frdLoc[0].row][frdLoc[0].col])
                if pitArr[frdLoc[0].row][frdLoc[0].col] in [0, 3] \
                        and wumpusArr[frdLoc[0].row][frdLoc[0].col] in [0, 3]:
                    currRow = frdLoc[0].row
                    currCol = frdLoc[0].col
                    # agentFace.insert(0, agentFaceNew[0])
                    agentLoc.append(cellDef(currRow, currCol))
                    visitedArr[currRow][currCol] = 1
                    visitedList.append(cellDef(currRow, currCol))
                    setEnv(currRow, currCol)
                    nextMove(currRow, currCol)
                else:
                    noSafeMove = 1
                    skippedCell.append(cellDef(frdLoc[0].row, frdLoc[0].col))
                    # print("SkippedCell: " + str(currRow) + " " + str(currCol))
            elif okArr[frdLoc[0].row][frdLoc[0].col] == 2:
                noSafeMove = 1
                skippedCell.append(cellDef(frdLoc[0].row, frdLoc[0].col))
    # Processing for Left Cell
    if noSafeMove == 1:
        noSafeMove = 0
        findLeft(currRow, currCol)
        # print("after findLeft: " + str(noLeft[0]))
        if noLeft[0] == '1':
            noLeft.insert(0, '0')
            noSafeMove = 1
        else:
            # ll = len(leftLoc) - 1
            if visitedArr[leftLoc[0].row][leftLoc[0].col] != 0:
                noSafeMove = 1
            else:
                if okArr[leftLoc[0].row][leftLoc[0].col] == 1:
                    currRow = leftLoc[0].row
                    currCol = leftLoc[0].col
                    agentFace.insert(0, agentFaceNew[0])
                    agentLoc.append(cellDef(currRow, currCol))
                    visitedArr[currRow][currCol] = 1
                    visitedList.append(cellDef(currRow, currCol))
                    setEnv(currRow, currCol)
                    nextMove(currRow, currCol)
                elif okArr[leftLoc[0].row][leftLoc[0].col] == 0:
                    if pitArr[leftLoc[0].row][leftLoc[0].col] in [0, 3] \
                            and wumpusArr[leftLoc[0].row][leftLoc[0].col] in [0, 3]:
                        currRow = leftLoc[0].row
                        currCol = leftLoc[0].col
                        agentFace.insert(0, agentFaceNew[0])
                        agentLoc.append(cellDef(currRow, currCol))
                        visitedArr[currRow][currCol] = 1
                        visitedList.append(cellDef(currRow, currCol))
                        setEnv(currRow, currCol)
                        nextMove(currRow, currCol)
                    else:
                        noSafeMove = 1
                        skippedCell.append(cellDef(leftLoc[0].row, leftLoc[0].col))
                elif okArr[leftLoc[0].row][leftLoc[0].col] == 2:
                    noSafeMove = 1
                    skippedCell.append(cellDef(leftLoc[0].row, leftLoc[0].col))
    # Processing for Right Node
    if noSafeMove == 1:
        noSafeMove = 0
        findRight(currRow, currCol)
        if noRight[0] == '1':
            noRight.insert(0, '0')
            noSafeMove = 1
        else:
            # rl = len(rightLoc) - 1
            # print("debugging right: " + str(visitedArr[rightLoc[0].row][rightLoc[0].col]))
            if visitedArr[rightLoc[0].row][rightLoc[0].col] != 0:
                noSafeMove = 1
            else:
                if okArr[rightLoc[0].row][rightLoc[0].col] == 1:
                    currRow = rightLoc[0].row
                    currCol = rightLoc[0].col
                    agentFace.insert(0, agentFaceNew[0])
                    agentLoc.append(cellDef(currRow, currCol))
                    visitedArr[currRow][currCol] = 1
                    visitedList.append(cellDef(currRow, currCol))
                    setEnv(currRow, currCol)
                    nextMove(currRow, currCol)
                elif okArr[rightLoc[0].row][rightLoc[0].col] == 0:
                    if pitArr[rightLoc[0].row][rightLoc[0].col] in [0, 3] \
                            and wumpusArr[rightLoc[0].row][rightLoc[0].col] in [0, 3]:
                        currRow = rightLoc[0].row
                        currCol = rightLoc[0].col
                        agentFace.insert(0, agentFaceNew[0])
                        agentLoc.append(cellDef(currRow, currCol))
                        visitedArr[currRow][currCol] = 1
                        visitedList.append(cellDef(currRow, currCol))
                        setEnv(currRow, currCol)
                        nextMove(currRow, currCol)
                    else:
                        noSafeMove = 1
                        skippedCell.append(cellDef(rightLoc[0].row, rightLoc[0].col))
                elif okArr[rightLoc[0].row][rightLoc[0].col] == 2:
                    noSafeMove = 1
                    skippedCell.append(cellDef(rightLoc[0].row, rightLoc[0].col))
    # Processing for Back Cell
    if noSafeMove == 1:
        noSafeMove = 0
        # print("Before moveback: " + str(currRow) + " " + str(currCol))
        moveBack(currRow, currCol)
        # bl = len(backLoc) - 1
        currRow = backLoc[0].row
        currCol = backLoc[0].col
        agentLoc.append(cellDef(currRow, currCol))
        # print("Moved Back to: " + str(currRow) + " " + str(currCol))
        nextMove(currRow, currCol)


# Driving Method
def main():
    # varInit()
    processEnvFile()
    global agentLoc, adjList, visitedList, agentFace
    # global screamArr
    adjList = []
    visitedList = []
    agentFace = []
    setBreezeStench()
    # Initialize Agent Location
    agentLoc = []
    agentLoc.append(cellDef(0, 0))
    currRow = agentLoc[len(agentLoc) - 1].row
    currCol = agentLoc[len(agentLoc) - 1].col
    agentFace.insert(0, 'N')
    print("Initial Agent Location: " + str(currRow + 1) + str(" ") + str(currCol + 1))
    print("Initially Agent is facing: " + str(agentFace[0]))
    # print(currRow)
    # print(currCol)
    okArr[currRow][currCol] = 1
    visitedArr[currRow][currCol] = 1
    visitedList.append(cellDef(currRow, currCol))
    # print(visitedList[0].row, visitedList[0].col)

    setEnv(currRow, currCol)

    # def setEnv(currRow, currCol):

    # movesTaken = []
    # movesTaken.append(agentLoc)
    # print(movesTaken)

    """
    print("okArr")
    for row in okArr:
        print(row)
    print("pitArr")
    for row in pitArr:
        print(row)
    print("wumpusArr")
    for row in wumpusArr:
        print(row)
    """
    global leftLoc, rightLoc, frdLoc, backLoc, skippedCell
    leftLoc = []
    rightLoc = []
    frdLoc = []
    backLoc = []
    skippedCell = []

    global noLeft, noRight, noFrd, agentFaceNew
    noLeft = []
    noRight = []
    noFrd = []
    noFrd.insert(0, '0')
    noLeft.insert(0, '0')
    noRight.insert(0, '0')
    agentFaceNew = []

    nextMove(currRow, currCol)

main()

