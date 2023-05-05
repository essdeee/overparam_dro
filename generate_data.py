'''
Utility file for generating datasets based on the linear model for 
Overparametrized DRO project.
'''
import numpy as np
import itertools

def gen_full_alignment(n, b, d, seed=42):
    # generate x_b
    bin_features = np.random.randint(2, size=(n, b))
    return X, y, true_beta

def gen_misaligned(b, d, seed=42):
    pass

def gen_nostruct(b, d, seed=42):
    pass

