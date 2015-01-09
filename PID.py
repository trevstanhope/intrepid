import time
import thread
from itertools import cycle
import numpy as np

class PID:
    
    def __init__(self, N=5):
        self.p = 0
        self.i = 0
        self.d = 0
        self.k_p = 0
        self.k_i = 0
        self.k_d = 0
        self.ref = 0
        self.sig = 0
        self.output = 0
        self.pool = [0] * N
        self.mag = 0
        
    def calculate(self, value):
        self.sig = value
        self.pool.append(self.sig)
        self.p = self.sig - self.ref
        self.i = np.mean(self.pool)
        self.d = self.sig - self.pool[-1] # difference from last
        self.pool[-1] = self.p # add newest value to pool, forget oldest
        self.output = self.k_p * self.p + self.k_i * self.i + self.k_d * self.d
        self.pool.reverse()
        self.pool.pop()
        self.pool.reverse()
        return self.output
        
    def tuning(self):
        return (self.k_p, self.k_i, self.k_d)
        
    def setpoint(self):
        return self.ref
