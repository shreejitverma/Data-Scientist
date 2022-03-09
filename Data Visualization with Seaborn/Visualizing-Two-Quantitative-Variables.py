# Creating subplots with col and row
# We've seen in prior exercises that students with more absences("absences") tend to have lower final grades("G3"). Does this relationship hold regardless of how much time students study each week?

# To answer this, we'll look at the relationship between the number of absences that a student has in school and their final grade in the course, creating separate subplots based on each student's weekly study time("study_time").

# Seaborn has been imported as sns and matplotlib.pyplot has been imported as plt.

# Change to use relplot() instead of scatterplot()
sns.relplot(x="absences", y="G3",
            data=student_data, kind='scatter')

# Show plot
plt.show()

# Creating two-factor subplots
# Let's continue looking at the student_data dataset of students in secondary school. Here, we want to answer the following question: does a student's first semester grade("G1") tend to correlate with their final grade("G3")?

# There are many aspects of a student's life that could result in a higher or lower final grade in the class. For example, some students receive extra educational support from their school ("schoolsup") or from their family ("famsup"), which could result in higher grades. Let's try to control for these two factors by creating subplots based on whether the student received extra educational support from their school or family.

# Seaborn has been imported as sns and matplotlib.pyplot has been imported as plt.
# Create a scatter plot of G1 vs. G3
sns.relplot(x='G1', y='G3', data=student_data, kind="scatter")


# Show plot
plt.show()

# Changing the size of scatter plot points
# In this exercise, we'll explore Seaborn's mpg dataset, which contains one row per car model and includes information such as the year the car was made, the number of miles per gallon("M.P.G.") it achieves, the power of its engine(measured in "horsepower"), and its country of origin.

# What is the relationship between the power of a car's engine ("horsepower") and its fuel efficiency ("mpg")? And how does this relationship vary by the number of cylinders ("cylinders") the car has? Let's find out.

# Let's continue to use relplot() instead of scatterplot() since it offers more flexibility.

# Import Matplotlib and Seaborn

# Create scatter plot of horsepower vs. mpg
sns.relplot(x='horsepower', y='mpg', data=mpg,
            size='cylinders', kind='scatter')


# Show plot
plt.show()

# Changing the style of scatter plot points
# Let's continue exploring Seaborn's mpg dataset by looking at the relationship between how fast a car can accelerate("acceleration") and its fuel efficiency("mpg"). Do these properties vary by country of origin("origin")?

# Note that the "acceleration" variable is the time to accelerate from 0 to 60 miles per hour, in seconds. Higher values indicate slower acceleration.

# Import Matplotlib and Seaborn

# Create a scatter plot of acceleration vs. mpg
sns.relplot(x='acceleration', y='mpg', data=mpg,
            kind='scatter', style='origin', hue='origin')


# Show plot
plt.show()

# Interpreting line plots
# In this exercise, we'll continue to explore Seaborn's mpg dataset, which contains one row per car model and includes information such as the year the car was made, its fuel efficiency(measured in "miles per gallon" or "M.P.G"), and its country of origin(USA, Europe, or Japan).

# How has the average miles per gallon achieved by these cars changed over time? Let's use line plots to find out!
# Import Matplotlib and Seaborn

# Create line plot
sns.relplot(x='model_year', y='mpg', data=mpg, kind='line')


# Show plot
plt.show()

# Visualizing standard deviation with line plots
# In the last exercise, we looked at how the average miles per gallon achieved by cars has changed over time. Now let's use a line plot to visualize how the distribution of miles per gallon has changed over time.

# Seaborn has been imported as sns and matplotlib.pyplot has been imported as plt.

# Make the shaded area show the standard deviation
sns.relplot(x="model_year", y="mpg",
            data=mpg, kind="line", ci='sd')

# Show plot
plt.show()

# Plotting subgroups in line plots
# Let's continue to look at the mpg dataset. We've seen that the average miles per gallon for cars has increased over time, but how has the average horsepower for cars changed over time? And does this trend differ by country of origin?

# Import Matplotlib and Seaborn

# Create line plot of model year vs. horsepower
sns.relplot(x='model_year', y='horsepower', data=mpg, kind='line', ci=None)


# Show plot
plt.show()
