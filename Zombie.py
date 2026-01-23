import random
import time

# SETTINGS
GRID_SIZE = 10
NUM_HUMANS = 5
NUM_ZOMBIES = 2

HUMAN_SYMBOL = "🧍"
ZOMBIE_SYMBOL = "🧟"
EMPTY_SPACE = "⬜"
# CREATE WORLD / 2D GRID
grid = [[EMPTY_SPACE for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
# Track humans and zombies positions
humans = []
zombies = []

# Place humans randomly
for _ in range(NUM_HUMANS):
    while True:
        x = random.randint(0, GRID_SIZE-1)
        y = random.randint(0, GRID_SIZE-1)
        if grid[y][x] == EMPTY_SPACE:
            grid[y][x] = HUMAN_SYMBOL
            humans.append([x, y])
            break

# Place zombies randomly
for _ in range(NUM_ZOMBIES):
    while True:
        x = random.randint(0, GRID_SIZE-1)
        y = random.randint(0, GRID_SIZE-1)
        if grid[y][x] == EMPTY_SPACE:
            grid[y][x] = ZOMBIE_SYMBOL
            zombies.append([x, y])
            break


# PRINT GRID

def print_grid():
    for row in grid:
        print(" ".join(row))
    print("-" * (GRID_SIZE*2))
# MOVE HUMANS
def move_humans():
    for i, (x, y) in enumerate(humans):
        grid[y][x] = EMPTY_SPACE  # Remove old position
        dx, dy = random.choice([(0,1),(0,-1),(1,0),(-1,0),(0,0)])  # Random move
        nx, ny = x + dx, y + dy
        if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and grid[ny][nx] == EMPTY_SPACE:
            humans[i] = [nx, ny]
            grid[ny][nx] = HUMAN_SYMBOL
        else:
            grid[y][x] = HUMAN_SYMBOL  # stay if blocked
# MOVE ZOMBIES
def move_zombies():
    for i, (zx, zy) in enumerate(zombies):
        grid[zy][zx] = EMPTY_SPACE
        if humans:  # only chase if humans exist
            # Find nearest human
            nearest = min(humans, key=lambda h: abs(h[0]-zx)+abs(h[1]-zy))
            hx, hy = nearest
            # Move one step toward human
            if hx > zx: zx += 1
            elif hx < zx: zx -= 1
            elif hy > zy: zy += 1
            elif hy < zy: zy -= 1

        # Check if zombie reaches human
        if [zx, zy] in humans:
            humans.remove([zx, zy])  # human turned into zombie
            zombies.append([zx, zy]) # new zombie
            grid[zy][zx]
