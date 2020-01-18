import json
import matplotlib.pyplot as plt
import numpy as np
import os
import wbdata

# initial run to grab categories
# topic 19 = climate change
data_categories = wbdata.get_indicator(topic=19)

print(data_categories)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# USE:
# output is a Boolean - if true, print as well as return
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def list_categories(output=True):
    category_list = []
    for x in range(len(data_categories)):
        item = data_categories[x]
        if output:
            print(str(x)+".", item["name"], item["id"])
        category_list.append([x, item["name"], item["id"]])

    return category_list

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# USE:
# number is the number of a data set according to list_categories
# returns an object {id of data set: name of data set}
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def category(number):
    return {data_categories[number]["id"]:data_categories[number]["name"]}

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# USE:
# number is the number of a data set according to list_categories
# country is an array of countries to get data on, or "all"
# returns the unstacked data from worldbank
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def returnData(number, country=["USA"]):
    try:
        cat = category(number)
        df = wbdata.get_dataframe(cat, country=country, convert_date=False)
        df = df.unstack(level=0)
        return df
    except IndexError:
        print("no data on this!")

#for item in data_categories:
#    print(item["name"], item["id"])

# df = wbdata.get_dataframe({"EN.ATM.CO2E.GF.KT":"CO2 emissions from gaseous fuel consumption (kt)"}, country=["all"], convert_date=False)
#
# df = df.unstack(level=0)
#
# df.plot().get_figure().savefig('co2fromfuelukusa.png')
