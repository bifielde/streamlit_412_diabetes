import streamlit as st
import joblib as jb
import pandas as pd
import sklearn as skl
@st.cache_resource()
def load_model(model_name):
    model = jb.load(model_name)
    return (model)
rfm = load_model("best_rf_model.pkl")
gbm = load_model("best_gb_model.pkl")
X = pd.DataFrame()
threshold = .35

form = st.form(key = "input")
form.header("Enter information below")
high_BP = form.checkbox('Have you been diagnosed with high blood pressure?')
if high_BP:
    X.loc[1,1] = 1
else:
    X.loc[1,1] = 0

high_chol = form.checkbox('Have you been diagnosed with high blood cholesterol?')
if high_chol:
    X.loc[1,2] = 1
else:
    X.loc[1,2] = 0

chol_check = form.checkbox('Have you had your cholesterol checked recently?')
if chol_check:
    X.loc[1,3] = 1
else:
    X.loc[1,3] = 0

height = form.number_input('Enter your Height in inches')
weight = form.number_input('Enter your weight in pounds')
if height >1 and weight >1:
    X.loc[1,4] = weight/height * 703

smoker = form.checkbox('are you a smoker?')
if smoker:
    X.loc[1,5] = 1
else:
    X.loc[1,5] = 0

stroke = form.checkbox('Have you ever had a stroke?')
if stroke:
    X.loc[1,6] = 1
else:
    X.loc[1,6] = 0

hdoa = form.checkbox('Have you had heart disease or a heart attack?')
if hdoa:
    X.loc[1,7] = 1
else:
    X.loc[1,7] = 0

phys_act = form.checkbox('would you consider yourself physically active?')
if phys_act:
    X.loc[1,8] = 1
else:
    X.loc[1,8] = 0

fruits = form.checkbox('do you regularly eat fruits?')
if fruits:
    X.loc[1,9] = 1
else:
    X.loc[1,9] = 0

veggies = form.checkbox('do you regurlarly eat vegetables?')
if veggies:
    X.loc[1,10] = 1
else:
    X.loc[1,10] = 0

heavy_alc = form.checkbox('do you have more than 3 alcoholic drinks/week?')
if heavy_alc:
    X.loc[1,11] = 1
else:
    X.loc[1,11] = 0

healthcare = form.checkbox('do you have any sort of healthcare?')
if healthcare:
    X.loc[1,12] = 1
else:
    X.loc[1,12] = 0

nodocbccost = form.checkbox('have you NOT been to a doctor due to cost?')
if nodocbccost:
    X.loc[1,13] = 1
else:
    X.loc[1,13] = 0

genhealth = form.slider('score your general health', min_value=0, max_value=5)
X.loc[1,14] = genhealth

menthealth = form.slider('score your mental health', min_value=0, max_value=30)
X.loc[1,15] = menthealth

physhealth = form.slider('score your physical health', min_value=0, max_value=30)
X.loc[1,16] = physhealth

sex = form.radio('Select your sex:', ['male','female'])
if sex == 'male':
    X.loc[1,17] = 0
else:
    X.loc[1,17] = 1

diff_walk = form.checkbox('do you have difficulty walking?')
if diff_walk:
    X.loc[1,18] = 1
else:
    X.loc[1,18] = 0

age = form.number_input('Enter your age in years')
X.loc[1,19] = age

education = form.selectbox('choose your education level: ', [1,2,3,4,5,6])
X.loc[1,20] = education

income = form.slider('score your income', min_value=0, max_value=8)
X.loc[1,21] = income

model_select = form.selectbox('choose which model to use', ['Random Forest Model', 'Gradient Boost Model'])

form_submit = form.form_submit_button('Submit form')

if form_submit:
    if model_select == 'Random Forest Model':
        model_guess = rfm.predict_proba(X)[:, 1]
        if model_guess > threshold:
            st.write ("you may be at risk of diabetes. Please contact your primary care physician or a diabetes specialist and they may assist you further.")
        else:
            st.write ("You are not likely to be at risk of diabetes. Be sure to keep up with your regularyl scheduled doctor's appointments")
    elif model_select == 'Gradient Boost Model':
        model_guess = rfm.predict_proba(X)[:, 1]
        if model_guess > threshold:
            st.write ("you may be at risk of diabetes. Please contact your primary care physician or a diabetes specialist and they may assist you further.")
        else:
            st.write ("You are not likely to be at risk of diabetes. Be sure to keep up with your regularly scheduled doctor's appointments")

