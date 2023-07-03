from docx2pdf import convert
import requests

if __name__ == '__main__':

    download_url = "http://c.gb688.cn/bzgk/gb/viewGb?hcno=97F140EC1874D4C25CB8DC53B1D102D0"
    download_response = requests.get(download_url)
    try:
        with open('111.pdf', 'wb') as ssss:
            ssss.write(download_response.content)
    except Exception as e:
        print(e)

    # word_file = "2023年安徽亳州中考历史试题及答案.docx"
    # pdf_file = word_file.replace(".docx", ".pdf")
    # with open(pdf_file, "w") as f:
    #     # 将 Word 文档转换为 PDF
    #     try:
    #         convert(word_file, pdf_file)
    #         print("转换成功！")
    #     except Exception as e:
    #         print("转换失败：", str(e))
