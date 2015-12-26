#!/usr/bin/env python3

#This will be the Grid Class. It will store every item and manage them based on certain criteria. For now it is a glorified dictionary where the keys are coordinates and the values are lists of Things. (See below)
class Grid(object):
    
    def __init__(self, width, height):
        self.contents = dict()
        for x in range(width):
            for y in range(height):
                self.contents[(x,y)] = []
                
    def addThing(self, thing_to_add):
        self.contents[thing_to_add.whereAmI()].append(thing_to_add)
    
#The Thing class will be a class that other Things, such as the player and monsters, will inherit from. Anything in a grid is a thing
class Thing(object):
    
    def __init__(self, containing_grid, coordinates):
        self.grid = containing_grid
        self.coords = list(coordinates)
        self.grid.addThing(self)
    
    def whichGridIsMine(self):
        return self.grid
    
    def whereAmI(self):
        return tuple(self.coords)

#Tiles are special things that will designate what the ground looks like. These are in the Grid Class because they do not fir in other places
class Tile(Thing):
    
    def __init__(self, containing_grid, coordinates, tile_id):
        super().__init__(containing_grid, coordinates)
        self.tileID = tile_id
        
    def whatAmI(self, tile_ID_dictionary):
        return tile_ID_dictionary[self.tileID]
    
