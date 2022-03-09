# Analyzing the effect of weather on policing!!
# In this chapter, you will use a second dataset to explore the impact of weather conditions on police behavior during traffic stops. You will practice merging and reshaping datasets, assessing whether a data source is trustworthy, working with categorical data, and other advanced skills.

# Plotting the temperature
# In this exercise, you'll examine the temperature columns from the weather dataset to assess whether the data seems trustworthy. First you'll print the summary statistics, and then you'll visualize the data using a box plot.

# When deciding whether the values seem reasonable, keep in mind that the temperature is measured in degrees Fahrenheit, not Celsius!


# Read 'weather.csv' into a DataFrame named 'weather'
weather = pd.read_csv('weather.csv')

# Describe the temperature columns
print(weather[['TMIN','TAVG','TMAX']].describe())

# Create a box plot of the temperature columns
weather[['TMIN','TAVG','TMAX']].plot(kind='box')

# Display the plot
plt.show()



# Plotting the temperature difference
# In this exercise, you'll continue to assess whether the dataset seems trustworthy by plotting the difference between the maximum and minimum temperatures.

# What do you notice about the resulting histogram? Does it match your expectations, or do you see anything unusual?


# Create a 'TDIFF' column that represents temperature difference
weather['TDIFF'] = weather['TMAX'] - weather['TMIN']

# Describe the 'TDIFF' column
print(weather['TDIFF'].describe())

# Create a histogram with 20 bins to visualize 'TDIFF'
weather['TDIFF'].plot(kind = 'hist', bins = 20)

# Display the plot
plt.show()



# Counting bad weather conditions
# The weather DataFrame contains 20 columns that start with 'WT', each of which represents a bad weather condition. For example:

# WT05 indicates "Hail"
# WT11 indicates "High or damaging winds"
# WT17 indicates "Freezing rain"
# For every row in the dataset, each WT column contains either a 1 (meaning the condition was present that day) or NaN (meaning the condition was not present).

# In this exercise, you'll quantify "how bad" the weather was each day by counting the number of 1 values in each row.


# Copy 'WT01' through 'WT22' to a new DataFrame
WT = weather.loc[:,'WT01':'WT22']

# Calculate the sum of each row in 'WT'
weather['bad_conditions'] = WT.sum(axis = 'columns')

# Replace missing values in 'bad_conditions' with '0'
weather['bad_conditions'] = weather.bad_conditions.fillna(0).astype('int')

# Create a histogram to visualize 'bad_conditions'
weather['bad_conditions'].plot(kind = 'hist')

# Display the plot
plt.show()


# Rating the weather conditions
# In the previous exercise, you counted the number of bad weather conditions each day. In this exercise, you'll use the counts to create a rating system for the weather.

# The counts range from 0 to 9, and should be converted to ratings as follows:

# Convert 0 to 'good'
# Convert 1 through 4 to 'bad'
# Convert 5 through 9 to 'worse'



# Count the unique values in 'bad_conditions' and sort the index
print(weather.bad_conditions.value_counts().sort_index())

# Create a dictionary that maps integers to strings
mapping = {0:'good', 1:'bad', 2:'bad', 3:'bad',4:'bad',5:'worse',6:'worse',7:'worse',8:'worse',9:'worse'}

# Convert the 'bad_conditions' integers to strings using the 'mapping'
weather['rating'] = weather.bad_conditions.map(mapping)

# Count the unique values in 'rating'
print(weather.rating.value_counts())



# Changing the data type to category
# Since the rating column only has a few possible values, you'll change its data type to category in order to store the data more efficiently. You'll also specify a logical order for the categories, which will be useful for future exercises.


# Create a list of weather ratings in logical order
cats = ['good', 'bad','worse']

# Change the data type of 'rating' to category
weather['rating'] = weather.rating.astype('category', ordered=True, categories = cats)

# Examine the head of 'rating'
print(weather.rating.head())


# Preparing the DataFrames
# In this exercise, you'll prepare the traffic stop and weather rating DataFrames so that they're ready to be merged:

# With the ri DataFrame, you'll move the stop_datetime index to a column since the index will be lost during the merge.
# With the weather DataFrame, you'll select the DATE and rating columns and put them in a new DataFrame.



# Reset the index of 'ri'
ri.reset_index(inplace = True)

# Examine the head of 'ri'
print(ri.head())

# Create a DataFrame from the 'DATE' and 'rating' columns
weather_rating = weather[['DATE', 'rating']]

# Examine the head of 'weather_rating'
print(weather_rating.head())



# Merging the DataFrames
# In this exercise, you'll merge the ri and weather_rating DataFrames into a new DataFrame, ri_weather.

# The DataFrames will be joined using the stop_date column from ri and the DATE column from weather_rating. Thankfully the date formatting matches exactly, which is not always the case!

# Once the merge is complete, you'll set stop_datetime as the index, which is the column you saved in the previous exercise.


# Examine the shape of 'ri'
print(ri.shape)

# Merge 'ri' and 'weather_rating' using a left join
ri_weather = pd.merge(left=ri, right=weather_rating, left_on='stop_date', right_on='DATE', how='left')

# Examine the shape of 'ri_weather'
print(ri_weather.shape)

# Set 'stop_datetime' as the index of 'ri_weather'
ri_weather.set_index('stop_datetime', inplace=True)



# Comparing arrest rates by weather rating
# Do police officers arrest drivers more often when the weather is bad? Find out below!

# First, you'll calculate the overall arrest rate.
# Then, you'll calculate the arrest rate for each of the weather ratings you previously assigned.
# Finally, you'll add violation type as a second factor in the analysis, to see if that accounts for any differences in the arrest rate.
# Since you previously defined a logical order for the weather categories, good < bad < worse, they will be sorted that way in the results.


# Calculate the overall arrest rate
print(ri_weather.is_arrested.mean())



# Selecting from a multi-indexed Series
# The output of a single .groupby() operation on multiple columns is a Series with a MultiIndex. Working with this type of object is similar to working with a DataFrame:

# The outer index level is like the DataFrame rows.
# The inner index level is like the DataFrame columns.
# In this exercise, you'll practice accessing data from a multi-indexed Series using the .loc[] accessor.


# Save the output of the groupby operation from the last exercise
arrest_rate = ri_weather.groupby(['violation', 'rating']).is_arrested.mean()

# Print the 'arrest_rate' Series
print(arrest_rate)

# Print the arrest rate for moving violations in bad weather
print(arrest_rate.loc['Moving violation','bad'])

# Print the arrest rates for speeding violations in all three weather conditions
print(arrest_rate.loc['Speeding'])




# Reshaping the arrest rate data
# In this exercise, you'll start by reshaping the arrest_rate Series into a DataFrame. This is a useful step when working with any multi-indexed Series, since it enables you to access the full range of DataFrame methods.

# Then, you'll create the exact same DataFrame using a pivot table. This is a great example of how pandas often gives you more than one way to reach the same result!

# Unstack the 'arrest_rate' Series into a DataFrame
print(arrest_rate.unstack())

# Create the same DataFrame using a pivot table
print(ri_weather.pivot_table(index='rating', columns='violation', values='is_arrested'))


