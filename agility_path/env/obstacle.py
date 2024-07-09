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
        self.entrance1, self.entrance2 = self._entrance_position()

    def _dimensions(self) -> Tuple[float, float]:
        # Center is at the origin
        if self.type == ObstType.Aframe:
            return 2, 0.2
        elif self.type == ObstType.DogWalk:
            return 3, 0.2
        elif self.type == ObstType.Seesaw:
            return 2, 0.2
        elif self.type == ObstType.Tunnel:
            return 2, 2
        elif self.type == ObstType.Jump:
            return 1, 0.2
        elif self.type == ObstType.Weave:
            return 2, 0.2

    def _entrance_position(self) -> Tuple[Tuple[float, float], Tuple[float, float]]:
        pos_x = 0
        pos_y = self.dim[1] / 2 + 0.2
        x = pos_x * cos(self.rotation) - pos_y * sin(self.rotation)
        y = pos_x * sin(self.rotation) + pos_y * cos(self.rotation)
        return (x, y), (-x, -y)
