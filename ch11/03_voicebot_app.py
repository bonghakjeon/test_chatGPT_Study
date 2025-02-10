# 가상환경 폴더 "ch11_env" 생성 터미널 명령어
# python -m venv ch11_env

# 가상환경 폴더 "ch11_env" 활성화 터미널 명령어
# ch11_env\Scripts\activate.bat

# Streamlit 패키지 터미널 설치 명령어
# pip install streamlit
# 참고 URL - https://python-programming-diary.tistory.com/111

# *** 이번 강의 실습 진행을 위해선 FFmpeg가 설치되어 있어야 합니다.

# 아이폰으로 무선 마이크 연결 방법
# 유튜브 참고 URL - https://youtu.be/jv7-1xuigzc?si=C-kZsQ3eVNrsaUd7
# 참고 URL - https://wolicheng.com/womic/

# * FFmpeg 란?
# FFmpeg는 오픈소스 멀티미디어 프레임워크로, 비디오, 오디오, 
# 그리고 기타 멀티미디어 파일 및 스트림을 레코드, 변환 및 스트리밍하는 데 사용됩니다. 
# 실습에서 하용하는 패키지에서 음성 파일 input을 ffmpeg를 통해 받고 있습니다.

# * FFmpeg 설치 방법
# * Windows
# 1 단계 : Chocolatey 설치 window powershell을 관리자 권한으로 실행합니다. 
# ([windosws] + [S] 키 입력 -> window powershell 검색 -> 마우스 우클릭 -> 관리자 권한으로 실행 클릭) 
# 아래 명령어를 입력하여 Chocolatey 를 설치 진행.
# Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# 2 단계 : FFmpeg 설치 이어서 아래 명령어를 입력하여 FFmpeg 를 설치합니다.
# choco install ffmpeg

# *** 주의사항 **** 
# Chocolatey 설치 진행시 아래와 같은 오류 메시지가 출력되는 경우 
# 응용 프로그램 "Windows PowerShell" 마우스 우클릭 -> 관리자 권한으로 실행 
# -> Chocolatey 삭제 명령어 "Remove-item C:\ProgramData\chocolatey -Recurse" 입력 및 엔터 
# -> 아래 명령어를 입력하여 Chocolatey 를 설치 진행.
# Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Chocolatey 설치 오류 메시지 해결 방법 
# 참고 URL - https://seemoon.tistory.com/527
# 참고 2 URL - https://stackoverflow.com/questions/66167230/message-while-installing-chocolatey
# Chocolatey 설치 진행시 오류 메시지
# 경고: 'choco' was found at 'C:\ProgramData\chocolatey\bin\choco.exe'.
# 경고: An existing Chocolatey installation was detected. Installation will not continue. This script will not overwrite
# existing installations.
# If there is no Chocolatey installation at 'C:\ProgramData\chocolatey', delete the folder and attempt the installation
# again.

# Please use choco upgrade chocolatey to handle upgrades of Chocolatey itself.
# If the existing installation is not functional or a prior installation did not complete, follow these steps:
#  - Backup the files at the path listed above so you can restore your previous installation if needed.
#  - Remove the existing installation manually.
#  - Rerun this installation script.
#  - Reinstall any packages previously installed, if needed (refer to the lib folder in the backup).

# Once installation is completed, the backup folder is no longer needed and can be deleted.


##### 기본 정보 입력 #####
import streamlit as st
# audiorecorder 패키지란?
# streamlit 안에서 사용자의 마이크로
# 음성 입력(Input)을 받을 수 있는 패키지이다.
# audiorecorder 패키지 추가
# audiorecorder 패키지 터미널 설치 명령어 
# pip install streamlit-audiorecorder
# 참고 URL - https://pypi.org/project/streamlit-audiorecorder/
# 참고 2 URL - https://www.inflearn.com/community/questions/1111523/ch11-03-voicebot-app-%EC%97%90%EB%9F%AC%EA%B4%80%EB%A0%A8?srsltid=AfmBOoovPg_z2EGzx4FHMZWN2_2OErLVdFnKEZ_XyzwL-0MZZDpk53DS
from audiorecorder import audiorecorder 
# OpenAI 패키지 추가
import openai
# 파일 삭제를 위한 패키지 추가
import os
# 시간 정보를 위한 패키지 추가
from datetime import datetime
# ChatGPT의 답변을 TTS(텍스트 -> 음성 파일로 생성)하기 위한 gTTS 패키지 추가
from gtts import gTTS
# 음원파일 재생을 위한 패키지 추가
import base64

