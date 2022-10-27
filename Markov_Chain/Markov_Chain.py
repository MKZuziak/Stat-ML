from itertools import chain
import numpy as np


class Markov_Chain:
    def __init__(self, transition_matrix, labels=None) -> None:
        self.transition_matrix = transition_matrix
        assert self.transition_matrix.ndim == 2 # Making test for a correct transition matrix Q.
        #TODO: Assert that transition_matrix is a proper MxM transition matrix.
       
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

    def simulate(self, nsim=10**4):
        states = len(self.transition_matrix) - 1
        X = np.zeros(nsim, dtype=int)
        X[0] = np.random.randint(low = 0, high = states, size = 1, dtype = int)
        for i in range(1, nsim):
            X[i] = np.random.choice(a=(states+1), size=1, p=self.transition_matrix[X[(i-1)], :])
        _, frequency = np.unique(X, return_counts=True)
        stat_dist = frequency / len(X)
        return stat_dist


matrix= np.array([[1/3, 1/3, 1/3],
                [1/3, 1/3, 1/3],
                [1/3, 1/3, 1/3]])
labels = ["Rainy", "Sunny", "I don't know"]
chain = Markov_Chain(matrix, labels)
chain.show_Q()