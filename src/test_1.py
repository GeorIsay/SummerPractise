import random
import numpy as np
import matplotlib.pyplot as plt
def pol(a, b, c, d, x):
    return a*x**3 + b*x**2 + c*x + d

A = [random.uniform(-10,10), random.uniform(-10,10)]
B = [random.uniform(-10,10), random.uniform(-10,10)]
C = [random.uniform(-10,10), random.uniform(-10,10)]
D = [random.uniform(-10,10), random.uniform(-10,10)]
X_coords = [-4, 2, 4, 5]
Y_coords = [5, -7, 1, 0]

p_1 = [random.uniform(0,100), random.uniform(0,100), random.uniform(0,100), random.uniform(0,100)]
v_1 = [random.uniform(-1,1), random.uniform(-1,1), random.uniform(-1,1), random.uniform(-1,1)]
p_2 = [random.uniform(0,100), random.uniform(0,100), random.uniform(0,100), random.uniform(0,100)]
v_2 = [random.uniform(-1,1), random.uniform(-1,1), random.uniform(-1,1), random.uniform(-1,1)]


p_1_abs = 0
p_2_abs = 0
p_abs = 0
p_1_best = p_1[:]
p_2_best = p_2[:]
p_best = []
flag = True
for i in range (100):
    func_1 = abs(A[1] - pol(p_1[0], p_1[1], p_1[2], p_1[3], A[0])) + abs(B[1] - pol(p_1[0], p_1[1], p_1[2], p_1[3], B[0])) + abs(C[1] - pol(p_1[0], p_1[1], p_1[2], p_1[3], C[0])) + abs(D[1] - pol(p_1[0], p_1[1], p_1[2], p_1[3], D[0]))
    func_2 = abs(A[1] - pol(p_2[0], p_2[1], p_2[2], p_2[3], A[0])) + abs(B[1] - pol(p_2[0], p_2[1], p_2[2], p_2[3], B[0])) + abs(C[1] - pol(p_2[0], p_2[1], p_2[2], p_2[3], C[0])) + abs(D[1] - pol(p_2[0], p_2[1], p_2[2], p_2[3], D[0]))
    if func_1 < p_1_abs or p_1_abs == 0:
        p_1_abs = func_1
        p_1_best = p_1[:]
    if func_2 < p_2_abs or p_2_abs == 0:
        p_2_abs = func_2
        p_2_best = p_2[:]

    if func_1 < func_2:
        func = func_1
        flag = True
    else:
        func = func_2
        flag = False

    if func < p_abs or p_abs == 0:
        p_abs = func
        if flag == True: p_best = p_1[:]
        else: p_best = p_2[:]

    r_1 = random.random()
    r_2 = random.random()
    v_1[0] = v_1[0] + r_1 * 0.5 * (p_1_best[0] - p_1[0]) + r_2 * 0.7 * (p_best[0] - p_1[0])
    v_1[1] = v_1[1] + r_1 * 0.5 * (p_1_best[1] - p_1[1]) + r_2 * 0.7 * (p_best[1] - p_1[1])
    v_1[2] = v_1[2] + r_1 * 0.5 * (p_1_best[2] - p_1[2]) + r_2 * 0.7 * (p_best[2] - p_1[2])
    v_1[3] = v_1[3] + r_1 * 0.5 * (p_1_best[3] - p_1[3]) + r_2 * 0.7 * (p_best[3] - p_1[3])

    v_2[0] = v_2[0] + r_1 * 0.5 * (p_2_best[0] - p_2[0]) + r_2 * 0.7 * (p_best[0] - p_2[0])
    v_2[1] = v_2[1] + r_1 * 0.5 * (p_2_best[1] - p_2[1]) + r_2 * 0.7 * (p_best[1] - p_2[1])
    v_2[2] = v_2[2] + r_1 * 0.5 * (p_2_best[2] - p_2[2]) + r_2 * 0.7 * (p_best[2] - p_2[2])
    v_2[3] = v_2[3] + r_1 * 0.5 * (p_2_best[3] - p_2[3]) + r_2 * 0.7 * (p_best[3] - p_2[3])

    p_1[0] = p_1[0] + v_1[0]
    p_1[1] = p_1[1] + v_1[1]
    p_1[2] = p_1[2] + v_1[2]
    p_1[3] = p_1[3] + v_1[3]

    p_2[0] = p_2[0] + v_2[0]
    p_2[1] = p_2[1] + v_2[1]
    p_2[2] = p_2[2] + v_2[2]
    p_2[3] = p_2[3] + v_2[3]

print(p_best)

y = lambda x: p_best[0]*x**3 + p_best[1]*x**2 + p_best[2]*x + p_best[3]
fig = plt.subplots()
x = np.linspace(-10, 10,1000)

a_coef = str(round(p_best[0], 1)) + 'x^3 '
if p_best[1] > 0: b_coef = ' +' + str(round(p_best[1], 1)) + 'x^2 '
else: b_coef = str(round(p_best[1],1)) + 'x^2 '

if p_best[2] > 0: c_coef = ' +' + str(round(p_best[2], 1)) + 'x '
else: c_coef =  str(round(p_best[2],1)) + 'x '

if p_best[3] > 0: d_coef = ' +' + str(round(p_best[3], 1))
else: d_coef = str(round(p_best[3],1))

name_res = a_coef + b_coef + c_coef + d_coef
plt.plot(x, y(x), label = name_res)
plt.scatter(X_coords, Y_coords, c ="red")
plt.legend(fontsize=10)
plt.show()