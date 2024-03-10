import matplotlib.pyplot as plt
import random
import numpy as np

class GradientDescent:
    def __init__(self,points):
        self.eta = 0.1
        for i in range(0,3):
            plt.scatter(points[i][0],points[i][1])
        self.do(points)

    def a_val(self,xi,yi,ak,bk):
        return ak-2*self.eta*(ak+bk*xi-yi)
    
    def b_val(self,xi,yi,ak,bk):
        return bk-2*self.eta*xi*(bk*xi+ak-yi)

    def plot(self,slope,intercept):
        x = np.linspace(-5, 5, 100)
        y = slope * x + intercept
        plt.plot(x, y, label=f'Line: y = {slope}x + {intercept}')

    def do(self,points):
        ak=0
        bk=0
        for i in range(1,10000):
            ch = random.randint(1,3)
            xi = points[ch-1][0]
            yi = points[ch-1][1]

            ak_1 = self.a_val(xi,yi,ak,bk)
            bk_1 = self.b_val(xi,yi,ak,bk)

            if i%50 == 0:
                self.plot(bk,ak)

            ak = ak_1
            bk = bk_1
            
        # self.plot(bk,ak)
        plt.grid(True)
        plt.axhline(0, color='black',linewidth=0.5)
        plt.axvline(0, color='black',linewidth=0.5)
        plt.xlabel('X')
        plt.ylabel('Y')
        # plt.legend()
        plt.show()
        return
        
obj =  GradientDescent([[2,2.5],[4,7.5],[3,1.5]])
obj1 =  GradientDescent([[1, 1], [1.5, 2], [3, 1.5]])
# Verify if it converges
obj1 =  GradientDescent([[1, 1], [2, 2], [3, 3]])


