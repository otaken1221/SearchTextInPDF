from PyPDF2 import PdfReader

# 検索する文字列を設定
search_strings = [""]

# 検索対象のPDFファイルのパスを設定
pdf_files = [""]


# PDFファイルを開く
pdf_readers = []
for pdf_file in pdf_files:
    pdf_reader = PdfReader(pdf_file)
    pdf_readers.append(pdf_reader)

# PDFファイルから文字列を検索する
found_pdfs = {}
for search_string in search_strings:
    found_pdfs[search_string] = []
    for i,pdf_reader in enumerate(pdf_readers):
        for page in range(len(pdf_reader.pages)):
            if search_string in pdf_reader.pages[page].extract_text():
                found_pdfs[search_string].append(i)

# 検索結果を出力する
for search_string, found_pdfs in found_pdfs.items():
    print(f"検索文字列: {search_string}")
    if found_pdfs == []:
        print("この文字列は存在しません")
    else:
      for found_pdf in found_pdfs:
          print(f"PDFファイル名: {found_pdf}")
