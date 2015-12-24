#!/usr/bin/env python

import random
import gridTools as gt
import math

g1 = gt.createGrid(200, 200)

gt.roomGenerator(g1,50,70,15,19,17,19)
gt.oreVeinGenerator(g1, 4, 10, 20, 10, 30)
gt.poolGenerator(g1, 5, 30,2, 15)
gt.perimeterWall(g1)
gt.exportGrid(g1, "grid")
