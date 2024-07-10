"""
Plot tools 2D
@author: huiming zhou
"""
import matplotlib.pyplot as plt

from agility_path.env.field import Field
from agility_path.util import *


class Plotting:
    def __init__(self, xI, xG):
        self.xI, self.xG = xI, xG
        self.env = Field()

    def animation(self, path, visited, name):
        self.plot_grid(name)
        # self.plot_visited(visited)
        self.plot_paths(path)
        plt.show()

    def plot_grid(self, name):
        self._plot_boundaries()
        self._plot_obstacles()

        plt.plot(self.xI[0], self.xI[1], "bs")
        plt.plot(self.xG[0], self.xG[1], "gs")
        plt.title(name)
        plt.axis("equal")

    def _plot_boundaries(self):
        obs_x = [x[0] for x in self.env.boundaries]
        obs_y = [x[1] for x in self.env.boundaries]
        plt.plot(obs_x, obs_y, "sk")

    def _plot_obstacles(self):
        for i, obs in enumerate(self.env.obstacles):
            center = sub_coord(obs.position, div_coord(obs.dim, 2))
            bound = patches.FancyBboxPatch(center, obs.dim[0], obs.dim[1], boxstyle="round,pad=0.1", ec="r",
                                           fc="gray", linewidth=0.5, linestyle='--')
            t = (transforms.Affine2D().rotate_deg_around(obs.position[0], obs.position[1], obs.rotation) +
                 plt.gca().transData)
            bound.set_transform(t)
            plt.gca().add_patch(bound)
            plt.plot(obs.gate1[0] + obs.position[0], obs.gate1[1] + obs.position[1], "ro", markersize=3)
            plt.plot(obs.gate2[0] + obs.position[0], obs.gate2[1] + obs.position[1], "go", markersize=3)
            plt.text(obs.position[0], obs.position[1], str(i), fontsize=8, color='black', ha='center', va='center')

    def plot_visited(self, visited, cl='gray'):
        if self.xI in visited:
            visited.remove(self.xI)

        if self.xG in visited:
            visited.remove(self.xG)

        count = 0

        for x in visited:
            count += 1
            plt.plot(x[0], x[1], color=cl, marker='o')
            plt.gcf().canvas.mpl_connect('key_release_event',
                                         lambda event: [exit(0) if event.key == 'escape' else None])

            if count < len(visited) / 3:
                length = 20
            elif count < len(visited) * 2 / 3:
                length = 30
            else:
                length = 40
            #
            # length = 15

            if count % length == 0:
                plt.pause(0.001)
        plt.pause(0.01)

    def plot_paths(self, paths: List[List[Tuple[float, float]]]):
        for path in paths:
            path_x = [path[i][0] for i in range(len(path))]
            path_y = [path[i][1] for i in range(len(path))]
            plt.plot(path_x, path_y, linewidth='1.5', color='r')

        plt.plot(self.xI[0], self.xI[1], "bs")
        plt.plot(self.xG[0], self.xG[1], "gs")

        # plt.pause(0.01)

    @staticmethod
    def color_list():
        cl_v = ['silver',
                'wheat',
                'lightskyblue',
                'royalblue',
                'slategray']
        cl_p = ['gray',
                'orange',
                'deepskyblue',
                'red',
                'm']
        return cl_v, cl_p

    @staticmethod
    def color_list_2():
        cl = ['silver',
              'steelblue',
              'dimgray',
              'cornflowerblue',
              'dodgerblue',
              'royalblue',
              'plum',
              'mediumslateblue',
              'mediumpurple',
              'blueviolet',
              ]
        return cl
