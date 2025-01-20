# TODO : 아래 오류 메시지 해결하기 위해 가상환경 "ch10_env" -> 폴더 Lib -> 폴더 site-packages -> 폴더 googletrans -> client.py
#        -> def __init__ 생성자에 들어가는 파라미터 "proxies" 수정 (2025.01.17 jbh)
# 오류 메시지 
# "ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. 
# This behaviour is the source of the following dependency conflicts.
# chromadb 0.6.3 requires httpx>=0.27.0, but you have httpx 0.13.3 which is incompatible.      
# langsmith 0.2.10 requires httpx<1,>=0.23.0, but you have httpx 0.13.3 which is incompatible. 
# Successfully installed googletrans-3.1.0a0 h11-0.9.0 httpcore-0.9.1 httpx-0.13.3" 
# 참고 URL - https://codemoney.tistory.com/entry/python-error-googletrans%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC-%ED%98%B8%ED%99%98%EB%AC%B8%EC%A0%9C-httpx%EC%B6%A9%EB%8F%8C
# 참고 2 URL - https://stackoverflow.com/questions/72796594/attributeerror-module-httpcore-has-no-attribute-synchttptransport

# def __init__ 생성자에 들어가는 파라미터 "proxies" 수정
# (수정 전) proxies: typing.Dict[str, httpcore.SyncHTTPTransport] = None
# (수정 후) proxies: typing.Dict[str, httpcore.AsyncHTTPProxy] = None


##### 기본 정보 입력 #####
# Streamlit 패키지 추가
import streamlit as st
# PDF reader - PDF 파일에서 텍스트를 추출할 때 쓰는 PyPDF2 패키지 불러오기 
from PyPDF2 import PdfReader
# Langchain 패키지들
# 패키지 langchain-core 터미널 설치 명령어 
# 종속성 해결 문제를 피하려면 아래처럼 
# --no-deps 옵션을 사용하여 패키지 설치
# pip install --no-deps langchain-core==0.3.30
# 참고 URL - https://zziii.tistory.com/entry/ERROR-pips-dependency-resolver-does-not-currently-take-into-account-all-the-packages-that-are-installed
from langchain.chat_models import ChatOpenAI
# from langchain_openai import ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains.question_answering import load_qa_chain
# 구글 번역 API 불러오기
# 구글 번역기 패키지 터미널 설치 명령어
# 종속성 해결 문제를 피하려면 아래처럼 
# --no-deps 옵션을 사용하여 패키지 설치
# pip install --no-deps googletrans==3.1.0a0
# pip install --no-deps googletrans==4.0.0-rc1
# 참고 URL - https://github.com/ssut/py-googletrans/issues/400
# 참고 2 URL - https://zziii.tistory.com/entry/ERROR-pips-dependency-resolver-does-not-currently-take-into-account-all-the-packages-that-are-installed
from googletrans import Translator

##### 기능 구현 함수 #####
# 영어로 된 텍스트를 입력 받고 
# 구글 번역기 API 기능을 활용해서
# 한글 번역 결과를 화면에 출력해주는 함수
def google_trans(messages):
    google = Translator()
    # 영어로된 텍스트(messages)를 입력 파라미터로 받아서
    # 인스턴스 메서드 google.translate 호출하여 영어 -> 한글 번역 
    result = google.translate(messages, dest="ko")
    return result.text   # 한글 번역 결과 리턴  

