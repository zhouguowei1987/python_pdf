# -*- coding:utf-8 -*-
# @Time   : 2022-02-23
# @Author : carl_DJ
import json

import fitz
import os


# 去除pdf的水印
def remove_pdf_watermark():
    pdf_dir = "../temp-www.ttbz.org.cn/"
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
                    page.clean_contents()
                    xref = page.get_contents()[0]
                    cont = bytearray(page.read_contents())
                    # if pno == 1:
                    #     print(cont)
                    #     print("======")
                    #     exit(1)
                    i1 = cont.find(b'/Xi%d' % (2 * pno))
                    if i1 < 0:
                        break
                    # 查看是否是单页
                    pre_single_page_i1 = cont.rfind(b'q\nQ\nq\nQ\nq\n', 0, i1)
                    if pre_single_page_i1 >= 0:
                        # 是单页
                        start_i1 = pre_single_page_i1
                    else:
                        # 不是单页，查找最近的空格
                        start_i1 = cont.rfind(b' ', 0, i1)

                    i2 = cont.find(b"Tj\nET\nQ\nq\nQ\n", i1)
                    # print(i2)
                    cont[start_i1: i2 + 12] = b""
                    # print(cont)
                    # exit(1)
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
