# -*- coding:utf-8 -*-
# @Time   : 2022-02-23
# @Author : carl_DJ
import json

import fitz
import os


# 去除pdf的水印
def remove_pdf_watermark():
    pdf_dir = "../temp-ksbz.chinamine-safety.gov.cn/"
    files = sorted(os.listdir(pdf_dir))
    for file in files:
        if ".pdf" in file:
            print(file)
            pdf_file = pdf_dir + file
            print(pdf_file)
            try:
                pdf_new_file = '../upload.doc88.com/hbba.sacinfo.org.cn/' + file
                doc = fitz.open(pdf_file)
                for pno in range(doc.page_count):
                    if pno == 0:
                        page = doc[pno]
                        # 获取页眉区域（这里需要根据实际页眉位置进行调整）
                        # 例如，假设页眉在顶部2厘米，宽度为A4纸的宽度
                        # print(page.rect.width)
                        # print(page.rect.height)
                        header_rect = fitz.Rect(0, 500, page.rect.width, page.rect.height-150)
                        # 删除页眉区域的内容
                        page.add_redact_annot(header_rect)
                        page.apply_redactions()
                doc.save(pdf_new_file)
                doc.close()
                print("删除源文件")
                os.remove(pdf_file)
            except Exception as e:
                print(e)
                print("删除文件333")
                os.remove(pdf_file)


if __name__ == '__main__':
    remove_pdf_watermark()
