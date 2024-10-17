#Importing the Dependencies
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn import metrics

#Data Collection & Procesing
calories = pd.read_csv("calories.csv")
print(calories.head())
exercise_data = pd.read_csv(("exercise.csv"))
print(exercise_data.head())

#Data Analysis
#Combining the two DataFrames
calories_data = pd.concat([exercise_data, calories['Calories']], axis=1)
print(calories_data.head())
print(calories_data.shape)
print(calories_data.info())
print(calories_data.isnull().sum())
print(calories_data.describe())

#Data Visualisation
sns.set()

#Converting text to numerical
calories_data.replace({'Gender': {'male':0, 'female':1}}, inplace=True)

plt.figure()
sns.distplot(calories_data['Gender'])
plt.title('Gender Distribution')
plt.show()

plt.figure()  # Creates a new figure
sns.distplot(calories_data['Age'])
plt.title('Age Distribution')
plt.show()

plt.figure()  # Creates a new figure
sns.distplot(calories_data['Height'])
plt.title('Height Distribution')
plt.show()

plt.figure()  # Creates a new figure
sns.distplot(calories_data['Weight'])
plt.title('Weight Distribution')
plt.show()

#Finding Correlation
correlation = calories_data.corr()

plt.figure(figsize=(10,10))
sns.heatmap(correlation, cbar=True, square=True, fmt='.1f', annot=True, annot_kws={"size":8}, cmap='Blues')
plt.show()

#Separating Features & Target
x = calories_data.drop(columns=["User_ID", "Calories"], axis=1)
y = calories_data["Calories"]

#Splitting data into train and test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=2)
print(x.shape, x_train.shape, x_test.shape)


#Model Training -> XGBoost Regressor
model = XGBRegressor()
model.fit(x_train, y_train)

#Evaluation
test_data_predictions = model.predict(x_test)
print(test_data_predictions)

#Mean Absolut Error
mae = metrics.mean_absolute_error(y_test, test_data_predictions)
print("Mean Absolut Error = ", mae)

