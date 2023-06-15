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

                    page.clean_contents()
                    xref = page.get_contents()[0]
                    cont = bytearray(page.read_contents())
                    # if pno == 1:
                    #     print(cont)
                    #     exit(1)

                    # 删除地方标准信息平台图片
                    im1 = cont.find(b'Do\nQ\nQ\nq\nQ\n')
                    if im1 >= 0:
                        im2 = cont.rfind(b"/Im", 0, im1)
                        if im2 >= 0:
                            cont[im2: im1] = b""

                    # if pno == 1:
                    #     print(cont)
                    #     exit(1)
                    # 记录要删除空白页
                    emptyCont = [
                        b'', b'q\nQ\n', b'q\nQ\nq\n',
                        b'q\n587.52 0 0 829.44 0 0 cm\n/Im1 Do\nQ\nq\nQ\nq\n/Xi%d gs\nq\n560 0 0 384 13 44 cm\nDo\nQ\nQ\nq\nQ\n' % (
                                3 * pno),
                        b'q\n596.16006 0 0 841.86007 0 0 cm\n/Im1 Do\nQ\nq\nQ\nq\n/Xi%d gs\nq\n560 0 0 384 17 45 cm\nDo\nQ\nQ\nq\nQ\n' % (
                                3 * pno),
                        b'q\nQ\nq\nQ\nq\nQ\n', b'q\nQ\nq\nQ\nq\n'
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
                doc.save(pdf_new_file)
                doc.close()
            except Exception as e:
                print(e)
                print("删除文件333")
                # os.remove(pdf_file)


if __name__ == '__main__':
    remove_pdf_watermark()
