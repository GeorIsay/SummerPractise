import numpy as np
from Swarm import Swarm


class Adapter:
    def __init__(self):
        pass

    def __conver_val(self, list_val):
        assert len(list_val) == 8
        try:
            min_val = np.array(list(map(float, list_val[:4])))
        except:
            raise (ValueError("Неверные аргументы у нижней границы."))
        try:
            max_val = np.array(list(map(float, list_val[4:8])))
        except:
            raise (ValueError("Неверные аргументы у верхней границы."))
        for i in range(4):
            if min_val[i] >= max_val[i]:
                raise (ValueError("Значение {} Min больше или равно значению {} Max.".format(
                    chr(65 + i), chr(65 + i))))
        return min_val, max_val

    def __conver_glwc(self, list_val):
        assert len(list_val) == 2
        gwc = float(list_val[0])
        lwc = float(list_val[1])
        if gwc == 0 and lwc == 0:
            raise (ValueError(
                "Global Weight Coefficient и Local Weight Coefficient не могут быть равны 0 однавременно."))
        return gwc, lwc

    def __conver_dots(self, text: str):
        list = text.split(',')
        x = np.zeros(len(list))
        y = np.zeros(len(list))
        for i in range(len(list)):
            try:
                _x, _y = filter(None, list[i].split())
            except:
                raise (ValueError(
                    "Координаты точки не могут принемать значние {}.".format(list[i])))
            try:
                x[i] = float(_x)
            except:
                raise (ValueError(
                    "На оси абсцисс не может быть значения {}.".format(_x)))
            try:
                y[i] = float(_y)
            except:
                raise (ValueError(
                    "На оси ординат не может быть значения {}.".format(_y)))
        return x, y

    def random_swarm(self, list_val) -> Swarm:
        assert len(list_val) == 14
        min_val, max_val = self.__conver_val(list_val[:8])
        gwc, lwc = self.__conver_glwc(list_val[8:10])
        swarm = list_val[10]
        iter = list_val[11]
        rat_coef = list_val[12]
        x = np.random.uniform(0, 100, (list_val[13]))
        y = np.random.uniform(0, 100, (list_val[13]))
        sw = Swarm(swarm, min_val, max_val, gwc, lwc, x, y)
        sw.iterations(iter, rat_coef)
        return sw

    def input_swarm(self, list_val) -> Swarm:
        assert len(list_val) == 14
        min_val, max_val = self.__conver_val(list_val[:8])
        gwc, lwc = self.__conver_glwc(list_val[8:10])
        swarm = list_val[10]
        iter = list_val[11]
        rat_coef = list_val[12]
        x, y = self.__conver_dots(list_val[13])
        sw = Swarm(swarm, min_val, max_val, gwc, lwc, x, y)
        sw.iterations(iter, rat_coef)
        return sw

    def save_file(self, list_val, file_name: str):
        self.__conver_val(list_val[:8])
        self.__conver_glwc(list_val[8:10])
        for i in range(8, 13):
            list_val[i] = str(list_val[i])
        self.__conver_dots(list_val[13])
        file = open(file_name, "w+")
        for i in list_val:
            file.write(i + '\n')

    def file_swarm(self, file_name):
        file = open(file_name, 'r')
        list_val = file.readlines()
        if len(list_val) == 14:
            try:
                min_val, max_val = self.__conver_val(list_val[:8])
                gwc, lwc = self.__conver_glwc(list_val[8:10])
                swarm = int(list_val[10])
                iter = int(list_val[11])
                rat_coef = float(list_val[12])
                x, y = self.__conver_dots(list_val[13])
                sw = Swarm(swarm, min_val, max_val, gwc, lwc, x, y)
                sw.iterations(iter, rat_coef)
                return sw
            except:
                pass
        raise (ValueError("Файл не соответсвует формату."))
