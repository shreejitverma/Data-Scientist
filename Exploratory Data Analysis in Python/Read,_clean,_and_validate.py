# Read, clean, and validate!!
# The first step of almost any data project is to read the data, check for errors and special cases, and prepare data for analysis. This is exactly what you'll do in this chapter, while working with a dataset obtained from the National Survey of Family Growth.

# Exploring the NSFG data
# To get the number of rows and columns in a DataFrame, you can read its shape attribute.

# To get the column names, you can read the columns attribute. The result is an Index, which is a Pandas data structure that is similar to a list. Let's begin exploring the NSFG data! It has been pre-loaded for you into a DataFrame called nsfg.

# Display the number of rows and columns


# Clean a variable
# In the NSFG dataset, the variable 'nbrnaliv' records the number of babies born alive at the end of a pregnancy.

# If you use .value_counts() to view the responses, you'll see that the value 8 appears once, and if you consult the codebook, you'll see that this value indicates that the respondent refused to answer the question.

# Your job in this exercise is to replace this value with np.nan. Recall from the video how Allen replaced the values 98 and 99 in the ounces column using the .replace() method:

# ounces.replace([98, 99], np.nan, inplace=True)


# Replace the value 8 with NaN
nsfg['____'].____(____, ____, ____)

# Print the values and their frequencies
print(nsfg['____'].____())


# Compute a variable
# For each pregnancy in the NSFG dataset, the variable 'agecon' encodes the respondent's age at conception, and 'agepreg' the respondent's age at the end of the pregnancy.

# Both variables are recorded as integers with two implicit decimal places, so the value 2575 means that the respondent's age was 25.75.

# Select the columns and divide by 100
agecon = ____
agepreg = ____



# Make a histogram
# Histograms are one of the most useful tools in exploratory data analysis. They quickly give you an overview of the distribution of a variable, that is, what values the variable can have, and how many times each value appears.

# As we saw in a previous exercise, the NSFG dataset includes a variable 'agecon' that records age at conception for each pregnancy. Here, you're going to plot a histogram of this variable. You'll use the bins parameter that you saw in the video, and also a new parameter - histtype - which you can read more about here in the matplotlib documentation. Learning how to read documentation is an essential skill. If you want to learn more about matplotlib, you can check out DataCamp's Introduction to Matplotlib course.

# Plot the histogram


# Label the axes
plt.xlabel('Age at conception')
plt.ylabel('Number of pregnancies')

# Show the figure
plt.show()


# Compute birth weight
# Now let's pull together the steps in this chapter to compute the average birth weight for full-term babies.

# I've provided a function, resample_rows_weighted, that takes the NSFG data and resamples it using the sampling weights in wgt2013_2015. The result is a sample that is representative of the U.S. population.

# Then I extract birthwgt_lb1 and birthwgt_oz1, replace special codes with NaN, and compute total birth weight in pounds, birth_weight.

# # Resample the data
# nsfg = resample_rows_weighted(nsfg, 'wgt2013_2015')

# # Clean the weight variables
# pounds = nsfg['birthwgt_lb1'].replace([98, 99], np.nan)
# ounces = nsfg['birthwgt_oz1'].replace([98, 99], np.nan)

# # Compute total birth weight
# birth_weight = pounds + ounces/16


# Create a Boolean Series for full-term babies
full_term = ____

# Select the weights of full-term babies
full_term_weight = ____

# Compute the mean weight of full-term babies
print(____)


# Filter
# In the previous exercise, you computed the mean birth weight for full-term babies; you filtered out preterm babies because their distribution of weight is different.

# The distribution of weight is also different for multiple births, like twins and triplets. In this exercise, you'll filter them out, too, and see what effect it has on the mean.


# Filter full-term babies
full_term = nsfg['prglngth'] >= 37

# Filter single births
single = ____

# Compute birth weight for single full-term babies
single_full_term_weight = birth_weight[____ & ____]
print('Single full-term mean:', single_full_term_weight.mean())

# Compute birth weight for multiple full-term babies
mult_full_term_weight = birth_weight[____ & ____]
print('Multiple full-term mean:', mult_full_term_weight.mean())



