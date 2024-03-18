#i mport csv

# with open("weather_data.csv") as d:
    # data = csv.reader(d)
    # temperatures = []
    # for row in data:
        # if row[1] == "temp":
            # pass
        # else:
            # temperatures.append(int(row[1]))

    # print(temperatures)

import pandas as pd

data = pd.read_csv("weather_data.csv")
print(data)

data_list = data["temp"].to_list()
print(data_list)

# First way to calculate average
total = 0
for num in data_list:
    total += num

average = total / len(data_list)

# Second way to calculate average

average_1 = sum(data_list) / len(data_list)

# Third way to calculate average with Pandas

average_2 = data["temp"].mean() # I was trying data_list.mean() but this doesn't work because I haven´t noticed that
# this variable is to transform a piece of series to a list. For it to work it would have to be data_list = data["temp"]
print(f"Mean: {average_2}")

# Get the max value

max = data["temp"].max()
print(f"Max Value of temp: {max}")

# Get data in columns

    # print(data["condition"])
    # or
    # print(data.condition)

# Get data in Row

monday = data[data.temp == 12]
print(monday)

# Get maximum temp if you know the position
    #print(data.temp[6])
    #print(data.loc[6, "temp"])

#Conver temp from Monday Celsius to fahrenheit


temp_monday_fahrenheit = data.temp[0] * 1.8 + 32 # or (int(monday.temp))
print(temp_monday_fahrenheit)

# Create dataframe from scratch

cars = pd.DataFrame(
    {
        "Brand": [
            "Toyota",
            "Sea",
            "Tesla",
            "BBW"
        ],
        "Color": [
            "white",
            "blue",
            "Black",
            "Red"
        ],
        "Number_of_kms": [
            39.000,
            125.000,
            21.000,
            225.000
        ]
    }
)

cars.to_csv("cars_data.csv")
# print(cars.describe())






