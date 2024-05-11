# -*- coding: utf-8 -*-
"""
Created on Sat May  4 16:08:57 2024

@author: aañinon, japolinar, dcordero, mcreis, and mviray
"""

import scipy.stats as sts
import numpy as np
import matplotlib.pyplot as plt

mu = np.linspace(1.65, 1.8, num = 50)
test = np.linspace(0, 2)
uniform_dist = sts.uniform.pdf(mu) + 1

def likelihood_func(datum, mu) :
   likelihood_out = sts.norm.pdf(datum, mu, scale = 0.1)
   return likelihood_out/likelihood_out.sum()

likelihood_out = likelihood_func(1.7, mu)

plt.plot(mu, likelihood_out)
plt.title("Likelihood of $\mu$ given observation 1.7m")
plt.ylabel("Probability Density/Likelihood")
plt.xlabel("Value of $\mu$")
plt.show()
