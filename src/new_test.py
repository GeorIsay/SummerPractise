import random
import numpy as np
import matplotlib.pyplot as plt
import math

class Swarm():
    def __init__(self):
        self.a = random.uniform(-100, 100)
        self.b = random.uniform(-100, 100)
        self.c = random.uniform(-100, 100)
        self.d = random.uniform(-100, 100)

        self.v_a = random.uniform(-10,10)
        self.v_b = random.uniform(-10,10)
        self.v_c = random.uniform(-10,10)
        self.v_d = random.uniform(-10,10)

        self.p_abs = 0
        self.p_abs_best = 0
        self.a_best = 0
        self.b_best = 0
        self.c_best = 0
        self.d_best = 0

    def pol(self, x):
        return self.a * x**3 + self.b * x**2 + self.c * x + self.d

    def deviation_func(self, dots):
        L = len(dots)
        res = 0
        for i in range(L):
            res += abs(dots[i][1] - self.pol(dots[i][0]))
        if res < self.p_abs or self.p_abs == 0:
            self.p_abs = res
            self.a_best = self.a
            self.b_best = self.b
            self.c_best = self.c
            self.d_best = self.d

    def speed_correction(self, a, b):
        global KOEF_BEST
        self.v_a += random.random() * a *(self.a_best - self.a) + random.random() * b * (KOEF_BEST[0] - self.a)
        self.v_b += random.random() * a *(self.b_best - self.b) + random.random() * b * (KOEF_BEST[1] - self.b)
        self.v_c += random.random() * a *(self.c_best - self.c) + random.random() * b * (KOEF_BEST[2] - self.c)
        self.v_d += random.random() * a *(self.d_best - self.d) + random.random() * b * (KOEF_BEST[3] - self.d)

    def speed_kanon(self):
        k = random.random()
        a = 1.6
        b = 2.7
        p = a+b
        tmp = 2 - p - (p*p - 4*p)**0.5
        x = (2*k) / math.fabs(tmp)
        global KOEF_BEST
        self.v_a = x*(self.v_a + random.random() * a * (self.a_best - self.a) + random.random() * b * (KOEF_BEST[0] - self.a))
        self.v_b = x*(self.v_b + random.random() * a * (self.b_best - self.b) + random.random() * b * (KOEF_BEST[1] - self.b))
        self.v_c = x*(self.v_c + random.random() * a * (self.c_best - self.c) + random.random() * b * (KOEF_BEST[2] - self.c))
        self.v_d = x*(self.v_d + random.random() * a * (self.d_best - self.d) + random.random() * b * (KOEF_BEST[3] - self.d))


    def move(self):
        self.a += self.v_a
        if self.a > 10 or self.a < -10: self.a = KOEF_BEST[0]
        self.b += self.v_b
        if self.b > 10 or self.b < -10: self.b = KOEF_BEST[0]
        self.c += self.v_c
        if self.c > 10 or self.c < -10: self.c = KOEF_BEST[0]
        self.d += self.v_d
        if self.d > 10 or self.d < -10: self.d = KOEF_BEST[0]

P_BEST = 10000000000
KOEF_BEST = []
def algorithm(swarms, dots):
    global P_BEST
    global KOEF_BEST
    for i in swarms:
        i.deviation_func(dots)
        if i.p_abs < P_BEST:
            P_BEST = i.p_abs
            KOEF_BEST = [i.a, i.b, i.c, i.d]
        i.speed_correction(1.5, 2.8)
        i.move()

def algorithm_kanon(swarms, dots):
    global P_BEST
    global KOEF_BEST
    for i in swarms:
        i.deviation_func(dots)
        if i.p_abs < P_BEST:
            P_BEST = i.p_abs
            KOEF_BEST = [i.a, i.b, i.c, i.d]
        i.speed_kanon()
        i.move()

###########

swarms = []
dots = []

X_coords = []
Y_coords = []


COUNT_DOTS = int(input("Введите кол-во аппроксимируемых точек: "))
COUNT_SWARMS = int(input("Введите кол-во частиц в рое: "))
COUNT_ITER = int(input("Введите кол-во итераций алгоритма: "))



for i in range(COUNT_DOTS):
    tmp = [random.uniform(-100,100), random.uniform(-100,100)]
    dots.append(tmp)
    X_coords.append(tmp[0])
    Y_coords.append(tmp[1])



for i in range(COUNT_SWARMS):
    tmp = Swarm()
    swarms.append(tmp)

for i in range(COUNT_ITER):
    algorithm_kanon(swarms, dots)
y = lambda x: KOEF_BEST[0]*x**3 + KOEF_BEST[1]*x**2 + KOEF_BEST[2]*x + KOEF_BEST[3]
fig = plt.subplots()
x = np.linspace(-100, 100, 10000)


a_coef = str(round(KOEF_BEST[0], 1)) + 'x^3 '
if KOEF_BEST[1] > 0: b_coef = ' +' + str(round(KOEF_BEST[1], 1)) + 'x^2 '
else: b_coef = str(round(KOEF_BEST[1],1)) + 'x^2 '

if KOEF_BEST[2] > 0: c_coef = ' +' + str(round(KOEF_BEST[2], 1)) + 'x '
else: c_coef =  str(round(KOEF_BEST[2],1)) + 'x '

if KOEF_BEST[3] > 0: d_coef = ' +' + str(round(KOEF_BEST[3], 1))
else: d_coef = str(round(KOEF_BEST[3],1))

print(KOEF_BEST)
print(P_BEST)
name_res = a_coef + b_coef + c_coef + d_coef
plt.plot(x, y(x), label = name_res)
plt.scatter(X_coords, Y_coords, c ="red")
plt.legend(fontsize=10)
plt.grid(True)
plt.show()


