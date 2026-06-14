#!/Users/krishnathejaupadhyaya/opt/anaconda3/bin/python

import sys

# (dc, dr): dc = column offset from left, dr = row offset from bottom (0 = ground level)
SHAPES = {
    "Q": [(0, 0), (1, 0), (0, 1), (1, 1)],
    "I": [(0, 0), (1, 0), (2, 0), (3, 0)],
    "T": [(1, 0), (0, 1), (1, 1), (2, 1)],
    "S": [(0, 0), (1, 0), (1, 1), (2, 1)],
    "Z": [(1, 0), (2, 0), (0, 1), (1, 1)],
    "L": [(0, 0), (0, 1), (0, 2), (1, 0)],
    "J": [(0, 0), (1, 0), (1, 1), (1, 2)],
}

def print_grid(grid:list[list[str]], width:int, piece:str=None):
    """Render the grid bottom-up as a `*`/`-` ascii diagram, row 0 at the bottom."""
    max_row = len(grid)
    if max_row == 0:
        print("Empty grid")
        return

    if piece:
        print(f"Grid after dropping piece {piece}")
    print(" " + "~"*(width+2))
    for row in range(max_row-1, -1, -1):
        line = ""
        for col in range(width):
            line += "*" if grid[row][col] != ' ' else '-'
        print(f" |{line}|")
    print(" " + "~"*(width+2))

def compute_height(pieces:list[str], show_grid:bool=True, width:int=10)->int:
    """Drop each piece (e.g. "Q0") onto the grid, clear full rows, and return the resulting max column height."""
    grid_height = [0] * width
    grid:list[list[str]]=[]
    full_row = ['*']*width

    def ensure_rows(needed:int):
        while len(grid) < needed:
            grid.append([" "] * width)

    for piece in pieces:
        shape_key = piece[0]
        col = int(piece[1:])
        cells = SHAPES[shape_key]

        land_height = 0
        for (dc, dr) in cells:
            c = col + dc
            land_height = max(land_height, grid_height[c] - dr)

        for (dc, dr) in cells:
            c = col + dc
            r = land_height + dr
            grid_height[c] = max(grid_height[c], r+1)
            ensure_rows(r+1)
            grid[r][c] = '*'

        if show_grid:
            print_grid(grid=grid, width=width, piece=piece)

        cleaned_rows = 0
        while full_row in grid:
            grid.remove(full_row)
            grid_height = [x - 1 for x in grid_height]
            cleaned_rows += 1

        if show_grid and cleaned_rows:
            print(f"Number of rows cleaned: {cleaned_rows}")
            print_grid(grid=grid, width=width)

    return max(grid_height)

INPUT_LINES = [
    "Q0",
    "Q0,Q1",
    "Q0,Q2,Q4,Q6,Q8",
    "Q0,Q2,Q4,Q6,Q8,Q1",
    "Q0,Q2,Q4,Q6,Q8,Q1,Q1",
    "I0,I4,Q8",
    "I0,I4,Q8,I0,I4",
    "L0,J2,L4,J6,Q8",
    "L0,Z1,Z3,Z5,Z7",
    "T0,T3",
    "T0,T3,I6,I6",
    "I0,I6,S4",
    "T1,Z3,I4",
    "L0,J3,L5,J8,T1",
    "L0,J3,L5,J8,T1,T6",
    "L0,J3,L5,J8,T1,T6,J2,L6,T0,T7",
    "L0,J3,L5,J8,T1,T6,J2,L6,T0,T7,Q4",
    "S0,S2,S4,S6",
    "S0,S2,S4,S5,Q8,Q8,Q8,Q8,T1,Q1,I0,Q4",
    "L0,J3,L5,J8,T1,T6,S2,Z5,T0,T7",
    "Q0,I2,I6,I0,I6,I6,Q2,Q4",
]

if __name__ == "__main__":
    for i, line in enumerate(INPUT_LINES):
        print("")
        print(f"{i+1}. input - {line}")
        print(f"Final height of the grid: {compute_height(pieces=line.split(','))}")
