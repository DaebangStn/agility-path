"""
Env 2D
@author: huiming zhou
"""
from agility_path.env.obstacle import ObstType, Obstacle
from agility_path.util import *


class Field:
    def __init__(self):
        self.x_range = 51  # size of background
        self.y_range = 31
        self.motions = [(-GRID_SIZE, 0), (-GRID_SIZE, GRID_SIZE), (0, GRID_SIZE), (GRID_SIZE, GRID_SIZE),
                        (GRID_SIZE, 0), (GRID_SIZE, -GRID_SIZE), (0, -GRID_SIZE), (-GRID_SIZE, -GRID_SIZE)]

        # There are two drawables, obstacle and boundaries
        self.boundaries = self._build_outline()
        self.obstacles = self._add_obstacles()  # indices of list is the order of obstacles

    def _build_outline(self):
        """
        Initialize obstacles' positions
        :return: map of obstacles
        """

        x = self.x_range
        y = self.y_range
        obs = set()

        for i in range(x):
            obs.add((i, 0))
        for i in range(x):
            obs.add((i, y - 1))

        for i in range(y):
            obs.add((0, i))
        for i in range(y):
            obs.add((x - 1, i))

        # for i in range(10, 21):
        #     obs.add((i, 15))
        # for i in range(15):
        #     obs.add((20, i))

        # for i in range(15, 30):
        #     obs.add((30, i))
        # for i in range(16):
        #     obs.add((40, i))

        return obs

    def _add_obstacles(self):
        obs = []
        obs.append(Obstacle(ObstType.Aframe, (15, 15)))
        obs.append(Obstacle(ObstType.DogWalk, (25, 15)))
        return obs
