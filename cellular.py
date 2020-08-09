import grid as g
import rules

class Cellular:

    def __init__(self, rule_func, **kwargs):
        self.rule = rule_func
        self.grid = g.Grid(**kwargs)

    def update(self):
        pList = self.grid.get_points()


def main():
    cell = Cellular(m=42, locations=[(3,4), (2,4),(3,5), (9,7), (18,17)])
    print(list(map(lambda x: cell.how_many_neighbours(x), cell.grid.get_points())))

if __name__ == "__main__":
    main()
