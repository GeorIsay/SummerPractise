import numpy as np
from Swarm import *


class Adapter:
    def __init__(self):
        self.valMin = None
        self.valMax = None
        self.GWC = None
        self.LWC = None
        self.size = None
        self.dots = None

    def __converVal(self, valList):
        assert len(valList) == 8
        try:
            self.valMin = np.array(list(map(float, valList[:4])))
        except:
            raise (ValueError("Неверные аргументы у нижней границы."))
        try:
            self.valMax = np.array(list(map(float, valList[4:8])))
        except:
            raise (ValueError("Неверные аргументы у верхней границы."))
        for i in range(4):
            if self.valMin[i] >= self.valMax[i]:
                raise (ValueError("Значение {} Min больше или равно значению {} Max.".format(
                    chr(65 + i), chr(65 + i))))

    def __converGLWC(self, valList):
        assert len(valList) == 2
        self.GWC = float(valList[0])
        self.LWC = float(valList[1])
        if self.GWC == 0 and self.LWC == 0:
            raise (ValueError(
                "Global Weight Coefficient и Local Weight Coefficient не могут быть равны 0 однавременно."))
    
    def makeSwarm(self):
        return Swarm(self.valMin, self.valMax, self.size, self.GWC, self.LWC, self.dots)
    
    def inputDots(self, text: str):
        list = text.split(',')
        self.dots = np.zeros((len(list), 2))
        for i in range(len(list)):
            try:
                _x, _y = filter(None, list[i].split())
            except:
                raise (ValueError(
                    "Координаты точки не могут принемать значние {}.".format(list[i])))
            try:
                self.dots[i, 0] = float(_x)
            except:
                raise (ValueError(
                    "На оси абсцисс не может быть значения {}.".format(_x)))
            try:
                self.dots[i, 1] = float(_y)
            except:
                raise (ValueError(
                    "На оси ординат не может быть значения {}.".format(_y)))
    
    def swarmSettings(self, valList):
        assert len(valList) == 11
        self.__converVal(valList[:8])
        self.size = int(valList[8])
        self.__converGLWC(valList[9:11])
    
    # def openSettingsFile(self, fileName):
    #     file = open(fileName, 'r')
    #     valList = file.readlines()
    #     if len(valList) == 12:
    #         try:
    #             self.__converVal(valList[:8])
    #             self.size = int(valList[8])
    #             self.__converGLWC(valList[9:11])
    #             self.inputDots(valList[11])
    #             return
    #         except:
    #             pass
    #     raise(ValueError("Файл не соответсвует формату."))
    
    def openIteratinsFile(self, valList):
        try:
            if len(valList) == 24:
                self.swarmSettings(valList[:11])
                self.inputDots(valList[11])
                valCurent = np.zeros((self.size, 4))
                valLocalBest = np.zeros((self.size, 4))
                velositys = np.zeros((self.size, 4))
                for i in range(12, 16):
                    valCurent[:, i - 12] = list(map(float, valList[i].split(' ')))
                for i in range(16, 20):
                    valLocalBest[:, i - 16] = list(map(float, valList[i].split(' ')))
                for i in range(20, 24):
                    velositys[:, i - 20] = list(map(float, valList[i].split(' ')))
                sw = self.makeSwarm()
                sw.setParticles(valCurent, valLocalBest, velositys)
                return sw
        except ValueError:
            raise(ValueError("Файл не соответсвует формату."))

    def randomDots(self, valList):
        assert len(valList) == 5
        try:
            xMin = float(valList[0])
        except:
            raise(ValueError("X Min не может принемать значение {}.".format(valList[0])))
        try:
            yMin = float(valList[1])
        except:
            raise(ValueError("X Min не может принемать значение {}.".format(valList[1])))
        try:
            xMax = float(valList[2])
        except:
            raise(ValueError("X Min не может принемать значение {}.".format(valList[2])))
        try:
            yMax = float(valList[3])
        except:
            raise(ValueError("X Min не может принемать значение {}.".format(valList[3])))
        self.dots = np.zeros((valList[4], 2))
        self.dots[:, 0] = np.random.uniform(xMin, xMax, valList[4])
        self.dots[:, 1] = np.random.uniform(yMin, yMax, valList[4])
    
    def setSwarmSettings(self, swarm):
        self.valMin = swarm.getMinVal()
        self.valMax = swarm.getMaxVal()
        self.size = swarm.getParticlesNumber()
        self.GWC = swarm.getGWC()
        self.LWC = swarm.getLWC()
        self.dots = swarm.getDots()
    
    def saveSettingsFile(self, fileName):
        file = open(fileName, "w+")
        file.writelines(self.getValList())
        file.close()

    def saveIterationsFile(self, swarm, fileName):
        self.setSwarmSettings(swarm)
        valCurent, valLocalBest, velositys = swarm.getParticles()
        file = open(fileName, "w+")
        file.writelines(self.getValList())
        for i in range(4):
            file.write(' '.join(list(map(str, valCurent[:, i]))) + '\n')
        for i in range(4):
            file.write(' '.join(list(map(str, valLocalBest[:, i]))) + '\n')
        for i in range(4):
            file.write(' '.join(list(map(str, velositys[:, i]))) + '\n')
        file.close()
    
    def getValList(self):
        valList = []
        for i in self.valMin:
            valList.append(str(i)+'\n')
        for i in self.valMax:
            valList.append(str(i)+'\n')
        valList.append(str(self.size)+'\n')
        valList.append(str(self.GWC)+'\n')
        valList.append(str(self.LWC)+'\n')
        dotsList = []
        for i in range(self.dots.shape[0]):
            dotsList.append(str(self.dots[i, 0]) + ' ' + str(self.dots[i, 1]))
        dotsText = ', '.join(dotsList)
        valList.append(dotsText +'\n')
        return valList