# Diabetes analytics streamlit application
## About
This projects is an extension of a team project I worked on in my Neural Network class at Arizona State University.
The application runs through streamlit, using neural networks developed by our team to predict a user's diabetes risk factor using three different machine learning models, based on the user input data.
##  Model information
All our models were trained on the [CDC's 2015 BRFSS dataset](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset?select=diabetes_binary_health_indicators_BRFSS2015.csv)
### Data preprocessing
Fortunately there were no null values we had to deal with in the dataset, although there were around 24,000 duplicate records that were removed.
the largest issue with the data by far was that there was a severe imbalance between records identified as diabetic and non-diabetic, with the latter making up almost 85% of the dataset.
To rectify this issue, we used SMOTE to balance out the data, after splitting the data 80-20 for training and testing purposes.

### Model evaluation
Since diabetes is a "better safe than sorry" type of problem, the team primarily focused on chasing a model's recall above accuracy, precision, or F-score.
Additionally, we used ROC graphs to further identify model performance, and used confusion matrices to visually evaluate how our models were making decisions.
### Random Forest Model
One of the models our team developed was a random forest regression model. We trained this model using a grid search algorithm, and after adjusting the model's threshold to .35, we achieved the following scores:

### Gradient Boost model
The next model we trained was a gradient boosting model. again, this model was trained using a grid search algorithm, and the threshold was adjusted to ___

### Neural Network
The final model we developed was a neural network model. Unfortunately, we were unable to use grid search for our hyperparameter tuning, as it simply was too time/resource intensive.
Instead, we manually experimented with various model architectures, adjusting number of nodes and hidden layers, as well as experimenting with learning rates, solvers, and iteration counts in order to further optimize the model.
in the end, we settled on a 2x5 model design: 2 hidden layers, and 5 nodes per layer. We ended up using the ADAM solver, but decided to leave the learning rates and iteration counts at the default values of 0.0001 and 100 (respectively).


## Streamlit application
The actual application itself is fairly simple:
The user inputs relevant data into a streamlit form (essentially inputting data for each column in the original dataset minus the target variable), and the models (previously dumped with joblib as mentioned) make a prediction based on the data in that form.
Some complications that arose: certain information (income, for example) was not raw data, but had been categorized into bins. Since a user is unaware of these bins, I took the information on those bins from the kaggle data dictionary, and implemented them into the application here.
Additionally, most users don't know their BMI off the top of their head. The goal for our project was to have users recieve results less than 10 minutes after opening the form. we wanted to keep the user experience as smooth as possible, in order to increase diabetes risk awareness.
for this issue, we simply calculate the user's BMI behind the scenes using their height and weight as input values.
Lastly, we wanted to give users the option to have "second opinions" from the different models, both as a risk mitigation step, as well as a way to demonstrate our three different models to our professor. 
To achieve this, we simply loaded all three models and added a drop down menu to select any of the three models available, or an average prediction based on the output of all three.

## Conclusion

We hope you find the experience to be straightforward and without issue! 
Please remember that while this dataset (and as a result, our application) is based off an actual CDC study, the prediction may not be wholly accurate to your own personal diabetic risk.
We are data analysts, not doctors, and this tool is NOT INTENDED TO REPLACE AN ACTUAL DIAGNOSIS.

Thank you for your time, and enjoy the app!
# [Link to streamlit](https://ryjmjdxgjcf3wmti4jvksz.streamlit.app/)
