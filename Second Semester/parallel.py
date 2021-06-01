import random
import time
import multiprocessing

def pi_finding(accuracy):
    g = random.Random()
    def make_cords():
        if g.random()**2+g.random()**2 <=1:
            return True
        return False
    good_dots=0
    for i in range(accuracy):
        if make_cords():
            good_dots += 1
    return (good_dots*4/accuracy)
#print(Pi_finding(1000000))
def test_all(pool):
    l = pool.map(pi_finding, [1000000])
    return l


if __name__ == '__main__':
    pool = multiprocessing.Pool()
    t0 = time.time()
    print(test_all(pool))
    print("Time spent:", time.time() - t0)
else:
    print(__name__)
