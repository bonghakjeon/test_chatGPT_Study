# TODO : 해당 PDF 파일 전용 모듈 pdf.py 소스파일은 MS Word 파일 -> PDF 파일 변환한 PDF 파일을 
#        VSCode, 아마존 웹서비스(AWS) 람다 함수(Lambda Funtion)에서 열었을 때 
#        텍스트(한글, 영어 포함) 깨짐 현상으로 인하여 해당 PDF 파일 전용 모듈 pdf.py 소스파일은 사용 안 함. (2025.04.30 minjae)

# PDF 파일 전용 모듈

# PyPDF2
# 참고 URL - https://pypdf2.readthedocs.io/en/3.0.0/user/suppress-warnings.html
# 참고 2 URL - https://stackoverflow.com/questions/77635169/how-do-i-use-pypdf2-to-read-and-display-the-contents-of-my-pdf-when-ran

# pdfplumber
# 참고 URL - https://taptorestart.tistory.com/entry/PDF%EB%A5%BC-%ED%85%8D%EC%8A%A4%ED%8A%B8%EB%A1%9C-%EB%B0%94%EA%BF%94%EC%A3%BC%EB%8A%94-pdfminersix-pypdf2-pdfplumber-%EB%B9%84%EA%B5%90%ED%95%B4%EB%B3%B4%EA%B8%B0
# 참고 2 URL - https://chatgpt.com/c/68117d6f-3d1c-8010-8175-f69aad5ae75b

# Python에서 OCR 구현하기
# 패키지 pytesseract, pdf2image 
# 참고 URL - https://datasciencebeehive.tistory.com/207
# 참고 2 URL - https://stackoverflow.com/questions/66995340/pdf-to-text-convert-using-python-pytesseract
# 참고 3 URL - https://where-change-begins.tistory.com/49
# 참고 4 URL - https://chatgpt.com/c/68117d6f-3d1c-8010-8175-f69aad5ae75b

# 터미널창에 PyPDF2 라이브러리 설치 명령어 입력 및 엔터  
# pip install PyPDF2
# from PyPDF2 import PdfReader   # 파이썬 PdfReader 클래스 사용하기 위해 패키지 PyPDF2 불러오기 

# 터미널창에 pdfplumber 라이브러리 설치 명령어 입력 및 엔터  
# 참고 URL - https://pypi.org/project/pdfplumber/
# pip install pdfplumber
# import pdfplumber              # 파이썬 PDF 텍스트 추출 관련 패키지 pdfplumber 불러오기 
# import os                      # 파일 존재 여부 확인해야 해서 패키지 "os" 불러오기
# import io
# 터미널창에 Langchain 라이브러리 설치 명령어 입력 및 엔터  
# pip install -U langchain-community
# from langchain.text_splitter import CharacterTextSplitter

# pdfplumber 패키지 기반 
# PDF 파일에 작성된 청크(chunk) 단위 텍스트 추출
# def getChunksFromPDF(filepath):
#     # 해당 경로에 PDF 파일 존재하는 경우 
#     # 참고 URL - https://wikidocs.net/14304
#     # 참고 2 URL - https://wikidocs.net/256287
#     if True == os.path.exists(filepath): 
#         # PDF 파일 텍스트 추출
#         with pdfplumber.open(filepath) as pdf:
#             text = ""
#             for page in pdf.pages:
#                 text += page.extract_text()

#         print('[테스트] PDF 파일 텍스트: ', text)

#         # 청크(chunk) 단위 텍스트 분할
#         text_splitter = CharacterTextSplitter(
#             separator="\n",
#             chunk_size=1000,
#             chunk_overlap=200,
#             length_function=len
#         )
#         chunks = text_splitter.split_text(text)

#     # 해당 경로에 PDF 파일 존재 안 하는 경우
#     else: 
#         chunks = []

#     return chunks

# PyPDF2 패키지 기반 
# PDF 파일에 작성된 청크(chunk) 단위 텍스트 추출
# def getChunksFromPDF(filepath):
#     # 해당 경로에 PDF 파일 존재하는 경우 
#     # 참고 URL - https://wikidocs.net/14304
#     # 참고 2 URL - https://wikidocs.net/256287
#     if True == os.path.exists(filepath):
#         # PDF 파일 텍스트 추출
#         pdf_reader = PdfReader(filepath)
#         text = ""
#         for page in pdf_reader.pages:
#             text += page.extract_text()
#         # 청크(chunk) 단위 텍스트 분할
#         text_splitter = CharacterTextSplitter(
#             separator="\n",
#             chunk_size=1000,
#             chunk_overlap=200,
#             length_function=len
#         )
#         chunks = text_splitter.split_text(text)
#     # 해당 경로에 PDF 파일 존재 안 하는 경우
#     else: 
#         chunks = []

#     return chunks