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
mlp = load_model("best_mlp_model.pkl")
X = pd.DataFrame()
high_threshold = .35
med_threshold = .25

form = st.form(key = "input")
form.header("Diabetes risk screening form")
form.subheader('Please enter your information below')
form.text('For checkbox questions, check the associated box if the answer is YES. Otherwise, leave the box blank. Please read all questions carefully and answer to the best of your knowledge.')
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

height = form.number_input('Height-feet', min_value = 1)*12 + form.number_input('Height-inches', min_value = 0)
weight = form.number_input('Enter your weight in pounds', min_value = 1)
X.loc[1,4] = weight/height * 703

smoker = form.checkbox('Are you a smoker?')
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

phys_act = form.checkbox('Would you consider yourself physically active?')
if phys_act:
    X.loc[1,8] = 1
else:
    X.loc[1,8] = 0

fruits = form.checkbox('Do you regularly eat fruits?')
if fruits:
    X.loc[1,9] = 1
else:
    X.loc[1,9] = 0

veggies = form.checkbox('Do you regurlarly eat vegetables?')
if veggies:
    X.loc[1,10] = 1
else:
    X.loc[1,10] = 0

heavy_alc = form.checkbox('Do you have more than 3 alcoholic drinks/week?')
if heavy_alc:
    X.loc[1,11] = 1
else:
    X.loc[1,11] = 0

healthcare = form.checkbox('Do you have any sort of healthcare?')
if healthcare:
    X.loc[1,12] = 1
else:
    X.loc[1,12] = 0

nodocbccost = form.checkbox('Have you NOT been to a doctor due to cost?')
if nodocbccost:
    X.loc[1,13] = 1
else:
    X.loc[1,13] = 0

genhealth = form.slider('Score your general health on a scale of 1-5, with 1=excellent, 5=poor', min_value=1, max_value=5)
X.loc[1,14] = genhealth

menthealth = form.slider('How many days have you had poor mental health over the past month?', min_value=0, max_value=30)
X.loc[1,15] = menthealth

physhealth = form.slider('How many days have you experienced an injury over the last month?', min_value=0, max_value=30)
X.loc[1,16] = physhealth

sex = form.radio('Select your sex:', ['Male','Female'])
if sex == 'male':
    X.loc[1,17] = 0
else:
    X.loc[1,17] = 1

diff_walk = form.checkbox('Do you have difficulty walking?')
if diff_walk:
    X.loc[1,18] = 1
else:
    X.loc[1,18] = 0

age = form.number_input('Enter your age in years', min_value = 1)
if age >= 80:
    X.loc[1,19] = 13
elif age >= 75:
    X.loc[1,19] = 12
elif age >= 70:
    X.loc[1,19] = 11
elif age >= 65:
    X.loc[1,19] = 10
elif age >= 60:
    X.loc[1,19] = 9
elif age >= 55:
    X.loc[1,19] = 8
elif age >= 50:
    X.loc[1,19] = 7
elif age >= 45:
    X.loc[1,19] = 6
elif age >= 40:
    X.loc[1,19] = 5
elif age >= 35:
    X.loc[1,19] = 4
elif age >= 30:
    X.loc[1,19] = 3
elif age >= 25:
    X.loc[1,19] = 2
else:
    X.loc[1,19] = 1

education = form.selectbox('Select your education level:', ['Kindergarten or no school','Elementary school','Some high school','High school graduate or GED','Some college or technical school','College graduate or higher'])
if education == 'Kindergarten or no school':
    X.loc[1,20] = 1
elif education == 'Elementary school':
    X.loc[1,20] = 2
elif education == 'Some high school':
    X.loc[1,20] = 3
elif education == 'High school graduate or GED':
    X.loc[1,20] = 4
elif education == 'Some college or technical school':
    X.loc[1,20] = 5
elif education == 'College graduate or higher':
    X.loc[1,20] = 6


income = form.selectbox('Select your income range', ['less than $10,000','$10,000-$15,000','$15,000-$20,000', '$25,000-$30,000', '30,000-$35,000', '$35,000-$45,000', '$45,000-$75,000', '$75,000 or higher'])
if income == 'less than $10,000':
    X.loc[1,21] = 1
elif income == '$10,000-$15,000':
    X.loc[1,21] = 2
elif income == '$15,000-$20,000':
    X.loc[1,21] = 3
elif income == '$25,000-$30,000':
    X.loc[1,21] = 4
elif income == '30,000-$35,000':
    X.loc[1,21] = 5
elif income == '$35,000-$45,000':
    X.loc[1,21] = 6
elif income == '$45,000-$75,000':
    X.loc[1,21] = 7
elif income == '$75,000 or higher':
    X.loc[1,21] = 8

model_select = form.selectbox('Choose which model to use', ['Random Forest Model', 'Gradient Boost Model', 'Multi-Layer Perceptron'])

form_submit = form.form_submit_button('Submit form')

if form_submit:
    if model_select == 'Random Forest Model':
        model_guess = rfm.predict_proba(X)[:, 1]
        st.write("model output:", model_guess)
        if model_guess > high_threshold:
            st.write ("you may be at high risk of diabetes. Please contact your primary care physician or a diabetes specialist and they may assist you further.")
        elif model_guess > med_threshold:
            st.write("you may be at increased risk of diabetes. Consider contacting your primary care physician or a diabetes specialist for recommendations on risk reduction.")
        else:
            st.write ("You are currently not likely to be at risk of diabetes. Be sure to keep up with your regularly scheduled medical appointments for continued risk mitigation")
    elif model_select == 'Gradient Boost Model':
        model_guess = gbm.predict_proba(X)[:, 1]
        st.write("model output:", model_guess)
        if model_guess > high_threshold:
            st.write ("you may be at high risk of diabetes. Please contact your primary care physician or a diabetes specialist and they may assist you further.")
        elif model_guess > med_threshold:
            st.write("you may be at increased risk of diabetes. Consider contacting your primary care physician or a diabetes specialist for recommendations on risk reduction.")
        else:
            st.write ("You are currently not likely to be at risk of diabetes. Be sure to keep up with your regularly scheduled medical appointments for continued risk mitigation")
    elif model_select == 'Multi-Layer Perceptron':
        model_guess = mlp.predict_proba(X)[:, 1]
        #correction for MLP model output:
        model_guess = model_guess*100000000000000
        st.write("model output:", model_guess)
        if model_guess > high_threshold:
            st.write ("you may be at high risk of diabetes. Please contact your primary care physician or a diabetes specialist and they may assist you further.")
        elif model_guess > med_threshold:
            st.write("you may be at increased risk of diabetes. Consider contacting your primary care physician or a diabetes specialist for recommendations on risk reduction.")
        else:
            st.write ("You are currently not likely to be at risk of diabetes. Be sure to keep up with your regularly scheduled medical appointments for continued risk mitigation")

