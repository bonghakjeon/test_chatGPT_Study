# PDF 문서 파일을 넣으면 해당 내용을 토대로 
# ChatGPT가 Hallucination(환각) 증상 일으키지 않고 
# 답변해주는 프로그램 제작하기

# 사용자가 ChatGPT에게 질문해보면 
# ChatGPT가 사용자의 질문에 대한 답변을 생성하는게 아니라 
# ChatGPT는 내부적으로 PDF 내용 기반으로 질문에 대한 답변을 찾아서 
# 사용자에게 답변해준다.

# 해당 프로그램에서 
# PDF 내용 기반 질문에 ChatGPT가 답변을 할 때, 
# 보통은 PDF 파일에서 추출된 글의 길이가 
# Max Token 이상일 경우가 존재한다.
# 이 때 만약 질문 내용에 대한 답변이 
# 해당 PDF 파일 내에서 어디에 위치하고 있는지 알 수 있다면
# 해당 부분만 따로 발췌해서 ChatGPT한테 다음과 같이 내 질문은 이것이고
# 그 질문에 대한 내용은 어느 위치에 있으니 이 부분에 위치한 내용만 읽고 대답해줘
# 라고 사용자가 물어볼 수만 있다면 더이상 글의 길이가 
# Max Token 이상일 경우를 걱정할 필요가 없다.
# 뿐만 아니라 PDF 파일에 존재하는 내용을 토대로 답변을 해주기 때문에
# 거짓 정보를 생성하는 Hallucination(환각) 증상 또한 없다.
# 여기서 가장 중요한 점은 내 질문에 대한 답변이 
# 도대체 어디에 있는지 찾아내는 과정이다.

# 프로그램 구조 
# *** 랭체인(LangChain) 프레임워크 사용 *** 
# 1. 사용자가 PDF 파일 입력 
# 2. 해당 PDF 파일 안에서 텍스트를 추출 
# 3. 2번에서 추출한 텍스트를 chunk 단위(사용하는 ChatGPT 언어 모델의 Max Token 보다 작은 크기인 한 묶음)로 분할 
# 4. 인간의 자연어를 컴퓨터가 알아들을 수 있는 언어인 벡터로 번역해주는 텍스트 임베딩 작업 실시 
# 5. 사용자의 질문 또한 컴퓨터의 언어인 벡터로 번역하는 텍스트 임베딩 작업 실시
# 6. 사용자의 질문과 유사한 chunk를 찾는 시맨틱서치(Semantic Search) 실행
# 7. 시맨틱서치(Semantic Search) 과정을 거치면 사용자의 질문과 유사한 내용이 포함되어 있는
#    몇개의 chunk 내용을 추출하게 된다. 
# 8. 마지막으로 ChatGPT에게 사용자의 질문은 이거고 이게 포함된 내용은
#    시맨틱서치(Semantic Search) 과정을 거쳐서 추출한 
#    몇개의 chunk 내용 안에 있으니 이 chunk 내용들을 읽고 사용자의 질문에 답해줘 라고 전달함.
# 9. ChatGPT가 마치 PDF 파일 내용을 다 읽고 사용자의 질문에 답변을 하는 것처럼
#    답변을 생성해서 화면으로 답변 출력 (데이터 시각화)

# 텍스트 임베딩
# 텍스트 문자열을 벡터화하는 자체를 임베딩이라 부른다.
# 사람은 텍스트를 읽을 때 텍스트를 바로 읽어서 이해한다면
# 텍스트를 처리하는 인공지능 모델들은 텍스트를 직접적으로 입력으로 
# 처리하는 것이 아니라 텍스트 임베딩 과정을 통해 벡터로 수치화한 뒤에 처리한다.
# 다시 말해 문서, 문장, 단어 등의 텍스트를 인공지능 모델이 처리할 때는
# 아래와 같이 [0.12, 0.34, 0.75, -0.12] 이런 식으로 실수가 나열된 값인
# 벡터로 변환해서 입력을 사용함.
# 아래처럼 변환하고자 하는 단위에 따라서 텍스트를 벡터화하는 과정의 용어가 조금씩 달라진다.
# 예를들어 
# 1) 단어를 임베딩 한다면 단어(Word) 임베딩
# 2) 문장을 임베딩 한다면 문장 임베딩
# 3) 문서를 임베딩 한다면 문서 임베딩
# '사과' -> 단어(Word) 임베딩 -> 벡터 : [0.12, 0.34, 0.75, -0.12]
# '안녕하세요' -> 문장 임베딩 -> 벡터 : [0.57, 0.25, 0.85, 3.24]
# '서울 청년 정책이 ... 중략 ...' -> 문서 임베딩 -> 벡터 : [0.54, 0.84, 0.28, 0.59]

