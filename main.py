# -*- coding:utf-8 -*-
# @Time   : 2022-02-23
# @Author : carl_DJ

from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import ByteStringObject, TextStringObject
import re
import os


def replace_text(content, replacements=None):
    if replacements is None:
        replacements = dict()
    lines = content.splitlines()

    result = ""
    in_text = False

    for line in lines:
        if line == "BT":
            in_text = True

        elif line == "ET":
            in_text = False

        elif in_text:
            cmd = line[-2:]
            if cmd.lower() == 'tj':
                replaced_line = line
                for k, v in replacements.items():
                    replaced_line = replaced_line.replace(k, v)
                result += replaced_line + "\n"
            else:
                result += line + "\n"
            continue

        result += line + "\n"

    return result


def process_data(stream_obj, replacements):
    print(type(stream_obj))
    data = stream_obj.get_data()
    decoded_data = data.decode('utf-8')

    replaced_data = replace_text(decoded_data, replacements)

    encoded_data = replaced_data.encode('utf-8')
    if stream_obj.decoded_self is not None:
        stream_obj.decoded_self.set_data(encoded_data)
    else:
        stream_obj.set_data(encoded_data)


# 去除pdf的水印
def remove_pdf_watermark():
    pdf_dir = "../aaa/"
    replacements = {"Quantifying": "111"}
    files = sorted(os.listdir(pdf_dir))
    for file in files:
        if ".pdf" in file:
            print(file)
            try:
                output = PdfWriter()
                pdffile = pdf_dir + file
                source = PdfReader(pdffile, 'rb')

                # if len(source.pages) < 3:
                #     print("删除文件")
                #     os.remove(pdffile)
                #     continue

                if len(source.pages[0].extract_text()) <= 0:
                    print("删除文件")
                    os.remove(pdffile)
                    continue

                for page in source.pages:
                    contents = page.get_contents()
                    # bdata = contents.get_data()
                    # print(11)
                    # ddata = bdata.decode('latin1')  # decoded data (string)
                    # print(ddata)
                    # print(22)
                    # for key in replacements.keys():
                    #     ddata = ddata.replace(key, replacements[key])
                    # print(ddata)
                    # print(333)
                    # contents.set_data(ddata.encode('latin1'))
                    # exit(1)
                    ss = '全国团体标准信息平台'

                    if len(contents) > 0:
                        for obj in contents:
                            ddata = obj.get_object().get_data()
                            print(TextStringObject(ss.encode(), 'utf-8').get_object())
                            print(ddata)
                            print("====================")
                            # try:
                            #     process_data(stream_obj, replacements)
                            # except Exception as e:
                            #     print(e)
                            #     print("shit when wrong")
                    else:
                        process_data(contents, replacements)
                    exit(1)
                    # if len(contents) > 0:
                    #     for obj in contents:
                    #         stream_obj = obj.get_object()
                    #         print(stream_obj)
                    #         exit(1)
                    #         try:
                    #             process_data(stream_obj, replacements)
                    #         except Exception as e:
                    #             print(e)
                    #             print("shit when wrong")
                    # else:
                    #     process_data(contents, replacements)
                    output.add_page(page)
                with open(pdffile, 'wb') as ouf:
                    output.write(ouf)
            except Exception as e:
                print(e)
                # print("删除文件")
                # os.remove(pdffile)


if __name__ == '__main__':
    remove_pdf_watermark()
