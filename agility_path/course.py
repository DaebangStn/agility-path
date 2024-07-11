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

    def compute_and_plot_path(self, s_start, s_end):
        tq = tqdm(total=len(self.coord_sequence), desc="Path Planning")
        self.coord_sequence[0][0] = s_start
        self.coord_sequence[-1][1] = s_end
        for i, seq in enumerate(self.coord_sequence):
            planner = AStar(seq[0], seq[1])
            p, _ = planner.searching()
            path_x = [p[i][0] for i in range(len(p))]
            path_y = [p[i][1] for i in range(len(p))]
            plt.plot(path_x, path_y, linewidth='1.5', color='r')

            # Parameterize the data points
            t = np.arange(len(path_x))

            # Create the spline with LSQUnivariateSpline
            smoothing_factor = 0.5  # Adjust this value to get the desired smoothness
            spline_x = UnivariateSpline(t, path_x, s=smoothing_factor, k=3)
            spline_y = UnivariateSpline(t, path_y, s=smoothing_factor, k=3)

            # Evaluate the spline
            t_new = np.linspace(t[0], t[-1], 100)
            path_x_new = spline_x(t_new)
            path_y_new = spline_y(t_new)

            # Enforce the start and end points
            path_x_new[0], path_y_new[0] = path_x[0], path_y[0]
            path_x_new[-1], path_y_new[-1] = path_x[-1], path_y[-1]
            plt.plot(path_x_new, path_y_new, 'b-')

            tq.update(1)
            update_plot()

    def _build_coord_sequence(self) -> List[List[Tuple[float, float]]]:
        seq = []
        obstacles = self.field.obstacles

        for i in range(len(self.idx_sequence)):
            if i == 0:
                ent = obstacles[self.idx_sequence[i][0]].gate_global_position(self.idx_sequence[i][1])
                seq.append([ent, ent])
            else:
                ent1 = obstacles[self.idx_sequence[i-1][0]].gate_global_position(3 - self.idx_sequence[i-1][1])
                ent2 = obstacles[self.idx_sequence[i][0]].gate_global_position(self.idx_sequence[i][1])
                seq.append([ent1, ent2])
        ent = obstacles[self.idx_sequence[-1][0]].gate_global_position(3 - self.idx_sequence[-1][1])
        seq.append([ent, ent])
        return seq
