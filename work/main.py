import tabula
import os

import csv
from xlsxwriter.workbook import Workbook

from utils.struct_csv_data import structure_csv_data
from utils.conv_pdf_to_csv import convert_pdf_to_csv

def structure_csv(path:str) -> None:
    path_csv = path+'/csv'
    csvs = [f for f in os.listdir(path_csv+'/') if f.endswith('.csv')]
    # print(csvs)
    for csv_file in csvs:
        with open(path_csv+'/'+csv_file, 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
            structure_csv_data(data)
            # print(data[6])
            # print(len(data[6]))

def get_pdf_files(path:str) -> list:
    pdfs = [f for f in os.listdir(path+'/') if f.endswith('.pdf')]
    print(pdfs)
    return pdfs

def main() -> None:
    path = os.getcwd()
    pdfs = get_pdf_files(path)
    for pdf in pdfs:
        convert_pdf_to_csv(pdf, path)
    structure_csv(path)


if __name__ == '__main__':
    main()