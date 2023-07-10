import random
import numpy
import math
import matplotlib.pyplot as plt

class Swarm (object):
    def __init__ (self, min_val, max_val, SwarmSize, a_g, a_l, dots):
        self.dots = dots.copy()
        self.swarmsize = SwarmSize
        self.min_val = numpy.array(min_val[:]) # MIN границы значений коэффециентов Ax^3 + Bx^2 + Cx + D: min_val[0] = A, min_val[1] = B ...
        self.max_val = numpy.array(max_val[:]) # MAX границы значений коэффециентов
        self.best_func = []
        self.iterCount = 0 # для графика!
        self.iterAmount = 5 # Для алгоритма
        self.Global_best = None # Минимальное отклонениние всего роя
        self.Global_pos = None # Лучшие коэффциенты всего роя, где Global_pos = [A, B, C, D]
        self.a_g = a_g # Весовой коэффициент при локальном отклонении
        self.a_l = a_l # Весовой коэффициент при глобальном отклонении
        self.swarm = self.createSwarm()

    def getBestVal(self):
        return numpy.array(self.Global_pos)

    def getDots(self):
        return self.dots.copy()

    def getMinVal(self):
        return self.min_val.copy()

    def getMaxVal(self):
        return self.max_val.copy()

    def getParticlesNumber(self):
        return self.swarmsize

    def getGWC(self):
        return self.a_g

    def getLWC(self):
        return self.a_l

    def getParticles(self):
        m1 = numpy.zeros((self.swarmsize, 4))
        m2 = numpy.zeros((self.swarmsize, 4))
        m3 = numpy.zeros((self.swarmsize, 4))
        for i in range(self.swarmsize):
            m1[i, :] = self.swarm[i].currentPosition
            m2[i, :] = self.swarm[i].localBestPosition
            m3[i, :] = self.swarm[i].velocity
        return m1, m2, m3

    def getMeanDeviationChange(self):
        return [x[1] / self.swarmsize for x in self.best_func]
    
    def setMeanDeviationChange(self, y):
        self.best_func = [[i, y[i] * self.swarmsize] for i in range(len(y))]

    def iterations(self, iterationsNumber):
        self.iterAmount = iterationsNumber
        self.doIteration()

    def setParticles(self, valCurent, valLocalBest, velositys):
        i = 0
        self.swarm = []
        self.swarmsize = valCurent.shape[0]
        for i in range(self.swarmsize):
            particle = Particle(self)
            particle.currentPosition[0:4] = valCurent[i, 0:4]
            particle.localBestPosition[0:4] = valLocalBest[i, 0:4]
            particle.velocity[0:4] = velositys[i, 0:4]
            self.swarm.append(particle)
            particle.CheckFunc(self)

    def createSwarm (self):
        return [Particle(self) for i in range (self.swarmsize) ]

    def doIteration(self):
        for i in range(self.iterAmount):
            self.iterCount+=1
            for particle in self.swarm:
                particle.nextIteration_canon(self)
            self.best_func.append([self.iterCount, self.Global_best])

        #Вывод
        # print(self.best_func)
        # X = [x[0] for x in self.best_func]
        # Y = [x[1] for x in self.best_func]
        # plt.plot(X, Y) #График функции отклонений

        # y = lambda x: self.Global_pos[0] * x ** 3 + self.Global_pos[1] * x ** 2 + self.Global_pos[2] * x + self.Global_pos[3]
        # X_coords = [x[0] for x in self.dots]
        # Y_coords = [x[1] for x in self.dots]
        # fig = plt.subplots()
        # x = numpy.linspace(-100, 100, 10000)
        # plt.plot(x, y(x))
        # plt.scatter(X_coords, Y_coords, c="red")
        # plt.grid(True)
        # plt.show()


