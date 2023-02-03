# -*- coding:utf-8 -*-
# @Time   : 2022-02-23
# @Author : carl_DJ
import json

import fitz
import os


def find_textbox(page: fitz.Page, keyword: str) -> dict:
    info = page.get_text('dict')
    if 'blocks' in info:
        for block in info['blocks']:
            if 'lines' in block:
                for line in block['lines']:
                    if 'spans' in line:
                        for span in line['spans']:
                            text = span.get('text', '').replace(' ', '')
                            print(span)
                            if text == keyword:
                                return span


# 去除pdf的水印
def remove_pdf_watermark():
    pdf_dir = "../aaa/"
    files = sorted(os.listdir(pdf_dir))
    for file in files:
        if ".pdf" in file:
            print(file)
            pdf_file = pdf_dir + file
            try:
                doc = fitz.open(pdf_file)

                # if len(source.pages) < 3:
                #     print("删除文件")
                #     os.remove(pdf_file)
                #     continue
                #
                # if len(source.pages[0].extract_text()) <= 0:
                #     print("删除文件")
                #     os.remove(pdf_file)
                #     continue
                pdf_new_file = '../bbb/111.pdf'
                keyword = '全国团体标准信息平台'
                for page in doc:
                    target = find_textbox(page, keyword)
                    page.add_redact_annot(target['bbox'])
                    page.apply_redactions()

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
