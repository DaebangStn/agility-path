import matplotlib.pyplot as plt

from agility_path.env.field import Field
from agility_path.env.obstacle import ObstType
from agility_path.env.plotting import Plotting
from agility_path.course import Course
from agility_path.util import *


if __name__ == "__main__":
    s_start = (5.0, 5.0)
    s_goal = (45.0, 25.0)

    f = Field(x_range=50, y_range=50)
    f.add_obstacle(ObstType.Tunnel, (15, 15))
    f.add_obstacle(ObstType.Jump, (25, 15))
    f.add_obstacle(ObstType.DogWalk, (25, 25))
    f.add_obstacle(ObstType.Aframe, (15, 35))
    plot = Plotting(s_start, s_goal, field=f)

    c = Course(f)
    plt.ion()
    plt.show()
    plot.plot_grid('test')
    update_plot()
    c.compute_and_plot_path(s_start, s_goal)
    plt.show(block=True)
