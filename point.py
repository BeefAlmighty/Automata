class Point:

    def __init__(self,
                 location,
                 gridSize,
                 alive=True):
        self._state = alive
        self._location = location
        self._gridSize = gridSize
        self.neighbourCells = {}
        self.neighbourCellList = []
        self.set_neighbour_cells()

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.location == other.location \
                   and self.gridsize == other.gridsize\
                    and self._state == other.state
        return False

    def __repr__(self):
        return '(' + str(self.location[0]) \
               + ',' + str(self.location[1]) + ')'


    def touching(self, point):
        return point.location in self.neighbourCells.values()

    @property
    def state(self):
        return self._state

    @property
    def gridsize(self):
        return self._gridSize

    @property
    def location(self):
        return self._location

    def die(self):
        self._state = False

    def live(self):
        self._state = True

    def apply_rules(self, rule_func):
        rule_func(self)
        return

    def set_neighbour_cells(self):
        dirs = ["u", "d", "l", "r", "ur", "ul", "dr", "dl"]
        pos = [self.neighbour_cell(item) for item in dirs]
        self.neighbourCellList = [item for item in pos if item]
        for dir in dirs:
            self.neighbourCells[dir] = self.neighbour_cell(dir)
        return

    @staticmethod
    def in_grid(location, gridShape):
        return location[0] in range(gridShape[0]) \
               and location[1] in range(gridShape[1])

    @staticmethod
    def create_point_list(locationList, gridSize, alive=True):
        ans = []
        for loc in locationList:
            point = Point(loc, gridSize, alive)
            point.set_neighbour_cells()
            ans += [point]
        return ans

    def neighbour_cell(self, dir=None):
        x, y = self.get_index()
        amt = 1 if dir in ["r", "d", "ur", "dr", "ru", "rd"] else -1
        if dir in ["u", "d", "ur", "ru", "ul", "lu", "dr", "rd", "dl", "ld"]:
            x += amt
        if dir in ["l", "r", "ur", "ru", "ul", "lu", "dr", "rd", "dl", "ld"]:
            y += amt
        if dir == "ur":
            x -= 2
        elif dir == "dl":
            x += 2
        if Point.in_grid((x, y), self.gridsize):
            return (x, y)
        else:
            return None

    def move(self, dir=None):
        if dir:
            self.__init__(self.neighbourCells[dir], self.gridsize)
        return

    def get_index(self):
        return [self.location[0], self.location[1]]

    def get_neighbour_list(self):
        return self.neighbourCellList

    def get_neighbours(self):
        return self.neighbourCells


def main():
    p = Point((2,3), (42, 42))
    q = Point((1,5),(42,42))
    print(p.touching(q))
    p.set_neighbour_cells()
    print(p.get_neighbours())
    p.move("ul")
    print(p)
    p.move("l")
    print(p)


if __name__ == "__main__":
    main()