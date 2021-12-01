import csv
import random


def join_lists(list1, list2):

    random.seed(0)

    returned_list = list1 + list2
    
    random.shuffle(returned_list)

    return returned_list


def clean_data(unclean_list):

    for element in unclean_list:
        pop_row = False
        for item in element:


            #Remove any rows with temperature outside normal range
            if float(item[1]) >= 75.0 and float(item[1]) <= 108.0:
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


def main():


    with open("cleaned_data.csv") as f:
        reader = csv.reader(f)

        df = reader

        next(reader)

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

