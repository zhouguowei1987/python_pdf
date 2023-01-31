# -*- coding:utf-8 -*-
# @Time   : 2022-02-23
# @Author : carl_DJ

from PyPDF4 import PdfFileReader, PdfFileWriter
from PyPDF4.pdf import ContentStream
from PyPDF4.generic import TextStringObject, NameObject
from PyPDF4.utils import b_
import os


# 去除pdf的水印
def remove_pdf_watermark():
    s = b'\x07\xfc'

    print(type(s))
    print(s)

    ss = str(s, 'utf8')
    print(ss)

    exit(1)

    pdf_dir = "../aaa/"
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

                # page0 = source.getPage(0)
                # page1 = source.getPage(1)
                # page2 = source.getPage(2)
                # print(page0)
                # print("=====")
                # print(page1)
                # print("=====")
                # print(page2)
                # print("=====")
                # exit(1)

                # page = source.getPage(1)
                # content_object = page["/Contents"].getObject()
                # content = ContentStream(content_object, source)
                # print(content.operations)
                # exit(1)

                for i in range(source.getNumPages()):
                    page = source.getPage(i)

                    # if '/XObject' in page['/Resources'].keys():
                    #     page['/Resources']['/XObject'].clear()

                    # if '/Font' in page['/Resources'].keys():
                    #     if '/Xi' + str(i * 2 + 1) in page['/Resources']['/Font'].keys():
                    #         page['/Resources']['/Font']['/Xi' + str(i * 2 + 1)].clear()
                    #
                    #     if '/Xi' + str(i * 2 + 3) in page['/Resources']['/Font'].keys():
                    #         page['/Resources']['/Font']['/Xi' + str(i * 2 + 3)].clear()

                    # if '/ExtGState' in page['/Resources'].keys():
                    #     page['/Resources']['/ExtGState'].clear()
                    # if '/Font' in page['/Resources'].keys():
                    #     page['/Contents'].clear()

                    content_object = page["/Contents"].getObject()
                    content = ContentStream(content_object, source)

                    for operands, operator in content.operations:
                        if operator == b_("Tj"):
                            text = operands[0]
                            print(text)
                            if isinstance(text, str) and text.startswith('全国团体标准信息平台'):
                                operands[0] = TextStringObject()

                    page.__setitem__(NameObject('/Contents'), content)
                    exit(1)
                    output.addPage(page)
                with open(pdffile, 'wb') as ouf:
                    output.write(ouf)
            except Exception as e:
                print(e)
                print("删除文件")
                os.remove(pdffile)


if __name__ == '__main__':
    remove_pdf_watermark()
