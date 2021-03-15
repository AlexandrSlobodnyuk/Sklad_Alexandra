import random
import time
import sys
import multiprocessing
def Pi_finding():
    def make_cords():
        g = random.Random()
        return [g.random(), g.random()]
    good_dots=0
    accuracy=100000
    t0 = time.time()
    dots = []
    for i in range(accuracy):
        dots.append(make_cords())
        if dots[-1][0]**2+dots[-1][1]**2<=1:
            good_dots+=1
    print("Time spent:", time.time() - t0)
    print(4*good_dots/accuracy)
Pi_finding()
def test_all(pool):
    l = pool.map(Pi_finding(), [10000000] * 50)
    return l


if __name__ == '__main__':
    pool = multiprocessing.Pool()
    t0 = time.time()
    print(test_all(pool))
    print("Time spent:", time.time() - t0)
else:
    print(__name__)



