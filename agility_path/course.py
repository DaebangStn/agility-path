from agility_path.Astar import AStar
from agility_path.env.field import Field
from agility_path.util import *


class Course:
    def __init__(self, field: Field):
        self.field = field
        self.num_obstacles = len(field.obstacles)
        self.idx_sequence = self._build_idx_sequence()
        self.coord_sequence = self._build_coord_sequence()

    def _build_idx_sequence(self) -> List[Tuple[int, int]]:
        seq = []
        for i in range(self.num_obstacles):
            ent_idx = randint(1, 2)
            seq.append((i, ent_idx))
        return seq

    def compute_path(self, s_start, s_end) -> List[List[Tuple[float, float]]]:
        path = []
        self.coord_sequence[0][0] = s_start
        self.coord_sequence[-1][1] = s_end
        for i, seq in enumerate(self.coord_sequence):
            planner = AStar(seq[0], seq[1])
            p, _ = planner.searching()
            path.append(p)
        return path

    def _build_coord_sequence(self) -> List[List[Tuple[float, float]]]:
        seq = []
        obstacles = self.field.obstacles

        for idx, ent_idx in self.idx_sequence:
            if idx == 0:
                ent = obstacles[0].gate_global_position(ent_idx)
                seq.append([ent, ent])
            else:
                ent1 = obstacles[idx-1].gate_global_position(3 - ent_idx)
                ent2 = obstacles[idx].gate_global_position(ent_idx)
                seq.append([ent1, ent2])
        ent = obstacles[-1].gate_global_position(3 - self.idx_sequence[-1][1])
        seq.append([ent, ent])
        return seq
