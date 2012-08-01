#!/usr/bin/env python
# gridTools.py
# 
# This is a utility module used for making 2D grid-based maps for games.
# Note that most of these functions act on grid objects, and the grid objects
# are 2D integer arrays

import random
import math

def createGrid(numRows = 200, numCols = 200, defaultVal=1):
    """Creates a grid object, which is a 2D array of integers.
    @param numRows The number of rows in the grid
    @param numCols The number of columns in the grid
    @param defaultVal The value each cell in the grid will be set to
    @return A grid filled with the defaultVal
    """
    rows = numRows
    cols = numCols
    val = defaultVal
    theGrid = [[val for i in range(cols)] for j in range(rows)]
    return theGrid

def perimeterWall(grid):
    """Takes a grid object and puts walls (value=2) around the perimeter."""
    
    for r in range(len(grid)):
        grid[r][0] = 2
        grid[r][-1] = 2
        
    for c in range(len(grid[0])):
        grid[0][c] = 2
        grid[-1][c] = 2

def randomBlocks(grid):
    """This randomly places a block in each row. Quite useless; kept for
    nostalgic reasons
    """
    cols = len(grid)
    rows = len(grid[0])    
    for r in range(rows):
        grid[r][random.randint(0,rows-1)] = 1

def exportGrid(grid, filename): 
    """This is what writes the grid object to a text file. It puts each row on a new line.
    @param grid The grid object
    @param filename The name for the file--don't add an extension, this function does that for you
    """
    gridFinal = ""
    for v in range(len(grid)):
        for w in range(len(grid[0])):
            gridFinal += str(grid[v][w])
        gridFinal += "\n"
    FILE = open(str(filename) + ".txt", "w")
    FILE.write(gridFinal)
    FILE.close
    
def roomMaker(grid, x, y, rh, rw):
    """This function generates a room
    @param grid The grid we will gnerate the room in
    @param x This is the x value of the upper left hand corner of the room
    @param y This is the y value of the upper left hand corner of the room
        Example: grid[y][x]
    @param rh Room height
    @param rw Room width"""
    rows = len(grid)
    cols = len(grid[0])
    validDimensions = True
    # if we decide to keep this in here we could return a tuple of both
    # a boolean and a string that describes the reason it failed.
    err = None
    # this could place a room on the outer row or column, so I like 
    # how we add the perimeter wall AFTER this.
    if x < 0:
        validDimensions = False
        err = "X is too low"
    elif x+rw > cols-1:
        validDimensions = False
        err = "Width is too high"
    else:
        if y < 0:
            validDimensions = False
            err = "Y is too low"
        elif y+rh > rows-1:
            validDimensions = False
            err = "Length is too high"
        else:
            if validDimensions:
                for i in range(rh):
                    for j in range(rw):
                        grid[y+i][x+j] = 0
    return validDimensions

def roomGenerator(grid, minRooms, maxRooms, minHeight, maxHeight, minWidth, maxWidth):
    """Randomly scatters rooms across the grid"""
    carvedRooms = 0
    numberOfRoomsToCarve = random.randint(minRooms, maxRooms)
    while carvedRooms <= numberOfRoomsToCarve:
        if roomMaker(grid, random.randint(1,len(grid[0])-1), random.randint(1, len(grid)-1), random.randint(minHeight,maxHeight), random.randint(minWidth,maxWidth)):
            carvedRooms += 1

def poolMaker(grid, x, y, radius):
    """Creates a pool at grid[y][x] with a radius set by user"""
    rows = len(grid)
    cols = len(grid[1])
    if x < 0 or x > cols-1 or y < 0 or y > rows-1:
        validDimensions = False
    else:
        center = grid[y][x]
        curX = x
        curY = y
        validDimensions = True
        for i in range((2 * radius)+1):
                for j in range((2 * radius)+1):
                    curX = x-(radius - j)
                    curY = y-(radius - i)
                    dist = math.sqrt((radius-j)**2 + (radius-i)**2)
                    if dist <= radius:
                        if curX < 0 or curX > cols-1 or curY < 0 or curY > rows-1:
                            validDimensions = False
                        else:
                            grid[curY][curX] = 3
    return validDimensions

def poolGenerator(grid, minPools, maxPools, minRadius, maxRadius):
    """Randomly scatters pools across the map"""
    poolsFilled = 0
    numberOfPoolsToFill = random.randint(minPools,maxPools)
    while poolsFilled <= numberOfPoolsToFill:
        if poolMaker(grid, random.randint(1,len(grid[0])-1), random.randint(1, len(grid)-1), random.randint(minRadius,maxRadius)):
            poolsFilled += 1

def oreVeinMaker(grid, x, y, oreVal, oreNum):
    """Makes a chunk of ore in a randomly determined shape"""
    validPlacement = True
    direction = None
    if x < 0 or x > len(grid[0])-1 or y < 0 or y > len(grid)-1: 
        validPlacement = False
    else:
        origX = x
        origY = y
        for i in range(oreNum):
            if x < 0 or x > len(grid[0])-1 or y < 0 or y > len(grid)-1: 
                x = origX
                y = origY
            else:
                grid[y][x] = oreVal
                direction = random.randint(0,3)
                if direction == 0:
                    while grid[y][x] == oreVal:
                        x += 1
                elif direction == 1:
                    while grid[y][x] == oreVal:
                        x -= 1
                elif direction == 2:
                    while grid[y][x] == oreVal:
                        y += 1
                else:
                    while grid[y][x] == oreVal:
                        y -= 1
    return validPlacement
    
def oreVeinGenerator(grid, oreVal, minVeins, maxVeins, minOreNum, maxOreNum):
    """Randomly scatters veins"""
    #Currently this function returns an error about 1/4 of the time. It has to do with the oreVeinMaker
    #Any ideas on how to fix it OR if you do fix it post to the forums please
    # Is this fixed now? I'll test it.... --G
    veinsMade = 0
    numberOfVeinsToMake = random.randint(minVeins,maxVeins)
    while veinsMade <= numberOfVeinsToMake:
        if oreVeinMaker(grid, random.randint(1,len(grid[0])-1), random.randint(1, len(grid)-1), oreVal, random.randint(minOreNum,maxOreNum)):
            veinsMade  += 1

if __name__ == "__main__":
    print "I ain't a standalone module, freeloader!"
