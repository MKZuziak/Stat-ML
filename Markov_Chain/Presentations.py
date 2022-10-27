from itertools import chain
import numpy as np
import Markov_Chain

def stationery_distribution_convergence(Q, nsim):
    chain = Markov_Chain.Markov_Chain(Q)
    for n in range(nsim):
        n = 10**(n+1)
        stat_dist = chain.simulate(n)
        print("After {} runs the stationary distrubution has converged to: {}.".format(n, stat_dist))

matrix= np.array([[1/2, 1/2, 0],
                [1/3, 1/3, 1/3],
                [1/2, 0, 1/2]])

stationery_distribution_convergence(Q=matrix, nsim=5)