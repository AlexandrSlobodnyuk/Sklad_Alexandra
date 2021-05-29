import math
#import numpy as np
def exp(x):
    def factorial(n):
        r = 1
        while n >= 1:
            r = r * n
            n = n-1
        return r
    def e_v_stepeni_x(x):
        a = 0
        for s in range(0, 30):
            a = a + (x**s)/(factorial(s))
        return a
    return(e_v_stepeni_x(x))
