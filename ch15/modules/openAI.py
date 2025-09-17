# [openai 전용 모듈] openai==1.77.0

import os   # 답변 결과를 테스트 파일로 저장할 때 경로 생성해야 해서 패키지 "os" 불러오기

from openai import OpenAI   # OPENAI 패키지 openai 불러오기 (ChatGPT, DALLE.2 사용)

from langchain_openai import ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
# import numpy as np
# from numpy import dot
# from numpy.linalg import norm
# import pandas as pd
# from langchain_community.vectorstores import Chroma

# TODO : 아래 경고 메시지로 인해 (기존) from langchain.vectorstores import FAISS -> (변경) from langchain_community.vectorstores import FAISS 처리함. (2025.04.30 minjae)
# (경고 메시지)
# LangChainDeprecationWarning: Importing FAISS from langchain.vectorstores is deprecated. Please replace deprecated imports:
# >> from langchain.vectorstores import FAISS
# with new imports of:
# >> from langchain_community.vectorstores import FAISS
# from langchain.vectorstores import FAISS
# You can use the langchain cli to **automatically** upgrade many imports. Please see documentation here <https://python.langchain.com/docs/versions/v0_2/>
# from langchain_community.vectorstores import FAISS

# TODO : 아래 경고 메시지로 인해 (기존) from langchain.embeddings import OpenAIEmbeddings -> (변경) from langchain_community.embeddings import OpenAIEmbeddings 처리함. (2025.04.30 minjae)
# (경고 메시지)
# LangChainDeprecationWarning: Importing OpenAIEmbeddings from langchain.embeddings is deprecated. Please replace deprecated imports:
# >> from langchain.embeddings import OpenAIEmbeddings
# with new imports of:
# >> from langchain_community.embeddings import OpenAIEmbeddings
# You can use the langchain cli to **automatically** upgrade many imports. Please see documentation here <https://python.langchain.com/docs/versions/v0_2/>
# from langchain.embeddings import OpenAIEmbeddings
# from langchain_community.embeddings import OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain_core.vectorstores import InMemoryVectorStore

# OpenAI API KEY
# 테스트용 카카오톡 챗봇 채팅방에서 
# ChatGPT와 통신하기 위해 OpenAI API 키 입력
# 1. 아마존 웹서비스(AWS) 함수 lambda_handler -> 환경변수로 저장한 OpenAI API 키 'OPENAI_API' 불러오기
# 2. 1번에서 불러온 OpenAI API 키 'OPENAI_API'를 인자로 전달하여 OpenAI 클래스 객체 client 선언 및 생성하기 
OPENAI_KEY = os.environ['OPENAI_API'] 
client = OpenAI(api_key=OPENAI_KEY)

# TODO : 테스트용 카카오톡 챗봇 채팅방에서 사용자가 메시지 입력시 ("/ask ~~~" 또는 "/img ~~~")
#        아래와 같은 2가지 유형의 오류 메시지가 출력되어 함수 "getMessageFromGPT", "getImageURLFromDALLE" 새로 구현함. (2025.05.07 minjae)
# 오류 메시지 1 (함수 "getMessageFromGPT")
# You tried to access openai.ChatCompletion, but this is no longer supported in openai>=1.0.0 - see the README at https://github.com/openai/openai-python for the API.
# You can run `openai migrate` to automatically upgrade your codebase to use the 1.0.0 interface. 
# Alternatively, you can pin your installation to the old version, e.g. `pip install openai==0.28`
# A detailed migration guide is available here: https://github.com/openai/openai-python/discussions/742

# 오류 메시지 2 (함수 "getImageURLFromDALLE")
# You tried to access openai.Image, but this is no longer supported in openai>=1.0.0 - see the README at https://github.com/openai/openai-python for the API.
# You can run `openai migrate` to automatically upgrade your codebase to use the 1.0.0 interface. 
# Alternatively, you can pin your installation to the old version, e.g. `pip install openai==0.28`
# A detailed migration guide is available here: https://github.com/openai/openai-python/discussions/742

