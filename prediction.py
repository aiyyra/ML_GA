import pickle
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
import numpy as np


model = LinearRegression()

pipeline = Pipeline([
    ('poly', PolynomialFeatures()),
    ('regression', model)
])

filename = 'finalPolyModel_pkl'
with open(filename,'rb') as f :
    pipeline=pickle.load(f)

tempd = np.array([[39, 25, 80, 2, 0, 0, 1, 2]])



def predict(data): 
    temp = pipeline['poly'].transform(data)
    return pipeline['lr'].predict(temp)

# test = pipeline2['poly'].transform(data0[0][0])
# pipeline2['lr'].predict(test)