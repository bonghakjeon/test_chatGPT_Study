# 터미널 설치 명령어 
# pip install PyPDF2
# pip install -U langchain-community
# pip install tiktoken
# pip install faiss-cpu

# 파이썬 절대 경로와 상대 경로
# 참고 URL - https://wikidocs.net/153154

# 파이썬 PdfReader(PDF 파일 읽기)
# 참고 URL - https://wikidocs.net/153818
# 참고 2 URL - https://seong6496.tistory.com/453

# 파이썬 extract_text(PDF 파일 텍스트 추출)
# 참고 URL - https://velog.io/@opjoobe/Python-pdf2text-PyPDF2

# 파이썬 LangChain - ChatOpenAI
# 참고 URL - https://databoom.tistory.com/entry/Langchain-Langchain-v03-%ED%8C%A8%EC%B9%98%EB%85%B8%ED%8A%B8
# 참고 2 URL - https://pypi.org/project/langchain-openai/
# 참고 3 URL - https://python.langchain.com/docs/integrations/chat/openai/

# PDF 파일 저장 위치 폴더 src vs public 차이
# 참고 URL - https://zindex.tistory.com/291
# 참고 2 URL - https://blog.naver.com/wjdgmlgus5/222456018683
# 참고 3 URL - https://velog.io/@daeun/React-public%ED%8F%B4%EB%8D%94-src%ED%8F%B4%EB%8D%94-%EC%96%B4%EB%94%94%EC%97%90-%EB%84%A3%EC%96%B4%EC%95%BC-%EB%90%98%EB%8A%94%EA%B1%B8%EA%B9%8C

import openai       # OPENAI 패키지 openai 불러오기 (ChatGPT, DALLE.2 사용)
import os           # 답변 결과를 테스트 파일로 저장할 때 경로 생성해야 해서 패키지 "os" 불러오기
# Langchain 패키지들
# TODO : ChatOpenAI 클래스 사용하기 위해 터미널창에 명령어 입력 및 엔터 (2025.04.14 minjae)
# 명령어 "pip install langchain-openai" 입력 및 엔터 
# 참고 URL - https://pypi.org/project/langchain-openai/
# 참고 2 URL - https://databoom.tistory.com/entry/Langchain-Langchain-v03-%ED%8C%A8%EC%B9%98%EB%85%B8%ED%8A%B8
# 참고 3 URL - https://python.langchain.com/docs/integrations/chat/openai/
# from langchain_openai import ChatOpenAI

# TODO : 아마존 웹서비스(AWS) 람다(Lambda) 함수 실행시 라이브 테일(Live Tail) 로그 실행시 아래와 같은 오류 메시지 출력되어 
#        "serverless-python-requirements" 사용하여 오류 해결 해야함. (2025.04.16 minjae)
# 오류 메시지 "[AWS] Unable to import module 'lambda_function': No module named 'pydantic_core._pydantic_core"
# 참고 URL - https://medium.com/@chullino/serverless-python-requirements-%ED%99%9C%EC%9A%A9%ED%95%98%EA%B8%B0-8c93fdf43c9a
# 참고 2 URL - https://velog.io/@_gyullbb/Serverless%EC%97%90%EC%84%9C-Python-Lambda-%EC%83%9D%EC%84%B1-%EB%B0%8F-%EB%B0%B0%ED%8F%AC%ED%95%98%EA%B8%B0-5
# 참고 3 URL - https://pacloud.tistory.com/40
# 참고 4 URL - https://dasoldasol.github.io/aws/serverless/sls-python/
# 참고 5 URL - https://youtu.be/Ke7DSpsszWY?si=4A7oNpU5e2vffPRy

