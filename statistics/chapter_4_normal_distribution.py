# -*- coding: utf-8 -*-
'''
    File name: 
    Author: Mohan Prasath Chinnasamy
    Date created: 20/August/2019
    Date last modified: 20/August/2019
    Python Version: 3.7.3
    Numpy Version: 1.6.13
    Scipy Version: 1.2.1
    Editor: Spyder
    Editor Version: 3.3.4
'''

import numpy as np
import scipy as sp
import scipy.stats as stats
import matplotlib.pyplot as plt
from scipy.stats import norm
import math

from random import seed
from random import random

class NormalDist:
    '''
        This class is written as a practice for understanding Normal 
        Distribution and to train myself with python, numpy and scipy 
        libraries.
        
        I'll learning some Python best practices as well. Trying to make a
        habit out of learning and programmign at the same time.
    '''
    def __init__(self, size, mu, sigma):
        self.data = []
        self.normal_data = None
        self.mu = mu
        self.sigma = sigma
        self.size = size
        self.np_data = None
        # adding 10000 random numbers with a seed value of 100
        seed(100)
        for _ in range(10000):
            self.data.append(random())
        self.np_data = np.array(self.data)
        self.normal_data = np.random.normal(self.mu, self.sigma, self.size)
    
    def print_data(self, some_data):
        print(some_data)
    
    def scatter_plot(self, length, some_data):
        plt.scatter(range(length), some_data[:length])
        
    def is_there_a_bell_cruve():
        pass
        
normal_dist = NormalDist(10000, 0, 1)
print(normal_dist.print_data(normal_dist.data))
# normal_dist.scatter_plot(1000, normal_dist.np_data)
normal_dist.scatter_plot(1000, normal_dist.normal_data)
# plt.plot(normal_dist.normal_data, stats.norm.pdf(normal_dist.normal_data, 0, 1))
plt.scatter(normal_dist.normal_data, norm.pdf(normal_dist.normal_data,0,1))
plt.scatter(normal_dist.data, norm.pdf(normal_dist.data,0,1))
plt.show()

# So fractiless are just another name for percentiles or quartiles. 

# Skewness can be upto 0 to 4 * sqrt*(6/n) - how skewed the data is?
# Kurtosis can be upto 0 to 4 * sqrt*(6/n) - how the tail of a ND appears?

# normal plot - we know how to plot it norm.pdf from scipy

# random no.s - we can generate them using libraries. But they aren't the same
# as np.random.normal, so remember mu sigma that you need for generating nums.

# population is the collection of all the data, while sample is a selection.
# This requires careful consideration, because the sampling affects the mean
# and standard deviation.
 