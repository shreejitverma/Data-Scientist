#!/usr/bin/env python
# coding: utf-8

# # import required library

# In[1]:


# Import numpy, pandas for data manipulation
import numpy as np
import pandas as pd

# Import matplotlib, seaborn for visualization
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# In[2]:


# Import the data
weather_data = pd.read_csv('weather.csv')
weather_data.head()


# In[8]:


rain_df = weather_data[['Date','Rainfall']]
rain_df.head()


# In[9]:


rain_df.shape


# In[10]:


rain_df.info()


# **Using 50 values**

# In[15]:


rain_df = rain_df.loc[:49]
rain_df.head()


# In[16]:


rain_df.shape


# In[17]:


# Convert the time column into datetime
rain_df['Date'] = pd.to_datetime(rain_df['Date'])
rain_df['Date'].head()


# In[18]:


rain_df.info()


# In[24]:


# fill the empty row
rain_df = rain_df.fillna(rain_df['Rainfall'].mean())
rain_df.head()


# ### Dataset Explanation

# In[27]:


rain_df.describe()


# In[29]:


# Output the maximum and minimum rain date
print(rain_df.loc[rain_df["Rainfall"] == rain_df["Rainfall"].max()])
print(rain_df.loc[rain_df["Rainfall"] == rain_df["Rainfall"].min()])


# In[30]:


# Reset the index 
rain_df.set_index("Date", inplace=True)


# ### Data Visualization

# In[32]:


# Plot the daily temperature change 
plt.figure(figsize=(16,10), dpi=100)
plt.plot(rain_df.index, rain_df.Rainfall, color='tab:red')
plt.gca().set(title="Daily Rain", xlabel='Date', ylabel="rain value")
plt.show()


# In[35]:


# Apply the Moving Average function by a subset of size 10 days.
rain_df_mean = rain_df.Rainfall.rolling(window=10).mean()
rain_df_mean.plot(figsize=(16,10))
plt.show()


# In[37]:


from statsmodels.tsa.seasonal import seasonal_decompose

# Additive Decomposition
result_add = seasonal_decompose(rain_df.Rainfall, model='additive', extrapolate_trend=0)

# Plot
plt.rcParams.update({'figure.figsize': (10,10)})
result_add.plot().suptitle('Additive Decomposition', fontsize=22)
plt.show()


# ### Baseline Model

# In[38]:


# Shift the current rain to the next day. 
predicted_df = rain_df["Rainfall"].to_frame().shift(1).rename(columns = {"Rainfall": "rain_pred" })
actual_df = rain_df["Rainfall"].to_frame().rename(columns = {"Rainfall": "rain_actual" })

# Concatenate the actual and predicted rain
one_step_df = pd.concat([actual_df,predicted_df],axis=1)

# Select from the second row, because there is no prediction for today due to shifting.
one_step_df = one_step_df[1:]
one_step_df.head(10)


# > Here you can the we have two column one is our **actual rain** column and othe is **predicted rain** column that we use next model 

# We could validate how well our model is by looking at the Root Mean Squared Error(RMSE) between the predicted and actual rain

# In[41]:


from sklearn.metrics import mean_squared_error as MSE
from math import sqrt

# Calculate the RMSE
rain_pred_err = MSE(one_step_df.rain_actual, one_step_df.rain_pred, squared=False)
print("The RMSE is",rain_pred_err)


# > Our RMSE value is 4.002 is arround 4 that are pretty good for model.

# ##  Using SARIMA model

# ### Parameter Selection
# #### Grid Search
# We are going to apply one of the most commonly used method for time-series forecasting, known as SARIMA, which stands for Seasonal Autoregressive Integrated Moving Average. SARIMA models are denoted with the notation SARIMA(p,d,q)(P,D,Q,s). These three parameters account for seasonality, trend, and noise in data:
# 
# We will use a “grid search” to iteratively explore different combinations of parameters. For each combination of parameters, we fit a new seasonal SARIMA model with the SARIMAX() function from the statsmodels module and assess its overall quality.

# In[42]:


import itertools

# Define the p, d and q parameters to take any value between 0 and 2
p = d = q = range(0, 2)

# Generate all different combinations of p, q and q triplets
pdq = list(itertools.product(p, d, q))

# Generate all different combinations of seasonal p, q and q triplets
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

print('Examples of parameter combinations for Seasonal ARIMA...')
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))


# In[43]:


for param in pdq:
    for param_seasonal in seasonal_pdq:
        try:
            mod = sm.tsa.statespace.SARIMAX(one_step_df.rain_actual,
                                            order=param,
                                            seasonal_order=param_seasonal,
                                            enforce_stationarity=False,
                                            enforce_invertibility=False)

            results = mod.fit()

            print('SARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
        except:
            continue


# ### Fitting the Model

# In[47]:


import warnings
warnings.filterwarnings("ignore") # specify to ignore warning messages
# Import the statsmodels library for using SARIMAX model
import statsmodels.api as sm

# Fit the SARIMAX model using optimal parameters
mod = sm.tsa.statespace.SARIMAX(one_step_df.rain_actual,
                                order=(1,1,1),
                                seasonal_order=(1,1,1,12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)


# In[48]:


results = mod.fit()


# In[49]:


results.summary()


# **Predictions**

# In[51]:


pred = results.predict(start=0,end=49)[1:]
pred


# In[52]:


pred = results.get_prediction(start=0,end = 49, dynamic=False)
pred_ci = pred.conf_int()


# In[53]:


pred_ci.head()


# In[55]:


print(pred)


# In[58]:


ax = one_step_df.rain_actual.plot(label='observed',figsize=(16,10))
ax.set_xlabel('Date')
ax.set_ylabel('value')
plt.ylim([0,2.0])
plt.legend()
plt.show()


# ### Forecast Diagnostic
# It is also useful to quantify the accuracy of our forecasts. We will use the MSE (Mean Squared Error), in which for each predicted value, we compute its distance to the true value and square the result

# In[65]:


y_forecasted = pred.predicted_mean[:49]
y_truth = one_step_df.rain_actual
print(y_forecasted.shape)
print(y_truth.shape)
# Compute the mean square error
mse = MSE(y_truth, y_forecasted, squared=True)
print('The Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))


# Amazziingggg! Our forecast model forecasts the rain with only an error of 25.85. 
# 
# In the weather forecast field, the prediction error of 2.19 degrees seems promising and sufficient, as there are many other factors that contribute to the change in rain, including but not limited to the wind speed, the air pressure, etc.

# ### Validating the Dynamic Forecast

# In this case, we only use information from the time series up to a certain point, and after that, forecasts are generated using values from previous forecasted time points.
# 

# In[66]:


pred_dynamic = results.get_prediction(start=0,end = 49, dynamic=True, full_results=True)
pred_dynamic_ci = pred_dynamic.conf_int()


# In[67]:


pred_dynamic_ci.head()


# Once again, we plot the real and forecasted values of the average daily rain to assess how well we did:

# In[71]:


ax = one_step_df.rain_actual.plot(label='observed', figsize=(15, 11))
pred_dynamic.predicted_mean.plot(label='Dynamic Forecast', ax=ax)

ax.fill_between(pred_dynamic_ci.index,
                pred_dynamic_ci.iloc[:, 0],
                pred_dynamic_ci.iloc[:, 1], color='k', alpha=.25)


ax.set_xlabel('Date')
ax.set_ylabel('Temperature (in Celsius)')
plt.ylim([0,2.0])
plt.legend()
plt.show()


# > In this case, the model seems to predict the rain inaccurately, with major fluctuations between the true value and the predicted value.

# ### Forecast Diagnostic

# In[73]:


# Extract the predicted and true values of our time series
y_forecasted = pred_dynamic.predicted_mean[:49]
y_truth = one_step_df.rain_actual

# Compute the mean square error
mse = sqrt(MSE(y_truth, y_forecasted).mean())
print('The Root Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))


# The **predicted** values obtained from the dynamic forecasts yield an MSE of 3.68. This is significantly higher than the one-step ahead, which is to be expected given that we are relying on less historical data from the time series.

# # Conclusion

# I described how to implement a seasonal SARIMA model in Python. I made extensive use of the pandas and statsmodels libraries and showed how to run model diagnostics, as well as how to produce forecasts of the Rain.

# Recall that in the assumption I made in the section 2.2 Baseline Model, I could even reinforce our assumption and continue our belief that the rainfall today depends on the rainfall yesterday, the rainfall yesterday depends on the day before yesterday, and so on. 
# 
# It is the best so far to use the history up to the point that we would like to make **predictions** on. Especially it holds for weather forecasting, where the rainfall today does not change much from yesterday, and the transition to another season signaling through the rainfall should gradually occur, unless there is any disastrous factors such as storm, drought, etc.
