from docx2pdf import convert

if __name__ == '__main__':
    word_file = "2023年安徽亳州中考历史试题及答案.docx"
    pdf_file = word_file.replace(".docx", ".pdf")
    with open(pdf_file, "w") as f:
        # 将 Word 文档转换为 PDF
        try:
            convert(word_file, pdf_file)
            print("转换成功！")
        except Exception as e:
            print("转换失败：", str(e))
