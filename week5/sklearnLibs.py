from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

digit = load_digits()

X, y = digit.data, digit.target
# print('input data shape{}, target data shape {}'.format(X.shape, y.shape))
# print(type(digit))
# print(type(X))
# print(type(y))
# print(X)
k = 100
im = X[k].reshape(8, 8)
plt.imshow(im)
plt.axis('off')
unique, count = np.unique(y, return_counts=True)
new = pd.DataFrame(y)
print(new.values())
