dataset_one = [50, 10, 4, -3, 4, -20, 2]
#Sorted dataset_one: [-20, -3, 2, 4, 4, 10, 50]

dataset_two = [24, 20, 1, 45, -15, 40]
# dataset_two = [-15, 1, 20, 24, 40, 45]
dataset_one_q2 = 4
dataset_two_q2 = 22
#Define the first and third quartile of both datasets here:
dataset_one_q1 = (-3 + 2) / 2
dataset_one_q3 = (4 + 10) / 2

dataset_two_q1 = 1
dataset_two_q3 = 40

#Ignore the code below here:
try:
  print("The first quartile of dataset one is " + str(dataset_one_q1))
except NameError:
  print("You haven't defined dataset_one_q1")
try:
  print("The second quartile of dataset one is " + str(dataset_one_q2))
except NameError:
  print("You haven't defined dataset_one_q2")
try:
  print("The third quartile of dataset one is " + str(dataset_one_q3) + "\n")
except NameError:
  print("You haven't defined dataset_one_q3\n")
try:
  print("The first quartile of dataset two is " + str(dataset_two_q1))
except NameError:
  print("You haven't defined dataset_two_q1")
try:
  print("The second quartile of dataset two is " + str(dataset_two_q2))
except NameError:
  print("You haven't defined dataset_two_q2")
try:
  print("The third quartile of dataset two is " + str(dataset_two_q3))
except NameError:
  print("You haven't defined dataset_two_q3")
