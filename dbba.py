# -*- coding:utf-8 -*-
# @Time   : 2022-02-23
# @Author : carl_DJ
import json

import fitz
import os


# 去除pdf的水印
def remove_pdf_watermark():
    pdf_dir = "../temp-dbba.sacinfo.org.cn/"
    files = sorted(os.listdir(pdf_dir))
    for file in files:
        is_save_new_file = True
        if ".pdf" in file:
            print(file)
            pdf_file = pdf_dir + file
            try:
                doc = fitz.open(pdf_file)

                if len(doc[0].get_text('dict')) <= 0:
                    print("删除文件111")
                    os.remove(pdf_file)
                    continue
                pdf_new_file = '../finish-dbba.sacinfo.org.cn/' + file

                # 记录需要删除页面id
                delete_page_ids = []
                for pno in range(doc.page_count):
                    page = doc[pno]

                    # 查看是否有"版权所有"字样
                    content = page.get_text('text')
                    if content.find('版权所有') > 0:
                        is_save_new_file = False
                        print("版权所有字样---跳过")
                        break
                    # 查看是否有"版权专有"字样
                    content = page.get_text('text')
                    if content.find('版权专有') > 0:
                        is_save_new_file = False
                        print("版权专有字样---跳过")
                        break
                    # 查看是否有"侵权必究"字样
                    content = page.get_text('text')
                    if content.find('侵权必究') > 0:
                        is_save_new_file = False
                        print("侵权必究字样---跳过")
                        break
                    # 查看是否有"不得翻印"字样
                    if content.find('不得翻印') > 0:
                        is_save_new_file = False
                        print("不得翻印字样---跳过")
                        break

                    page.clean_contents()
                    xref = page.get_contents()[0]
                    cont = bytearray(page.read_contents())
                    # if pno == 14:
                    #     print(cont)
                    #     exit()

                    # 删除地方标准信息平台图片
                    im1 = cont.rfind(b'Do\nQ\nQ\nq\nQ\n')
                    if im1 >= 0:
                        im2 = cont.rfind(b"/Im", 0, im1)
                        if im2 >= 0:
                            cont[im2: im1] = b""

                    # if file == "气体灭火系统质量检验评定规程(DB64-T 408-2017).pdf":
                    #     if pno == 1:
                    #         print(cont)
                    #         exit(1)
                    # 记录要删除空白页
                    emptyCont = [
                        b'q\n587.52 0 0 829.44 0 0 cm\n/Im1 Do\nQ\nq\nQ\nq\n/Xi%d gs\nq\n560 0 0 384 13 44 cm\nDo\nQ\nQ\nq\nQ\n' % (
                                3 * pno),
                        b'q\n596.16006 0 0 841.86007 0 0 cm\n/Im1 Do\nQ\nq\nQ\nq\n/Xi%d gs\nq\n560 0 0 384 17 45 cm\nDo\nQ\nQ\nq\nQ\n' % (
                                3 * pno),
                        b'q\n587.52 0 0 840.96 0 0 cm\n/Im1 Do\nQ\nq\nQ\nq\n/Xi%d gs\nq\n560 0 0 384 13 45 cm\nDo\nQ\nQ\nq\nQ\n' % (
                                3 * pno),
                        b'q\n591.36 0 0 837.12 0 0 cm\n/Im1 Do\nQ\nq\nQ\nq\n/Xi%d gs\nq\n560 0 0 384 15 45 cm\nDo\nQ\nQ\nq\nQ\n' % (
                                3 * pno),
                        b'q\n595.2 0 0 841.92 0 0 cm\n/Im1 Do\nQ\nq\nQ\nq\n/Xi%d gs\nq\n560 0 0 384 17 45 cm\nDo\nQ\nQ\nq\nQ\n' % (
                                3 * pno),
                        b'q\nQ\nq\nQ\nq\n/Xi%d gs\nq\n560 0 0 384 17 45 cm\nDo\nQ\nQ\nq\nQ\n' % (3 * pno),
                        b'q\nQ\nq\n/Xi%d gs\nq\n560 0 0 384 17 45 cm\nDo\nQ\nQ\nq\nQ\n' % (3 * pno),
                    ]
                    if cont in emptyCont:
                        delete_page_ids.append(pno)

                    doc.update_stream(xref, cont)
                if os.path.exists(pdf_new_file):
                    os.remove(pdf_new_file)

                if len(delete_page_ids):
                    doc.delete_pages(delete_page_ids)

                if doc.page_count < 5:
                    print("删除文件222")
                    # os.remove(pdf_new_file)
                    continue
                if is_save_new_file:
                    doc.save(pdf_new_file)
                doc.close()
            except Exception as e:
                print(e)
                print("删除文件333")
                # os.remove(pdf_file)


if __name__ == '__main__':
    remove_pdf_watermark()
