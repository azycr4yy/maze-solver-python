# Maze Solver in Python

This project loads a maze image, detects the entry and exit points automatically, and solves the maze using the A* pathfinding algorithm.  
It visualizes the detected openings and the found path over the maze image using OpenCV and Matplotlib.

## Features

- Converts maze images into a binary grid representation.
- Detects start and end openings on the maze edges.
- Solves the maze using an A* algorithm with Manhattan distance heuristic.
- Visualizes the maze, openings, and solution path.

## Requirements

- Python 3.7+
- OpenCV (`opencv-python`)
- NumPy
- Matplotlib

Install dependencies via:

```bash
pip install numpy opencv-python matplotlib
