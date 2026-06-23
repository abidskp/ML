import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model
df = pd.read_excel("df = pd.read_excel('/content/house_priece.xlsx")
df.head(5)
Area	bedrooms	houseage	distance	Price
800	    2	        10	      2	        50
850	    2	         8	      3        	55
900	    2	         12	      1	        60
950	    3	          5	      4	        65
1000	  3	          7	      3	        70

plt.xlabel("Area", color = "red")
plt.ylabel("Price", color = "red")
plt.scatter(df.Area, df.Price)
lr = linear_model.linear_regression()
lr.fit(df[[Area]], df.Price)
lr.predict([[1600]])

============predicted value is below=============
/usr/local/lib/python3.12/dist-packages/sklearn/utils/validation.py:2739: UserWarning: X does not have valid feature names, but LinearRegression was fitted with feature names
  warnings.warn(
array([131.66666667])
    
=============== now to check accurary of the model, calculate coef and intercept(y =wx + b)  ==========================
lr.coef_
array([0.1])

lr.intercept_
np.float64(-28.3333333333333)

====== by applying formula of y =wx + b=========
y = 0.1 * 1600 -28.3333333333333
  = 131.66666666666669 (this valu is same as predicted valueof model)

========= to check the score/accuracy of the model==========
lr.score(df[['Area']], df.Price)
0.9925143697366662


