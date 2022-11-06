from itertools import chain
import numpy as np


class Markov_Chain:
    def __init__(self, transition_matrix, labels=None) -> None:
        self.transition_matrix = transition_matrix
        # I) 1st assertion - passed parameter is a 2-dimensional array (a Matrix)
        assert self.transition_matrix.ndim == 2 # Making test for a correct transition matrix Q.

        # II) 2nd assertion - passed matrix is a square matrix:
        assert self.transition_matrix.shape[0] == self.transition_matrix.shape[1]
       
        if False in np.isclose([self.transition_matrix.sum(axis=1)], [1.0], rtol=1e-05, atol=1e-08): # Checking whether each row is summing up to 1.
            print("Warning! One or more rows in the transition matrix were not summing up to 1.")
            print("Warning! Matrix was readjusted.")
            self.transition_matrix = self.transition_matrix / self.transition_matrix.sum(axis=1)[:, None]
        
        if labels != None:
            assert len(labels) == len(self.transition_matrix)
            self.labels = labels
            self.labels_description = {label:i for (i, label) in enumerate(labels)}
            print(self.labels_description)

    def show_Q(self):
        print(self.transition_matrix)

    def simulate(self, nsim=10**4, starting_distribution=None):
        states = len(self.transition_matrix) - 1
        X = np.zeros(nsim, dtype=int)
        if starting_distribution is None:
            X[0] = np.random.randint(low = 0, high = states, size = 1, dtype = int)
        else:
            X[0] = np.random.choice(a=(states+1), size=1, p=starting_distribution)
        for i in range(1, nsim):
            X[i] = np.random.choice(a=(states+1), size=1, p=self.transition_matrix[X[(i-1)], :])
        _, frequency = np.unique(X, return_counts=True)
        stat_dist = frequency / len(X)
        return stat_dist

    def simulate_2(self, nsim=50):
        Q = self.transition_matrix
        for i in range(nsim):
            Q_n = Q.dot(Q)
            Q = Q_n
        return Q

matrix= np.array([[2/5, 3/5], [3/7, 4/7]])
chain = Markov_Chain(matrix)
stat_dist = chain.simulate()
stat_dist2 = chain.simulate_2()

print(stat_dist, stat_dist2)