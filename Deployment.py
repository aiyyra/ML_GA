
import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict

st.title("Health insurance claim prediction")
st.markdown("Providing suggestion on health insurance premium to overcome financial problem and gain access to health industry")

st.header("Details : ")
#age bmi bp #children gender diabetic smoker region

customerage = st.slider('Age : ',value=25,max_value=65,min_value=18)
#st.write(customerage," is customer age")

gender = st.selectbox("Gender : ",('Male','Female'))

if(gender == 'Male'):
    genderE=1
else:
    genderE=0

children = st.selectbox("Children : ",(0,1,2,3,4,5))

bmi = st.slider("BMI : ", value=25, min_value=15, max_value=55)

bp = st.slider("Blood Pressure : ",value=85, min_value=70,max_value=150)


diabeticStatus = st.selectbox("Has Diabetes : ",('Yes','No'))
if(diabeticStatus == 'Yes'):
    diabetic = 1
else:
    diabetic = 0

SmokingStatus = st.selectbox("Smoking : ",('Yes','No'))
if(SmokingStatus == 'Yes'):
    smoker = 1
else:
    smoker = 0

regionFrom = st.selectbox("Region : ",('northeast','northwest','southeast','southwest'))

if(regionFrom == 'northeast'):
    region=1
elif(regionFrom == 'northwest'):
    region=2
elif(regionFrom == 'southeast'):
    region=3
elif(regionFrom == 'southwest'):
    region=4


data = np.array([[customerage, bmi, bp, children, diabetic, smoker, genderE, region]])
st.header("Summary of Data : ")
data


if (st.button("Press to predict your optimum Insurance premium",key="try")):
    result = predict(data)[0]
    st.write(round(result,2))
    print(result)
