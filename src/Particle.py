import numpy as np


class Particle:
    def __init__(self, arr: np.ndarray, swarm):
        self.__swarm = swarm
        self.__val = arr.copy()
        self.__best_val = arr.copy()
        self.__cur_deviat = swarm._func(self)
        self.__best_deviat = self.__cur_deviat

    def next_iteration(self, velosity: np.ndarray):
        self.__val += velosity
        self.__cur_deviat = self.__swarm._func(self)
        if self.__cur_deviat < self.__best_deviat:
            self.__best_deviat = self.__cur_deviat
            self.__best_val = self.__val.copy()
        return self.__best_deviat

    def best_deviation(self):
        return self.__best_deviat

    def best_local_val(self):
        return self.__best_val
