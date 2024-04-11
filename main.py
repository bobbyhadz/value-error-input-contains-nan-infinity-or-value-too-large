# Input contains infinity or value too large for dtype(float64)

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Contains inf and nan
data = {'A': [1, np.inf, 3],
        'B': [4, np.nan, 6],
        'C': [7, 8, 9]}
df = pd.DataFrame(data)

#      A    B  C
# 0  1.0  4.0  7
# 1  inf  NaN  8
# 2  3.0  6.0  9
print(df)