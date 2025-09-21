# Time-series-analysis-on-covid-19-
Time Series Analysis
🔹 What is Time Series Analysis?
•	A technique to analyze data points collected over time (e.g., COVID-19 cases).
•	Helps in understanding seasonality, trends, and forecasting future values.
🔹 Techniques Used
✔ Trend Decomposition – Using seasonal_decompose() to break data into Trend, Seasonality, and Residuals.
✔ Moving Average – Smooths fluctuations by computing 7-day rolling averages (rolling(window=7).mean()).
✔ ARIMA Forecasting – Used to predict future cases using past trends.
________________________________________
Forecasting with ARIMA Model
🔹 What is ARIMA?
•	AutoRegressive Integrated Moving Average (ARIMA) is a statistical model for time series forecasting.
•	It predicts future values based on past trends.
🔹 ARIMA Steps in Code
1.	Split data into train (80%) and test (20%).
2.	Train the ARIMA model using ARIMA(train, order=(5,1,0)).
3.	Make Predictions on the test set using .forecast().
4.	Plot actual vs. predicted values to evaluate accuracy.
________________________________________
📌 Conclusion
This project analyzes COVID-19 trends, detects patterns, and forecasts future cases using data visualization, decomposition, and ARIMA modeling. These techniques help understand the impact of COVID-19 and make informed decisions.
