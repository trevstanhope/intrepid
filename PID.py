import time
import thread
from itertools import cycle
import numpy as np

"""
PID Class for continuous systems
"""
class sPID:
    
    def __init__(self, N=5, P=0, I=0, D=0, KP=1, KI=1, KD=1, REF=0, SIG=0):
        self.p = P
        self.i = I
        self.d = D
        self.k_p = KP
        self.k_i = KI
        self.k_d = KD
        self.ref = REF
        self.sig = SIG
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
        self.output = self.k_p * self.p + self.k_i * self.i + self.k_d * self.d # calculate sum
        self.pool.reverse()
        self.pool.pop()
        self.pool.reverse()
        return self.output
        
    def tuning(self):
        return (self.k_p, self.k_i, self.k_d)
        
    def setpoint(self):
        return self.ref

"""
PID Class for discrete systems
"""
class zPID:
    def __init__(self):
        pass
