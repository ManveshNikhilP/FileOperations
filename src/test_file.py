# import glob


# res_bin_data = b''
# # res_bin_data = ''
# for file in glob.glob('C:\\Fi**Op**\\sr**\\In**Fi**\\**'):
#     with open(file, mode='rb') as f:
#         res_bin_data += f.read()
#         # res_bin_data += ('\n' + f.read())
#         # res_bin_data = (b'\n' + f.read())
#         # res_bin_data += ('\n' + f.read())
#         # res_bin_data += ('\n' + str(f.read()))
#         # res_bin_data += str(f.read())


# with open(glob.glob('C:\\Fi**Op**\\sr**\\Out**Fi**\\**')[0], mode='rb') as f1:
#     actual_bin_data = f1.read()

# print(res_bin_data == actual_bin_data)

import glob
import PyPDF2
import sys


for file in glob.glob('C:\\Fi**Op**\\sr**\\In**Fi**\\**'):
    print('file ---> ', file)
    with open(file, mode='rb') as f:
        # pdf_reader_obj = PyPDF2.ReadPdfFile(f.read())
        # pdf_reader_obj = PyPDF2.PdfFileReader(f.read())
        # pdf_reader_obj = PyPDF2.PdfFileReader(f)
        try:
            pdf_reader_obj = PyPDF2.PdfFileReader(f)
            pdf_content = pdf_reader_obj.getPage(0).extractText()
            break
        except Exception as ex:
            print((type(ex), sys.exc_info()[1], sys.exc_info()[2]))
    # break
print('pdf_reader_obj ---> ', pdf_reader_obj)
print('pdf_content ---> ', pdf_content)