class Particle():
    def __init__ (self, swarm):
        #Текущее положение частицы
        self.currentPosition = [random.uniform(swarm.min_val[0], swarm.max_val[0]), random.uniform(swarm.min_val[1], swarm.max_val[1]), random.uniform(swarm.min_val[2], swarm.max_val[2]), random.uniform(swarm.min_val[3], swarm.max_val[3])]

        #Начальные скорости velocity = [v_A, v_B, v_C, v_D]
        self.velocity = [random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)]

        #Лучшие состояние частицы
        self.localBestPosition = self.currentPosition[:]
        self.localBestDeviation = None

    def deviation(self, swarm): #Целевая функция отклонения полинома от набора точек
        res = 0
        for i in swarm.dots:
            F = self.currentPosition[0] * (i[0] ** 3) + self.currentPosition[1] * i[0] ** 2 + self.currentPosition[2] * i[0] + self.currentPosition[3]
            res += math.fabs(i[1] - F)
        return res

    def CheckFunc(self, swarm): #Проверка целевой функции
        func = self.deviation(swarm)
        if(self.localBestDeviation == None or func < self.localBestDeviation):
            self.localBestDeviation = func
            self.localBestPosition = self.currentPosition[:]
        if (swarm.Global_best == None or func < swarm.Global_best):
            swarm.Global_best = func
            swarm.Global_pos = self.currentPosition[:]


    def nextIteration_classic(self, swarm): #Классический алгоритм
        self.CheckFunc(swarm)

        #Корректировка скорости
        self.velocity[0] += swarm.a_l * random.random() * (self.localBestPosition[0] - self.currentPosition[0]) + swarm.a_g * random.random() * (swarm.Global_pos[0] - self.currentPosition[0])
        self.velocity[1] += swarm.a_l * random.random() * (self.localBestPosition[1] - self.currentPosition[1]) + swarm.a_g * random.random() * (swarm.Global_pos[1] - self.currentPosition[1])
        self.velocity[2] += swarm.a_l * random.random() * (self.localBestPosition[2] - self.currentPosition[2]) + swarm.a_g * random.random() * (swarm.Global_pos[2] - self.currentPosition[2])
        self.velocity[3] += swarm.a_l * random.random() * (self.localBestPosition[3] - self.currentPosition[3]) + swarm.a_g * random.random() * (swarm.Global_pos[3] - self.currentPosition[3])

        # Обновить позицию частицы
        self.currentPosition[0] += self.velocity[0]
        self.currentPosition[1] += self.velocity[1]
        self.currentPosition[2] += self.velocity[2]
        self.currentPosition[3] += self.velocity[3]

    def nextIteration_canon(self, swarm): #Канонический алгоритм
        self.CheckFunc(swarm)
        k = random.random()
        a = swarm.a_l
        b = swarm.a_g
        if a + b < 4:
            a = 1.7
            b = 2.8
        p = a + b
        tmp = 2 - p - (p * p - 4 * p) ** 0.5
        x = (2 * k) / math.fabs(tmp)

        #Корректировка скорости
        self.velocity[0] = x * (self.velocity[0] + random.random()) * a * (self.localBestPosition[0] - self.currentPosition[0]) + random.random() * b * (swarm.Global_pos[0] - self.currentPosition[0])
        self.velocity[1] = x * (self.velocity[1] + random.random()) * a * (self.localBestPosition[1] - self.currentPosition[1]) + random.random() * b * (swarm.Global_pos[1] - self.currentPosition[1])
        self.velocity[2] = x * (self.velocity[2] + random.random()) * a * (self.localBestPosition[2] - self.currentPosition[2]) + random.random() * b * (swarm.Global_pos[2] - self.currentPosition[2])
        self.velocity[3] = x * (self.velocity[3] + random.random()) * a * (self.localBestPosition[3] - self.currentPosition[3]) + random.random() * b * (swarm.Global_pos[3] - self.currentPosition[3])

        #Движение частиц
        self.currentPosition[0] += self.velocity[0]
        self.currentPosition[1] += self.velocity[1]
        self.currentPosition[2] += self.velocity[2]
        self.currentPosition[3] += self.velocity[3]
        x = 10
        if self.currentPosition[0] > swarm.max_val[0] or self.currentPosition[1] > swarm.max_val[1] or self.currentPosition[2] > swarm.max_val[2] or self.currentPosition[3] > swarm.max_val[3] or self.currentPosition[0] < swarm.min_val[0] or self.currentPosition[1] < swarm.min_val[1] or self.currentPosition[2] < swarm.min_val[2] or self.currentPosition[3] < swarm.min_val[3]:
            self.currentPosition[0] = swarm.Global_pos[0]
            self.currentPosition[1] = swarm.Global_pos[1]
            self.currentPosition[2] = swarm.Global_pos[2]
            self.currentPosition[3] = swarm.Global_pos[3]


if __name__ == "__main__":
    swarmsize = 200
    dots = numpy.array([[0,0], [25,2], [-10, -20], [30, 20], [5, 6]])
    min_val = [-10,-10,-10,-10]
    max_val = [10, 10, 10, 10]
    a_g = 0.7
    a_l = 0.5
    swarm = Swarm(min_val, max_val, swarmsize, a_g, a_l, dots)
    swarm.iterAmount = 2
    swarm.doIteration()
    swarm.doIteration()
    print(swarm.Global_best)
    print(swarm.Global_pos)
    print(swarm.dots)
    print(swarm.best_func)