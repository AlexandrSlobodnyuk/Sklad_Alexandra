import math                                                     #импортирую библиотеку math
import numpy                                                    #импортирую библиотеку numpy
import matplotlib.pyplot as mpp                                 #импортирую библиотеку atplotlib.pyplot как mpp 

if __name__=='__main__':                                        #если переменная name равна значению main
    arguments = numpy.r_[0:200:0.1]                             #создается массив с числами от 0.1 до 200 с шагом 0.1
    mpp.plot(                                                   #строится график 
        arguments,
        [math.sin(a) * math.sin(a/20.0) for a in arguments]     #условия построения графика
    )
    mpp.show()                                                  #изображение графика
