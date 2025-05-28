import numpy as np
import cv2
from queue import PriorityQueue
import matplotlib.pyplot as plt

def convertImageToMaze(jpeg):
    if jpeg is None:
        raise Exception("FAILED TO LOAD IMAGE")
    image = cv2.imread(jpeg, cv2.IMREAD_GRAYSCALE)
    _, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    maze = (binary // 255).astype(np.uint8)
    return maze

def FindStartAndEnd(jpeg):
    maze = convertImageToMaze(jpeg)
    height, width = maze.shape
    openings = set()
    for x in range(width):
        if maze[0, x] == 1:
            openings.add((0, x))
    for x in range(width):
        if maze[height - 1, x] == 1:
            openings.add((height - 1, x))
    for y in range(height):
        if maze[y, 0] == 1:
            openings.add((y, 0))
    for y in range(height):
        if maze[y, width - 1] == 1:
            openings.add((y, width - 1))

    start = None
    for pt in openings:
        if pt[0] == 0 or pt[1] == 0:
            start = pt
            break
    end = None
    for pt in openings:
        if pt[0] == height - 1 or pt[1] == width - 1:
            end = pt
            break
    return openings, start, end

def Manhattan_Value(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def maze_solver(maze, start, end):
    q = PriorityQueue()
    q.put((Manhattan_Value(start, end), 0, start))
    cost_so_far = {start: 0}
    came_from = {}
    while not q.empty():
        _, cost, node = q.get()
        if node == end:
            path = []
            while node in came_from:
                path.append(node)
                node = came_from[node]
            path.append(start)
            return path[::-1]
        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            neighbour = (node[0] + dx, node[1] + dy)
            if (0 <= neighbour[0] < maze.shape[0] and
                0 <= neighbour[1] < maze.shape[1] and
                maze[neighbour] == 1):
                new_cost = cost + 1
                if new_cost < cost_so_far.get(neighbour, float('inf')):
                    cost_so_far[neighbour] = new_cost
                    priority = Manhattan_Value(neighbour, end) + new_cost
                    q.put((priority, new_cost, neighbour))
                    came_from[neighbour] = node
    return None

if __name__ == '__main__':
    jpeg_path = r"file_name"
    openings, start, end = FindStartAndEnd(jpeg_path)
    maze = convertImageToMaze(jpeg_path)
    path = maze_solver(maze, start, end)
    img = cv2.imread(jpeg_path)
    for pt in openings:
        cv2.circle(img, (pt[1], pt[0]), radius=4, color=(0, 0, 255), thickness=-1)
    if path is not None:
        for pt in path:
            cv2.circle(img, (pt[1], pt[0]), radius=0, color=(0, 255, 0), thickness=0)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img_rgb)
    plt.axis('off')
    plt.show()
