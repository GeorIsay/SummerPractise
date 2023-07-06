import numpy as np
from Particle import Particle
import abc


class AbstractSwarm(abc.ABC):
    def __init__(self, size: int, min_val: np.ndarray, max_val: np.ndarray, gwc: float, lwc: float):
        self.__size = size
        assert len(min_val) == len(max_val)
        self.__min_val = min_val
        self.__max_val = max_val
        self.__gwc = gwc
        self.__lwc = lwc
        self.__best_particle = None
        self.__swarp = self.__creat_swarp()

    def __creat_swarp(self):
        coef = (self.__max_val - self.__min_val) / (self.size + 1)
        cur = self.__max_val
        for _ in range(self.size):
            cur += coef
            self.__swarp.append(Particle(cur, self))
            if self.__particle_comparer(self.__swarp[-1], self.__best_particle):
                self.__best_particle = self.__swarp[-1]

    def best_particle(self):
        return self.__best_particle

    @abc.abstractmethod
    def __particle_comparer(self, particle_1: Particle, particle_2: Particle):
        pass

    @abc.abstractmethod
    def _func(self, particle: Particle):
        # оценка чистицы
        pass

    @abc.abstractmethod
    def iterations(self, num, coef):
        # делает сам алгоритм num шагов или пока среднее откланение не будет ниже coef

        pass
