# -*- coding:utf-8 -*-
# @Time   : 2022-02-23
# @Author : carl_DJ

from PyPDF4 import PdfFileReader, PdfFileWriter
import os


# 去除pdf的水印
def remove_pdf_watermark():
    pdf_dir = "../down.foodmate.net/"
    files = sorted(os.listdir(pdf_dir))
    for file in files:
        if ".pdf" in file:
            print(file)
            try:
                output = PdfFileWriter()
                pdffile = pdf_dir + file
                source = PdfFileReader(pdffile, 'rb')

                if source.getNumPages() < 3:
                    print("删除文件")
                    os.remove(pdffile)
                    continue

                page = source.getPage(0)
                if len(page.extractText()) <= 0:
                    print("删除文件")
                    os.remove(pdffile)
                    continue

                for i in range(source.getNumPages()):
                    page = source.getPage(i)

                    # if '/XObject' in page['/Resources'].keys():
                    #     page['/Resources']['/XObject'].clear()

                    if '/Font' in page['/Resources'].keys():
                        if '/Xi' + str(i * 2 + 1) in page['/Resources']['/Font'].keys():
                            page['/Resources']['/Font']['/Xi' + str(i * 2 + 1)].clear()

                        if '/Xi' + str(i * 2 + 3) in page['/Resources']['/Font'].keys():
                            page['/Resources']['/Font']['/Xi' + str(i * 2 + 3)].clear()

                    output.addPage(page)
                with open(pdffile, 'wb') as ouf:
                    output.write(ouf)
            except Exception as e:
                print(e)
                print("删除文件")
                os.remove(pdffile)


if __name__ == '__main__':
    remove_pdf_watermark()
