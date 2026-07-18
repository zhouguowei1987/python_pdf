# -*- coding:utf-8 -*-
# @Time   : 2022-02-23
# @Author : carl_DJ
import json

import fitz
import os


# 去除pdf的水印
def remove_pdf_watermark():
    pdf_dir = "../temp-www.cvma.org.cn/"
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
                pdf_new_file = '../upload.doc88.com/hbba.sacinfo.org.cn/' + file

                # 记录需要删除页面id
                delete_page_ids = []
                for pno in range(doc.page_count):
                    page = doc[pno]

                    page.clean_contents()
                    xref = page.get_contents()[0]
                    cont = bytearray(page.read_contents())
                    # if pno == 1:
                    #     print(cont)
                    #     exit()
                    # 删除中国兽医协会水印
                    im1 = cont.rfind(b'/Fm0 Do Q EMC')
                    if im1 >= 0:
                        im2 = cont.rfind(b"/Artifact<</Type/Pagination/Subtype/Watermark>>", 0, im1)
                        if im2 >= 0:
                            cont[im2: im1 + 13] = b""
                    doc.update_stream(xref, cont)
                if os.path.exists(pdf_new_file):
                    os.remove(pdf_new_file)

                if len(delete_page_ids):
                    doc.delete_pages(delete_page_ids)

                if doc.page_count < 5:
                    print("删除文件222")
                    os.remove(pdf_file)
                    os.remove(pdf_new_file)
                    continue
                if is_save_new_file:
                    doc.save(pdf_new_file)
                doc.close()
                print("删除源文件")
                os.remove(pdf_file)
            except Exception as e:
                print(e)
                print("删除文件333")


if __name__ == '__main__':
    remove_pdf_watermark()