# OpenAI 임베딩 모델
# 1536개의 축(차원)으로 이루어짐 
# OpenAI 임베딩 모델을 사용하면 각 단어를 1536개의 의미를 가진 축(차원)으로 임베딩 처리 해준다.
# 하나의 문장이나 단어를 OpenAI 임베딩 모델을 통해 임베딩 처리하면 총 1536개의 실수를 가진 벡터가 생성된다.
# 아래 참고 URL로 접속하면 OpenAI에서 지원하는 임베딩 모델의 사용방법을 확인할 수 있다.
# 참고 URL - https://platform.openai.com/docs/guides/embeddings/use-cases

# OpenAI 임베딩 모델도 똑같이 OpenAI 패키지를 설치하고 
# Python을 활용하게 간단하게 사용 가능하다.

import openai
import numpy as np
from numpy import dot
from numpy.linalg import norm
import pandas as pd

openai.api_key = 'API_key 입력'

# OpenAI 임베딩 모델 안에 있는 함수 openai.Embedding.create 사용해서 벡터 생성하기
# 함수 파라미터 input에 전달 받은 인자 '저는 배가 고파요' 텍스트를 활용해서 임베딩 처리
# 함수 파라미터 model에 전달 받은 인자 'text-embedding-ada-002' 임베딩 모델 활용
# 'text-embedding-ada-002' 임베딩 모델은 기본적으로 텍스트를 임베딩하면
# 총 1536개의 축(차원)의 숫자값이 나열된 벡터로 변환한다.
# 그래서 '저는 배가 고파요'라는 문자열도 1536개의 축(차원)의 숫자가 나열된 벡터 값으로 변환이 됐습니다.
# 해당 변환된 벡터 값들이 어떤 의미인지는 사람이 해석하기는 불가능하다.
# 여기서 확인할 수 있는 것은 텍스트가 벡터로 변환됐다는 사실이다.
embedding_result = openai.Embedding.create(input = '저는 배가 고파요', model="text-embedding-ada-002")['data'][0]['embedding']
print(embedding_result)   # 다양한 실수값이 나열된 벡터값들 출력 
print('변환된 벡터 갯수(축/차원) - ' + str(len(embedding_result)))   # 텍스트 '저는 배가 고파요'가 변환된 벡터값의 갯수 출력

# 텍스트 문장 '저는 배가 고파요'와 유사한 텍스트 문장 찾기 
# 데이터 프레임이란 Python의 Pandas 라이브러리로 사용할 수 있는
# 테이블 형태의 데이터를 의미한다.
# 비유하자면 프로그래밍 코드로 제어하는 Python의 Excel 같은것이라고 보면 된다.
# 실제로 행과 열을 갖고 있기 때문에 해당 데이터 프레임은 Excel과 호환성을 갖고 있어서
# Excel로 파일을 불러오거나 저장하기도 한다.
# 아래의 코드는 총 6개의 텍스트 문장으로 구성된 임의의 데이터를 
# 'text' 라는 열(columns)에 할당하여 6행 1열의 데이터 프레임를 만드는 코드이다.

# 총 6개의 텍스트 문장으로 구성된 임의의 데이터 리스트 객체 data 생성 
data = ['저는 배가 고파요',
        '저기 배가 지나가네요',
        '굶어서 허기가 지네요',
        '허기 워기라는 게임이 있는데 즐거워',
        '스팀에서 재밌는 거 해야지',
        '스팀에어프라이어로 연어구이 해먹을거야']

