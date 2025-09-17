# TEXT 파일 전용 모듈

import os   # 파일 존재 여부 확인해야 해서 패키지 "os" 불러오기
from modules import chatbot_logger   # 폴더 "modules" -> 카카오 챗봇 로그 작성 모듈 "chatbot_logger" 불러오기

# 터미널창에 Langchain 라이브러리 설치 명령어 입력 및 엔터  
# pip install -U langchain-community
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

# TEXT 파일에 작성된 청크(chunk) 단위 텍스트 추출
# 참고 URL - https://rudaks.tistory.com/entry/langchain-CharacterTextSplitter%E1%84%8B%E1%85%AA-RecursiveCharacterTextSplitter%E1%84%8B%E1%85%B4-%E1%84%8E%E1%85%A1%E1%84%8B%E1%85%B5
# 참고 2 URL - https://wikidocs.net/233998
# 참고 3 URL - https://wikidocs.net/231568
# 참고 4 URL - https://chatgpt.com/c/6811c621-90ec-8010-875b-a26b9ef09405
def getChunksFromText(filepath):
    # 해당 경로에 PDF 파일 존재하는 경우 
    # 참고 URL - https://wikidocs.net/14304
    # 참고 2 URL - https://wikidocs.net/256287
    if True == os.path.exists(filepath): 
        # text 파일 텍스트 추출
        loader = TextLoader(filepath)
        data = loader.load()

        # 청크(chunk) 단위 텍스트 분할
        text_splitter = CharacterTextSplitter(
            separator='\n',
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        
        chunks = text_splitter.split_text(data[0].page_content)

        print('[테스트] 청크(chunk) 단위 텍스트 분할: ', chunks)

    # 해당 경로에 PDF 파일 존재 안 하는 경우
    else: 
        chunks = []

    return chunks


# TEXT 파일에 작성된 모든 텍스트 가져오기 
def getResponseFromText(filepath):
    # 해당 경로에 TEXT 파일 존재하는 경우 
    # 참고 URL - https://wikidocs.net/14304
    # 참고 2 URL - https://wikidocs.net/256287
    if True == os.path.exists(filepath):
        # TEXT 파일에 작성된 모든 텍스트 가져오기
        # with 문 사용해서 TEXT 파일 자동으로 열고(open) 닫기(close)
        # 참고 URL - https://wikidocs.net/26
        with open(filepath, 'r') as file:
            response = file.read()
            filename = os.path.basename(filepath)   # 텍스트 파일 이름 가져오기 
            # chatbot_logger.log_write(chatbot_logger._info, f'TEXT 파일({filename}) 작성된 텍스트', response)
            chatbot_logger.log_write(chatbot_logger._info, f'{filename} 작성된 텍스트 가져오기', 'OK!')
    # 해당 경로에 PDF 파일 존재 안 하는 경우
    else: 
        response = ''
        chatbot_logger.log_write(chatbot_logger._info, f'{filename} 존재 안 함.', response)

    return response