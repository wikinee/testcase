#!/usr/bin/python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
x = np.arange(20, 80, 1)
y1 = np.ceil(48 / x) * x + 10
plt.figure(1)
plt.subplot(211)
plt.plot(x, y1)
plt.show()