# 데이터 리스트 객체 data를 pd.DataFrame 사용하여 데이터 프레임 변환 후
# 데이터 프레임 객체 df 생성
df = pd.DataFrame(data, columns=['text'])
print('데이터 프레임 열(columns) - text')
print(df) 

# 데이터 프레임 객체 df에 'text' 라는 열(columns)에 존재하는
# 6개의 텍스트 데이터들을 임베딩해서 벡터로 변환하고 
# 새로운 'embedding' 이라는 열(columns)을 만들어서 저장하는 코드이다.
# 함수 embedding_func 기능
# 파라미터 text로 텍스트 문장을 인자로 전달받으면
# 함수 openai.Embedding.create 호출 및 텍스트 임베딩 처리하여 변환된 벡터를 리턴하는 함수이다.
def embedding_func(text):
    embedding_result = openai.Embedding.create(input = text, model="text-embedding-ada-002")['data'][0]['embedding']
    return embedding_result

# Pandas 패키지의 존재하는 기능을 활용해서 'embedding' 라는 열(columns)에
# 텍스트를 임베딩한 결과를 저장한다.
df['embedding'] = df.apply(lambda row: embedding_func(row.text), axis=1)
print('데이터 프레임 열(columns) - embedding')
# 데이터 프레임 열(columns)
# 'text'에 존재하는 문자열 텍스트 출력 
# 'embedding'에 존재하는 OpenAI 임베딩 모델을 활용해서 변환된 벡터 데이터 출력 
print(df) 

# 아래는 OpenAI 임베딩 모델을 활용해서 변환된 벡터 데이터들 중에서
# 가장 유사한 두 개의 벡터를 찾으면 
# 해당 두 개의 벡터와 매핑된 두 개의 텍스트 문장은 유사한 의미를 가진 문장이다.
# 유사한 두 개의 벡터를 찾는 가장 대표적인 방법인 
# 코사인 유사도에 대한 실습 코드이다.

# 코사인 유사도란?
# 두 벡터 간의 코사인 각도라는 개념을 이용해서 
# 두 벡터가 얼마나 유사한지 유사도 값을 얻을 수 있는 방법이다.
# 유사도 값 범위는 -1 ~ +1 사이이며,
# 유사도가 높을수록 +1에 가깝고
# 유사도가 낮을수록 -1에 가깝게 된다.
# 여기서 코사인 유사도란 각 벡터 간의 각도를 뜻한다.
# 즉, 2차원 좌표평면상에 
# 벡터A에 매핑된 단어와 벡터B에 매핑된 단어의 코사인 유사도 값을 구하면
# 벡터A와 벡터B사이의 각도를 통해서 구할 수 있다.
# 이 때, 벡터A와 벡터B사이의 각도가 작을수록 코사인 유사도 값이 높아져서
# 유사도가 높은 벡터로 찾을 수가 있다.

# 함수 cos_sim에 파라미터 A, B에 2가지 벡터를 인자로 전달 받으면,
# 코사인 유사도(Cosine Similarity)를 계산해서
# 코사인 유사도(Cosine Similarity) 값을 리턴해준다.
def cos_sim(A, B):
    return dot(A, B)/(norm(A)*norm(B)) 

# 3가지 벡터 변수 (vec1, vec2, vec3)에 코사인 유사도(Cosine Similarity) 계산
vec1 = np.array([0,1,1,1])
vec2 = np.array([1,0,1,1])
vec3 = np.array([2,0,2,2])

# '벡터2(vec2)와 벡터3(vec3)의 유사도'가 1로 가장 높다
# 왜냐면 벡터2(vec2)에 존재하는 데이터 [1,0,1,1]에 존재하는 각 요소를 2배 곱한 값이
# 벡터3(vec3) [2,0,2,2]와 같고 서로 패턴이 유사하기 때문이다.
print('벡터1과 벡터2의 유사도 :', cos_sim(vec1, vec2))
print('벡터1과 벡터3의 유사도 :', cos_sim(vec1, vec3))
print('벡터2와 벡터3의 유사도 :', cos_sim(vec2, vec3))


