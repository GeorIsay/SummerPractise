from AbstractSwarm import *
from Particle import *
import numpy as np


class Swarm(AbstractSwarm):
    def __init__(self, size: int, min_val: np.ndarray, max_val: np.ndarray, gwc: float, lwc: float, x: np.ndarray, y: np.ndarray):
        assert len(x) == len(y)
        self.__x = x.copy()
        self.__y = y.copy()
        super().__init__(size, min_val, max_val, gwc, lwc)
        # AbstractSwarm.__init__(self, size, min_val, max_val, gwc, lwc)
        self.__mean_deviation_change = []

    def _particle_comparer(self, particle_1: Particle, particle_2: Particle):
        if particle_1 == None:
            return False
        elif particle_2 == None or particle_1.best_deviation() < particle_2.best_deviation():
            return True
        return False

    def _func(self, particle: Particle):
        # оценка чистицы
        arr = particle.best_local_val()
        size = len(self.__x)
        return sum(abs(self.__y[i] - arr[0] * (self.__x[i] ** 3) - arr[1] * (self.__x[i] ** 2) - arr[2] * self.__x[i] - arr[3]) for i in range(size)) / size

    def iterations(self, num, coef):
        # сам алгоритм
        # num - количество шагов
        # coef - погрешность, при достижении которой можно не продолжать делать шаги до num
        # с кождым откланение добовлять среднее откланение в self.__mean_deviation_change для будущего графика
        pass

    def mean_deviation_change(self):
        return self.__mean_deviation_change

    def x_y(self):
        return self.__x, self.__y
