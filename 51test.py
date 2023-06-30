from docx2pdf import convert

if __name__ == '__main__':
    word_file = "../upload.doc88.com/finish.tikuvip（2023）.51test.net-高考/2023年江苏苏州中考道德与法治真题(含答案).docx"
    pdf_file = word_file.replace(".docx", ".pdf")
    file = open(pdf_file, "w")
    file.close()
    # 将 Word 文档转换为 PDF
    try:
        convert(word_file, pdf_file)
        print("转换成功！")
    except Exception as e:
        print("转换失败：", str(e))
