# Multivariate Thinking!!
# Explore multivariate relationships using multiple regression to describe non-linear relationships and logistic regression to explain and predict binary variables.


# Using StatsModels
# Let's run the same regression using SciPy and StatsModels, and confirm we get the same results.


from scipy.stats import linregress
import statsmodels.formula.api as smf

# Run regression with linregress
subset = brfss.dropna(subset=['INCOME2', '_VEGESU1'])
xs = subset['INCOME2']
ys = subset['_VEGESU1']
res = linregress(xs,ys)
print(res)

# Run regression with StatsModels
results = smf.ols('_VEGESU1 ~ INCOME2', data = brfss).fit()
print(results.params)




# Plot income and education
# To get a closer look at the relationship between income and education, let's use the variable 'educ' to group the data, then plot mean income in each group.

# Here, the GSS dataset has been pre-loaded into a DataFrame called gss.


# Group by educ
grouped = gss.groupby('educ')

# Compute mean income in each group
mean_income_by_educ = grouped['realinc'].mean()

# Plot mean income as a scatter plot
plt.plot(mean_income_by_educ, 'o', alpha = 0.5)

# Label the axes
plt.xlabel('Education (years)')
plt.ylabel('Income (1986 $)')
plt.show()



# Non-linear model of education
# The graph in the previous exercise suggests that the relationship between income and education is non-linear. So let's try fitting a non-linear model.

import statsmodels.formula.api as smf

# Add a new column with educ squared
gss['educ2'] = ____

# Run a regression model with educ, educ2, age, and age2
results = ____

# Print the estimated parameters
print(results.params)



# Making predictions
# At this point, we have a model that predicts income using age, education, and sex.

# Let's see what it predicts for different levels of education, holding age constant.


# Run a regression model with educ, educ2, age, and age2
results = smf.ols('realinc ~ educ + educ2 + age + age2', data=gss).fit()

# Make the DataFrame
df = pd.DataFrame()
df['educ'] = np.linspace(0,20)
df['age'] = 30
df['educ2'] = df['educ']**2
df['age2'] = df['age']**2

# Generate and plot the predictions
pred = results.predict(df)
print(pred.head())



# Visualizing predictions
# Now let's visualize the results from the previous exercise!


# Plot mean income in each age group
plt.clf()
grouped = gss.groupby('educ')
mean_income_by_educ = grouped['realinc'].mean()
plt.plot(mean_income_by_educ, 'o', alpha = 0.5)

# Plot the predictions
pred = results.predict(df)
plt.plot(df['educ'], pred, label='Age 30')

# Label axes
plt.xlabel('Education (years)')
plt.ylabel('Income (1986 $)')
plt.legend()
plt.show()


# Predicting a binary variable
# Let's use logistic regression to predict a binary variable. Specifically, we'll use age, sex, and education level to predict support for legalizing cannabis (marijuana) in the U.S.

# In the GSS dataset, the variable grass records the answer to the question "Do you think the use of marijuana should be made legal or not?"


# Recode grass
gss['grass'].replace(2, 0, inplace=True)

# Run logistic regression
results = smf.logit('grass~ age + age2 + educ + educ2 + C(sex)', data = gss).fit()
results.params





