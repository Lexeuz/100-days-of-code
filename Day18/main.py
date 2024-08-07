import colorgram

colors = colorgram.extract("image.jpg", 6)
color_list = []

for i in range(0, len(colors)):
    color_list.append(colors[i].rgb)

print(color_list[0])
