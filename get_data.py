import json
import matplotlib.pyplot as plt
import numpy as np
import os
import wbdata

# initial run to grab categories
data_categories = wbdata.get_indicator(topic=19)

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

#for item in data_categories:
#    print(item["name"], item["id"])

# df = wbdata.get_dataframe({"EN.ATM.CO2E.GF.KT":"CO2 emissions from gaseous fuel consumption (kt)"}, country=["all"], convert_date=False)
#
# df = df.unstack(level=0)
#
# df.plot().get_figure().savefig('co2fromfuelukusa.png')
