from itertools import chain
import numpy as np


class Markov_Chain:
    def __init__(self, transition_matrix, labels=None) -> None:
        self.transition_matrix = transition_matrix
        assert self.transition_matrix.ndim == 2 # Making test for a correct transition matrix Q.
        #TODO: Assert that transition_matrix is a proper MxM transition matrix.
       
        if False in (self.transition_matrix.sum(axis=1) == 1): # Checking whether each row is summing up to 1.
            print("Warning! One or more rows in the transition matrix were not summing up to 1.")
            print("Warning! Matrix was readjusted.")
            self.transition_matrix = normalise(self.transition_matrix)
        
        if labels != None:
            assert len(labels) == len(self.transition_matrix)
            self.labels = labels
            self.labels_description = {label:i for (i, label) in enumerate(labels)}
            print(self.labels_description)

    
    def show_Q(self):
        print(self.transition_matrix)
    
def normalise(matrix):
    norm_c = 1.00 / matrix.sum(axis=1)
    for i in range(len(matrix)):
        matrix[i] = matrix[i] * norm_c[i]
    return matrix

m = np.random.rand(6).reshape(2, 3)
labels = ["Rainy", "Sunny"]
chain = Markov_Chain(m, labels)
chain.show_Q()
chain.labels_description