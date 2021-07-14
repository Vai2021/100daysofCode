# # with open("./weather_data.csv") as data:
# #     weather = data.readlines()
# #     print(weather)
# #
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data_f = csv.reader(data_file)
# #     temperature = []
# #     for row in data_f:
# #         if row[1] != "temp":
# #             temperature.append(int(row[1]))
# #     print(temperature)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])
#
# #temp_list = data["temp"].to_list()
# # l = len(temp_list)
# # sum =0
# # for d in temp_list:
# #     sum += d
# # avg = sum/l
# #
# # print(avg)
# max_t = data["temp"].max()
# print(data[data.temp == max_t])
import pandas

squirrel = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_s_count = len(squirrel[squirrel["Primary Fur Color"] == "Gray"])
Cinnamon_s_count = len(squirrel[squirrel["Primary Fur Color"] == "Cinnamon"])
black_s_count = len(squirrel[squirrel["Primary Fur Color"] == "Black"])

print(grey_s_count)
print(Cinnamon_s_count)
print(black_s_count)

data_dict = {
    "Fur Color": ["Grey", "Cinnamon", "Black"],
    "Count": [grey_s_count, Cinnamon_s_count, black_s_count ]
}

df = pandas.DataFrame(data_dict)
df.to_csv("my_squirrel_file.csv")