# 텍스트 문자열 '아무 것도 안 먹었더니 꼬르륵 소리가나네'라는 문자열을 기준으로
# 해당 문자열과 가장 유사한 의미를 지니는 문자열을 벡터 시뮬리티 방법을 활용해서 찾는 실습 코드이다.
# 물론 위에서 생성한 데이터 프레임 객체 df에 속한 6개의 데이터셋 중에서
# 해당 텍스트 문자열 '아무 것도 안 먹었더니 꼬르륵 소리가나네'과 가장 유사한 뜻을 가진 
# 문장을 찾는 실습을 진행한다.
# 함수 return_answer_candidate 기능?
# 함수 return_answer_candidate 파라미터 query에 전달된 인자 '아무 것도 안 먹었더니 꼬르륵 소리가나네'를
# 함수 embedding_func 호출하면서 인자로 query 그대로 전달 하여 텍스트 문자열 임베딩 처리 진행 
# 함수 return_answer_candidate 파라미터 df에 전달된 인자에 속한
# 임베딩된 벡터들 과의 코사인 유사도(Cosine Similarity)를 구하기 위해 함수 cos_sim 호출하기
# 코사인 유사도(Cosine Similarity) 구한 결과를 데이터 프레임 객체 df에 속한 열(Columns) - "similarity"에 저장
# 그리고 최종적으로 유사도("similarity")가 높은 상위 3개의 문장만 데이터셋 변수 top_three_doc에 할당해서 리턴해준다. 
def return_answer_candidate(df, query):
    query_embedding = embedding_func(query)
    df["similarity"] = df.embedding.apply(lambda x: cos_sim(np.array(x),
                                                            np.array(query_embedding)))

    # 코사인 유사도(Cosine Similarity)를 구하고 
    # 이중 의미가 통하는 상위 3개의 문장들만 시맨틱 서치(Semantic Search)해서 구하고 나서 변수 top_three_doc에 할당한다.
    top_three_doc = df.sort_values("similarity", ascending=False).head(3)
    return top_three_doc

sim_result = return_answer_candidate(df, '아무 것도 안 먹었더니 꼬르륵 소리가나네')

# 텍스트 문자열 '아무 것도 안 먹었더니 꼬르륵 소리가나네'과 
# 가장 유사한 텍스트 문자열은 '굶어서 허기가 지네요' 이다.
# 왜냐면 유사도("similarity")가 높은 상위 3개의 문장 중에서
# 코사인 유사도(Cosine Similarity) 값이 '0.838963'으로 가장 높기 때문이다.
# 그 다음으로 유사한 텍스트 문자열은 코사인 유사도(Cosine Similarity) 값이 '0.821658'인
# '스팀에어프라이어로 연어구이 해먹을거야' 이고 
# 마지막으로 유사한 텍스트 문자열은 코사인 유사도(Cosine Similarity) 값이 '0.814633'인
# '저는 배가 고파요' 이다.
# 그 외 유사하지 않은 다른 문장들은 코사인 유사도(Cosine Similarity)를 구하는 과정에서 걸러지고
# 의미가 통하는 상위 3개의 문장들만 시맨틱 서치(Semantic Search)해서 구한다.
print(sim_result)

# Langchain을 활용하여 PDF 내용 질문 방법 익히기
# 파이썬 패키지 "PyPDF2" 터미널 설치 명령어
# pip install PyPDF2

# 패키지 불러오기
from PyPDF2 import PdfReader

# PDF 파일 경로를 지정하여 불러오기. 
pdf_reader = PdfReader('Summary of ChatGPTGPT-4 Research.pdf')

# 텍스트 추출하기
total_text = ""
for page in pdf_reader.pages:
    total_text += page.extract_text()

# print('---------- 텍스트 추출하기 ----------')
# print(total_text)

