import random

def generate_braid_maze(width, height):
    # Create a grid
    maze = [[1 for _ in range(width)] for _ in range(height)]

    # Create the initial paths
    for i in range(1, width, 2):
        for j in range(height):
            maze[j][i] = 0

    # Create random connections between paths
    for i in range(1, width - 2, 2):
        for j in range(height):
            if random.random() < 0.5:
                direction = random.choice([-1, 1])
                if 0 <= j + direction < height:
                    maze[j][i + 1] = 0
                    maze[j + direction][i] = 0

    # Set the entrance and exit
    maze[0][0] = 'S'  # Start
    maze[height - 1][width - 1] = 'E'  # End

    return maze

def print_maze(maze):
    for row in maze:
        print(''.join(map(str, row)))

# Example usage
maze = generate_braid_maze(48, 62)
print_maze(maze)
