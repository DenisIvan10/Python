#S&P500 Price Data
import yfinance as yf

sp500 = yf.Ticker("^GSPC")
sp500 = sp500.history(period="max")
print(sp500.index)


#Cleaning & Visualizing S&P500 Market Data
sp500.plot.line(y="Close", use_index=True)
sp500 = sp500.drop(['Dividends', 'Stock Splits'], axis=1)


#Target For ML
sp500['Tomorrow'] = sp500['Close'].shift(-1) #The column that shows tomorrow's price
sp500['Target'] = (sp500['Tomorrow'] > sp500['Close']).astype(int)
sp500 = sp500.loc["1990-01-01":].copy() #Work with data after 1990 to not take into account big changes until that point


#Training The Model
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100, min_samples_split=100, random_state=1)

train = sp500.iloc[:-100]
test = sp500[-100:]

predictors = ['Close', 'Volume', 'Open', 'High', 'Low']

model.fit(train[predictors], train['Target'])

from sklearn.metrics import precision_score

preds = model.predict(test[predictors])

import pandas as pd

preds = pd.Series(preds, index=test.index)

score = precision_score(test['Target'], preds)
print(score)

combined = pd.concat([test['Target'], preds], axis=1) #Compare the actual values with generated ones
combined.plot()


#Building Backtsting Sysytem
def predict(train, test, predictors, model):
    model.fit(train[predictors], train['Target'])
    preds = model.predict(test[predictors])
    preds = pd.Series(preds, index=test.index, name="Predictions")
    combined = pd.concat([test['Target'], preds], axis=1)
    return combined

def backtest(data, model, predictors, start=2500, step=250): #Traing the model for 10 years(~2500 days). We will train year by year(~250 days)
    all_predictions = []
    for i in range(start, data.shape[0], step):
        train = data.iloc[0:i].copy() #All years prior to current year(2024)
        test = data.iloc[i:(i+step)].copy() #Current year(2024)
        predictions = predict(train, test, predictors, model)
        all_predictions.append(predictions)
    return pd.concat(all_predictions)

predictions = backtest(sp500, model, predictors)
print(predictions['Predictions'].value_counts())
score2 = precision_score(predictions['Target'], predictions['Predictions'])
print(score2)

percent = predictions['Target'].value_counts() / predictions.shape[0]
print(percent)


#Adding Aditional Predictors To The Model
horizons = [2,5,60,250,1000] #Rolling means 2 days - 4 years
new_predictors = []

for horizon in horizons:
    rolling_averages = sp500.rolling(horizon).mean()
    ratio_column = f"Close_Ratio_{horizon}"
    sp500[ratio_column] = sp500['Close'] / rolling_averages['Close'] #Average between todays close and the average close in the last 2,5,60,250,1000 days
    trend_column = f"Trend_{horizon}" #Column where the stock price actually go up
    sp500[trend_column] = sp500.shift(1).rolling(horizon).sum()['Target'] #Looks on a day and sums the privious days targets where the price went up
    new_predictors += [ratio_column, trend_column]

#If it can't find enought days to compute a rolling average it will return a NaN
sp500 = sp500.dropna() #Now tha data starts from 1993 and not 1990


#Improving The Model
model = RandomForestClassifier(n_estimators=200, min_samples_split=50, random_state=1)

def predict(train, test, predictors, model):
    model.fit(train[predictors], train['Target'])
    preds = model.predict_proba(test[predictors])[:,1] #Now it returns probability instead 0 or 1 -> we'll work with probability grather or equal with 60%
    preds[preds >= .6] = 1
    preds[preds < .6] = 0
    preds = pd.Series(preds, index=test.index, name="Predictions")
    combined = pd.concat([test['Target'], preds], axis=1)
    return combined

predictions = backtest(sp500, model, new_predictors)
print(predictions['Predictions'].value_counts())
score3 = precision_score(predictions['Target'], predictions['Predictions'])
print(score3)


