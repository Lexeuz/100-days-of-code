# with open("weather_data.csv") as weather_file:
#     data = weather_file.readlines()

# print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
# print(temperatures)
# To manipulate external data pandas is needed.
import pandas

# data = pandas.read_csv('weather_data.csv')
# print(type(data))
# print(data['temp'])

# data_dict = data.to_dict()
# print(data_dict)
#
# data_temp = data['temp'].tolist()
# print(data_temp)
#
# print(round(sum(data_temp) / len(data_temp)))
#
# print(max(data_temp))
# print(data['temp'].max())
#
# print(data.day)

# # How to get data from a specific section.
# print(data[data.day == 'Monday'])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == 'Monday']
# print((monday.temp * 1.8) + 32)

# Create a dataframe from scratch.
data_dict = {
    "students": ["Amy", "James", "Alexander"],
    "Scores": [76, 56, 100]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
