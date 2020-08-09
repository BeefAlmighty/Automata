import point as pt
import numpy as np
import matplotlib.pyplot as plt
import random

class Grid:

    def __init__(self, **kwargs):
        self.updates = 0
        self.livePointList = None
        if 'arr' in kwargs:
            self.grid = kwargs['arr']
        elif 'm' in kwargs and 'n' in kwargs:
            self.grid = np.zeros((kwargs['m'], kwargs['n']))
        elif 'm' in kwargs and not 'n' in kwargs:
            self.grid = np.zeros((kwargs['m'], kwargs['m']))
        self.shape = self.grid.shape
        if 'locations' in kwargs:
            indexList = kwargs['locations']
            self.livePointList = pt.Point.create_point_list(indexList,
                                                            self.shape)
            for indices in indexList:
                self.grid[indices[0], indices[1]] = 1
        self.deadPointList = []
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                if not self.grid[i,j]:
                    self.deadPointList.append(pt.Point((i,j),
                                                       self.shape,
                                                       alive = False))


    def remove_point(self, point):
        self.livePointList.remove(point)
        return

    def update(self):
        self.grid = np.zeros(self.grid.shape)
        for point in self.livePointList:
            ind = point.get_index()
            point.set_neighbour_cells()
            self.grid[ind[0], ind[1]] = 1
        for point in self.deadPointList:
            ind = point.get_index()
            point.set_neighbour_cells()
            self.grid[ind[0], ind[1]] = 0
        self.updates += 1
        return

    def switch_colours(self):
        self.grid = np.ones(self.grid.shape)
        for point in self.livePointList:
            ind = point.get_index()
            self.grid[ind[0], ind[1]] = 0
        self.livePointList = pt.Point.create_point_list(
                      list(zip(np.where(self.grid > 0)[0],
                               np.where(self.grid > 0)[1])),
            self.shape)

    def how_many_live_neighbours(self, point):
        locations = self.get_live_points()
        other_points = [item for item in locations if item != point]
        return sum([1 for item in other_points if point.touching(item)])

    def get_grid(self):
        return self.grid

    def get_live_points(self):
        return self.livePointList

    def get_dead_points(self):
        return self.deadPointList

    def randomize(self, point):
        num = random.randint(0,1)
        if num == 1:
            return pt.Point(point.location,
                            self.shape,
                            alive=True)
        else:
            return pt.Point(point.location,
                            self.shape,
                            alive=False)


    def view(self):
        plt.imshow(self.grid)
        plt.show()

    def close(self):
        plt.close()

    def updates(self):
        return self.updates

    def rules_of_life(self, point):
        live_neighbours = self.how_many_live_neighbours(point)
        if not point.state and live_neighbours == 3:
            return pt.Point(point.location,
                            self.shape,
                            alive=True)
        elif point.state and live_neighbours != 2 and live_neighbours != 3:
            return pt.Point(point.location,
                            self.shape,
                            alive=False)
        else:
            return point

    def apply_rule(self, rule):
        newPoints = list(map(rule, self.livePointList + self.deadPointList))
        self.livePointList = [item for item in newPoints if item.state]
        self.deadPointList = [item for item in newPoints if not item.state]
        self.update()
        return None

if __name__=='__main__':
    g = Grid(m=10, locations=[(4,7),(5,7),(6,7),(6,6), (5,5)])
    g.view()
    while g.updates < 15:
        g.close()
        g.apply_rule(g.rules_of_life)
        g.view()