from django.shortcuts import render
from rest_framework.views import APIView
import os
import PyPDF2
from glob import glob
import sys
import bs4
# Create your views here.

try:
    os.mkdir('OutputFiles')
except Exception as ex:
    print((type(ex), sys.exc_info()[1], sys.exc_info()[2]))

try:
    os.mkdir('Templates')
except Exception as ex:
    print((type(ex), sys.exc_info()[1], sys.exc_info()[2]))

class MergeFilesIntoOne(APIView):
    def post(self, request):
        # folder_path = request.data['folder_path'][0]
        folder_path = request.data['folder_path']
        extension_type = request.data['extension_type']
        print('folder_path ---> ', folder_path)
        print('extension_type ---> ', extension_type)
        # try:
        #     os.mkdir('OutputFiles')
        # except Exception as ex:
        #     print((type(ex), sys.exc_info()[1], sys.exc_info()[2]))

        if extension_type == 'PDF':
            pdf_writer = PyPDF2.PdfFileWriter()

            with open('OutputFiles\\merged_file.pdf', mode='wb') as f1:
                for file_path in glob(os.path.join(folder_path, '**')):
                    print('file_path--->', file_path)
                    with open(file_path, mode='rb') as f:
                        # pdf_obj = PyPDF2.PdfFileReader(f.read())
                        pdf_reader = PyPDF2.PdfFileReader(f)
                        total_number_of_pages = pdf_reader.numPages
                        # print('The_total_number_of_pages_in_the_given_pdf_are ---> ', total_number_of_pages)
                        if total_number_of_pages:
                            for page_number in range(total_number_of_pages):
                                # pdf_content = pdf_obj.getPage(page_number).extractText()
                                # print('pdf_content ---> ', pdf_content)
                                pdf_content = pdf_reader.getPage(page_number)
                                # print('pdf_binary_content ---> ', pdf_content)
                                pdf_writer.addPage(pdf_content)
                                pdf_writer.write(f1)
        
        html_str = """
            <!doctype html>
            <html>
                <body>
                    %s merged successfully.
                </body>
            </html>
        """ % (extension_type + 's')

        # with open('Templates\\%s_template.html' % extension_type, mode='w') as f:
        #     f.write(bs4.BeautifulSoup(html_str, 'html.parser').prettify())
        with open(os.path.join('Templates', '%s_template.html' % extension_type), mode='w') as f:
            f.write(bs4.BeautifulSoup(html_str, 'html.parser').prettify())

        return render(request, '%s_template.html' % extension_type, {})
