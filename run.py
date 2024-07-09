from agility_path.Astar import AStar
from agility_path.env.field import Field
from agility_path.env.plotting import Plotting
from agility_path.course import Course


if __name__ == "__main__":
    s_start = (5.0, 5.0)
    s_goal = (45.0, 25.0)
    plot = Plotting(s_start, s_goal)
    # astar = AStar(s_start, s_goal)
    # path, _ = astar.searching()
    # plot.animation(path, [], "A*")

    f = Field()
    c = Course(f)
    plot.animation(c.compute_path(s_start, s_goal), [], "A*")
