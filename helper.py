import numpy as np
import pandas as pd
import os

def _embed(x, order=3, delay=1):
    N = len(x)
    if order * delay > N:
        raise ValueError("Error: order * delay should be lower than x.size")
    if delay < 1:
        raise ValueError("Delay has to be at least 1.")
    if order < 2:
        raise ValueError("Order has to be at least 2.")
    Y = np.zeros((order, N - (order - 1) * delay))
    for i in range(order):
        Y[i] = x[i * delay:i * delay + Y.shape[1]]
    return Y.T

def get_paths(path):
  paths = []
  for file in os.listdir(path):
      fl = path + file
      paths.append(fl)
  return sorted(paths)

def get_data(paths):
  all_data = []
  for file in paths:
      with open(file) as f:
          data_oi = [int(val) for val in f.read().splitlines()]
          all_data.append(data_oi)
  return np.array(all_data)
