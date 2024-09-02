import pandas

# Colors: Cinnamon, Gray, Black
data = pandas.read_csv("2018_Census_Squirrel_Data.csv")
gray_squirrels = len(data[data['Primary Fur Color'] == "Gray"])
red_squirrels = len(data[data['Primary Fur Color'] == "Cinnamon"])
black_squirrels = len(data[data['Primary Fur Color'] == "Black"])

table = {"Fur Color": ["Gray", "Red", "Black"], "Count": [gray_squirrels, red_squirrels, black_squirrels]}
data_dict = pandas.DataFrame(table)
data_dict.to_csv("squirrel_count.csv")
