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
                        i2 = cont.find(b"Do\nQ\nQ\nQ\nq\n", i1)
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

                    # 插入页眉文本
                    header_fontsize_to_use = 12
                    header_fontname_to_use = "china-s"
                    header_text = "年寒窗苦读日，只盼金榜题名时，祝你考试拿高分，鲤鱼跳龙门！加油！"
                    header_rect = fitz.Rect(100, 28, 500, 48)

                    page.insert_textbox(header_rect, header_text,
                                        fontsize=header_fontsize_to_use,
                                        fontname=header_fontname_to_use,
                                        color=(1, 0, 0),
                                        align=1)

                    doc.update_stream(xref, cont)

                if os.path.exists(pdf_new_file):
                    os.remove(pdf_new_file)

                # 添加封面页
                doc.new_page(0)
                title_fontsize_to_use = 18
                title_fontname_to_use = "china-ss"
                title_text = "2023年国家公务员考试行测试题及答案\n（副省级）"
                title_rect = fitz.Rect(50, 350, 500, 500)

                doc[0].insert_textbox(title_rect, title_text,
                                      fontsize=title_fontsize_to_use,
                                      fontname=title_fontname_to_use,
                                      lineheight=2,
                                      color=(0, 0, 0),
                                      align=1)
                doc.save(pdf_new_file)
            except Exception as e:
                print(e)
                print("删除文件")


if __name__ == '__main__':
    handle_pdf()