# ChatGPT 텍스트 응답 메시지 
# 참고 URL - https://github.com/openai/openai-python
def getMessageFromGPT(prompt): 
    response = client.responses.create(model="gpt-3.5-turbo", 
                                       instructions='You are a thoughtful assistant. Respond to all input in 300 words and answer in korea', 
                                       input=prompt)

    message = response.output_text
    return message

# DALLE2 이미지 응답
# 참고 URL - https://wikidocs.net/228931
def getImageURLFromDALLE(prompt):
    # response = openai.Image.create(prompt=prompt,n=1,size="512x512")
    response = client.images.generate(model="dall-e-3",
                                      prompt=prompt,
                                      size="1024x1024",
                                      quality="hd",
                                      n=1)

    image_url = response.data[0].url

    return image_url

# 함수 embedding_func 기능
# 파라미터 text로 텍스트 문장을 인자로 전달받으면
# 함수 openai.Embedding.create 호출 및 텍스트 임베딩 처리하여 변환된 벡터를 리턴하는 함수이다.
def embedding_func(prompt):
    # TODO : openai 패키지 openai-1.78.0 버전에서 openai.Embedding.create 함수가 더이상 사용되지 않아서
    #        (기존) openai.Embedding.create() => (변경) client.embeddings.create()
    #        변경 처리함. (2025.05.09 minjae)
    # 참고 URL - https://platform.openai.com/docs/guides/embeddings
    # 참고 2 URL - https://chatgpt.com/c/681db0bb-7768-8010-b66a-7d70982c9965
    embedding_result = client.embeddings.create(input = prompt, model="text-embedding-3-small")['data'][0]['embedding']
    return embedding_result

# 함수 cos_sim에 파라미터 A, B에 2가지 벡터를 인자로 전달 받으면,
# 코사인 유사도(Cosine Similarity)를 계산해서
# 코사인 유사도(Cosine Similarity) 값을 리턴해준다.
# def cos_sim(A, B):
#     return dot(A, B)/(norm(A)*norm(B)) 

# 함수 return_answer_candidate 기능?
# 함수 return_answer_candidate 파라미터 prompt에 전달된 인자 ex) 'AutoCAD 2024 버전 Language Pack 한국어 설치 방법'를
# 함수 embedding_func 호출하면서 인자로 query 그대로 전달 하여 텍스트 문자열 임베딩 처리 진행 
# 함수 return_answer_candidate 파라미터 df에 전달된 인자에 속한
# 임베딩된 벡터들 과의 코사인 유사도(Cosine Similarity)를 구하기 위해 함수 cos_sim 호출하기
# 코사인 유사도(Cosine Similarity) 구한 결과를 데이터 프레임 객체 df에 속한 열(Columns) - "similarity"에 저장
# 그리고 최종적으로 유사도("similarity")가 높은 상위 3개의 문장만 데이터셋 변수 answer_candidate에 할당해서 리턴해준다. 
# def return_answer_candidate(dataFrame, query):
#     query_embedding = embedding_func(query)
#     dataFrame["similarity"] = dataFrame.embedding.apply(lambda x: cos_sim(np.array(x),
#                                                                           np.array(query_embedding)))

    # 코사인 유사도(Cosine Similarity)를 구하고 
    # 이중 의미가 통하는 상위 3개의 문장들만 시맨틱 서치(Semantic Search)해서 구하고 나서 변수 answer_candidate에 할당한다.
    # answer_candidate = dataFrame.sort_values("similarity", ascending=False).head(3)
    # return answer_candidate

