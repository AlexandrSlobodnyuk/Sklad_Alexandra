import matplotlib.pyplot as plt
import numpy
import random

i = 0
sp = [[],[]]
while i <= 40000:

    sign = random.Random().randrange(1, 5)
    if sign == 1:
        sp[0].append(random.Random().random())
        sp[1].append(random.Random().random())
    if sign == 2:
        sp[0].append(-random.Random().random())
        sp[1].append(random.Random().random())
    if sign == 3:
        sp[0].append(-random.Random().random())
        sp[1].append(-random.Random().random())
    if sign == 4:
        sp[0].append(random.Random().random())
        sp[1].append(-random.Random().random())
    i += 1

ps = [[],[]]
for i in range(40000):
    if abs(sp[0][i]) + abs(sp[1][i]) <= 1:
        ps[0].append(sp[0][i])
        ps[1].append(sp[1][i])


plt.plot(ps[0], ps[1])
plt.show()
#print(sp[1])
