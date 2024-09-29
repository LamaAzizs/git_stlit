import streamlit as st
import joblib
 
st.title(" hello world")
model = joblib.load('linear.pkl')

st.write('Salary Preduction')

X = st.slider('Experiance' , 0 ,40)
y = model.predict([[X]])
st.write('salary is : ' , y)