# 텍스트 청크(Chunk) 사이즈로 자르기
# 랭체인 프레임워크 "langchain" 터미널 설치 명령어
# pip install -U langchain-community
from langchain.text_splitter import CharacterTextSplitter

text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )

chunks = text_splitter.split_text(total_text)

# print('----- total_text Chunk len -----')
# print(len(chunks))
# print('----- chunks[0] Messages -----')
# 인덱스 0에 존재하는 chunk 문서 묶음 텍스트로 출력
# print(chunks[0])
# print('----- chunks[1] Messages -----')
# 인덱스 1에 존재하는 chunk 문서 묶음 텍스트로 출력
# print(chunks[1])

# 텍스트 임베딩 / 시멘틱 인덱싱하기 
# 패키지 "tiktoken" 터미널 설치 명령어 
# pip install tiktoken
# 패키지 "faiss-cpu" 터미널 설치 명령어 
# pip install faiss-cpu
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(api_key="API_key 입력")
knowledge_base = FAISS.from_texts(chunks, embeddings)
# PDF 파일 "Summary of ChatGPTGPT-4 Research.pdf" 내에서 
# 사용자의 질문 "where can i use chatGPT"과 가장 유사한 내용이 포함되어 있는
# Chink 4개 추출하기 (질문에 대한 답변이 포함되어 있기 보다는 질문과 가장 유사한 의미를 내포하는 chunk 묶음을 뽑은 것이다.)
docs = knowledge_base.similarity_search("where can i use chatGPT")
# print(docs)

# ChatGPT에게 최종 질문하기(load_qa_chain)
# 위에서 추출한 chunk 묶음 "docs"와 사용자의 질문 "where can i use chatGPT"을 같이 포함해서 
# ChatGPT에게 질문에 대한 답변을 요청하기 
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain

llm = ChatOpenAI(temperature=0,
                 openai_api_key="API_key 입력",
                 max_tokens=3000,
                 model_name='gpt-3.5-turbo',
                 request_timeout=120)

chain = load_qa_chain(llm, chain_type="stuff")

# 함수 chain.run 호출하면 
# 사용자의 질문은 "where can i use chatGPT" 이고 
# 그리고 이질문에 대한 답변은 함수 chain.run 매개변수 input_documents로 넣어준
# 총 4개의 chunk(docs)를 ChatGPT 너가 읽어보고 답변 해주면 된다.
response = chain.run(input_documents=docs, question="where can i use chatGPT")
print('----- ChatGPT에게 최종 질문하기(load_qa_chain) -----')
print(response)

# Langchain을 활용한 또다른 질문방법 RetrivalQA
# 패키지 "chromadb" 터미널 설치 명령어 
# 종속성 해결 문제를 피하려면 아래처럼 
# --no-deps 옵션을 사용하여 패키지 설치
# 참고 URL - https://zziii.tistory.com/entry/ERROR-pips-dependency-resolver-does-not-currently-take-into-account-all-the-packages-that-are-installed
# pip install --no-deps chromadb
# pip install -U langchain-chroma
# pip install -U --no-deps langchain-chroma

from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma

db = Chroma.from_texts(chunks, embeddings)
retriever = db.as_retriever(search_type="similarity", search_kwargs={"k":2})

qa = RetrievalQA.from_chain_type(
    llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=True)
query = "where can i use chatGPT"
result = qa({"query": query})
print(result["result"])
print(result["source_documents"])

# 이전 질문 기록을 포함하여 질문하는 방법 
from langchain.memory import ConversationBufferMemory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

from langchain.chains import ConversationalRetrievalChain
qa = ConversationalRetrievalChain.from_llm(llm=llm, retriever=retriever, memory=memory)

chat_history = []
query = "where can i use chatGPT"
result = qa({"question": query, "chat_history": chat_history})
print(result["answer"])

#이전 질문 및 답변 저장
chat_history = [(query, result["answer"])]
#다시 질문
query = "which field is the most used?"
result = qa({"question": query, "chat_history": chat_history})
print(result["answer"])