##### 메인 함수 #####
def main():
    # st.set_page_config 사용하여 프로그램 타이틀(제목) "PDF analyzer" 지정
    st.set_page_config(page_title="PDF analyzer", layout="wide")

    # 사이드바
    with st.sidebar:

        # Open AI API 키 입력받기
        open_apikey = st.text_input(label='OPENAI API 키', placeholder='Enter Your API Key', value='',type='password')
        
        # 입력받은 API 키 표시
        if open_apikey:
            # LangChain 모듈에 OpenAI API 키를 넣기 위해서
            # st.session_state["OPENAI_API"]에 OpenAI API 키 값 open_apikey 할당 
            st.session_state["OPENAI_API"] = open_apikey 
        st.markdown('---')
        
    # 메인공간
    st.header("PDF 내용 질문 프로그램📜") # 프로그램 제목 "PDF 내용 질문 프로그램" 지정 
    st.markdown('---')
    st.subheader("PDF 파일을 넣으세요") # PDF 파일 업로드 하는 기능 상단에 SubHeader "PDF 파일을 넣으세요" 지정  
    # PDF 파일 받기
    # 함수 st.file_uploader 사용하면 PDF 파일 뿐만 아니라 다양한 종류의 파일을 Input(또는 업로드) 받을 수 있다.
    # 드래그 앤 드롭 또는 버튼 Browse files 클릭하여 PDF 파일 업로드 가능 
    # 주의사항 - streamlit 사용하여 파일을 Input(또는 업로드) 받을 때는 
    #           200 MB 이하인 파일만 Input 받을 수 있다.
    #           왜냐하면 내부적으로 연산 속도를 최적화 시키기 위해서
    #           메모리 제한(Limit)을 200 MB로 걸어놓았기 때문이다.
    #           단, streamlit에서는 메모리 제한(Limit)을 200 MB 를 풀 수도 있다.
    # 참고 URL - https://docs.streamlit.io/develop/api-reference/widgets/st.file_uploader
    # Input(또는 업로드)으로 받은 파일 정보를 pdf라는 변수에 저장 
    pdf = st.file_uploader(" ", type="pdf")
    
    if pdf is not None:
        # PDF 파일 텍스트 추출하기
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            # PdfReader 클래스 객체 pdf_reader 사용하여 
            # PDF 파일에 있는 텍스트 추출(page.extract_text()) 해서 text 변수에 저장 
            text += page.extract_text()
        # 청크 단위로 분할하기
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        # text_splitter.split_text 사용하여 추출된 텍스트 변수 text를
        # chunk 단위로 쪼개서 변수 chunks에 할당 
        chunks = text_splitter.split_text(text)

        st.markdown('---')
        st.subheader("질문을 입력하세요")
        # 사용자 질문 받기
        # 사용자가 질문 입력한 텍스트를 변수 user_question에 할당 
        user_question = st.text_input("Ask a question about your PDF:")
        # 사용자로 부터 질문을 입력받은 경우 (user_question)
        if user_question:
            # 위에서 chunk 단위로 쪼개서 할당한 변수 chunks를  
            # 임베딩/ 시멘틱 인덱스 처리 진행 
            # 임베딩 하는 것도 OpenAI API 요금 부과될 수 있기 때문에
            # 사용자로 부터 질문을 입력받은 경우에만 OpenAI API 요금이 부과되고 
            # 사용자로 부터 질문을 입력받지 않은 경우에는 OpenAI API 요금이 부과되지 않는다.
            embeddings = OpenAIEmbeddings(openai_api_key=st.session_state["OPENAI_API"])
            knowledge_base = FAISS.from_texts(chunks, embeddings)
            
            # 함수 knowledge_base.similarity_search 사용해서 
            # 질문(user_question)과 가장 유사한 chunk들을 추출해서 변수 docs에 저장
            docs = knowledge_base.similarity_search(user_question)

            # 질문하기
            # ChatOpenAI 클래스 객체 llm 생성 및 
            # ChatGPT의 언어 모델 설정(model_name='gpt-3.5-turbo')
            llm = ChatOpenAI(temperature=0,
                    openai_api_key=st.session_state["OPENAI_API"],
                    max_tokens=2000,
                    model_name='gpt-3.5-turbo',
                    request_timeout=120
                    )
            # 함수 load_qa_chain 사용해서 인스턴스 chain 생성 
            chain = load_qa_chain(llm, chain_type="stuff")
            # 답변에 사용할 chunk값이 담긴 변수 docs를 함수 chain.run의 입력 파라미터 값으로 넣어주고
            # 사용자의 질문(user_question) 또한 함수 chain.run의 입력 파라미터 값으로 넣어준다.
            # ChatGPT로 부터 얻은 답변 결과를 변수 response에 저장 
            response = chain.run(input_documents=docs, question=user_question)
            # 답변결과
            # st.info 사용하여 ChatGPT로 부터 얻은 답변 결과 화면 출력 
            st.info(response)
            #한국어로 번역하기
            # 버튼 "번역하기" 클릭한 경우
            if st.button(label="번역하기"):
                # ChatGPT로 부터 얻은 답변 결과가 담긴 변수 response를
                # 함수 google_trans의 인자값으로 전달 
                # 영어 -> 한글로 번역한 답변 결과를 변수 trans에 저장
                trans = google_trans(response)
                st.success(trans) # st.success 사용해서 프로그램에 영어 -> 한글로 번역한 답변 결과 출력 

if __name__=='__main__':
    main()