import sys
from pathlib import Path

project_root = str(Path(__file__).parent.parent)
sys.path.append(project_root)

from utils.base import script_handler

input = """.....8............1r.....a....................O...
.a..............4..q.........................0...9
....a.........8...................................
.................D.....................V0.........
.....d............................................
.r..........q....................................O
..................q...........................9...
..............D..............X..................V.
........D................X.................0......
.........8............X...........................
....................J....................9..0.....
..a..B............r..W........J...............R..Q
......WD...q.....1..........Q..............R..V...
.1W...................u...........................
..............................u.............R.....
....B..............d..c..................R........
.............J..............X............V........
......1...........................3...............
......B...........d...................3...........
............8..J.......u.....3....................
...........4.............6........................
.....4v.............d.......................O.....
..........................v.2.....................
.............................................s....
..................4...M..W..................s.....
......................m...........................
...........M......................................
..b..................c............................
....................Co..........KQ.......O.s......
.................C............................s...
.......x............c............................3
........o......A....U.....Q.........5.............
...............U..................j...5...........
.....K.......U................j..........2........
.......A.v.....w.....................c...5........
..K....................................j..........
...............K.yk....B.............2............
......C....b..............x...........Y...........
.....mA..C......U.................................
........M.....A.....................2..6...5......
.............................7.......Y............
.m.M......w..v....................................
............m...........x.....Y...................
....................k....w........................
......b.....w..S....7.............................
..............S..............x...........Y........
....................S...6.........................
.y...............S..........7.6.................9.
o..........k...............b......................
yo...........k...................................."""

def find_antinodes(grid):
    # Find all antenna locations
    antennas = {}
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell != '.':
                if cell not in antennas:
                    antennas[cell] = []
                antennas[cell].append((x, y))
    
    # Set to track unique antinode locations
    antinodes = set()
    
    # Check antinodes for each frequency
    for freq, locations in antennas.items():
        # Check every pair of antennas with this frequency
        for i in range(len(locations)):
            for j in range(i+1, len(locations)):
                x1, y1 = locations[i]
                x2, y2 = locations[j]
                
                # Calculate direction and distance
                dx = x2 - x1
                dy = y2 - y1
                
                # Find the two antinodes
                antinodes_for_pair = [
                    (x1 - dx, y1 - dy),  # antinode before first antenna
                    (x2 + dx, y2 + dy)   # antinode after second antenna
                ]
                
                # Add valid antinodes (within map bounds)
                for ax, ay in antinodes_for_pair:
                    if 0 <= ax < len(grid[0]) and 0 <= ay < len(grid):
                        antinodes.add((ax, ay))
    
    return len(antinodes)

@script_handler
def main() -> None:
    # Convert input to 2D grid
    grid = [list(line.strip()) for line in input.strip().splitlines()]
    
    # Calculate and print number of unique antinode locations
    result = find_antinodes(grid)
    print(f"Number of unique antinode locations: {result}")
    
if __name__ == "__main__":
    main()