##### 기능 구현 함수 #####
# 사용자가 질문을 음원 파일로 입력하면
# 해당 음원 파일을 Input으로 받아서 최종적으로 그 음원파일 내에 사용자의 질문을
# text로 추출해서 리턴해주는 함수이다.
def STT(audio):
    # 사용자에게 Input으로 받은 음원 파일을
    # 'input.mp3'라는 파일로 생성합니다.
    # 파일 저장
    # filename='input.mp3' # 마이크 기능이 안되서 filename='input.mp3' 주석 처리
    filename="test.mp3"
    # audio.export(filename, format="mp3")
    # 위에서 생성한 음원 파일 'input.mp3' 열기
    audio_file = open(filename, "rb")
    # 위에서 열은 음원 파일 'input.mp3'을 
    # Whisper 모델을 활용해 Input으로 넣고 텍스트 추출해서 변수 transcript에 저장 
    # 텍스트 얻기
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    # audio_file.close()  # 마이크 기능이 안되서 코드 audio_file.close() 주석처리 진행 
    # 마이크 기능이 안되서 os.remove(filename) 주석 처리 진행 
    # 파일 삭제
    # os.remove(filename) # Window OS안에 존재하는 음원 파일 'input.mp3' 접근해서 삭제 처리 
    return transcript["text"]

# def ask_gpt(prompt, model):
# 위의 함수 STT 호출해서 추출한 텍스트 "transcript["text"]"를 ChatGPT에게 질문하는 함수 
def ask_gpt(prompt, model):
    # ChatGPT에게 질문하고 최종적으로 ChatGPT의 답변을 리턴하는 함수로
    # 질문 프롬프트와 ChatGPT에서 사용할 언어 모델을 Input으로 받는다.

    response = openai.ChatCompletion.create(model=model, messages=prompt)
    system_message = response["choices"][0]["message"]
    return system_message["content"]

