from sklearn.datasets import make_regression
import pandas as pd
import os
import numpy as np

if os.path.isfile('large_data.csv'):
    n=1
else:
    n=50

for i in range(0, n):
    X, y= make_regression(100000, n_features=10)
    df= pd.DataFrame(X)
    df.to_csv('large_data.csv', mode='a')