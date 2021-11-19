import csv
import sklearn.tree
import sklearn.model_selection
import sklearn.neighbors
import sklearn.neural_network
import random


def join_lists(list1, list2):
    """Joins lists, randomizes the observations, and pulls out the dependent variable into a list"""
    random.seed(0)
    #Generates combined list but randomized
    returned_list = list1 + list2
    
    random.shuffle(returned_list)

    y_data = []
    for i in range(0, len(returned_list)):

        y_data.append(returned_list[i][8])


    return returned_list, y_data


def clean_data(unclean_list):
    """This function is used to clear any data points that are abnormal, out of range, or blank"""
    for element in unclean_list:
        pop_row = False
        for item in element:


            #Remove any rows with temperature outside normal range
            if float(item[1]) >= 75 and float(item[1]) <= 108:
                pass
            else:
                pop_row = True
                break

            #Remove any rows with resprate outside normal range
            if float(item[3]) < 100 and float(item[3]) > 10:
                pass
            else:
                pop_row = True
                break

            #Remove any o2 state below 60
            if float(item[4]) > 60:
                pass
            else:
                pop_row = True
                break

            #Remove any pain that is not within normal range (0-10)
            if float(item[7]) <= 10 and float(item[7]) >= 0:
                pass
            else:
                pop_row = True
                break

        if pop_row == True:
            unclean_list.remove(element)
        pop_row = False

        cleaned_list = unclean_list

    return cleaned_list





def main():

    with open("D:\AI Lab\DHS_Hololens\BDA594-Group10\cleaned_data.csv", "r") as cleaned_data_file:

        reader = csv.reader(cleaned_data_file)

        #Skips the first row b/c it is the header row
        next(reader)
        #Split dataset into positive observations (acuity = 1) and negative observations (acuity = 0)
        mount_data_positive = []
        mount_data_negative = []


        #for loop to seperate out positive and negative observations
        for row in reader:
            
            if row[8] == "1":
                temp_list = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]]
                mount_data_positive.append(temp_list)
            elif row[8] == "0":
                temp_list = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]]
                mount_data_negative.append(temp_list)
            else:
                continue

        print("Total Positive: " + str(len(mount_data_positive)))
        print("Total Negative: " + str(len(mount_data_negative)))
        
        #Splitting data
        training_data_positive = []
        test_data_positive = []
        training_data_negative = []
        test_data_negative = []

        #Splitting 67/33 training vs test for positive observations (acuity = 1)
        for i in range(0, len(mount_data_positive)):
            if i < len(mount_data_positive) * .67:
                training_data_positive.append(mount_data_positive[i])
            else:
                test_data_positive.append(mount_data_positive[i])
        print("Total Training Points: " + str(len(training_data_positive)))
        print("Total Testing Points: " + str(len(test_data_positive)))

        #Splitting 67/33 training vs test for negative observations (acuity = 0)
        for i in range(0, len(mount_data_negative)):
            if i < len(mount_data_negative) * .67:
                training_data_negative.append(mount_data_negative[i])
            else:
                test_data_negative.append(mount_data_negative[i])

        joined_random_data_training, y_train = join_lists(training_data_positive, training_data_negative)

        joined_random_data_test, y_test_train = join_lists(test_data_positive, test_data_negative)


        





if __name__ == "__main__":
    main()
