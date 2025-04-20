import streamlit as st
import pandas as pa

st.title("BMI CALCULATOR")

height = st.slider("Enter your height (in feet)", 2, 5, 10)
weight = st.slider("Enter your weight (in kg)", 40, 200, 70)

bmi = weight / ((height/100)**2)

st.write(f'Your BMI is {bmi:.2f}')

st.write("### BMI Categories ###")
st.write("- Underweight: BMI is less than 18.5")
st.write("- Normal Weight: BMI is Between 18.5 and 24.9")
st.write("- Over Weight: BMI is Between 25 and 29.9")
st.write("- Obesity: BMI 30 or greater")