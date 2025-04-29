# PDF 파일 전용 모듈

# 터미널창에 PyPDF2 라이브러리 설치 명령어 입력 및 엔터  
# pip install PyPDF2
from PyPDF2 import PdfReader   # 파이썬 PdfReader 클래스 사용하기 위해 패키지 PyPDF2 불러오기 
import os                      # 파일 존재 여부 확인해야 해서 패키지 "os" 불러오기
# 터미널창에 Langchain 라이브러리 설치 명령어 입력 및 엔터  
# pip install -U langchain-community
from langchain.text_splitter import CharacterTextSplitter

# PDF 파일에 작성된 청크(chunk) 단위 텍스트 추출
def getChunksFromPDF(filepath):
    # 해당 경로에 PDF 파일 존재하는 경우 
    # 참고 URL - https://wikidocs.net/14304
    # 참고 2 URL - https://wikidocs.net/256287
    if True == os.path.exists(filepath):
        # PDF 파일 텍스트 추출
        pdf_reader = PdfReader(filepath)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        # 청크(chunk) 단위 텍스트 분할
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_text(text)
    # 해당 경로에 PDF 파일 존재 안 하는 경우
    else: 
        chunks = []

    return chunks