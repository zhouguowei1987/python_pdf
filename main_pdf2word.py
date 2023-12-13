# -*- coding:utf-8 -*-
# @Time   : 2022-02-23
# @Author : carl_DJ
import json

import PyPDF2
from docx import Document
from pdf2docx import Converter
import os


# 去除pdf的水印
def pdf2word():
    pdf_dir = "../upload.doc88.com/finish-www.ttbz.org.cn/"
    docx_dir = "../docx.ttbz.org.cn/"
    files = sorted(os.listdir(pdf_dir))
    for file in files:
        if ".pdf" in file:
            print(file)
            pdf_file = pdf_dir + file
            docx_file = docx_dir + file.replace(".pdf", ".docx")
            if os.path.exists(docx_file):
                continue
            try:
                # 转换并保存Word文档
                pdf_cv = Converter(pdf_file)

                pdf_cv.convert(docx_file, start=0, end=None)

                pdf_cv.close()
            except Exception as e:
                print(e)
                # print("删除文件")
                # os.remove(pdf_file)


if __name__ == '__main__':
    pdf2word()
