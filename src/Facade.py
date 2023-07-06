import numpy as np
import sys
from Swarm import *
from Adapter import Adapter
from PyQt5 import QtWidgets
from UI import *


class Facade:
    def __init__(self):
        self.adapter = Adapter()
        self.swarm = None
        self.app = QtWidgets.QApplication(sys.argv)
        self.GUI = UI(self)
        self.GUI.show()
        sys.exit(self.app.exec_())

    def __swarm_isnt_create(self):
        raise (AttributeError(
            "Swarm isn't create. Please press \"random\", \"input\" or \"file\"."))

    def get_dots(self):
        try:
            return self.swarm.x_y()
        except AttributeError:
            self.__swarm_isnt_create()

    def get_val(self):
        try:
            return self.swarm.best_particle()
        except AttributeError:
            self.__swarm_isnt_create()

    def get_mean_deviation_change(self):
        try:
            self.swarm.mean_deviation_change()
        except AttributeError:
            self.__swarm_isnt_create()

    def random_swarm(self, list):
        self.swarm = self.adapter.random_swarm(list)
        x, y = self.swarm.x_y()
        self.GUI.plot_func(self.swarm.best_particle().best_local_val(), x, y)
        # x, y = self.swarm.mean_deviation_change()
        # self.GUI.plot_mean_deviation_change(x, y)

    def input_swarm(self, list_val):
        self.swarm = self.adapter.input_swarm(list_val)
        x, y = self.swarm.x_y()
        self.GUI.plot_func(self.swarm.best_particle().best_local_val(), x, y)
        # x, y = self.swarm.mean_deviation_change()
        # self.GUI.plot_mean_deviation_change(x, y)

    def file_swarm(self, file_name):
        self.swarm = self.adapter.file_swarm(file_name)
        x, y = self.swarm.x_y()
        self.GUI.plot_func(self.swarm.best_particle().best_local_val(), x, y)
        # x, y = self.swarm.mean_deviation_change()
        # self.GUI.plot_mean_deviation_change(x, y)

    def save_file(self, list, name: str):
        self.adapter.save_file(list, name)


if __name__ == "__main__":
    Facade()
