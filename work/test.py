import tabula
import os

# get all .pdf from the file path
# pdfs = [f for f in os.listdir('.') if f.endswith('.pdf')]
# print(pdfs)

path = os.getcwd()
print(path)

# for pdf in pdfs:
#     asd = pdf.split('.')[0]
#     print(asd)
#     # read pdf into DataFrame
#     df = tabula.read_pdf(pdf, pages='all')[0]
#     tabula.convert_into(pdf, asd+".csv", output_format="csv", pages='all')



def get_pdf_files(path):
    pdfs = [f for f in os.listdir(path+'/') if f.endswith('.pdf')]
    print(pdfs)
    return pdfs

def convert_pdf_to_csv(pdf:str, path:str):
    asd = pdf.split('.')[0]
    tabula.convert_into(path+'/'+pdf, path+'/'+asd+".csv", output_format="csv", pages='all')

def main():
#     # get current working directory
    path = os.getcwd()
#     # path = ''
    pdfs = get_pdf_files(path)
    # print(pdfs)
    for pdf in pdfs:
        convert_pdf_to_csv(pdf, path)

if __name__ == '__main__':
    main()