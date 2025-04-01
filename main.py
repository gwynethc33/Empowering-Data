# This code is written in python
# The pandas library is used for data processing and to read data files
import pandas as pd 
#The matplotlib library is used to plot histograms and scatter plots
import matplotlib.pyplot as plt
# The GWCutilities has functions to help format data printed to the console
import GWCutilities as util

# Read a comma separated values (CSV) files into a variable
# as a pandas DataFrame
lwd=pd.read_csv("livwell135.csv")

# Print out the number of rows and columns
print(lwd.shape)

#  basic colors:
# 'blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'white'

#see countries
listOfcountries = lwd["country_name"].unique()
#print(util.vformat_list(listOfcountries))

#filtering data
oneCountryBooleanList = lwd["country_name"] == "Cambodia"
oneCountryData = lwd.loc[oneCountryBooleanList]


print("In Cambodia, the average age of marriage for women in Cambodia has been low as young women feel a pressure to conform to cultural norms")

input("Press return to continue.\n")

print("Over the years, Cambodia’s civilization absorbed cultural influences from India and China.\n")

print("Cambodia’s culture is based on the traditional beliefs of its people. Particulalry, Buddhism.")

input("Press return to continue.\n")

print("Since 1993, Cambodia has recognized Theravada Buddhism as its religion.\n")

print("Theravada Buddhism is a religion that influences many customs especially marriage, promoting consistency with the tradition contributing to the stable average age for marriage.\n")

input("Press return to show the scatter plot\n")

#filter by year
oneCountryData = oneCountryData[(oneCountryData["year"] >= 2000) & (oneCountryData["year"] <= 2020)]

#remove rows with missing values
oneCountryData = oneCountryData.dropna(subset=["DM_age_marr_mean"])

# Check if the new column contains numerical data
#print(oneCountryData["DM_age_marr_mean"])


# create a scatter plot
plt.figure(figsize=(10,6))
plt.scatter(oneCountryData["year"], oneCountryData["DM_age_marr_mean"], color="red")

# add a title to the plot
plt.title("Female Average Age at Marriage in Cambodia Over Time")

#Label the x-axis
plt.xlabel("Year")

# label the y-axis
plt.ylabel("Female Average Age at Marriage")

plt.ylim(0,100)

print("Close the graph by pressing the 'X' in the top right corner.\n")

# show the plot
plt.show()

      
print("Based on these findings, my proposed research question is:\n")

print("In what ways does the teaching of Theravada Buddhism still affect when people get married?")