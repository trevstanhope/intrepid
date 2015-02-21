"""
intrepid - simple PID solutions
"""

import time
import thread
from itertools import cycle
import numpy as np
from matplotlib import pyplot as plt

"""
PID Class for discrete systems
"""
class PID:
    
    def __init__(self, pool, P=0, I=0, D=0, Kp=1.0, Ki=1.0, Kd=1.0, ref=0.0, sig=0.0, gain=1.0):
        self.p = P
        self.i = I
        self.d = D
        self.k_p = Kp
        self.k_i = Ki
        self.k_d = Kd
        self.ref = ref
        self.sig = sig
        self.output = 0
        self.pool = pool
        self.gain = gain
        
    # Calculate control output
    def calculate(self):
        self.pool.append(self.sig)
        self.p = self.sig - self.ref
        self.i = np.mean(self.pool)
        self.d = self.sig - self.pool[-1] # difference from last
        self.pool[-1] = self.p # add newest value to pool, forget oldest
        self.output = self.gain * (self.k_p * self.p + self.k_i * self.i + self.k_d * self.d) # calculate sum
        self.pool.reverse()
        self.pool.pop()
        self.pool.reverse()
        return self.output
    
    # Set Signal
    def signal(self, sig):
        self.sig = sig
        
    # Set/Get Tuning Parameters
    def tuning(self, gain, Kp=None, Ki=None, Kd=None):
        if Kp:
            self.k_p = Kp
        if Ki:
            self.k_i = Ki
        if Kd:
            self.k_d = Kd
        return (self.k_p, self.k_i, self.k_d)

    # Set/Get Reference
    def reference(self, ref=None):
        if ref:
            self.ref = ref
        return self.ref

    # Plot
    def plot(self):
        plt.plot(self.pool)
        plt.show()

if __name__ == '__main__':
    pool = [10] * 10
    pid = PID(pool)
    for a in [1] * 10:
        pid.calculate()
        pid.signal(a)
        pid.plot()
