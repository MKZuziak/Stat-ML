from itertools import chain
import numpy as np
import Markov_Chain

def stationery_distribution_convergence(Q, nsim):
    chain = Markov_Chain.Markov_Chain(Q)
    for n in range(nsim):
        n = 10**(n+1)
        stat_dist = chain.simulate(n)
        print("After {} runs the stationary distrubution has converged to: {}.".format(n, stat_dist))

def once_s_always_s(Q):
    chain = Markov_Chain.Markov_Chain(Q)
    stat_dist = chain.simulate(10**5)
    print("The stationary distribution of the chain after 10^5 runs is close: {}".format(stat_dist))
    print("We can multiply {} and {} to receive {}".format(stat_dist, Q, stat_dist.dot(Q)))

matrix= np.array([[1/3, 2/3], [1/2, 1/2]])

#stationery_distribution_convergence(Q=matrix, nsim=5)
#once_s_always_s(Q=matrix)