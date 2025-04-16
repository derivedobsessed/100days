# import csv
#
# with open("weather_data.csv","r") as file:
#     weather_data = csv.reader(file)
#     temperatures = []
#     print(weather_data)
#     for row in weather_data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)
#

# import pandas
# data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
#
#
# def celsius_to_fahr(temp_celsius):
#     return temp_celsius*(9/5) + 32
#
# average_temp = data["temp"].mean()
# max_temp = data["temp"].max()
#
# monday = data[data.day == 'Monday']
# monday_temp = monday.temp
# monday_temp_fahr = celsius_to_fahr(monday_temp)
# print(monday_temp)
# print(monday_temp_fahr)

import pandas

data = pandas.read_csv("CP_squirrels.csv")
number_black = 0
number_grey = 0
number_cinnamon = 0

for color in data["Primary Fur Color"]:
    if color == "Black":
        number_black += 1
    elif color == "Gray":
        number_grey += 1
    elif color == "Cinnamon":
        number_cinnamon += 1

dictionary = {
              "Fur Color": ['black', 'grey', 'cinnamon'],
             "Number": [number_black, number_grey, number_cinnamon]
}

data_dict = pandas.DataFrame(dictionary)
data_dict.to_csv("number_squirrels.csv")



