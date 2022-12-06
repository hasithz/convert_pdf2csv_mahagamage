from .csv_struct import CSV_STRUCT
import csv 
import os

def structure_csv_data(all_data:list, ):
    os.chdir(os.getcwd()+'/work/csvs/')
    csv_file_check = [f for f in os.listdir('.') if f.endswith('.csv')]
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
            csv_struct = CSV_STRUCT(temp)
            structured_list = csv_struct.set_Structure()
            # break
            if csv_struct.getname() in csv_file_check:
                with open(f'{csv_struct.getname()}.csv', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([])
                    writer.writerows(structured_list)
            else:
                with open(f'{csv_struct.getname()}.csv', 'w') as f:
                    writer = csv.writer(f)
                    writer.writerow(["name", "serial_No", "CAK_MT_WT", "MT_Applied_1", "No_Boxes", "Begin_Sail","Load_port", "Bkg_Dest_Port", "Carrier", "Voyage_Name", "Voyage_No", "Est_MT_WT", "Est_No_Boxes", "MT_Applied", "Applied_No_Boxes", "Shipped_Date", "Arrival_Date"])
                    writer.writerows(structured_list)

            # with open(f'{csv_struct.getname()}.csv', 'a+') as f:
            #     write = csv.writer(f)
            #     write.writerow([])
            #     write.writerows(structured_list)
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
