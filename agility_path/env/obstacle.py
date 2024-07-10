from agility_path.util import *


class ObstType(Enum):
    Aframe = auto()
    DogWalk = auto()
    Seesaw = auto()
    Tunnel = auto()
    Jump = auto()
    Weave = auto()


class Obstacle:
    def __init__(self, type_: ObstType, position: Tuple[float, float], rotation: float = 0, margin: float = 0.2):
        self.type = type_
        self.position = position
        self.rotation = rotation
        self.margin = margin
        self.dim = self._dimensions()
        self.gate1, self.gate2 = self._compute_gate_local_position()

    def _dimensions(self) -> Tuple[float, float]:
        # Center is at the origin
        if self.type == ObstType.Aframe:
            return 2, 0.2
        elif self.type == ObstType.DogWalk:
            return 3, 0.2
        elif self.type == ObstType.Seesaw:
            return 2, 0.2
        elif self.type == ObstType.Tunnel:
            return 4, 4
        elif self.type == ObstType.Jump:
            return 1, 0.2
        elif self.type == ObstType.Weave:
            return 2, 0.2

    def _compute_gate_local_position(self) -> Tuple[Tuple[float, float], Tuple[float, float]]:
        MARGIN = 0.3
        if self.type == ObstType.Jump:
            pos_x = 0
            pos_y = self.dim[1] / 2 + MARGIN
            return self._rotate_and_opposite(pos_x, pos_y, self.rotation)
        elif self.type == ObstType.Aframe:
            pos_x = self.dim[0] / 2 + MARGIN
            pos_y = 0
            return self._rotate_and_opposite(pos_x, pos_y, self.rotation)
        elif self.type == ObstType.DogWalk:
            pos_x = self.dim[0] / 2 + MARGIN
            pos_y = 0
            return self._rotate_and_opposite(pos_x, pos_y, self.rotation)
        elif self.type == ObstType.Tunnel:
            pos_x1 = self.dim[0] / 2 + MARGIN
            pos_y1 = -self.dim[1] / 2
            x1, y1 = rotate((pos_x1, pos_y1), radians(self.rotation))
            pos_x2 = -self.dim[0] / 2
            pos_y2 = self.dim[1] / 2 + MARGIN
            x2, y2 = rotate((pos_x2, pos_y2), radians(self.rotation))
            return (x1, y1), (x2, y2)
        raise ValueError

    def check_collision(self, line_start: Tuple[float, float], line_end: Tuple[float, float]) -> bool:
        line_start = sub_coord(line_start, self.position)
        line_end = sub_coord(line_end, self.position)
        line_start = rotate(line_start, -radians(self.rotation))
        line_end = rotate(line_end, -radians(self.rotation))

        # use aabb collision detection
        x1, y1 = line_start
        x2, y2 = line_end
        x, y = self.dim
        x_min, x_max = -x / 2, x / 2
        y_min, y_max = -y / 2, y / 2
        return (x_min <= x1 <= x_max and y_min <= y1 <= y_max) or (x_min <= x2 <= x_max and y_min <= y2 <= y_max)

    def gate_global_position(self, idx: int) -> Tuple[float, float]:
        if idx == 1:
            return add_coord(self.gate1, self.position)
        elif idx == 2:
            return add_coord(self.gate2, self.position)

    @staticmethod
    def _rotate_and_opposite(x: float, y: float, theta_deg: float) -> Tuple[Tuple[float, float], Tuple[float, float]]:
        x, y = rotate((x, y), radians(theta_deg))
        return (x, y), (-x, -y)
