import numpy as np
from Particle import *
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
        self.__swarm = self.__creat_swarp()

    def __creat_swarp(self):
        coef = (self.__max_val - self.__min_val) / (self.__size + 1)
        cur = self.__max_val
        swarm = []
        for _ in range(self.__size):
            cur += coef
            swarm.append(Particle(cur, self))
            if self._particle_comparer(swarm[-1], self.__best_particle):
                self.__best_particle = swarm[-1]
        return swarm

    def best_particle(self):
        return self.__best_particle

    @abc.abstractmethod
    def _particle_comparer(self, particle_1: Particle, particle_2: Particle):
        # Если первая лучше вернуть True
        pass

    @abc.abstractmethod
    def _func(self, particle: Particle):
        # оценка чистицы
        pass

    @abc.abstractmethod
    def iterations(self, num, coef):
        # делает сам алгоритм num шагов или пока среднее откланение не будет ниже coef
        # возрашает лучшие коэф

        pass
