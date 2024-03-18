# The You can first the exercise in the coding rooms from the course 100 days of code.

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:

#(temp_c * 9/5) + 32 = temp_f

new_dic = {key:value * 9/5 + 32 for (key, value) in weather_c.items()}

print(new_dic)
