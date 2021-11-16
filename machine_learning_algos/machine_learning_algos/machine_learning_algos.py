import csv
import sklearn.tree
import sklearn.model_selection
import sklearn.neighbors
import sklearn.neural_network
import random


def join_lists(list1, list2):

    random.seed(0)

    returned_list = list1 + list2
    
    random.shuffle(returned_list)

    return returned_list

    
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








if __name__ == "__main__":
    main()
