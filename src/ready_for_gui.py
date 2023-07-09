import random
import numpy
import math

class Swarm (object):
    def __init__ (self, SwarmSize, dots_num, min_val, max_val, a_g, a_l):
        self.dots = [[random.uniform(-10, 10), random.uniform(-10, 10)] for i in range(dots_num) ]
        self.swarmsize = SwarmSize
        self.min_val = numpy.array(min_val[:])
        self.max_val = numpy.array(max_val[:])
        self.Global_best = None
        self.Global_pos = None
        self.a_g = a_g
        self.a_l = a_l
        self.swarm = self.createSwarm()

    def createSwarm (self):
        return [Particle(self) for i in range (self.swarmsize) ]

    def doIteration(self, num):
        for i in range(num):
            for particle in self.swarm:
                particle.nextIteration(self)


class Particle(Swarm):
    def __init__ (self, swarm):
        # Текущее положение частицы
        self.currentPosition = [random.uniform(swarm.min_val[0], swarm.max_val[0]), random.uniform(swarm.min_val[1], swarm.max_val[1]), random.uniform(swarm.min_val[2], swarm.max_val[2]), random.uniform(swarm.min_val[3], swarm.max_val[3])]
        self.velocity = [random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)]
        self.localBestPosition = self.currentPosition
        self.localBestDeviation = None
    def deviation(self, swarm):
        res = 0;
        for i in swarm.dots:
            F = self.currentPosition[0] * (i[0] ** 3) + self.currentPosition[1] * i[0] ** 2 + self.currentPosition[2] * i[0] + self.currentPosition[3]
            res += math.fabs(i[1] - F)
        return res

    def CheckFunc(self, swarm):
        func = self.deviation(swarm)
        if (swarm.Global_best == None or func < swarm.Global_best):
            swarm.Global_best = func
            swarm.Global_pos = self.currentPosition[:]
    def nextIteration(self, swarm):
        self.CheckFunc(swarm)
        self.velocity[0] += 0.5 * random.random() * (self.localBestPosition[0] - self.currentPosition[0]) + 0.7 * random.random() * (swarm.Global_pos[0] - self.currentPosition[0])
        self.velocity[1] += 0.5 * random.random() * (self.localBestPosition[1] - self.currentPosition[1]) + 0.7 * random.random() * (swarm.Global_pos[1] - self.currentPosition[1])
        self.velocity[2] += 0.5 * random.random() * (self.localBestPosition[2] - self.currentPosition[2]) + 0.7 * random.random() * (swarm.Global_pos[2] - self.currentPosition[2])
        self.velocity[3] += 0.5 * random.random() * (self.localBestPosition[3] - self.currentPosition[3]) + 0.7 * random.random() * (swarm.Global_pos[3] - self.currentPosition[3])

        # Обновить позицию частицы
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
    a_g = 0,7
    a_l = 0,5
    swarm = Swarm(swarmsize, dots_num, min_val, max_val, a_g, a_l)
    swarm.doIteration(iterCount)
    print(swarm.Global_best)
    print(swarm.Global_pos)
