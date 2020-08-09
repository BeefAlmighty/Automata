import point as pt
import grid

def rules_of_life(point):
    num_neighbours = grid.Grid.how_many_neighbours(point)