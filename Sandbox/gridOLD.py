import point as pt
import numpy as np
import matplotlib.pyplot as plt

class Grid:

    def __init__(self, **kwargs):
        self.updates = 0
        self.pointList = None
        if 'arr' in kwargs:
            self.grid = kwargs['arr']
        elif 'm' in kwargs and 'n' in kwargs:
            self.grid = np.zeros((kwargs['m'], kwargs['n']))
        elif 'm' in kwargs and not 'n' in kwargs:
            self.grid = np.zeros((kwargs['m'], kwargs['m']))
        self.shape = self.grid.shape
        if 'locations' in kwargs:
            indexList = kwargs['locations']
            self.pointList = pt.Point.create_point_list(indexList, self.shape)
            for indices in indexList:
                self.grid[indices[0], indices[1]] = 1

    def remove_point(self, point):
        self.pointList.remove(point)
        return

    def update(self):
        self.grid = np.zeros(self.grid.shape)
        for point in self.pointList:
            ind = point.getindex()
            point.set_neighbour_cells()
            self.grid[ind[0], ind[1]] = 1
        self.updates += 1
        return

    def switch_colours(self):
        self.grid = np.ones(self.grid.shape)
        for point in self.pointList:
            ind = point.get_index()
            self.grid[ind[0], ind[1]] = 0
        self.pointList = pt.Point.create_point_list(
                      list(zip(np.where(self.grid > 0)[0],
                               np.where(self.grid > 0)[1])),
            self.shape)

    def move(self, dir="d"):
        self.grid = np.zeros(self.grid.shape)
        inds = map(lambda x: x.get_index(), self.pointList)
        amt = 1 if dir == "d" or dir == "r" else -1
        if dir == "d" or dir == "u":
            temp = [((item[0] + amt) % self.grid.shape[0], item[1])
                for item in inds]
        else:
            temp = [(item[0], (item[1] + amt) % self.grid.shape[1])
                for item in inds]
        self.pointList = pt.Point.create_point_list(temp, self.shape)
        for indices in inds:
            self.grid[indices[0], indices[1]] = 1

    def get_grid(self):
        return self.grid

    def get_points(self):
        return self.pointList

    def randomize(self):
        self.updates += 1
        self.grid = np.random.randint(2, size=self.shape)

    def view(self):
        plt.imshow(self.grid)
        plt.show()

    def updates(self):
        return self.updates


if __name__=='__main__':
    g = Grid(m=42, locations=[(3,4), (9,7), (18,17)])
    g.view()
    # g.view()
    # print(g.get_points())
    g.move("d")
    print(g.get_points())