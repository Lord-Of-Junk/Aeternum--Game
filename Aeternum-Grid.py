#!/usr/bin/env python3

#This will be the Grid Class. It will store every item and manage them based on certain criteria. For now it is a glorified dictionary where the keys are coordinates and the values are lists of Things. (See below)
class Grid():
    
    def __init__(self, width, height):
        self.contents = dict()
        for x in range(width):
            for y in range(height):
                self.contents[(x,y)] = []
    
#The Thing class will be a class that other Things, such as the player and monsters, will inherit from.
class Thing():
    
    def __init__(self, containing_grid, coordinates):
        self.grid = containing_grid
        self.coords = list(coordinates)
    
    def whichGridIsMine(self):
        return self.grid
    
    def whereAmI(self):
        return tuple(self.coords)

#Tiles are special things that will designate what the ground loks like.
class Tile(Thing):
    
    def __init__(self, containing_grid, coordinates, tile_id):
        super(containing_grid, coordinates)
        self.tileID = tile_id