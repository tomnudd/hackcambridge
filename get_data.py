import json
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import wbdata

# initial run to grab categories
# topic 19 = climate change
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

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# USE:
# number is the number of a data set according to list_categories
# country is an array of countries to get data on, or "all"
# returns the unstacked data from worldbankd
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def return_data(number, country=["USA"]):
    try:
        cat = category(number)
        df = wbdata.get_dataframe(cat, country=country, convert_date=False)
        df = df.unstack(level=0)
        return df
    except IndexError:
        print("no data on this!")

# for the sake of Tom's eyes
def plot_data(df):
    df.plot()
    ax = plt.gca()
    plt.xticks(rotation=60)
    plt.title("ok")
    plt.xlabel("Date")
    plt.ylabel("test")
    labels = [item.get_text() for item in ax.get_xticklabels()]
    for x in range(len(labels)):
        new = labels[x][-5:-1]
        if len(new) > 0:
            labels[x] = new
    ax.set_xticklabels(labels)
    plt.tight_layout()
    plt.savefig("testplot")

def to_csv(df):
    df = pd.DataFrame(df)
    df.to_csv("temp_file.csv")
    rd = pd.read_csv("temp_file.csv", usecols=["date", "0"])
    rd.dropna(inplace=True)
    return rd

def generate(number, filename):
    item = return_data(number)
    file = to_csv(item)
    cat = list(category(number).values())
    file = file.rename({'0': cat[0]}, axis=1)
    file.to_csv(str(filename) + ".csv")

generate(13, "yeeting")

#for item in data_categories:
#    print(item["name"], item["id"])

# df = wbdata.get_dataframe({"EN.ATM.CO2E.GF.KT":"CO2 emissions from gaseous fuel consumption (kt)"}, country=["all"], convert_date=False)
#
# df = df.unstack(level=0)
#
# df.plot().get_figure().savefig('co2fromfuelukusa.png')
