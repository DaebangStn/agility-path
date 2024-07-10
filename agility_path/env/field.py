"""
Env 2D
@author: huiming zhou
"""
from agility_path.env.obstacle import ObstType, Obstacle
from agility_path.util import *


class Field:
    def __init__(self):
        self.x_range = 51  # size of background
        self.y_range = 51
        self.motions = [(-GRID_SIZE, 0), (-GRID_SIZE, GRID_SIZE), (0, GRID_SIZE), (GRID_SIZE, GRID_SIZE),
                        (GRID_SIZE, 0), (GRID_SIZE, -GRID_SIZE), (0, -GRID_SIZE), (-GRID_SIZE, -GRID_SIZE)]

        # There are two drawables, obstacle and boundaries
        self.boundaries = self._build_boundary()
        self.obstacles = self._add_obstacles()  # indices of list is the order of obstacles

    def _build_boundary(self):
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
        return obs

    def _add_obstacles(self):
        obs = []
        obs.append(Obstacle(ObstType.Tunnel, (15, 15)))
        obs.append(Obstacle(ObstType.Jump, (25, 15)))
        obs.append(Obstacle(ObstType.DogWalk, (25, 25)))
        obs.append(Obstacle(ObstType.Aframe, (15, 35)))
        return obs

    def check_collision(self, s_start: Tuple[float, float], s_end: Tuple[float, float]) -> bool:
        # boundary
        if s_start in self.boundaries or s_end in self.boundaries:
            return True

        if s_start[0] != s_end[0] and s_start[1] != s_end[1]:
            if s_end[0] - s_start[0] == s_start[1] - s_end[1]:
                s1 = (min(s_start[0], s_end[0]), min(s_start[1], s_end[1]))
                s2 = (max(s_start[0], s_end[0]), max(s_start[1], s_end[1]))
            else:
                s1 = (min(s_start[0], s_end[0]), max(s_start[1], s_end[1]))
                s2 = (max(s_start[0], s_end[0]), min(s_start[1], s_end[1]))

            if s1 in self.boundaries or s2 in self.boundaries:
                return True

        # obstacle
        for obs in self.obstacles:
            if obs.check_collision(s_start, s_end):
                return True

        return False
