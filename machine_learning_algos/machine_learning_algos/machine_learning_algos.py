import csv
import random
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
import numpy as np
import joblib

def join_lists(list1, list2):
    """Joins lists, randomizes the observations, and pulls out the dependent variable into a list"""
    random.seed(0)
    #Generates combined list but randomized
    returned_list = list1 + list2

    random.shuffle(returned_list)

    y_data = []
    for i in range(0, len(returned_list)):

        y_data.append(returned_list[i][8])

    print("List joins complete")
    return returned_list, y_data


def clean_data(unclean_list):
    """This function is used to clear any data points that are abnormal, out of range, or blank"""
    for element in unclean_list:
        pop_row = False


        #Remove any rows with temperature outside normal range
        if float(element[0]) >= 75 and float(element[0]) <= 108:
            pass
        else:
            pop_row = True


        #Remove any rows with resprate outside normal range
        if float(element[2]) < 100 and float(element[2]) > 10:
            pass
        else:
            pop_row = True


        #Remove any o2 state below 60
        if float(element[3]) > 60:
            pass
        else:
            pop_row = True


        #Remove any pain that is not within normal range (0-10)
        if float(element[6]) <= 10 and float(element[6]) >= 0:
            pass
        else:
            pop_row = True


        if pop_row == True:
            print(element, "Popped")
            unclean_list.remove(element)
        pop_row = False

    cleaned_list = unclean_list
    print("List clean complete")
    return cleaned_list

def main():

    with open("D:\AI Lab\DHS_Hololens\BDA594-Group10\cleaned_data2.csv", "r") as cleaned_data_file:

        reader = csv.reader(cleaned_data_file)

        #Skips the first row b/c it is the header row
        next(reader)
        #Split dataset into positive observations (acuity = 1) and negative observations (acuity = 0)
        mount_data_positive = []
        mount_data_negative = []

        #for loop to seperate out positive and negative observations. Get rid of ?
        for row in reader:

            if row[7] == "1":
                temp_list = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]]
                mount_data_positive.append(temp_list)
            elif row[7] == "0":
                temp_list = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]]
                mount_data_negative.append(temp_list)
            else:
                continue

        print("Total Positive: " + str(len(mount_data_positive)))
        print("Total Negative: " + str(len(mount_data_negative)))

        #clean the data!
        cleaned_mount_data_positive = clean_data(mount_data_positive)
        cleaned_mount_data_negative = clean_data(mount_data_negative)

        all_cleaned_data = cleaned_mount_data_negative + cleaned_mount_data_positive
        with open("cleaned_data2_python.csv", "w") as file:

            writer = csv.writer(file)
            writer.writerow(["temperature", "heartrate", "resprate", "o2sat", "sbp", "dbp", "pain", "acuity"])
            for row in all_cleaned_data:

                writer.writerow(row)

        print("New file with outliers deleted was created")
        #split using sklearn

        x = []
        y = []

        for row in all_cleaned_data:
            temp_list_x = [row[0],row[1],row[2],row[3],row[4],row[5],row[6]]

            x.append(temp_list_x)
            y.append(row[7])

        x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = .67)
        #Splitting data
        #training_data_positive = []
        #test_data_positive = []
        #training_data_negative = []
        #test_data_negative = []

        #Splitting 67/33 training vs test for positive observations (acuity = 1)
        #for i in range(0, len(cleaned_mount_data_positive)):
            #if i < len(mount_data_positive) * .67:
                #training_data_positive.append(cleaned_mount_data_positive[i])
            #else:
                #test_data_positive.append(clenaed_mount_data_positive[i])
        #print("Total Training Points: " + str(len(training_data_positive)))
        #print("Total Testing Points: " + str(len(test_data_positive)))

        #Splitting 67/33 training vs test for negative observations (acuity = 0)
        #for i in range(0, len(cleaned_mount_data_negative)):
            #if i < len(cleaned_mount_data_negative) * .67:
                #training_data_negative.append(cleaned_mount_data_negative[i])
            #else:
                #test_data_negative.append(cleaned_mount_data_negative[i])


        clf = sklearn.neural_network.MLPClassifier()

        standard = StandardScaler()
        x_train_standard = standard.fit_transform(x_train)
        x_test_standard = standard.fit_transform(x_test)

        clf = clf.fit(x_train_standard, y_train)

        predict_train = clf.predict(x_train_standard)
        predict_test = clf.predict(x_test_standard)

        print(confusion_matrix(y_train, predict_train))
        print(classification_report(y_train, predict_train))

        joblib.dump(clf,"bda594_ML_NN.joblib")


        data = list(reader)

        # # create list of the dataset
        # df_list = []
        # for row in reader:
        #     df_list.append(row)
        #
        # print(df_list)

    clean_data(data)

if __name__ == "__main__":
    main()
