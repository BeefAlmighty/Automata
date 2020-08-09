import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation
from IPython.display import HTML
import matplotlib.animation as animation




class Point:

    def __init__(self, location, gridSize):
        self.location = location
        self.gridSize = gridSize
        self.neighbours = []  # Will be L, R, U, D

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.location == other.location and self.gridSize == other.gridSize
        return False

    def __repr__(self):
        return '(' + str(self.location[0]) + ',' + str(self.location[1]) + ')'

    def setNeighbours(self):
        pos = [self.PointUp(), self.PointDown(), self.PointLeft(), self.PointRight()]
        self.neighbours = [item for item in pos if item != None]
        return

    @staticmethod
    def inGrid(location, gridShape):
        return location[0] in range(gridShape[0]) and location[1] in range(gridShape[1])

    @staticmethod
    def createPointList(locationList, gridSize):
        ans = []
        for loc in locationList:
            point = Point(loc, gridSize)
            point.setNeighbours()
            ans += [point]
        return ans

    def PointUp(self):
        x, y = self.getIndex()
        up = (x - 1, y)
        if Point.inGrid(up, self.getGridSize()):
            return Point(up, self.getGridSize())
        return None

    def PointDown(self):
        x, y = self.getIndex()
        down = (x + 1, y)
        if Point.inGrid(down, self.getGridSize()):
            return Point(down, self.getGridSize())
        return None

    def PointLeft(self):
        x, y = self.getIndex()
        left = (x, y - 1)
        if Point.inGrid(left, self.getGridSize()):
            return Point(left, self.getGridSize())
        return None

    def PointRight(self):
        x, y = self.getIndex()
        right = (x, y + 1)
        if Point.inGrid(right, self.getGridSize()):
            return Point(right, self.getGridSize())
        return None

    def getIndex(self):
        return [self.location[0], self.location[1]]

    def getNeighours(self):
        return self.neighbours

    def getGridSize(self):
        return self.gridSize





class Grid:

    def __init__(self, **kwargs):
        self.updates = 0
        self.points=None
        if 'arr' in kwargs:
            self.grid = kwargs['arr']
        elif 'm' in kwargs and 'n' in kwargs:
            self.grid = np.zeros((kwargs['m'], kwargs['n']))
        elif 'm' in kwargs and not 'n' in kwargs:
            self.grid = np.zeros((kwargs['m'], kwargs['m']))
        self.shape = self.grid.shape
        if 'locations' in kwargs:
            indexList = kwargs['locations']
            self.points = Point.createPointList(indexList, self.shape)
            for indices in indexList:
                self.grid[indices[0], indices[1]] = 1


    def getPoints(self):
        return self.points

    def removePoint(self, point):
        self.points.remove(point)
        return

    def updateGrid(self):
        self.grid = np.zeros(self.grid.shape)
        for point in self.points:
            ind = point.getindex()
            point.set_neighbour_cells()
            self.grid[ind[0], ind[1]] = 1
        return

    def switch(self):
        self.grid = np.ones(self.grid.shape)
        for point in self.points:
            ind=point.get_index()
            self.grid[ind[0], ind[1]] = 0
        self.points = Point.createPointList(list(zip(np.where(self.grid > 0)[0], np.where(self.grid > 0)[1])), self.shape)

    def moveDown(self):
        self.grid = np.zeros(self.grid.shape)
        temp = [((item[0] + 1) % self.grid.shape[0], item[1]) for item in self.points]
        self.points=Point.createPointList(temp, self.shape)
        for indices in self.points:
            self.grid[indices[0], indices[1]] = 1

    def moveUp(self):
        self.grid = np.zeros(self.grid.shape)
        temp = [((item[0] - 1) % self.grid.shape[0], item[1]) for item in self.points]
        self.points=Point.createPointList(temp, self.shape)
        for indices in self.points:
            self.grid[indices[0], indices[1]] = 1

    def moveLeft(self):
        self.grid = np.zeros(self.grid.shape)
        temp = [(item[0], (item[1] - 1) % self.grid.shape[1]) for item in self.points]
        self.points=Point.createPointList(temp, self.shape)
        for indices in self.points:
            self.grid[indices[0], indices[1]] = 1

    def moveRight(self):
        self.grid = np.zeros(self.grid.shape)
        temp = [(item[0], (item[1] - 1) % self.grid.shape[1]) for item in self.points]
        self.points=Point.createPointList(temp, self.shape)
        for indices in self.points:
            self.grid[indices[0], indices[1]] = 1

    def getGrid(self):
        return self.grid

    def getPoints(self):
        return self.points

    def randomize(self):
        self.updates += 1
        self.grid = np.random.randint(2, size=self.shape)

    def view(self):
        plt.imshow(self.grid)
        plt.show()

    def updates(self):
        return self.updates



if __name__=='__main__':
    g=Grid(m=42, locations=[(3,4), (9,7), (18,17)])
   # print(Point.createPointList([(3,4), (9,7), (18,17)], (42, 42)))
    g.view()
 #   print(g.getPoints())
#    g.moveDown()
 #   print(g.getPoints())

