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
                pdf_new_file = '../upload.doc88.com/finish-www.ttbz.org.cn/' + file.replace(
                    file.split("-")[0].replace(" ", "") + "-", "")
                pdf_new_file = pdf_new_file.replace("：", "-")
                pdf_new_file = pdf_new_file.replace("《", "")
                pdf_new_file = pdf_new_file.replace("》", "")
                pdf_new_file = pdf_new_file.replace("（", "")
                pdf_new_file = pdf_new_file.replace("）", "")

                # if os.path.exists(pdf_new_file):
                #     print("文件已存在-删除文件")
                #     os.remove(pdf_file)
                #     continue

                doc = fitz.open(pdf_file)

                if len(doc[0].get_text('dict')) <= 0:
                    print("删除文件111")
                    os.remove(pdf_file)
                    continue

                # 记录需要删除页面id
                delete_page_ids = []
                for pno in range(doc.page_count):
                    page = doc[pno]
                    page.clean_contents()
                    xref = page.get_contents()[0]
                    cont = bytearray(page.read_contents())
                    # if pno == 0:
                    #     print(cont)
                    #     exit(1)
                    # print("===============================================")

                    # 删除全国标准信息平台文字
                    i1 = cont.find(b'/Xi%d' % (2 * pno))
                    if i1 >= 0:
                        i2 = cont.find(b"Tj ET Q q", i1)
                        if i2 >= 0:
                            cont[i1: i2 + 9] = b""

                    # 删除全国标准信息平台文字
                    i3 = cont.find(b'/Xi%d' % (2 * pno + 1))
                    if i3 >= 0:
                        i4 = cont.find(b"Tj ET Q q", i3)
                        if i4 >= 0:
                            cont[i3: i4 + 9] = b""

                    # 删除全国标准信息平台文字
                    i5 = cont.find(b'/Xi%d' % (2 * pno + 3))
                    if i5 >= 0:
                        i6 = cont.find(b"Tj ET Q q Q", i5)
                        if i6 >= 0:
                            cont[i5: i6 + 11] = b""

                    # # 删除全国标准信息平台图片1
                    # im1 = cont.find(b'/Im1')
                    # if im1 >= 0:
                    #     start_im1 = cont.rfind(b'q\n/GS1 gs\n344 0 0 73', 0, im1)
                    #     if start_im1 < 0:
                    #         start_im1 = cont.rfind(b'q\n/GS2 gs\n344 0 0 73', 0, im1)
                    #     im2 = cont.find(b"Do\nQ\n", im1)
                    #     cont[start_im1: im2 + 5] = b""
                    #
                    # # 删除全国标准信息平台图片2
                    # im3 = cont.find(b'/Im2')
                    # if im3 >= 0:
                    #     start_im3 = cont.rfind(b'q\n/GS0 gs\n344 0 0 73', 0, im3)
                    #     if start_im3 < 0:
                    #         start_im3 = cont.rfind(b'q\n/GS1 gs\n344 0 0 73', 0, im3)
                    #     im4 = cont.find(b"Do\nQ\n", im3)
                    #     cont[start_im3: im4 + 5] = b""

                    # 删除新版全国标准信息平台图片-带个人证件信息2
                    im5 = 0
                    im5_1 = cont.find(b'/Im1')
                    if im5_1 > 0:
                        im5 = im5_1

                    im5_2 = cont.find(b'/Im2')
                    if im5_2 > 0:
                        im5 = im5_2

                    im5_3 = cont.find(b'/Im3')
                    if im5_3 > 0:
                        im5 = im5_3

                    im5_4 = cont.find(b'/Im4')
                    if im5_4 > 0:
                        im5 = im5_4

                    im5_5 = cont.find(b'/Im5')
                    if im5_5 > 0:
                        im5 = im5_5

                    im5_6 = cont.find(b'/Im6')
                    if im5_6 > 0:
                        im5 = im5_6

                    im5_7 = cont.find(b'/Im7')
                    if im5_7 > 0:
                        im5 = im5_7

                    im5_8 = cont.find(b'/Im8')
                    if im5_8 > 0:
                        im5 = im5_8

                    im5_9 = cont.find(b'/Im9')
                    if im5_9 > 0:
                        im5 = im5_9

                    im5_10 = cont.find(b'/Im10')
                    if im5_10 > 0:
                        im5 = im5_10

                    if im5 > 0:
                        im6 = cont.find(b" Do Q q Q", im5)
                        cont[im5: im6 + 9] = b""
                        if im6 < 0:
                            im6 = cont.find(b" Do Q", im5)
                            cont[im5: im6 + 5] = b""
                    doc.update_stream(xref, cont)
                if os.path.exists(pdf_new_file):
                    os.remove(pdf_new_file)

                if len(delete_page_ids):
                    doc.delete_pages(delete_page_ids)
                doc.save(pdf_new_file)
                if doc.page_count < 3:
                    print("删除文件222")
                    os.remove(pdf_file)
                    os.remove(pdf_new_file)
                    continue
                doc.close()
                print("删除源文件")
                os.remove(pdf_file)
            except Exception as e:
                print(e)
                # exit(1)
                # print("删除文件333")
                # os.remove(pdf_file)


if __name__ == '__main__':
    remove_pdf_watermark()
