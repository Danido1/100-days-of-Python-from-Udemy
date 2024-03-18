#Central Park Squirrel Data Analysis
import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(data)

# Print the series column assigned to "Primary Fur Color"
series_color = data["Primary Fur Color"]
print(series_color)

# Take the colors and count each
colors = data.loc[:, "Primary Fur Color"].value_counts()
print(colors)

#Trnsform to a csv file

colors.to_csv("Squirrel_colour_data.csv")




