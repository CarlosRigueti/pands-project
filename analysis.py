# Data frames.[3]
import pandas as pd

# Data visualization library.[3]
import seaborn as sns

# Plotting.[5]
import matplotlib.pyplot as plt

# Numerical arrays ad random numbers.[6]
import numpy as np
# -----------------------------------------------------------
# Load the dataset into a DataFrame [8]
df = pd.read_csv("iris.csv")
print (df)
# -----------------------------------------------------------

#          sepal_length  sepal_width  petal_length  petal_width  species
#0             5.1          3.5           1.4          0.2       setosa
#1             4.9          3.0           1.4          0.2       setosa
#2             4.7          3.2           1.3          0.2       setosa
#3             4.6          3.1           1.5          0.2       setosa
#4             5.0          3.6           1.4          0.2       setosa
#..            ...          ...           ...          ...         ...
#145           6.7          3.0           5.2          2.3       virginica
#146           6.3          2.5           5.0          1.9       virginica
#147           6.5          3.0           5.2          2.0       virginica
#148           6.2          3.4           5.4          2.3       virginica
#149           5.9          3.0           5.1          1.8       virginica

# -----------------------------------------------------------