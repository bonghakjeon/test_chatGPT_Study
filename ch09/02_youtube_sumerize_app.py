# 가상환경 폴더 "ch09_env" 생성 터미널 명령어
# python -m venv ch09_env

# 가상환경 폴더 "ch09_env" 활성화 터미널 명령어
# ch09_env\Scripts\activate.bat

# OpenAI API 터미널 설치 명령어 
# pip install openai==0.28.1

# 랭체인(langchain) 공식 문서 
# 참고 URL - https://python.langchain.com/docs/integrations/chat/openai/
# 참고 2 URL - https://python.langchain.com/api_reference/openai/index.html

# 랭체인(langchain) 프레임워크 터미널 설치 명령어
# (X) pip install langchain
# (O) pip install -U langchain-community

# 유튜브 대본 api 터미널 설치 명령어
# pip install youtube_transcript_api

# 유튜브 대본(스크립트) 번역할 동영상 URL 주소
# 참고 URL - https://www.youtube.com/watch?v=Pn-W41hC764 

# OpenAI에서 텍스트의 토큰수를 세어야 될 때 사용하는 패키지 "tiktoken" 설치하기 
# pip install tiktoken

# 영어 -> 한글 구글 번역 패키지 "googletrans" 터미널 설치 명령어
# pip install googletrans==3.1.0a0

##### 기본 정보 입력 #####
import streamlit as st   # streamlit 패키지 불러오기 
# 정규 표현식 확인을 위해 (URL 분석을 위해) re 파이썬 기본 내장 패키지 불러오기
# 정규 표현식 사용하는 이유? 
# 유튜브 URL의 형식 유효성 체크하기 위해서이다.
# 유튜브 URL의 형식 (예) https://www.youtube.com/watch?~~~~~
import re 
# 유튜브 대본(스크립트)요약할 때 사용할 Langchain 패키지 불러오기
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
# 유튜브 대본(스크립트) 불러오기
# 랭체인(langchain) 프레임워크 안에 YoutubeLoader 불러오기 
from langchain.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chat_models import ChatOpenAI
# 요약한 유튜브 대본(스크립트)을 영어 -> 한국어 번역을 위해 googletrans 패키지 불러오기
from googletrans import Translator

##### 기능 구현 함수 #####
# googletrans 패키지 사용 영어 -> 한국어 번역
def google_trans(messages):
    google = Translator()
    # 영어 -> 한국어 번역
    result = google.translate(messages, dest="ko")

    return result.text

# 정규 표현식 확인을 위해 (URL 분석을 위해) Youtube URL 유효성 체크
# Youtube URL 주소가 잘못된 URL 입력이 있을시에는 더이상 분석하지 않고 안내(오류) 메시지 출력 
def youtube_url_check(url):
    pattern = r'^https:\/\/www\.youtube\.com\/watch\?v=([a-zA-Z0-9_-]+)(\&ab_channel=[\w\d]+)?$'
    match = re.match(pattern, url)
    return match is not None

