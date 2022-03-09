#Making a scatter plot with lists

# In this exercise, we'll use a dataset that contains information about 227 countries. This dataset has lots of interesting information on each country, such as the country's birth rates, death rates, and its gross domestic product(GDP). GDP is the value of all the goods and services produced in a year, expressed as dollars per person.

# We've created three lists of data from this dataset to get you started. gdp is a list that contains the value of GDP per country, expressed as dollars per person. phones is a list of the number of mobile phones per 1,000 people in that country. Finally, percent_literate is a list that contains the percent of each country's population that can read and write.

# Import Matplotlib and Seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# In the last exercise, we explored a dataset that contains information about 227 countries. Let's do more exploration of this data - specifically, how many countries are in each region of the world?

# To do this, we'll need to use a count plot. Count plots take in a categorical list and return bars that represent the number of list entries per category. You can create one here using a list of regions for each country, which is a variable named region.

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns


# Create count plot with region on the y-axis
sns.countplot(y=region)

# Show plot
plt.show()

# "Tidy" vs. "untidy" data
# Here, we have a sample dataset from a survey of children about their favorite animals. But can we use this dataset as- is with Seaborn? Let's use Pandas to import the csv file with the data collected from the survey and determine whether it is tidy, which is essential to having it work well with Seaborn.

# To get you started, the filepath to the csv file has been assigned to the variable csv_filepath.

# Note that because csv_filepath is a Python variable, you will not need to put quotation marks around it when you read the csv.
# Import Pandas

# Create a DataFrame from csv file
df = pd.read_csv(csv_filepath)

# Print the head of df
print(df.head())

# Making a count plot with a DataFrame
# In this exercise, we'll look at the responses to a survey sent out to young people. Our primary question here is: how many young people surveyed report being scared of spiders? Survey participants were asked to agree or disagree with the statement "I am afraid of spiders". Responses vary from 1 to 5, where 1 is "Strongly disagree" and 5 is "Strongly agree".

# To get you started, the filepath to the csv file with the survey data has been assigned to the variable csv_filepath.

# Note that because csv_filepath is a Python variable, you will not need to put quotation marks around it when you read the csv.

# Import Matplotlib, Pandas, and Seaborn


# Create a DataFrame from csv file
df = pd.read_csv(csv_filepath)

# Create a count plot with "Spiders" on the x-axis
sns.countplot(x='Spiders', data=df)

# Display the plot
plt.show()

# Hue and scatter plots
# In the prior video, we learned how hue allows us to easily make subgroups within Seaborn plots. Let's try it out by exploring data from students in secondary school. We have a lot of information about each student like their age, where they live, their study habits and their extracurricular activities.

# For now, we'll look at the relationship between the number of absences they have in school and their final grade in the course, segmented by where the student lives(rural vs. urban area).
# Import Matplotlib and Seaborn

# Create a scatter plot of absences vs. final grade
sns.scatterplot(x='absences', y='G3', data=student_data, hue='location')


# Show plot
plt.show()

# Hue and count plots
# Let's continue exploring our dataset from students in secondary school by looking at a new variable. The "school" column indicates the initials of which school the student attended - either "GP" or "MS".

# In the last exercise, we created a scatter plot where the plot points were colored based on whether the student lived in an urban or rural area. How many students live in urban vs. rural areas, and does this vary based on what school the student attends? Let's make a count plot with subgroups to find out.
# Import Matplotlib and Seaborn

# Create a dictionary mapping subgroup values to colors
palette_colors = {'Rural': "green", 'Urban': "blue"}

# Create a count plot of school with location subgroups
sns.countplot(x='school', data=student_data,
              hue='location', palette=palette_colors)


# Display plot
plt.show()




