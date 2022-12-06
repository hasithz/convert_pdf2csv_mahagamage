import os
import tabula

def check_dir(path:str) -> bool:
    if not os.path.exists(path):
        os.makedirs(path)
        return True
    return False

def convert_pdf_to_csv(pdf:str, path:str) -> None:
    name_csv = pdf.split('.')[0]
    check_dir(path+'/csv')
    tabula.convert_into(path+'/'+pdf, path+'/csv/'+name_csv+".csv", output_format="csv", pages='all')
