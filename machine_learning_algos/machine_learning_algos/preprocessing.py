from machine_learning_algos import *
import csv
import pandas as pd

#dataset = pd.read_csv(r'/Users/marrionmac/PycharmProjects/cleaned_data.csv')

with open("cleaned_data.csv", "r") as cleaned_data_file:
    reader = csv.reader(cleaned_data_file)
    i = 10
    for i in reader[10]:
        print(i)
        if i == 10:
            break