# TEXT 파일 청크(chunk) 단위 텍스트 기반 응답 메시지 
# 참고 URL - https://wikidocs.net/234014
# 참고 2 URL - https://wikidocs.net/234014
# 참고 3 URL - https://chatgpt.com/c/6811e007-9a5c-8010-b023-700a286c2618
# 참고 4 URL - https://wikidocs.net/231568
# 참고 5 URL - https://wikidocs.net/233998
def getMessageFromChunks(chunks, prompt):
    # 질문을 입력한 경우 
    if prompt:
        # 임베딩/ 시멘틱 인덱스 (API 요금 부과)
        embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_KEY)
        vectorstore = InMemoryVectorStore.from_texts(chunks, embeddings)
        # retriever = vectorstore.as_retriever()

        # vectorstore.similarity_search()
        # ----- 참고 URL - https://rudaks.tistory.com/entry/langchain-PDF%EC%9A%A9-%EC%A7%88%EB%AC%B8%EC%9D%91%EB%8B%B5-%EC%8B%9C%EC%8A%A4%ED%85%9C-%EA%B5%AC%EC%B6%95-1
        docs = vectorstore.similarity_search(prompt, k=1)
        
        print('[테스트] 질문과 유사한 응답 메시지: ', docs[0].page_content)

        # 질문하기
        llm = ChatOpenAI(temperature=0,
                         openai_api_key=OPENAI_KEY,
                         max_tokens=2000,
                         model_name='gpt-3.5-turbo',
                         request_timeout=120)
        chain = load_qa_chain(llm, chain_type="stuff")
        message = chain.run(input_documents=docs, question=prompt)

    else:
        message = '질문을 다시 입력해주세요.'

    return message

# TODO: 아래 주석친 코드 필요시 참고 (2025.05.09 minjae)
# def getMessageFromChunks(chunks, prompt):
#     # 질문을 입력한 경우 
#     if prompt:
#         dataFrame = pd.DataFrame(chunks, columns=['text'])
        
#         message = return_answer_candidate(dataFrame, prompt)

#     else:
#         message = '질문을 다시 입력해주세요.'

#     return message

# TODO: 아래 주석친 코드 필요시 참고 (2025.05.09 minjae)
# def getMessageFromChunks(chunks, prompt):
#     # 질문을 입력한 경우 
#     if prompt:
#         # 임베딩/ 시멘틱 인덱스 (API 요금 부과)
#         embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_KEY)
#         # TODO : 아마존 웹서비스(aws) 람다 함수(lambda function)에서 아래와 같은 오류 메시지가 출력되어 
#         #        (기존) FAISS.from_texts(chunks, embeddings) -> (변경) Chroma.from_texts(chunks, embeddings) 
#         #        (가존) docs = knowledge_base.similarity_search(prompt) -> (변경) retriever = db.as_retriever(search_type="similarity", search_kwargs={"k":1})
#         #        처리함. (2025.05.09 minjae)
#         # Could not import faiss python package. Please install it with pip install faiss-gpu (for CUDA supported GPU) or pip install faiss-cpu (depending on Python version).
#         # knowledge_base = FAISS.from_texts(chunks, embeddings)   # TEXT 파일 청크(chunk) 단위 텍스트  
#         # docs = knowledge_base.similarity_search(prompt)

#         vectorstore = Chroma.from_texts(texts=chunks, embedding=embeddings)
#         # retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k":1})
#         # results = vectorstore.similarity_search(prompt, k=1)
        
#         print('[테스트] 질문과 유사한 응답 메시지: ', vectorstore)

#         message = vectorstore

#         # 질문하기
#         # llm = ChatOpenAI(temperature=0,
#         #                  openai_api_key=OPENAI_KEY,
#         #                  max_tokens=2000,
#         #                  model_name='gpt-3.5-turbo',
#         #                  request_timeout=120)
#         # chain = load_qa_chain(llm, chain_type="stuff")
#         # message = chain.run(input_documents=docs, question=prompt)
#     # 질문을 입력하지 않은 경우
#     else:
#         message = '질문을 다시 입력해주세요.'
    
#     return message