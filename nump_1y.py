import numpy as np 

b = np.array([1,2,3])


c = np.array([[1,2,4,3,5,6,7,8],[1,2,4,3,2,6,7,3]])
#in this field c[this detect row,this detect column]
# print(c[1,-2])
# print(c[0,:])

#to step c[row ,start indes:end index:step]
print(c[0,-8:-2:3])