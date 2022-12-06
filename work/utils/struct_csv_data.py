from .csv_struct import CSV_STRUCT
import csv 

def structure_csv_data(all_data:list, ):
    splitted_data = []
    temp = []
    skip = False
    print(all_data[5][7])
    print(all_data[6][7])
    count = 0
    for data in all_data:
        if data[7] == 'Booking Total':
            temp.append(data)
            splitted_data.append(temp)
            # print(temp)
            structured_list = CSV_STRUCT(temp).set_Structure()
            # break
            with open(f'{count}.csv', 'a+') as f:
                write = csv.writer(f)
                write.writerows(structured_list)
                # file.close()
            temp = []
            count += 1
            # next(data)
            skip = True
            # check_null = 0
        else:
            if skip:
                skip = False
                continue
            else:
                temp.append(data)

    return splitted_data
