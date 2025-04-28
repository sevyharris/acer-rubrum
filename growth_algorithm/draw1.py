# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

# +
# def class Acer():

# +
my_tree = []

N = 4
unit = 1.0
for i in range(N):
    branch = {
        'X0': 0.0,
        'Y0': unit * i,
        'X1': 0.0,
        'Y1': unit * (i + 1)
    }
    
    my_tree.append(branch)
    

# -

my_tree

# +
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

for branch in my_tree:
    plt.plot([branch['X0'], branch['X1']], [branch['Y0'], branch['Y1']], linestyle='-', linewidth=2)
# -


