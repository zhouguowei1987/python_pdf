import os
import fitz


def handle_pdf():
    pdf_dir = "../www.chinagwy.org/"
    files = sorted(os.listdir(pdf_dir))
    for file in files:
        if ".pdf" in file:
            print(file)
            pdf_file = pdf_dir + file
            try:
                doc = fitz.open(pdf_file)

                pdf_new_file = '../finish.chinagwy.org/' + file
                # 删除第一页
                doc.delete_page(0)
                for pno in range(doc.page_count):
                    page = doc[pno]
                    page.clean_contents()
                    xref = page.get_contents()[0]
                    cont = bytearray(page.read_contents())

                    # print(cont)
                    # exit()

                    # 第一种情况：不带连接-删除页码文字
                    i1 = cont.rfind(b'cm\n0 0 0 rg\n0 0 0')
                    if i1 >= 0:
                        i2 = cont.find(b"d\nQ\nq\n0 0 0", i1)
                        cont[i1: i2 + 11] = b""

                    # 第二种情况：带连接-删除页码文字
                    i5 = cont.find(b'/Im1')
                    if i5 >= 0:
                        i6 = cont.find(b"Tj\nET\nQ\nq\n0 J\n", i5)
                        cont[i5: i6 + 14] = b""

                    links = page.get_links()
                    for link in links:
                        if link.get('uri') == 'http://www.chinaexam.org':
                            page.delete_link(link)

                    # 插入文本
                    fontsize_to_use = 12
                    fontname_to_use = "china-s"
                    text = "年寒窗苦读日，只盼金榜题名时，祝你考试拿高分，鲤鱼跳龙门！加油！"
                    rect = fitz.Rect(100, 25, 500, 45)

                    # Uncomment if you wish to display rect
                    page.draw_rect(rect, color=(.25, 1, 0.25))
                    page.insert_textbox(rect, text,
                                        fontsize=fontsize_to_use,
                                        fontname=fontname_to_use,
                                        color=(1, 0, 0),
                                        align=1)

                    doc.update_stream(xref, cont)
                # 插入第一个

                if os.path.exists(pdf_new_file):
                    os.remove(pdf_new_file)
                doc.save(pdf_new_file)
            except Exception as e:
                print(e)
                print("删除文件")


if __name__ == '__main__':
    handle_pdf()
