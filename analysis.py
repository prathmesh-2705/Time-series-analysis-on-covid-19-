import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima.model import ARIMA

# ✅ Load Updated COVID-19 Dataset
url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/jhu/full_data.csv"
covid_data = pd.read_csv(url)

# ✅ Convert Date Column to Datetime Format
covid_data["date"] = pd.to_datetime(covid_data["date"])

# ✅ Aggregate Global Cases
global_cases = covid_data.groupby("date")["new_cases"].sum().reset_index()

# ✅ Plot Global Cases
plt.figure(figsize=(10, 6))
plt.plot(global_cases["date"], global_cases["new_cases"], color="blue", label="Global Cases")
plt.title("Global COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Number of Cases")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ✅ Decompose Time Series Data
decomposition = seasonal_decompose(global_cases["new_cases"], model="additive", period=30)
decomposition.plot()
plt.show()

# ✅ Moving Average for Smoothing
global_cases["7-day MA"] = global_cases["new_cases"].rolling(window=7).mean()

plt.figure(figsize=(10, 6))
plt.plot(global_cases["date"], global_cases["new_cases"], label="Daily Cases", color="blue", alpha=0.5)
plt.plot(global_cases["date"], global_cases["7-day MA"], label="7-Day Moving Average", color="red", linestyle="--")
plt.title("COVID-19 Cases with 7-Day Moving Average")
plt.xlabel("Date")
plt.ylabel("Number of Cases")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
