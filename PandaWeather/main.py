# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperature = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperature.append(int(row[1]))
# #     print(temperature)
#
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# maxi = data["temp"].max()
# print(maxi)
#
# # Get data in columns
# print(data.condition)
# print(data["condition"])
#
# # Get data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# # Create a pandas Dataframe
# data_dictionary = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# new_dataframe = pandas.DataFrame(data_dictionary)
# new_dataframe.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

colors = ["Gray", "Cinnamon", "Black"]
count = []
for color in colors:
    squirrels = len(data[data["Primary Fur Color"] == color])
    count.append(squirrels)
print(count)

data_dict = {
    "Fur Color": colors,
    "Count": count
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrels_count.csv")

