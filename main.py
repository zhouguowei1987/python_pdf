# -*- coding:utf-8 -*-
# @Time   : 2022-02-23
# @Author : carl_DJ
import json

import fitz
import os


# 去除pdf的水印
def remove_pdf_watermark():
    pdf_dir = "../www.ttbz.org.cn/"
    files = sorted(os.listdir(pdf_dir))
    for file in files:
        if ".pdf" in file:
            print(file)
            pdf_file = pdf_dir + file
            try:
                doc = fitz.open(pdf_file)

                if doc.page_count < 3:
                    print("删除文件")
                    os.remove(pdf_file)
                    continue
                if len(doc[0].get_text('dict')) <= 0:
                    print("删除文件")
                    os.remove(pdf_file)
                    continue
                pdf_new_file = '../finish-www.ttbz.org.cn/' + file.replace(file.split("-")[0] + "-", "")

                for pno in range(doc.page_count):
                    page = doc[pno]
                    xref = page.get_contents()[0]
                    cont = bytearray(page.read_contents())
                    i1 = cont.find(b'\x07\x9e\\r3\\r\x18\x05\x89\x1e=')
                    if i1 < 0:
                        break
                    i2 = cont.find(b"\x07\xfc\x06\x17\x16\xa5\x14\xa9\\n&", i1)
                    cont[i1 - 2: i2 + 3] = b""
                    doc.update_stream(xref, cont)
                if os.path.exists(pdf_new_file):
                    os.remove(pdf_new_file)
                doc.save(pdf_new_file)
                doc.close()
            except Exception as e:
                print(e)
                print("删除文件")
                os.remove(pdf_file)


if __name__ == '__main__':
    remove_pdf_watermark()