# ChatGPT의 답변 텍스트를 Input으로 받고 
# 해당 텍스트를 한글 음원 파일(텍스트 -> 음성 변환)로 생성하는 함수 
def TTS(response):
    # gTTS 를 활용하여 음성 파일 생성
    # ChatGPT의 답변 텍스트를 Input으로 받고 
    filename = "output.mp3"
    # 해당 텍스트를 한글 음원 파일(텍스트 -> 음성 변환)로 생성하는 함수 
    # 구글 Translate 패키지 gTTS 활용해서 
    # 해당 텍스트를 음원 파일 "output.mp3"로 생성
    tts = gTTS(text=response,lang="ko")
    tts.save(filename)

    # with문 사용하여 streamlit 사용하는 화면에서
    # 편법을 사용하여 아래처럼 자동으로 음원 파일 재생하는 코드 추가 
    # 음원 파일 자동 재생
    with open(filename, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        # 음원 파일 "output.mp3"을 자동으로 생성하는
        # HTML 문법 기반의 코드를 먼저 작성 
        md = f"""
            <audio autoplay="True">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        # HTML 문법이 마크다운 형식 안에서 실행된다는 방법을 사용해서
        # 아래 st.markdown 안에 위에서 작성한 HTML 문법이 할당된 변수 md를 인자로 넣기  
        st.markdown(md,unsafe_allow_html=True,)
    # 음원 파일 자동 재생이 끝나면(위의 with문 실행 종료)
    # 음원 파일 "output.mp3" 삭제
    os.remove(filename)

##### 메인 함수 #####
def main():
    # 기본 설정
    # st.set_page_config 사용해서 프로그램 타이틀(제목) "음성 비서 프로그램" 지정
    st.set_page_config(
        page_title="음성 비서 프로그램",
        layout="wide")

    # session state 초기화
    # 아래 3가지 session state "chat", "messages", "check_reset" 초기화 
    if "chat" not in st.session_state:
        st.session_state["chat"] = [] # "chat"은 사용자와 음성 비서의 대화 내용 저장 하는 session_state이다. 프로그램 내에서 채팅창으로 표시한다.

    if "messages" not in st.session_state:
        # "messages"는 ChatGPT에게 Input(입력)으로 전달할 프롬프트 양식을 저장. 
        # 해당 "messages"같은 st.session_state의 경우 프로그램 내에서는 이전 질문 내용을 포함해서
        # ChatGPT에게 물어볼 수 있도록 구현했기 때문에 이전의 질문과 답변 모두 차례로
        # 해당 "messages" 안에 차곡차곡 누적해서 저장함.
        # 시스템 프롬프트 
        # 내용 - "You are a thoughtful assistant. Respond to all input in 25 words and answer in korea"
        # 번역 - "너는 굉장히 훌륭한 조수이다. 너의 답변은 25자 내외의 한국어로 답변을 해줘."
        st.session_state["messages"] = [{"role": "system", "content": "You are a thoughtful assistant. Respond to all input in 25 words and answer in korea"}]

    if "check_reset" not in st.session_state:
        # "check_reset"은 프로그램 내에서 대화 내용을 리셋할 때 사용하는 st.session_state이다. 
        st.session_state["check_reset"] = False

    # 제목 
    st.header("음성 비서 프로그램") # st.header 앨레멘트를 활용해서 프로그램의 제목 넣기 
    # 구분선
    st.markdown("---")  

    # st.expander 앨레멘트를 활용해서 
    # 프로그램이 어떤 패키지로 구성되어 있는지 자세한 설명(description)을 넣는다.
    # 기본 설명
    with st.expander("음성비서 프로그램에 관하여", expanded=True):
        st.write(
        """     
        - 음성비서 프로그램의 UI는 스트림릿을 활용했습니다.
        - STT(Speech-To-Text)는 OpenAI의 Whisper AI를 활용했습니다. 
        - 답변은 OpenAI의 GPT 모델을 활용했습니다. 
        - TTS(Text-To-Speech)는 구글의 Google Translate TTS를 활용했습니다.
        """
        )

        st.markdown("")

    # 사이드바 생성
    with st.sidebar:

        # Open AI API 키 입력받기
        openai.api_key = st.text_input(label="OPENAI API 키", placeholder="Enter Your API Key", value="", type="password")

        st.markdown("---")

        # GPT 모델을 선택하기 위한 라디오 버튼 생성
        model = st.radio(label="GPT 모델",options=["gpt-4", "gpt-3.5-turbo"])

        st.markdown("---")

        # 리셋 버튼 "초기화" 생성
        if st.button(label="초기화"):
            # 리셋 코드 
            st.session_state["chat"] = [] # 이전 까지 대화 내용 누적되어 저장된 "chat"이라는 session_state 초기화
            # "messages"라는 session_state 초기화
            st.session_state["messages"] = [{"role": "system", "content": "You are a thoughtful assistant. Respond to all input in 25 words and answer in korea"}]
            # "check_reset"라는 session_state True 저장 
            st.session_state["check_reset"] = True
            
    # 기능 구현 공간
    col1, col2 = st.columns(2)
    with col1:
        # 왼쪽 영역 작성
        # st.subheader앨리먼트 사용하여 "질문하기" 출력 
        st.subheader("질문하기")
        # streamlit에는 사용자 마이크로 음성을 입력받는 엘레멘트가 없다.
        # 하여 streamlit-audiorecorder 패키지를 설치하였다.
        # streamlit-audiorecorder 패키지를 설치하면 
        # 바로 아래 audiorecorder 함수가 streamlit에서 실제 있었던
        # 엘레멘트 같이 아주 쉽게 audiorecorder 불러오면 바로 사용 가능하다.
        # 음성 녹음 아이콘 추가
        # audiorecorder 함수 
        # 첫번째 파라미터 인자값 "클릭하여 녹음하기" 
        # - 클릭하여 녹음하기로 녹음을 시작하기 전에 버튼에 보여주는 안내 메시지이다.
        # 두번째 파라미터 인자값 "녹음중..."
        # - 녹음하는 중에는 "녹음중..."이 해당 텍스트가 출력된다.
        # 아이폰 마이크 설정 및 PC와 연결하기 
        audio = audiorecorder("클릭하여 녹음하기", "녹음중...")
        # audio.duration_seconds - 사용자가 새로 녹음(질문)한 음성 파일의 오디오 재생시간 의미
        # st.session_state["check_reset"]==False - 리셋 버튼 "초기화"가 클릭되지 않은 경우 의미
        if (audio.duration_seconds > 0) and (st.session_state["check_reset"]==False):
            # 음성 재생 
            # st.audio 엘레멘트는 Streamlit 안에서 음성 파일을 재생할 때 사용하는 엘레멘트이다.
            # st.audio 엘레멘트가 실행되면 크롬(Chrome) 웹브라우저 Streamlit UI 화면에서  
            # 사용자가 방금 전에 질문해서 녹음한 음성 파일을 다시 한번 재생할 수 있다.
            # 아래처럼 st.audio 엘레멘트안에 인자값으로 "audio.export().read()"으로 전달 
            st.audio(audio.export().read())
            # 음원 파일에서 텍스트 추출
            # 함수 STT 사용해서 음성 파일에 있는 텍스트 추출하기
            question = STT(audio)

            # 채팅을 시각화하기 위해 질문 내용 저장
            # 현재 시간과 분을 변수 now에 저장
            # 현재 시간과 분을 변수 now에 저장 하는 이유?
            # 크롬(Chrome) 웹브라우저 Streamlit UI 화면에서  
            # 사용자의 질문과 ChatGPT의 답변을 아이폰 iMessage 형태로 구현한 곳 
            # 옆에 시간과 분을 화면상에 출력하기 위해서이다.
            now = datetime.now().strftime("%H:%M")
            # "chat"이라는 session_state 안에 "user" 즉 사용자가 질문했다고 명명을 하고 
            # 위에 저장한 현재 시간과 분 저장한 변수 "now" 
            # 그리고 사용자의 질문 텍스트(question)를
            # 아래처럼 튜플 형태로 저장 ("user",now, question) 및
            # 왼쪽에 있는 "chat"이라는 session_state(st.session_state["chat"])와 더해준다.(+)
            # 왜 더해주냐면 앞에 채팅이랑(기존 대화 내용) 계속 누적해서 표시하기 위해서이다.
            st.session_state["chat"] = st.session_state["chat"]+ [("user",now, question)]
            # "messages"라는 session_state 안에
            # ChatGPT API에게 질문하는 형태([{"role": "user", "content": question}])와
            # 왼쪽에 있는 "messages"라는 session_state(st.session_state["messages"])와 더해줘서(+)
            # GPT 모델에 넣을 프롬프트를 위해 질문 내용 저장

            # 왜 더해주냐면 
            # 시스템 프롬프트 
            # 내용 - "You are a thoughtful assistant. Respond to all input in 25 words and answer in korea"
            # 번역 - "너는 굉장히 훌륭한 조수이다. 너의 답변은 25자 내외의 한국어로 답변을 해줘."
            # 이어서 사용자의 질문을 넣어주기 위해서
            # 그리고 앞에 채팅이랑(기존 대화 내용) 계속 누적해서 
            # ChatGPT한테 질문을 하기 위해서이다.
            st.session_state["messages"] = st.session_state["messages"]+ [{"role": "user", "content": question}]

    with col2:
        # 오른쪽 영역 작성
        st.subheader("질문/답변")
        # audio.duration_seconds - 사용자가 새로 녹음(질문)한 음성 파일의 오디오 재생시간 의미
        # st.session_state["check_reset"]==False - 리셋 버튼 "초기화"가 클릭되지 않은 경우 의미
        if  (audio.duration_seconds > 0)  and (st.session_state["check_reset"]==False):
            #ChatGPT에게 답변 얻기
            response = ask_gpt(st.session_state["messages"], model)

            # GPT 모델에 넣을 프롬프트를 위해 답변 내용 저장
            # ChatGPT에게 얻은 답변이 저장된 변수 response를
            # "messages"라는 session_state(st.session_state["messages"])에 저장
            # "messages"라는 session_state(st.session_state["messages"])에 저장하는 이유는
            # 사용자가 이전에 했던 질문과 ChatGPT가 이전에 해줬던 답변 내용을 누적해서
            # 사용자가 현재 질문할 때 반영해서 답변을 요청한다.
            # 그렇기 때문에 지금 ChatGPT가 해주는 답변도
            # 아래처럼 "messages"라는 session_state(st.session_state["messages"])에 저장해서
            # 갖고 있어야지만 그 다음번에 사용자가 질문을 할 때, 해당 내용도 같이
            # ChatGPT한테 전달해서 답변을 얻을 수 있다.
            st.session_state["messages"] = st.session_state["messages"]+ [{"role": "system", "content": response}]

            # 아이폰 iMessage 형식으로 채팅창 시각화를 위한 답변 내용 저장
            # 현재 시간과 분을 변수 now에 저장
            now = datetime.now().strftime("%H:%M")
            # "chat"이라는 session_state(st.session_state["chat"]) 안에
            # ChatGPT의 답변이기 때문에 "bot"이라고 명명해주고 
            # 현재의 시간과 분(now) / ChatGPT 답변(response)을 
            # 튜플 형태로 저장 ("bot",now, response)

            st.session_state["chat"] = st.session_state["chat"]+ [("bot",now, response)]

            # iMessage 형식 채팅창 형식으로 시각화 하기
            # "chat"이라는 session_state(st.session_state["chat"])에 속한
            # for문을 돌면서 튜플 3가지 (sender, time, message) 
            # 왼쪽부터 순서대로 먼저 가져와서
            for sender, time, message in st.session_state["chat"]:
                if sender == "user":   # 만약 sender가 "user"인 경우 (즉 ChatGPT가 아니라 사용자가 질문을 했을 경우 의미)
                    # 사용자 "user"가 질문한 경우 아래처럼 iMessage 형식 채팅창 형식으로 시각화 하기
                    # 아래 html 코드 뜻 - 아이폰 iMessage 형태로 시각화 하겠다는 뜻이다.
                    st.write(f'<div style="display:flex;align-items:center;"><div style="background-color:#007AFF;color:white;border-radius:12px;padding:8px 12px;margin-right:8px;">{message}</div><div style="font-size:0.8rem;color:gray;">{time}</div></div>', unsafe_allow_html=True)
                    st.write("")
                else:  # 만약 sender가 "bot"인 경우 (즉 사용자가 아니라 ChatGPT가 질문을 했을 경우 의미)
                    # 아래 html 코드 뜻 - 아이폰 iMessage 형태로 시각화 하겠다는 뜻이다.
                    st.write(f'<div style="display:flex;align-items:center;justify-content:flex-end;"><div style="background-color:lightgray;border-radius:12px;padding:8px 12px;margin-left:8px;">{message}</div><div style="font-size:0.8rem;color:gray;">{time}</div></div>', unsafe_allow_html=True)
                    st.write("")
            
            # gTTS 를 활용하여 ChatGPT의 답변을 
            # 텍스트 -> 음성 파일 생성(추출/변환) 및 음성 재생
            TTS(response)
        else: # if문 조건(if  (audio.duration_seconds > 0)  and (st.session_state["check_reset"]==False):) 만족하지 않을 경우 
            # 버튼 "초기화"를 클릭한 경우 "check_reset"라는 
            # session_state(st.session_state["check_reset"])를 False로 다시 초기화 진행
            # 왜냐하면 버튼 "초기화"를 클릭하여 크롬(Chrome) 웹브라우저 화면이 초기화 되고 나서
            # 다음번에 사용자가 다시 한번 질문을 시작하면 
            # "chat"이라는 st.session_state["chat"]
            # "messages"라는 st.session_state["messages"]
            # 두개의 session_state가 리셋된 상태로 마치 처음 질문을 받는 것처럼
            # 프로그램이 동작하게 하기 위해서이다.
            st.session_state["check_reset"] = False 

if __name__=="__main__":
    main()