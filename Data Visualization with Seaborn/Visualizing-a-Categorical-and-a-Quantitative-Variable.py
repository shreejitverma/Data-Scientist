# Visualizing a Categorical and a Quantitative Variable
# Categorical variables are present in nearly every dataset, but they are especially prominent in survey data. In this chapter, you will learn how to create and customize categorical plots such as box plots, bar plots, count plots, and point plots. Along the way, you will explore survey data from young people about their interests, students about their study habits, and adult men about their feelings about masculinity.

# Count plots
# In this exercise, we'll return to exploring our dataset that contains the responses to a survey sent out to young people. We might suspect that young people spend a lot of time on the internet, but how much do they report using the internet each day? Let's use a count plot to break down the number of survey responses in each category and then explore whether it changes based on age.

# As a reminder, to create a count plot, we'll use the catplot() function and specify the name of the categorical variable to count(x=____), the Pandas DataFrame to use(data=____), and the type of plot(kind="count").

# Seaborn has been imported as sns and matplotlib.pyplot has been imported as plt.
# Create count plot of internet usage
sns.catplot(x='Internet usage', data=survey_data, kind='count')


# Show plot
plt.show()

# Bar plots with percentages
# Let's continue exploring the responses to a survey sent out to young people. The variable "Interested in Math" is True if the person reported being interested or very interested in mathematics, and False otherwise. What percentage of young people report being interested in math, and does this vary based on gender? Let's use a bar plot to find out.

# As a reminder, we'll create a bar plot using the catplot() function, providing the name of categorical variable to put on the x-axis(x=____), the name of the quantitative variable to summarize on the y-axis(y=____), the Pandas DataFrame to use(data=____), and the type of categorical plot(kind="bar").

# Seaborn has been imported as sns and matplotlib.pyplot has been imported as plt.
# Create a bar plot of interest in math, separated by gender
sns.catplot(x='Gender', y='Interested in Math', data=survey_data, kind='bar')


# Show plot
plt.show()

# Customizing bar plots
# In this exercise, we'll explore data from students in secondary school. The "study_time" variable records each student's reported weekly study time as one of the following categories: "<2 hours", "2 to 5 hours", "5 to 10 hours", or ">10 hours". Do students who report higher amounts of studying tend to get better final grades? Let's compare the average final grade among students in each category using a bar plot.

# Seaborn has been imported as sns and matplotlib.pyplot has been imported as plt.
# Create bar plot of average final grade in each study category
sns.catplot(x='study_time', y='G3', data=student_data, kind='bar')


# Show plot
plt.show()


# Create and interpret a box plot
# Let's continue using the student_data dataset. In an earlier exercise, we explored the relationship between studying and final grade by using a bar plot to compare the average final grade("G3") among students in different categories of "study_time".

# In this exercise, we'll try using a box plot look at this relationship instead. As a reminder, to create a box plot you'll need to use the catplot() function and specify the name of the categorical variable to put on the x-axis(x=____), the name of the quantitative variable to summarize on the y-axis(y=____), the Pandas DataFrame to use(data=____), and the type of plot(kind="box").

# We have already imported matplotlib.pyplot as plt and seaborn as sns.

# Specify the category ordering
study_time_order = ["<2 hours", "2 to 5 hours",
                    "5 to 10 hours", ">10 hours"]

# Create a box plot and set the order of the categories
sns.catplot(x='study_time', y="G3", data=student_data,
            order=study_time_order, kind='box')


# Show plot
plt.show()

# Omitting outliers
# Now let's use the student_data dataset to compare the distribution of final grades ("G3") between students who have internet access at home and those who don't. To do this, we'll use the "internet" variable, which is a binary(yes/no) indicator of whether the student has internet access at home.

# Since internet may be less accessible in rural areas, we'll add subgroups based on where the student lives. For this, we can use the "location" variable, which is an indicator of whether a student lives in an urban("Urban") or rural("Rural") location.

# Seaborn has already been imported as sns and matplotlib.pyplot has been imported as plt. As a reminder, you can omit outliers in box plots by setting the sym parameter equal to an empty string("").

# Create a box plot with subgroups and omit the outliers
sns.catplot(x='internet', y='G3', data=student_data,
            kind='box', hue='location', sym='')


# Show plot
plt.show()

# Adjusting the whiskers
# In the lesson we saw that there are multiple ways to define the whiskers in a box plot. In this set of exercises, we'll continue to use the student_data dataset to compare the distribution of final grades ("G3") between students who are in a romantic relationship and those that are not. We'll use the "romantic" variable, which is a yes/no indicator of whether the student is in a romantic relationship.

# Let's create a box plot to look at this relationship and try different ways to define the whiskers.

# We've already imported Seaborn as sns and matplotlib.pyplot as plt.
# Set the whiskers to 0.5 * IQR
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box", whis=0.5)

# Show plot
plt.show()

# Customizing point plots
# Let's continue to look at data from students in secondary school, this time using a point plot to answer the question: does the quality of the student's family relationship influence the number of absences the student has in school? Here, we'll use the "famrel" variable, which describes the quality of a student's family relationship from 1 (very bad) to 5 (very good).

# As a reminder, to create a point plot, use the catplot() function and specify the name of the categorical variable to put on the x-axis(x=____), the name of the quantitative variable to summarize on the y-axis(y=____), the Pandas DataFrame to use(data=____), and the type of categorical plot(kind="point").

# We've already imported Seaborn as sns and matplotlib.pyplot as plt.

# Create a point plot of family relationship vs. absences
sns.catplot(x='famrel', y='absences', data=student_data, kind='point')


# Show plot
plt.show()

# Point plots with subgroups
# Let's continue exploring the dataset of students in secondary school. This time, we'll ask the question: is being in a romantic relationship associated with higher or lower school attendance? And does this association differ by which school the students attend? Let's find out using a point plot.

# We've already imported Seaborn as sns and matplotlib.pyplot as plt.

# Create a point plot with subgroups
sns.catplot(x='romantic', y='absences',
            data=student_data, kind='point', hue='school')


# Show plot
plt.show()


