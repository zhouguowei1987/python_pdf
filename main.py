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
                pdf_new_file = '../finish-www.ttbz.org.cn/' + file.replace(
                    file.split("-")[0].replace(" ", "") + "-", "")
                pdf_new_file = pdf_new_file.replace("：", "-")
                pdf_new_file = pdf_new_file.replace("《", "")
                pdf_new_file = pdf_new_file.replace("》", "")
                pdf_new_file = pdf_new_file.replace("（", "")
                pdf_new_file = pdf_new_file.replace("）", "")

                if os.path.exists(pdf_new_file):
                    continue

                doc = fitz.open(pdf_file)

                if len(doc[0].get_text('dict')) <= 0:
                    print("删除文件")
                    os.remove(pdf_file)
                    continue

                # 记录需要删除页面id
                delete_page_ids = []
                for pno in range(doc.page_count):
                    page = doc[pno]
                    # 查看是否有"版权所有"字样
                    content = page.get_text('text')
                    if content.find('版权所有') > 0:
                        print("版权所有字样---跳过")
                        break
                    # 查看是否有"不得翻印"字样
                    if content.find('不得翻印') > 0:
                        print("不得翻印字样---跳过")
                        break

                    page.clean_contents()
                    xref = page.get_contents()[0]
                    cont = bytearray(page.read_contents())

                    # if pno == 2:
                    #     print(cont)
                    #     exit(1)

                    # 删除全国标准信息平台文字
                    i1 = cont.find(b'/Xi%d' % (2 * pno))
                    if i1 >= 0:
                        i2 = cont.find(b"Tj\nET\nQ\nq\nQ\n", i1)
                        if i2 >= 0:
                            cont[i1: i2 + 12] = b""

                    # 删除全国标准信息平台文字
                    i3 = cont.find(b'/Xi%d' % (2 * pno + 2))
                    if i3 >= 0:
                        i4 = cont.find(b"Tj\nET\nQ\nq\nQ\n", i3)
                        if i4 >= 0:
                            cont[i3: i4 + 12] = b""

                    # 删除全国标准信息平台图片1
                    im1 = cont.find(b'/Im1')
                    if im1 >= 0:
                        start_im1 = cont.rfind(b'q\n/GS1 gs\n344 0 0 73', 0, im1)
                        if start_im1 < 0:
                            start_im1 = cont.rfind(b'q\n/GS2 gs\n344 0 0 73', 0, im1)
                        im2 = cont.find(b"Do\nQ\n", im1)
                        cont[start_im1: im2 + 5] = b""

                    # 删除全国标准信息平台图片2
                    im3 = cont.find(b'/Im2')
                    if im3 >= 0:
                        start_im3 = cont.rfind(b'q\n/GS0 gs\n344 0 0 73', 0, im3)
                        if start_im3 < 0:
                            start_im3 = cont.rfind(b'q\n/GS1 gs\n344 0 0 73', 0, im3)
                        im4 = cont.find(b"Do\nQ\n", im3)
                        cont[start_im3: im4 + 5] = b""

                    # 删除ZZB-T标准水印
                    # w1 = cont.rfind(b'/Artifact')
                    # if w1 >= 0:
                    #     w2 = cont.find(b"EMC", w1)
                    #     if w2 >= 0:
                    #         cont[w1: w2 + 3] = b""

                    # if pno == 2:
                    #     print(cont)
                    #     exit(1)

                    # 记录要删除空白页
                    emptyCont = [b'', b'q\nQ\n', b'q\nQ\nq\n', b'q\nQ\nq\nQ\nq\nQ\n', b'q\nQ\nq\nQ\nq\n']
                    if cont in emptyCont:
                        delete_page_ids.append(pno)

                    doc.update_stream(xref, cont)
                if os.path.exists(pdf_new_file):
                    os.remove(pdf_new_file)

                if len(delete_page_ids):
                    doc.delete_pages(delete_page_ids)
                doc.save(pdf_new_file)
                if doc.page_count < 5:
                    print("删除文件")
                    os.remove(pdf_new_file)
                    continue
                doc.close()
            except Exception as e:
                print(e)
                print("删除文件")
                os.remove(pdf_file)


if __name__ == '__main__':
    remove_pdf_watermark()