# TODO : Docker 응용 프로그램(VMWare 가상머신과 비슷한 프로그램) 사용하여 파이썬 Langchain 패키지 (langchain_community, langchain 등등...) 
#        리눅스 환경에서 다운로드 및 압축 파일(.zip) 생성하여 아마존 웹서비스(AWS) 람다 함수에 계층(Layer)으로 업로드 하기 (2025.04.17 minjae) 
# 참고 URL - https://chatgpt.com/c/68005088-0ad4-8010-80bc-2c06f4bae328
# 참고 2 URL - https://yooloo.tistory.com/188
# 참고 3 URL - https://junside.tistory.com/265
# 참고 4 URL - https://velog.io/@nnijgnus/AWS-Lambda%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-AI-%EB%AA%A8%EB%93%88-%EA%B5%AC%ED%98%84-LangChain%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EB%89%B4%EC%8A%A4-%EC%9A%94%EC%95%BD-API-%EA%B0%9C%EB%B0%9C
# 참고 5 URL - https://chatgpt.com/c/68100355-d55c-8010-b573-32ee9f510b79
# 참고 6 URL - https://seoyeonhwng.medium.com/aws-docker%EB%A1%9C-lambda-layer-%EB%A7%8C%EB%93%A4%EA%B8%B0-b18237c7fbcf

# TODO : 아마존 웹서비스(AWS) 람다(Lambda) 함수 실행시 라이브 테일(Live Tail) 로그 실행시 아래와 같은 오류 메시지 출력되어 
#        (기존) from langchain_openai import ChatOpenAI -> (변경) from langchain_community.chat_models import ChatOpenAI 처리함. (2025.04.15 minjae)
# 유튜브 참고 URL - https://youtu.be/CbOZBDfxPl4?si=5Sb476FEHxZlYKw0
# [ERROR] Runtime.ImportModuleError: Unable to import module 'lambda_function': No module named 'langchain_openai' Traceback (most recent call last):
from langchain_openai import ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains.question_answering import load_qa_chain

# OpenAI API KEY
# 테스트용 카카오톡 챗봇 채팅방에서 
# ChatGPT와 통신하기 위해 OpenAI API 키 입력
# 아마존 웹서비스(AWS) 함수 lambda_handler -> 환경변수로 저장한 OpenAI API 키 'OPENAI_API' 불러오기
openai.api_key = os.environ['OPENAI_API']
# 비쥬얼스튜디오코드(VSCode) cmd 터미널창에 
# 아래처럼 최신 버전 OpenAI 라이브러리 "openai" 설치 및 함수 "getTextFromGPTNew" 구현 및 사용하기
# pip install openai
OPENAI_KEY = os.environ['OPENAI_API'] 
# OPENAI_KEY = os.getenv("OPENAI_KEY")

# ChatGPT 텍스트 응답 메시지 
def getMessageFromGPT(prompt):  
    messages_prompt = [{"role": "system", "content": 'You are a thoughtful assistant. Respond to all input in 300 words and answer in korea'}]
    messages_prompt += [{"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages_prompt)

    message = response["choices"][0]["message"]["content"]
    return message   

# DALLE2 이미지 응답
def getImageURLFromDALLE(prompt):
    response = openai.Image.create(prompt=prompt,n=1,size="512x512")
    image_url = response['data'][0]['url']
    return image_url

# PDF 파일 청크(chunk) 단위 텍스트 기반 응답 메시지 
def getMessageFromChunks(chunks, prompt):
    # 질문을 입력한 경우 
    if prompt:
        # 임베딩/ 시멘틱 인덱스 (API 요금 부과)
        embeddings = OpenAIEmbeddings(openai_api_key=openai.api_key)
        knowledge_base = FAISS.from_texts(chunks, embeddings)
            
        docs = knowledge_base.similarity_search(prompt)

        # 질문하기
        llm = ChatOpenAI(temperature=0,
                         openai_api_key=openai.api_key,
                         max_tokens=2000,
                         model_name='gpt-3.5-turbo',
                         request_timeout=120)
        chain = load_qa_chain(llm, chain_type="stuff")
        message = chain.run(input_documents=docs, question=prompt)
    # 질문을 입력하지 않은 경우
    else:
        message = '질문을 다시 입력해주세요.'

    return message