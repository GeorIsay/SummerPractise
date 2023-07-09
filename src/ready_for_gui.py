import random
import numpy
import math

class Swarm (object):
    def __init__ (self, SwarmSize, dots_num, min_val, max_val, a_g, a_l):
        self.dots = [[random.uniform(-10, 10), random.uniform(-10, 10)] for i in range(dots_num) ]
        self.swarmsize = SwarmSize
        self.min_val = numpy.array(min_val[:]) # MIN границы значений коэффециентов Ax^3 + Bx^2 + Cx + D: min_val[0] = A, min_val[1] = B ...
        self.max_val = numpy.array(max_val[:]) # MAX границы значений коэффециентов
        self.Global_best = None # Минимальное отклонениние всего роя
        self.Global_pos = None # Лучшие коэффциенты всего роя, где Global_pos = [A, B, C, D]
        self.a_g = a_g # Весовой коэффициент при локальном отклонении
        self.a_l = a_l # Весовой коэффициент при глобальном отклонении
        self.swarm = self.createSwarm()

    def createSwarm (self):
        return [Particle(self) for i in range (self.swarmsize) ]

    def doIteration(self, num):
        for i in range(num):
            for particle in self.swarm:
                particle.nextIteration_canon(self)


class Particle(Swarm):
    def __init__ (self, swarm):
        #Текущее положение частицы
        self.currentPosition = [random.uniform(swarm.min_val[0], swarm.max_val[0]), random.uniform(swarm.min_val[1], swarm.max_val[1]), random.uniform(swarm.min_val[2], swarm.max_val[2]), random.uniform(swarm.min_val[3], swarm.max_val[3])]

        #Начальные скорости velocity = [v_A, v_B, v_C, v_D]
        self.velocity = [random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)]

        #Лучшие состояние частицы
        self.localBestPosition = self.currentPosition
        self.localBestDeviation = None

    def deviation(self, swarm): #Целевая функция отклонения полинома от набора точек
        res = 0;
        for i in swarm.dots:
            F = self.currentPosition[0] * (i[0] ** 3) + self.currentPosition[1] * i[0] ** 2 + self.currentPosition[2] * i[0] + self.currentPosition[3]
            res += math.fabs(i[1] - F)
        return res

    def CheckFunc(self, swarm): #Проверка целевой функции
        func = self.deviation(swarm)
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


if __name__ == "__main__":
    iterCount = 10
    swarmsize = 200
    dots_num = 10
    min_val = [-10,-10,-10,-10]
    max_val = [10, 10, 10, 10]
    a_g = 0.7
    a_l = 0.5
    swarm = Swarm(swarmsize, dots_num, min_val, max_val, a_g, a_l)
    swarm.doIteration(iterCount)
    print(swarm.Global_best)
    print(swarm.Global_pos)
