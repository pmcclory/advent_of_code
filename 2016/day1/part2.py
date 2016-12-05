#! /usr/bin/python

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

def get_distance(directions):
    north_blocks = 0
    east_blocks = 0 
    current_dir = NORTH

    visited = set()
    visited.add((0,0))

    for step in directions.split(","):
        step = step.strip()
        step_dir = 1 if step[0] == "R" else -1
        step_size = int(step[1:])
       
        current_dir = (current_dir + step_dir) % 4

        for i in range(0, step_size):
            if current_dir == NORTH:
                north_blocks += 1
            elif current_dir == SOUTH:
                north_blocks -= 1
            elif current_dir == EAST:
                east_blocks += 1
            else:
                east_blocks -= 1
            if (north_blocks, east_blocks) in visited:
                return abs(north_blocks) + abs(east_blocks)
            else:
                visited.add((north_blocks, east_blocks))

assert(get_distance("R8, R4, R4, R8") == 4)
print "%d blocks" % (get_distance("L1, L3, L5, L3, R1, L4, L5, R1, R3, L5, R1, L3, L2, L3, R2, R2, L3, L3, R1, L2, R1, L3, L2, R4, R2, L5, R4, L5, R4, L2, R3, L2, R4, R1, L5, L4, R1, L2, R3, R1, R2, L4, R1, L2, R3, L2, L3, R5, L192, R4, L5, R4, L1, R4, L4, R2, L5, R45, L2, L5, R4, R5, L3, R5, R77, R2, R5, L5, R1, R4, L4, L4, R2, L4, L1, R191, R1, L1, L2, L2, L4, L3, R1, L3, R1, R5, R3, L1, L4, L2, L3, L1, L1, R5, L4, R1, L3, R1, L2, R1, R4, R5, L4, L2, R4, R5, L1, L2, R3, L4, R2, R2, R3, L2, L3, L5, R3, R1, L4, L3, R4, R2, R2, R2, R1, L4, R4, R1, R2, R1, L2, L2, R4, L1, L2, R3, L3, L5, L4, R4, L3, L1, L5, L3, L5, R5, L5, L4, L2, R1, L2, L4, L2, L4, L1, R4, R4, R5, R1, L4, R2, L4, L2, L4, R2, L4, L1, L2, R1, R4, R3, R2, R2, R5, L1, L2"))
