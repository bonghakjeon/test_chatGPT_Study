# 가상환경 폴더 "ch12_env" 생성 터미널 명령어
# python -m venv ch12_env

# 가상환경 폴더 "ch12_env" 활성화 터미널 명령어
# ch12_env\Scripts\activate.bat

# 개발자 로컬 PC룰 FastAPI와 ngrok를 사용해서
# 텔레그램이란 손님을 초대해 보는 기능 구현

# FastAPI란?
# 파이썬(python) 기반의 웹서버를 생성하기 위한 오픈소스이다.
# FastAPI를 사용하면 빠르게 웹서버를 생성할 수 있다.
# 하여 해당 FastAPI를 사용하면 개발자 로컬 PC 내부에 
# 텔레그램 챗봇 프로그램이 동작하고 있는 로컬 Port 지정 가능

# FastAPI 패키지 "fastapi" 터미널 설치 명령어 
# pip install fastapi

# 주의사항 
# 1. FastAPI 패키지 "fastapi" 단독으로는 웹개발을 할 수 없다.
#    하여 아래처럼 유비콘 패키지 "uvicorn[standard]"를 추가로 터미널 설치 진행 
#    pip install "uvicorn[standard]"
# 2. 유비콘 패키지 "uvicorn[standard]"를 사용하는 파이썬 파일의 경우 
#     일반 파이썬 파일을 터미널에서 실행하는 명령어(python 06_fastapi_example.py)를 
#     그대로 쓰면 파일 안에 있는 FastAPI 서버(FastAPI 클래스 객체 app)가 생성 불가하다.
#     하여 유비콘 패키지 "uvicorn[standard]"를 사용하는 파이썬 파일은
#     아래와 같은 명령어를 입력 해야만 해당 파일 안에 있는 FastAPI 서버(FastAPI 클래스 객체 app)가 생성된다.
#     uvicorn 06_fastapi_example:app --reload
# 터미널 명령어 "uvicorn 06_fastapi_example:app --reload" 입력 및 엔터 
# -> FastAPI 서버(FastAPI 클래스 객체 app)가 정상적으로 생성되면
#    터미널창에 아래와 같은 안내메시지(INFO)가 출력된다.
#    해당 안내메시지(INFO) 중 "http://127.0.0.1:8000" 문자열은
#    FastAPI 서버 로컬 PC URL 주소를 의미한다.
# INFO:     Will watch for changes in these directories: ['D:\\bhjeon\\test_chatGPT\\ch12']
# INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
# INFO:     Started reloader process [19788] using WatchFiles
# INFO:     Started server process [15124]
# INFO:     Waiting for application startup.
# INFO:     Application startup complete.


# 텔레그램 챗봇 프로그램 실행 순서 
# 1 단계 : FastAPI를 사용해서 로컬 파이썬 서버(07_telegramebot_serverset.py) 실행(생성)
# 2 단계 : ngrok를 활용해서 외부 서버에서 개발자 로컬 PC로 접속하기 위한 주소 발급 받기
# 3 단계 : 텔레그램 API 웹훅을 사용해서 텔레그램 서버와 로컬 파이썬 서버(07_telegramebot_serverset.py) 연결 

# 텔레그램 챗봇 프로그램 구조
# 1. 실행파일 - 08_telegramebot.py 
# - 실행파일 - 08_telegramebot.py 먼저 실행
# - FastAPI 파이썬 서버(07_telegramebot_serverset.py) 실행(생성)
# - 내부 주소로 실행 (http://localhost:8000/) 
# - 외부 서버에서 접근 불가 

# 2. FastAPI 서버 - 07_telegramebot_serverset.py 
# - 주소 별 특정 기능 수행 
# - 기본 연결 확인 "/"
#   http://localhost:8000/
# - 텔레그램 응답 "/chat" (텔레그램 서버로 전송)
#   http://localhost:8000/chat/

# 3. 텔레그램 서버
# - ngrok를 활용해서 외부 서버에서 개발자 로컬 PC로 접속하기 위한 주소 발급 받기
#   해당 외부 서버에서 접속 가능 주소를 Telegram API의 웹훅과 연결하기 

from fastapi import FastAPI   # FastAPI 패키지 "fastapi" 불러오기 

app = FastAPI()  # FastAPI 클래스 객체 app 생성 

# 위에서 생성한 객체 app 이라는 웹서버에 
# HTTP 통신 get() 메소드에 인자 "/" 전달 후 
# -> get() 메소드 호출시 메인 주소("/")로 접속 진행
# -> root 함수 실행 
@app.get("/")
async def root():
    # 크롬(Chrome) 웹브라우저 상에서 
    # URL 주소 "http://127.0.0.1:8000/"로 접속을 했을 때, 
    # 웹브라우저상에서 아래와 같은 메시지({"message": "This is my house"}) 출력
    return {"message": "This is my house"}

# 위에서 생성한 객체 app 이라는 웹서버에 
# HTTP 통신 get() 메소드에 인자 "/room1" 전달 후 
# -> get() 메소드 호출시 메인 주소 하위 주소("/room1")로 접속 진행
# -> room1 함수 실행 
@app.get("/room1")
async def room1():
    # 크롬(Chrome) 웹브라우저 상에서 
    # URL 주소 "http://127.0.0.1:8000/room1"로 접속을 했을 때, 
    # 웹브라우저상에서 아래와 같은 메시지({"message": "Welcome to room1"}) 출력
    return {"message": "Welcome to room1"}

# 위에서 생성한 객체 app 이라는 웹서버에 
# HTTP 통신 get() 메소드에 인자 "/room2" 전달 후 
# -> get() 메소드 호출시 메인 주소 하위 주소("/room2")로 접속 진행
# -> room2 함수 실행 
@app.get("/room2")
async def room2():
    # 크롬(Chrome) 웹브라우저 상에서 
    # URL 주소 "http://127.0.0.1:8000/room2"로 접속을 했을 때, 
    # 웹브라우저상에서 아래와 같은 메시지({"message": "Welcome to room2"}) 출력
    return {"message": "Welcome to room2"}
