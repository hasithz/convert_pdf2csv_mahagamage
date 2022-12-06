import csv
import os


class CSV_STRUCT:
    def __init__(self, data:list):
        self.data = data
        self.length = len(data)
        self.items = []
        self.DEBUG = False
    
    def getname(self):
        self.name = ''
        for i in range(0, self.length):
            self.name += self.data[i][1] + " " 
            self.name = " ".join(self.name.split())
        # print(self.name)
        return self.name
        
    def get_serial_No(self):
        self.serial_No = ""
        for i in range(0, self.length):
            self.serial_No += self.data[i][0] + " "
            self.serial_No = " ".join(self.serial_No.split())
        # print(self.serial_No)
        return self.serial_No

    def get_CAK_MT_WT(self):
        self.CAK_MT_WT = self.data[1][2]
        # print(self.CAK_MT_WT)
        return self.CAK_MT_WT

    def get_MT_Applied_1(self):
        self.MT_Applied = self.data[1][3]
        # print(self.MT_Applied)
        return self.MT_Applied

    def get_No_Boxes(self):
        self.No_Boxes = self.data[1][4]
        # print(self.No_Boxes)
        return self.No_Boxes
    
    def get_Begin_Sail(self):
        self.Begin_Sail = self.data[1][5]
        # print(self.Begin_Sail)
        return self.Begin_Sail

    def get_End_Sail(self):
        self.End_Sail = self.data[1][6]
        # print(self.End_Sail)
        return self.End_Sail

    def get_Booking_No(self):
        self.Booking_No = []
        for i in range(0, self.length):
            if self.data[i][7] != '':
                self.Booking_No.append(self.data[i][7])
                self.items.append(i)
        # print(self.Booking_No[:-1])
        return self.Booking_No[:-1]
    
    def get_Load_port(self):
        self.Load_port = []
        Load_port_temp = ""
        if self.DEBUG:
            self.get_Booking_No()
        first = True
        count = 0
        # print(self.items)
        for i in self.items[:-1]:
            for j in range(i, self.items[count+1]):
                Load_port_temp += self.data[j][8] + " "
                Load_port_temp =" ".join(Load_port_temp.split())
            self.Load_port.append(Load_port_temp)
            Load_port_temp = ""
            count += 1
            # if j == i:
            #     break
            # print(self.Load_port)
        # print(self.Load_port)
        return self.Load_port

    def get_Bkg_Dest_Port(self):
        self.Bkg_Dest_Port = []
        Bkg_Dest_Port_temp = ""
        if self.DEBUG:
            self.get_Booking_No()
        first = True
        count = 0
        # print(self.items)
        for i in self.items[:-1]:
            for j in range(i, self.items[count+1]):
                Bkg_Dest_Port_temp += self.data[j][9] + " "
                Bkg_Dest_Port_temp =" ".join(Bkg_Dest_Port_temp.split())
            self.Bkg_Dest_Port.append(Bkg_Dest_Port_temp)
            Bkg_Dest_Port_temp = ""
            count += 1
            # if j == i:
            #     break
            # print(self.Load_port)
        # print(self.Bkg_Dest_Port)
        return self.Bkg_Dest_Port

    def get_Carrier(self):
        self.Carrier = []
        Carrier_temp = ""
        if self.DEBUG:
            self.get_Booking_No()
        first = True
        count = 0
        # print(self.items)
        for i in self.items[:-1]:
            for j in range(i, self.items[count+1]):
                Carrier_temp += self.data[j][10] + " "
                Carrier_temp =" ".join(Carrier_temp.split())
            self.Carrier.append(Carrier_temp)
            Carrier_temp = ""
            count += 1
            # if j == i:
            #     break
            # print(self.Load_port)
        # print(self.Carrier)
        return self.Carrier

    def get_Voyage_Name(self):
        self.Voyage_Name = []
        Voyage_Name_temp = ""
        if self.DEBUG:
            self.get_Booking_No()
        first = True
        count = 0
        # print(self.items)
        for i in self.items[:-1]:
            for j in range(i, self.items[count+1]):
                Voyage_Name_temp += self.data[j][11] + " "
                Voyage_Name_temp =" ".join(Voyage_Name_temp.split())
            self.Voyage_Name.append(Voyage_Name_temp)
            Voyage_Name_temp = ""
            count += 1
            # if j == i:
            #     break
            # print(self.Load_port)
        # print(self.Voyage_Name)
        return self.Voyage_Name

    def get_Voyage_No(self):
        self.Voyage_No = []
        Voyage_No_temp = ""
        if self.DEBUG:
            self.get_Booking_No()
        first = True
        count = 0
        # print(self.items)
        for i in self.items[:-1]:
            for j in range(i, self.items[count+1]):
                Voyage_No_temp += self.data[j][12] + " "
                Voyage_No_temp = " ".join(Voyage_No_temp.split())
            self.Voyage_No.append(Voyage_No_temp)
            Voyage_No_temp = ""
            count += 1
            # if j == i:
            #     break
            # print(self.Load_port)
        # print(self.Voyage_No)
        return self.Voyage_No

    def get_Est_MT_WT(self):
        self.Est_MT_WT = []
        if self.DEBUG:
            self.get_Booking_No()
        for i in self.items[:-1]:
            self.Est_MT_WT.append(self.data[i][13])
        
        # print(self.Est_MT_WT)
        return self.Est_MT_WT

    def get_Est_No_Boxes(self):
        self.Est_No_Boxes = []
        if self.DEBUG:
            self.get_Booking_No()
        for i in self.items[:-1]:
            self.Est_No_Boxes.append(self.data[i][14])
        
        # print(self.Est_No_Boxes)
        return self.Est_No_Boxes

    def get_MT_Applied(self):
        self.MT_Applied = []
        if self.DEBUG:
            self.get_Booking_No()
        for i in self.items[:-1]:
            self.MT_Applied.append(self.data[i][15])
        
        # print(self.MT_Applied)
        return self.MT_Applied

    def get_Applied_No_Boxes(self):
        self.Applied_No_Boxes = []
        if self.DEBUG:
            self.get_Booking_No()
        for i in self.items[:-1]:
            self.Applied_No_Boxes.append(self.data[i][16])
        
        # print(self.Applied_No_Boxes)
        return self.Applied_No_Boxes

    def get_Shipped_Date(self):
        self.Shipped_Date = []
        if self.DEBUG:
            self.get_Booking_No()
        for i in self.items[:-1]:
            self.Shipped_Date.append(self.data[i][17])
        
        # print(self.Shipped_Date)
        return self.Shipped_Date

    def get_Arrival_Date(self):
        self.Arrival_Date = []
        if self.DEBUG:
            self.get_Booking_No()
        for i in self.items[:-1]:
            self.Arrival_Date.append(self.data[i][18])
        
        # print(self.Arrival_Date)
        return self.Arrival_Date

    def set_Structure(self) -> list:
        self.structured_list = []
        self.get_Booking_No()
        for i in range(0,len(self.items[:-1])):
            self.structured_list.append([
                self.getname(), self.get_serial_No(), self.get_CAK_MT_WT(), self.get_MT_Applied_1(), self.get_No_Boxes(), self.get_Begin_Sail(), 
                self.get_Load_port()[i], self.get_Bkg_Dest_Port()[i], self.get_Carrier()[i], self.get_Voyage_Name()[i], self.get_Voyage_No()[i], 
                self.get_Est_MT_WT()[i], self.get_Est_No_Boxes()[i], self.get_MT_Applied()[i], self.get_Applied_No_Boxes()[i], self.get_Shipped_Date()[i], 
                self.get_Arrival_Date()[i]
            ])
        print(self.structured_list)
        # print(self.get_MT_Applied_1())
        return self.structured_list