##### 메인 함수 #####
def main():

    #기본 설정
    # 함수 st.set_page_config 사용해서 프로그램 제목(page_title) 지정
    st.set_page_config(page_title="YouTube Summerize", layout="wide")

    # session state 초기화
    # 프로그램에서 어떤 이벤트가 발생해도 정보를 잃지 않고 유지할 3가지 session_state 지정하기 
    # session_state 초기화 코드 
    # "flag" - 유튜브 대본(스크립트) 요약 진행여부 알려주는 flag 의미 (유튜브 대본(스크립트) 요약을 무의미하게 중복 진행해서 API 요금이 발생하는 것을 방지하는 역할이다.)
    #          true - 유튜브 대본(스크립트) 요약 진행 X
    #          false - 유튜브 대본(스크립트) 요약 완료 O
    if "flag" not in st.session_state:
        st.session_state["flag"] = True
    # "OPENAI_API" - OPENAI API 키를 의미
    if "OPENAI_API" not in st.session_state:
        st.session_state["OPENAI_API"] = ""
    # "summerize" - 유튜브 대본(스크립트)을 영어로 요약된 결과 저장 
    # "summerize"를 st.session_state 저장하는 이유?
    # 프로그램 실행 중에 다른 이벤트가 발생해도 저장된 정보를 사용해서 
    # 화면에 출력(데이터 시각화)해서 반복된 요약 진행을 막기 위해서 
    # 유튜브 대본(스크립트) 요약 내용도 st.session_state["summerize"] 활용해서 
    # 유튜브 대본(스크립트) 요약 내용을 저장한다.
    if "summerize" not in st.session_state:
        st.session_state["summerize"] = ""

    # 제목
    # st.header 앨리먼트 사용해서 프로그램 제목 "📹영어 YouTube 내용 요약/대본 번역기" 지정  
    st.header(" 📹영어 YouTube 내용 요약/대본 번역기")
    st.markdown('---')   # markdown 사용해서 구분선 생성(st.markdown('---'))
    # URL 입력받기
    # st.subheader 앨리먼트 사용해서 프로그램 안내 메시지 "YouTube URL을 입력하세요" 지정 
    st.subheader("YouTube URL을 입력하세요")
    # st.text_input 앨리먼트 사용해서 유튜브 URL 주소 받아와서 
    # 변수 youtube_video_url에 유튜브 URL 주소 저장 
    youtube_video_url = st.text_input("  ",placeholder="https://www.youtube.com/watch?v=**********")

    # 사이드바 생성
    with st.sidebar:
        # st.text_input 앨리먼트 사용해서 Open AI API 키 입력받기
        open_apikey = st.text_input(label='OPENAI API 키', placeholder='Enter Your API Key', value='',type='password')
        
        # 입력받은 API 키 표시
        if open_apikey:
            # 위에서 st.text_input 앨리먼트 사용해서 
            # 입력받은 Open AI API 키값이 담긴 변수 open_apikey를
            # 변수 st.session_state["OPENAI_API"]에 저장 
            # 변수 st.session_state["OPENAI_API"] 사용 이유?
            # 랭체인(LangChain) 프레임워크의 함수 안에 
            # Open AI API 키값을 인자로 전달하기 위해서 
            # 따로 변수 st.session_state["OPENAI_API"]를 생성함.
            st.session_state["OPENAI_API"] = open_apikey 
        st.markdown('---')   # markdown 사용해서 구분선 생성(st.markdown('---'))


    # 변수 youtube_video_url의 길이(len())가 2초과일 경우
    # 즉 변수 youtube_video_url에 할당된 유튜브 URL 주소가 존재하는 경우만 if절 실행
    if len(youtube_video_url)>2:
        # 유튜브 URL 주소 유효성 체크 
        # 해당 유튜브 URL 주소가 정상적으로 입력되는지를 확인
        # 비정상적인 유튜브 URL 주소가 입력된 경우 
        if not youtube_url_check(youtube_video_url):
            # 오류 메시지 출력 
            st.error("YouTube URL을 확인하세요.")
        # 정상적인 유튜브 URL 주소가 입력된 경우
        else:
            # 유튜브 영상 출력되는 크기를 조절하기 위해
            # 변수 width, side 사용 및 
            # st.columns 앨리먼트 사용하여 공간을 세로로 3등분(side, width, side) 처리
            # 3등분 비율 (1 : 2 : 1)로 하고 
            # 이중 가장 큰 가운데 비율 "2"를 담을 공간의 이름(변수)를 container로 설정 
            width = 50  
            side = width/2 # side는 25 
            _, container, _ = st.columns([side, width, side])

            # streamlit 패키지 video 앨리먼트 사용하여 
            # URL 주소 입력받은 유튜브 영상을 화면의 가운데 공간(비율 "2"공간 container) 
            # 보여주기 (유튜브 재생 기능 포함)
            container.video(data=youtube_video_url)
            
            # 유튜브 대본(스크립트) 원본 추출하기
            # 함수 YoutubeLoader.from_youtube_url에 대본을 불러오고 싶은 
            # 유튜브 URL 주소값이 담긴 변수 youtube_video_url를 인자로 전달
            loader = YoutubeLoader.from_youtube_url(youtube_video_url)
            transcript = loader.load()   # 인스턴스 loader의 인스턴스 메소드 load() 사용해서 대본 추출 
        
            st.subheader("요약 결과")
            if st.session_state["flag"]:
                # 랭체인(langchain) 프레임워크 안에서 사용할
                # ChatGPT 언어 모델 설정하기 
                # LLM 모델 설정
                llm = ChatOpenAI(temperature=0,
                        # OpenAI API 키 입력 
                        openai_api_key=st.session_state["OPENAI_API"],
                        max_tokens=3000,
                        # ChatGPT 3.5-turbo 모델 입력 
                        model_name="gpt-3.5-turbo",
                        request_timeout=120
                    )
                
                # 요약 프롬프트 설정
                # 요약에 사용할 프롬프트 작성 
                # PromptTemplate 메소드 사용하여 프롬프트를 일종의 템플릿을 갖춰서 작성할 수 있도록 함.
                # 각각의 분할된 문서 조각을 요약 및 요청하는 프롬프트이다.
                # 각각의 chunck 를 요약하기
                prompt = PromptTemplate(
                    # 아래 시스템 프롬프트 문자열 "각각의 분할된 문서들을 요약해줘" 작성 
                    template="""Summarize the youtube video whose transcript is provided within backticks \
                    ```{text}```
                    """, input_variables=["text"]
                )
                # 요약된 내용들을 취합하여 다시한번 요약하기 
                combine_prompt = PromptTemplate(
                    # 아래 시스템 프롬프트 문자열 "유튜브 대본(스크립트) 요약한 것을 조합해서 다시 한번 8개에서 10개 사이로 문장을 요약해줘" 작성
                    template="""Combine all the youtube video transcripts  provided within backticks \
                    ```{text}```
                    Provide a concise summary between 8 to 10 sentences.
                    """, input_variables=["text"]
                )

                # 대본 쪼개기
                # 함수 RecursiveCharacterTextSplitter 사용해서 인스턴스 text_splitter 생성
                # 함수 RecursiveCharacterTextSplitter 파라미터 
                # 1) "chunk_size"는 각각의 분할한 문서의 사이즈를 뜻한다.
                # 2) "chunk_overlap"은 문서를 분할할 때 앞에 문서와 뒤에 문서의 내용을 겹치게(Overlap) 해서 분할할 수 있다.
                #    "chunk_overlap" 값이 0인 경우 문서의 내용을 겹치지 않고 (Not Overlap)
                #     텍스트가 쪼개진다.
                text_splitter = RecursiveCharacterTextSplitter(chunk_size=4000, chunk_overlap=0)
                # 인스턴스 메서드 text_splitter.split_documents 사용해서 
                # 해당 메서드 안에 위에서 추출한 유튜브 대본(스크립트)가 들어있는 변수 transcript를 인자로 전달
                text = text_splitter.split_documents(transcript)

                #요약 실행
                # 함수 load_summarize_chain 파라미터 
                # 1. ChatGPT 언어 모델 인스턴스 llm
                # 2. 각각의 분할된 대본을 요청할 때 사용하는 프롬프트 map_prompt=prompt 
                # 3. 최종적으로 분할되어 있는 요약된 내용들을 조합해서 최종 요약본을 작성할 때 사용하는 프롬프트 combine_prompt=combine_prompt
                # 인스턴스 chain 생성 
                chain = load_summarize_chain(llm, chain_type="map_reduce", verbose=False,
                                             map_prompt=prompt, combine_prompt=combine_prompt)
                # 유튜브 대본(스크립트) 요약 시작하기 
                # 인스턴스 메서드 chain.run(text) 실행해야 유튜브 대본(스크립트) 요약이 시작된다.
                # 유튜브 대본(스크립트) 요약을 진행할 변수 text를
                # 인스턴스 메서드 chain.run(text) 파라미터로 넣고 
                # 유튜브 대본(스크립트) 요약 시작하여 해당 요약한 결과를 
                # 변수 st.session_state["summerize"]에 넣기
                st.session_state["summerize"] = chain.run(text)
                # 요약 완료 결과값 False를 변수 st.session_state["flag"]에 저장 
                st.session_state["flag"]=False
            # st.success 앨리먼트 사용하여 최종적으로 요약된 결과가 담긴 변수 st.session_state["summerize"]를
            # 활용해서 화면에 출력(데이터 시각화) 
            st.success(st.session_state["summerize"])
            # googletrans 패키지 사용하여 영어 -> 한국어 번역 후 변수 transe에 저장    
            transe = google_trans(st.session_state["summerize"])
            st.subheader("요약 번역 결과")
            st.info(transe) # 영어 -> 한국어 번역된 결과를 화면에 출력(데이터 시각화)
            
            # 유튜브 대본(스크립트) 원본 영어 -> 한국어 번역
            st.subheader("대본 번역하기")  
            # 버튼 "대본 번역실행" 클릭한 경우 
            if st.button("대본 번역실행"):
                # 함수 google_trans 사용하여 
                # 유튜브 대본(스크립트) 원본 영어 -> 한국어 번역한 결과를 변수 transe에 저장 
                transe = google_trans(transcript[0])
                # st.markdown 앨리먼트 사용하여  
                # 유튜브 대본(스크립트) 원본 영어 -> 한국어 번역한 결과를 화면에 출력(데이터 시각화)
                st.markdown(transe)

if __name__=="__main__":
    main() 
