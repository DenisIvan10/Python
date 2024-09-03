<h1>Description</h1>
<p>This project utilizes historical S&P 500 data to build a machine learning model that predicts whether the next day's closing price will be higher than the current day's closing price. The model uses RandomForestClassifier to make these predictions and includes a backtesting analysis to evaluate the model's performance.</p>
<h1>Features</h1>
<h3>Data collection</h3>
<ul>
  <li>Data is collected using yfinance to obtain historical S&P 500 prices</li>
</ul>
<h3>Data cleaning and visualization</h3> 
<ul>
  <li>Data is cleaned by removing irrelevant columns and visualized to understand price distributions and other characteristics</li>
</ul>
<h3>Creating the "Target" for Machine Learning</h3>
<ul>
  <li>A "Target" column is created indicating whether the next day's closing price is higher than the current day's closing price</li>
</ul>
<h3>Model training</h3>
<ul>
  <li>A RandomForestClassifier model is trained on the historical data, using closing prices and trading volumes as predictors</li>
</ul>
<h3>Model evaluation</h3>
<ul>
  <li>Model performance is evaluated using the "precision_score" on the test dataset</li>
  <li>Backtesting is performed to assess the model's performance over time</li>
</ul>
<h3>Adding additional predictors</h3>
<ul>
  <li>New predictors based on rolling averages are added to improve the model</li>
</ul>
<h3>Model improvement</h3>
<ul>
  <li>The model is refined using new predictors and probabilities instead of discrete values to make more accurate predictions</li>
</ul>
