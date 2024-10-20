import csv

with open("weather_data.csv", "r") as data_file:
    data = csv.reader(data_file)
    next(data)
    temperatures = []
    for row in data:
        temperatures.append(int(row[1]))

    print(temperatures)
