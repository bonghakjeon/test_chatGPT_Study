# Streamlit 패키지 터미널 설치 명령어
# pip install streamlit
# 참고 URL - https://python-programming-diary.tistory.com/111

# *** 이번 강의 실습 진행을 위해선 FFmpeg가 설치되어 있어야 합니다.

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
# audiorecorder 패키지 추가
# audiorecorder 패키지 터미널 설치 명령어 
# pip install streamlit-audiorecorder
# 참고 URL - https://www.inflearn.com/community/questions/1111523/ch11-03-voicebot-app-%EC%97%90%EB%9F%AC%EA%B4%80%EB%A0%A8?srsltid=AfmBOoovPg_z2EGzx4FHMZWN2_2OErLVdFnKEZ_XyzwL-0MZZDpk53DS
from audiorecorder import audiorecorder 
# OpenAI 패키지 추가
import openai
# 파일 삭제를 위한 패키지 추가
import os
# 시간 정보를 위한 패키지 추가
from datetime import datetime
# TTS 패키지 추가
from gtts import gTTS
# 음원파일 재생을 위한 패키지 추가
import base64

##### 기능 구현 함수 #####
def STT(audio):
    # 파일 저장
    filename='input.mp3'
    audio.export(filename, format="mp3")
    # 음원 파일 열기
    audio_file = open(filename, "rb")
    #Whisper 모델을 활용해 텍스트 얻기
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    audio_file.close()
    # 파일 삭제
    os.remove(filename)
    return transcript["text"]

def ask_gpt(prompt, model):
    response = openai.ChatCompletion.create(model=model, messages=prompt)
    system_message = response["choices"][0]["message"]
    return system_message["content"]

def TTS(response):
    # gTTS 를 활용하여 음성 파일 생성
    filename = "output.mp3"
    tts = gTTS(text=response,lang="ko")
    tts.save(filename)

    # 음원 파일 자동 재성
    with open(filename, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio autoplay="True">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(md,unsafe_allow_html=True,)
    # 파일 삭제
    os.remove(filename)

##### 메인 함수 #####
def main():
    # 기본 설정
    st.set_page_config(
        page_title="음성 비서 프로그램",
        layout="wide")

    # session state 초기화
    if "chat" not in st.session_state:
        st.session_state["chat"] = []

    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "system", "content": "You are a thoughtful assistant. Respond to all input in 25 words and answer in korea"}]

    if "check_reset" not in st.session_state:
        st.session_state["check_reset"] = False

    # 제목 
    st.header("음성 비서 프로그램")
    # 구분선
    st.markdown("---")

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

        # 리셋 버튼 생성
        if st.button(label="초기화"):
            # 리셋 코드 
            st.session_state["chat"] = []
            st.session_state["messages"] = [{"role": "system", "content": "You are a thoughtful assistant. Respond to all input in 25 words and answer in korea"}]
            st.session_state["check_reset"] = True
            
    # 기능 구현 공간
    col1, col2 =  st.columns(2)
    with col1:
        # 왼쪽 영역 작성
        st.subheader("질문하기")
        # 음성 녹음 아이콘 추가
        audio = audiorecorder("클릭하여 녹음하기", "녹음중...")
        if (audio.duration_seconds > 0) and (st.session_state["check_reset"]==False):
            # 음성 재생 
            st.audio(audio.export().read())
            # 음원 파일에서 텍스트 추출
            question = STT(audio)

            # 채팅을 시각화하기 위해 질문 내용 저장
            now = datetime.now().strftime("%H:%M")
            st.session_state["chat"] = st.session_state["chat"]+ [("user",now, question)]
            # GPT 모델에 넣을 프롬프트를 위해 질문 내용 저장
            st.session_state["messages"] = st.session_state["messages"]+ [{"role": "user", "content": question}]

    with col2:
        # 오른쪽 영역 작성
        st.subheader("질문/답변")
        if  (audio.duration_seconds > 0)  and (st.session_state["check_reset"]==False):
            #ChatGPT에게 답변 얻기
            response = ask_gpt(st.session_state["messages"], model)

            # GPT 모델에 넣을 프롬프트를 위해 답변 내용 저장
            st.session_state["messages"] = st.session_state["messages"]+ [{"role": "system", "content": response}]

            # 채팅 시각화를 위한 답변 내용 저장
            now = datetime.now().strftime("%H:%M")
            st.session_state["chat"] = st.session_state["chat"]+ [("bot",now, response)]

            # 채팅 형식으로 시각화 하기
            for sender, time, message in st.session_state["chat"]:
                if sender == "user":
                    st.write(f'<div style="display:flex;align-items:center;"><div style="background-color:#007AFF;color:white;border-radius:12px;padding:8px 12px;margin-right:8px;">{message}</div><div style="font-size:0.8rem;color:gray;">{time}</div></div>', unsafe_allow_html=True)
                    st.write("")
                else:
                    st.write(f'<div style="display:flex;align-items:center;justify-content:flex-end;"><div style="background-color:lightgray;border-radius:12px;padding:8px 12px;margin-left:8px;">{message}</div><div style="font-size:0.8rem;color:gray;">{time}</div></div>', unsafe_allow_html=True)
                    st.write("")
            
            # gTTS 를 활용하여 음성 파일 생성 및 재생
            TTS(response)
        else:
            st.session_state["check_reset"] = False

if __name__=="__main__":
    main()