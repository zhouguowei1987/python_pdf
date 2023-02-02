# -*- coding:utf-8 -*-
# @Time   : 2022-02-23
# @Author : carl_DJ

from PyPDF2 import PdfReader, PdfWriter
import os


# 去除pdf的水印
def remove_pdf_watermark():
    pdf_dir = "../www.ttbz.org.cn/"
    files = sorted(os.listdir(pdf_dir))
    for file in files:
        if ".pdf" in file:
            print(file)
            try:
                output = PdfWriter()
                pdffile = pdf_dir + file
                source = PdfReader(pdffile, 'rb')

                if len(source.pages) < 3:
                    print("删除文件")
                    os.remove(pdffile)
                    continue

                if len(source.pages[0].extract_text()) <= 0:
                    print("删除文件")
                    os.remove(pdffile)
                    continue

                for page_number in range(len(source.pages)):
                    page = source.pages[page_number]
                    # print(page['/Contents'])
                    try:
                        page['/Contents'].pop(2)
                    except Exception as e:
                        print(e)
                    output.add_page(page)
                with open(pdffile, 'wb') as ouf:
                    output.write(ouf)
            except Exception as e:
                print(e)
                print("删除文件")
                os.remove(pdffile)


if __name__ == '__main__':
    remove_pdf_watermark()
