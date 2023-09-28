import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(row[1])
#     print(temperature)


import pandas

#data = pandas.read_csv("weather_data.csv")
# 2print(data)
# data_dict = data.to_dict("series")
# print(data_dict)
#print(pandas.DataFrame({'day': [data.day], 'temp': [data.temp]}))

# print(data[data.temp == data["temp"].max()])

# print(data[data.day == "Monday"])
# print(data.temp)
# data.temp = (data.temp * 9/5) + 32
# print(data.temp)
# print(data)

# monday = data[data.day == "Monday"]
# print(monday.condition)

#Create a dataframe from scratch
# data_dict = {
#     "students": ["Ania", "James", "Angela"],
#     "scores": [76, 56, 53]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels)
print(red_squirrels)
print(black_squirrels)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels, red_squirrels, black_squirrels]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
