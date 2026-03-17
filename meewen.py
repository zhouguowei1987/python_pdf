# -*- coding:utf-8 -*-
# @Time   : 2022-02-23
# @Author : carl_DJ
import json

import fitz
import os


# 去除pdf的水印
def remove_pdf_watermark():
    category = ["专题讲稿", "领导讲话", "遴选题库", "公考素材", "表格合同"]
    for i in range(len(category)):
        pdf_dir = "../www.meewen.com/temp-www.meewen.com/"+category[i]+"/"
        files = sorted(os.listdir(pdf_dir))
        for file in files:
            if ".pdf" in file:
                print(file)
                pdf_file = pdf_dir + file
                try:
                    pdf_new_dir = "../www.meewen.com/2026-03-17/"+category[i]+"/"
                    if not os.path.exists(pdf_new_dir):
                        os.makedirs(pdf_new_dir)

                    sub_file = file
                    sub_file = sub_file.replace(".pdf","")
                    point_flag_index = sub_file.find(".")
                    if point_flag_index != 0:
                        sub_file = sub_file[point_flag_index + 1:]

                    sub_file = sub_file + ".pdf"
                    pdf_new_file = pdf_new_dir + sub_file.replace("／", "-")
                    pdf_new_file = pdf_new_file.replace("：", "-")
                    pdf_new_file = pdf_new_file.replace("：", "-")
                    pdf_new_file = pdf_new_file.replace("+", "-")
                    pdf_new_file = pdf_new_file.replace("(已过期)", "")
                    pdf_new_file = pdf_new_file.replace("《", "")
                    pdf_new_file = pdf_new_file.replace("》", "")
                    pdf_new_file = pdf_new_file.replace("（", "")
                    pdf_new_file = pdf_new_file.replace("）", "")

                    doc = fitz.open(pdf_file)
                    # 记录需要删除页面id
                    delete_page_ids = []
                    for pno in range(doc.page_count):
                        page = doc[pno]
                        if len(page.get_text()) <= 0:
                            delete_page_ids.append(pno)
                        if page.get_text().find("公文搜") != -1:
                            # 获取页眉区域（这里需要根据实际页眉位置进行调整）
                            # 例如，假设页眉在顶部2厘米，宽度为A4纸的宽度
                            header_rect = fitz.Rect(0, 0, page.rect.width, page.rect.height - 750)
                            # 删除页眉区域的内容
                            page.add_redact_annot(header_rect)
                            page.apply_redactions()
                    if len(delete_page_ids):
                        doc.delete_pages(delete_page_ids)
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
