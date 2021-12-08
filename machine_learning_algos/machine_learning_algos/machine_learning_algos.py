import csv
<<<<<<< HEAD
=======
import sklearn.tree
import sklearn.model_selection
import sklearn.neighbors
import sklearn.neural_network
>>>>>>> 0a8ec474836a2151c1269c919ba45458ebf0c7b0
import random
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
<<<<<<< HEAD
import numpy as np
import joblib
=======
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import joblib
from sklearn import metrics
from sklearn.metrics import mean_squared_error
from math import sqrt
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
>>>>>>> 0a8ec474836a2151c1269c919ba45458ebf0c7b0

def join_lists(list1, list2):
    """Joins lists, randomizes the observations, and pulls out the dependent variable into a list"""
    random.seed(0)
    #Generates combined list but randomized
    returned_list = list1 + list2
<<<<<<< HEAD

=======
    
>>>>>>> 0a8ec474836a2151c1269c919ba45458ebf0c7b0
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
<<<<<<< HEAD

=======
    
>>>>>>> 0a8ec474836a2151c1269c919ba45458ebf0c7b0

        #Remove any rows with temperature outside normal range
        if float(element[0]) >= 75 and float(element[0]) <= 108:
            pass
        else:
            pop_row = True
<<<<<<< HEAD

=======
            
>>>>>>> 0a8ec474836a2151c1269c919ba45458ebf0c7b0

        #Remove any rows with resprate outside normal range
        if float(element[2]) < 100 and float(element[2]) > 10:
            pass
        else:
            pop_row = True
<<<<<<< HEAD

=======
            
>>>>>>> 0a8ec474836a2151c1269c919ba45458ebf0c7b0

        #Remove any o2 state below 60
        if float(element[3]) > 60:
            pass
        else:
            pop_row = True
<<<<<<< HEAD

=======
            
>>>>>>> 0a8ec474836a2151c1269c919ba45458ebf0c7b0

        #Remove any pain that is not within normal range (0-10)
        if float(element[6]) <= 10 and float(element[6]) >= 0:
            pass
        else:
            pop_row = True
<<<<<<< HEAD

=======
            
>>>>>>> 0a8ec474836a2151c1269c919ba45458ebf0c7b0

        if pop_row == True:
            print(element, "Popped")
            unclean_list.remove(element)
        pop_row = False
<<<<<<< HEAD

=======
        
>>>>>>> 0a8ec474836a2151c1269c919ba45458ebf0c7b0
    cleaned_list = unclean_list
    print("List clean complete")
    return cleaned_list

<<<<<<< HEAD
def main():

    with open("D:\AI Lab\DHS_Hololens\BDA594-Group10\cleaned_data2.csv", "r") as cleaned_data_file:
=======




def main():

    with open("cleaned_data2.csv", "r") as cleaned_data_file:
>>>>>>> 0a8ec474836a2151c1269c919ba45458ebf0c7b0

        reader = csv.reader(cleaned_data_file)

        #Skips the first row b/c it is the header row
        next(reader)
        #Split dataset into positive observations (acuity = 1) and negative observations (acuity = 0)
        mount_data_positive = []
        mount_data_negative = []

        #for loop to seperate out positive and negative observations. Get rid of ?
        for row in reader:
<<<<<<< HEAD

=======
            
>>>>>>> 0a8ec474836a2151c1269c919ba45458ebf0c7b0
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
<<<<<<< HEAD
        cleaned_mount_data_positive = clean_data(mount_data_positive)
        cleaned_mount_data_negative = clean_data(mount_data_negative)

        all_cleaned_data = cleaned_mount_data_negative + cleaned_mount_data_positive
        with open("cleaned_data2_python.csv", "w") as file:
=======
        #cleaned_mount_data_positive = clean_data(mount_data_positive)
        #cleaned_mount_data_negative = clean_data(mount_data_negative)

        all_cleaned_data = mount_data_negative + mount_data_positive
        with open("cleaned_data2_python.csv", "w", newline="") as file:
>>>>>>> 0a8ec474836a2151c1269c919ba45458ebf0c7b0

            writer = csv.writer(file)
            writer.writerow(["temperature", "heartrate", "resprate", "o2sat", "sbp", "dbp", "pain", "acuity"])
            for row in all_cleaned_data:

                writer.writerow(row)

        print("New file with outliers deleted was created")
        #split using sklearn
<<<<<<< HEAD

=======
        
>>>>>>> 0a8ec474836a2151c1269c919ba45458ebf0c7b0
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
<<<<<<< HEAD


        clf = sklearn.neural_network.MLPClassifier()

        standard = StandardScaler()
        x_train_standard = standard.fit_transform(x_train)
        x_test_standard = standard.fit_transform(x_test)

        clf = clf.fit(x_train_standard, y_train)

        predict_train = clf.predict(x_train_standard)
        predict_test = clf.predict(x_test_standard)
=======
        standard = StandardScaler()
        x_train_standard = standard.fit_transform(x_train)
        x_test_standard = standard.fit_transform(x_test)
        if not joblib:
            
            clf = sklearn.neural_network.MLPClassifier()

            clf = clf.fit(x_train_standard, y_train)

            predict_train = clf.predict(x_train_standard)
            predict_test = clf.predict(x_test_standard)

            joblib.dump(clf,"bda594_ML_NN.joblib")

        else:

            clf = joblib.load("bda594_ML_NN.joblib")

            predict_train = clf.predict(x_train_standard)
            predict_test = clf.predict(x_test_standard)
>>>>>>> 0a8ec474836a2151c1269c919ba45458ebf0c7b0

        print(confusion_matrix(y_train, predict_train))
        print(classification_report(y_train, predict_train))

<<<<<<< HEAD
        joblib.dump(clf,"bda594_ML_NN.joblib")


        data = list(reader)

        # # create list of the dataset
        # df_list = []
        # for row in reader:
        #     df_list.append(row)
        #
        # print(df_list)

    clean_data(data)
=======
        x_values = []
        y_values_knn = []
        y_values_rmse = []

        for i in range(1,100, 2):
            clf_knn = KNeighborsClassifier(i)
            
            clf_knn = clf_knn.fit(x_train_standard, y_train)
        
            y_pred = clf_knn.predict(x_test_standard)
            
            y_values_knn.append(metrics.accuracy_score(y_test, y_pred))
            
            print("Accruacy:", metrics.accuracy_score(y_test, y_pred))
            
            train_preds = clf_knn.predict(x_train_standard)
            print(confusion_matrix(y_train, train_preds))
            mse = mean_squared_error(y_train, train_preds)

            rmse = sqrt(mse)

            y_values_rmse.append(rmse)
            
            print("RMSE:", rmse)

            x_values.append(i)

        print("KNN Accruacy values:\n",y_values_knn)
        print("RMSE values:\n",y_values_rmse)

        plt.plot(x_values, y_values_knn, c = "blue", label = "KNN Accuracy")
        plt.plot(x_values, y_values_rmse, c = "red", label = "RMSE")
        plt.legend(loc = "upper left")
        plt.xlabel("KNN Iteration")
        plt.ylabel("KNN Accuracy/RMSE Score")
        plt.show()



>>>>>>> 0a8ec474836a2151c1269c919ba45458ebf0c7b0

if __name__ == "__main__":
    main()
