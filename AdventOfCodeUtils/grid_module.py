DIRECTIONS = {
    "N": (0,-1),
    "NE": (1,-1),
    "E": (1,0),
    "SE": (1,1),
    "S": (0,1),
    "SW": (-1,1),
    "W": (-1,0),
    "NW": (-1,-1),
}

def tuple_add(tup1, tup2):
    return tuple(a+b for a, b in zip(tup1, tup2))

def get_pos(grid, coord):
    return grid[coord[1]][coord[0]]

def set_pos(grid, coord, val):
    grid[coord[1]][coord[0]] = val

def valid_coord(grid, coord):
    return coord[0] >= 0 and \
           coord[1] >= 0 and \
           coord[0] < len(grid[0]) and \
           coord[1] < len(grid)

def pos_move(coord, dir):
    return tuple_add(coord, DIRECTIONS[dir])

def get_adjacent(grid, coord):
    return [tuple_add(coord, dir) for dir in DIRECTIONS.values() if valid_coord(grid, tuple_add(coord, dir))]

def grid_print(grid):
    print("\n".join(["".join(row) for row in grid]))

def get_locations(grid, val):
    locs = []
    for i in range(len(grid)):
        cols = [j for j,x in enumerate(grid[i]) if x == val]
        locs.extend([(j,i) for j in cols])
    return locs