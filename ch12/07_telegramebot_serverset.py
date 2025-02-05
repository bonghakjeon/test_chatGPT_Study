# FastAPI 패키지 "fastapi" 터미널 설치 명령어 
# pip install fastapi

# 주의사항 
# 1. FastAPI 패키지 "fastapi" 단독으로는 웹개발을 할 수 없다.
#    하여 아래처럼 유비콘 패키지 "uvicorn[standard]"를 추가로 터미널 설치 진행 
#    pip install "uvicorn[standard]"
# 2. 유비콘 패키지 "uvicorn[standard]"를 사용하는 파이썬 파일의 경우 
#     일반 파이썬 파일을 터미널에서 실행하는 명령어(python 07_telegramebot_serverset.py)를 
#     그대로 쓰면 파일 안에 있는 FastAPI 서버(FastAPI 클래스 객체 app)가 생성 불가하다.
#     하여 유비콘 패키지 "uvicorn[standard]"를 사용하는 파이썬 파일은
#     아래와 같은 명령어를 입력 해야만 해당 파일 안에 있는 FastAPI 서버(FastAPI 클래스 객체 app)가 생성된다.
#     uvicorn 07_telegramebot_serverset:app --reload
# 터미널 명령어 "uvicorn 07_telegramebot_serverset:app --reload" 입력 및 엔터 
# -> FastAPI 서버(FastAPI 클래스 객체 app)가 정상적으로 생성되면
#    터미널창에 아래와 같은 안내메시지(INFO)가 출력된다.
#    해당 안내메시지(INFO) 중 "http://127.0.0.1:8000" 문자열은
#    FastAPI 서버 로컬 PC URL 주소를 의미한다.
# INFO:     Will watch for changes in these directories: ['D:\\bhjeon\\test_chatGPT\\ch12']
# INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
# INFO:     Started reloader process [20884] using WatchFiles
# INFO:     Started server process [17836]
# INFO:     Waiting for application startup.
# INFO:     Application startup complete.

# 텔레그램과 소통할 텔레그램 서버 구현

# ngrok 역할?
# 외부에서 개발자 로컬 PC로 접속할 수 있는 URL 주소가 필요하다.
# ngrok는 개발자 로컬 PC에서 생성한 서버 개발 환경을
# 외부 서버에서도(전세계 어디 서버에서도) 접속할 수 있도록 공유해주는 서비스이다.
# 즉, 외부에서 개발자 로컬 PC로 접속할 수 있는 URL 주소를 발급해준다.
# ngrok 웹사이트
# 참고 URL - https://ngrok.com/ 

# ngrok 응용 프로그램 실행 방법
# 1) 비쥬얼스튜디오코드(VSCode) 실행 
#    -> 유비콘 패키지 "uvicorn[standard]"를 사용하는 파이썬 파일 "07_telegramebot_serverset.py" 열기
#    -> 터미널창 열어서 명령어 "uvicorn 07_telegramebot_serverset:app --reload" 입력 및 엔터 
#    -> FastAPI 서버(FastAPI 클래스 객체 app)가 정상적으로 생성 완료

# 2) PC 바탕 화면 -> ngrok 바로가기 아이콘 더블 클릭
# ngrok 바로가기 아이콘 존재하지 않으면 아래 파일경로 들어가서 ngrok 응용 프로그램 실행
# 파일 경로 - "C:\Users\bhjeon\Desktop\회사_업무_및_공부_자료\상상진화 회사 업무\AI 챗봇_개발\텔레그램_카카오_챗봇_ngrok_실행_프로그램" -> 응용 프로그램 ngrok

# 3) ngrok 전용 터미널창 출력 
#    -> 아래 명령어 "ngrok authtoken 2sZKZBZ9stzdWgsAPcHt9JtrNzN_5QpYosiEkadfnfffAvsvn" 입력 및 엔터 
# (명령어 형식) ngrok authtoken <Your token>
# (명령어 예시) ngrok authtoken 2sZKZBZ9stzdWgsAPcHt9JtrNzN_5QpYosiEkadfnfffAvsvn

# 4) 3)번의 토큰 번호 입력이 잘 되었을 경우 터미널창에 아래와 같은 메시지 출력
# Authtoken saved to configuration file: C:\Users\bhjeon\AppData\Local/ngrok/ngrok.yml

# 5) ngrok 응용 프로그램 터미널창에 명령어 "ngrok http 8000" 입력 및 엔터 
#    -> 외부 서버에서도 개발자 로컬 PC로 접속할 수 있는 URL 주소 생성 
# 참고사항 
# - 위에 명령어 중 "8000"이 뜻하는 바는 개발자 로컬 PC안에 포트(Port) 번호를 의미함.
# - 파이썬 파일 "07_telegramebot_serverset.py"을 유비콘 패키지 "uvicorn[standard]"를 사용하여 FastAPI 웹서버를 생성해 놓은 상태이다.
#   FastAPI 서버 로컬 PC URL 주소는 "http://127.0.0.1:8000" 이다.
#   해당 URL 주소 중 "http://127.0.0.1"은 개발자의 로컬 PC를 의미하며,
#   "8000"은 개발자의 로컬 PC 안에서 몇동 몇호, 즉 예를들어 105동 105호가 "8000"을 뜻한다.
#   하여 개발자의 로컬 PC 안에 "8000"이라는 포트(Port) 번호 안에 
#   새로 생성한 FastAPI 웹서버를 오픈한 것을 의미한다.
#   즉, ngrok 응용 프로그램 터미널창에서 명령어 "ngrok http 8000" 입력 및 엔터를 치면
#   외부 서버에서도 개발자 로컬 PC에 있는 포트(Port) 번호 "8000"에 있는
#   새로 생성한 FastAPI 웹서버에 접속할 수 있는 URL 주소를 생성해준다.

# 6) ngrok 응용 프로그램 터미널창에 아래와 같은 메시지가 출력되면
#    이제 외부 서버에서도 개발자 로컬 PC로 접속할 수 있는 FastAPI 웹서버 URL 주소 생성 완료.
#    아래에 출력된 메시지 중 외부 서버에서도 개발자 로컬 PC로 접속할 수 있는 
#    FastAPI 웹서버 URL 주소 "https://7839-14-52-67-173.ngrok-free.app" 
#    로 외부 서버에서 접속을 하면 
#    개발자 로컬 PC에 포트(Port) 번호 "8000"로 접속이 가능("http://localhost:8000")하다는 것을 의미한다.
# 주의사항 - ngrok 응용 프로그램 터미널창에 URL 주소 "https://7839-14-52-67-173.ngrok-free.app" 
#           복사하려고 단축키 Ctrl + C 키를 누르면 ngrok 응용 프로그램이 종료된다.(Ctrl+C to quit)
#           하여 절대 단축키 Ctrl + C 키를 누르지 말고 마우스로 해당 URL 주소를 드래그 한 후 
#           키보드 단축키 Ctrl + Insert 키를 눌러서 해당 URL 주소를 복사한다.
# ngrok    (Ctrl+C to quit)        
# Sign up to try new private endpoints https://ngrok.com/new-features-update?ref=private                                                                                                                                                                                                                          
# Session Status                online                                                                                                                    
# Account                       minjaejeon0827@gmail.com (Plan: Free)                                                                                     
# Version                       3.19.1                                                                                                                    
# Region                        Japan (jp)                                                                                                                
# Latency                       36ms                                                                                                                      
# Web Interface                 http://127.0.0.1:4040                                                                                                     
# Forwarding                    https://7839-14-52-67-173.ngrok-free.app -> http://localhost:8000                                                                                                                                                                                                                 
# Connections                   ttl     opn     rt1     rt5     p50     p90                                                                                                             
#                               0       0       0.00    0.00    0.00    0.00  

# 7) 6)번에서 복사한 외부 서버에서도 개발자 로컬 PC로 접속할 수 있는 
#    FastAPI 웹서버 URL 주소를 가지고 구글 크롬(Chrome) 웹브라우저에서 붙여넣기 하면
#    아래와 같은 메시지가 출력되면 버튼 "사이트 방문" 클릭
# 당신은 방문하려고합니다 :
# 7839-14-52-67-173.ngrok-free.app
# 웹사이트 IP: 14.52.67.173
# * 이 웹사이트는 ngrok.com을 통해 무료로 제공됩니다 .
# * 신뢰할 수 있는 경우에만 이 웹사이트를 방문하세요. 링크를 보낸 사람을 신뢰하는 경우에만 이 웹사이트를 방문하세요.
# * 비밀번호, 전화번호, 신용카드 정보와 같은 개인정보나 금융정보를 공개하는 데는 주의하세요.

# 8) 7)번 처럼 구글 크롬(Chrome) 웹브라우저 버튼 "사이트 방문" 클릭시 
#    아래와 같은 JSON 데이터가 웹브라우저 화면에 출력
#    {"message":"TelegramChatbot"}
#    해당 데이터가 출력되는 이유는 외부 서버(외부 구글 크롬(Chrome) 웹브라우저)에서 접속을 해서 
#    유비콘 패키지 "uvicorn[standard]"를 사용하는 파이썬 파일 "07_telegramebot_serverset.py"을 통해
#    생성한 "8000" 포트(Port)번호를 가진 FastAPI 웹서버 접속이 완료되었기 때문이다.

# 9) ngrok 터미널창에서 생성한 외부 서버(텔레그램 서버)에서도 개발자 로컬 PC로 접속할 수 있는 
#    FastAPI 웹서버 URL 주소 "https://7839-14-52-67-173.ngrok-free.app" 
#    와 텔레그램 서버만 연결 진행 
#    -> 구글 크롬(Chrome) 웹브라우저에 아래와 같은 URL 주소 입력 및 엔터
#    "https://api.telegram.org/bot7717605195:AAHJGNKRR_aK_dG0HELQUBu1WeEsclERRb0/setWebhook?url=https://7839-14-52-67-173.ngrok-free.app/chat" 
#    (URL 주소 형식) 
#    * 텔레그램 챗봇의 메인코드를 실행하는 chat함수를
#      실행할 수 있는 주소 ('/chat')를 아래처럼 추가해야 
#      텔레그램 서버와 개발자 로컬 PC로 접속할 수 있는 FastAPI 웹서버가 연결될 수 있다.
#    https://api.telegram.org/bot<토큰>/setWebhook?url=<ngrok 터미널창에서 생성한 FastAPI 웹서버 URL 주소>/chat
#    (URL 주소 예)
#    https://api.telegram.org/bot7717605195:AAHJGNKRR_aK_dG0HELQUBu1WeEsclERRb0/setWebhook?url=https://7839-14-52-67-173.ngrok-free.app/chat

# 참고사항
#    텔레그램 서버와 FastAPI 웹서버 URL 주소를 연결하려면
#    텔레그램 API에 있는 webhook이라는 메소드를 사용하면 된다.
#    해당 webhook이라는 메소드를 사용하면 텔레그램 채팅방과 
#    FastAPI 웹서버 URL 주소를 연결해서 해당 FastAPI 웹서버 URL 주소로
#    텔레그램 채팅방의 채팅 정보를 바로바로 전달 받을 수 있다.
#    즉, 텔레그램 API의 webhook이라는 메소드와 
#    ngrok 터미널창에서 생성한 외부 서버(텔레그램 서버)에서도 개발자 로컬 PC로 접속할 수 있는 
#    FastAPI 웹서버 URL 주소 "https://7839-14-52-67-173.ngrok-free.app" 
#    를 연결을 하고 텔레그램 채팅방에서 사용자가 채팅을 치면 
#    해당 URL 주소를 통해서 개발자 로컬 PC에 포트(Port) 번호 "8000"로 
#    접속을("http://localhost:8000") 하여 채팅 정보가 넘어온다.

# 10) 구글 크롬(Chrome) 웹브라우저에 아래와 같은 JSON 데이터 출력되고,
#     이 때, 항목 "description"에 "Webhook was set"이라고 출력되면
#     텔레그램 채팅방과 개발자 로컬 PC에서 생성한 FastAPI 연결 완료
# {"ok":true,"result":true,"description":"Webhook was set"} 

# FastAPI 패키지 "fastapi" 불러오기
# Request 패키지 불러오기 
from fastapi import Request, FastAPI   

# FastAPI 클래스 객체 app 생성 
app = FastAPI()

# 위에서 생성한 객체 app 이라는 웹서버에 
# HTTP 통신 get() 메소드에 인자 "/" 전달 후 
# -> get() 메소드 호출시 메인 주소("/")로 접속 진행
# -> root 함수 실행 
@app.get("/")
async def root():
    # 크롬(Chrome) 웹브라우저 상에서 
    # URL 주소 "http://127.0.0.1:8000/"로 접속을 했을 때, 
    # 웹브라우저상에서 아래와 같은 메시지({"message": "TelegramChatbot"}) 출력
    return {"message": "TelegramChatbot"}

# 위에서 생성한 객체 app 이라는 웹서버에 
# HTTP 통신 post() 메소드에 인자 "/chat" 전달 후 
# -> post() 메소드 호출시 메인 주소 하위 주소("/chat")로 접속 진행
# -> chat 함수 실행 -> 텔레그램 웹훅과 연결 진행
# 주의사항 - 일반 HTTP 통신 GET 방식으로 구글 크롬 웹브라우저 URL 접속하면 
#           (URL 주소 "http://127.0.0.1:8000/chat) 아래와 같은 오류 메시지 출력
#           "405 Method Not Allowed"
#           왜냐면 post() 메소드로 호출하기 때문에 
#           구글 크롬 웹브라우저 URL 접속시에는 GET 방식이 아닌
#           POST 방식으로 접근해야 하기 때문이다.
#           하여 해당 오류를 해결하려면 ngrok와 텔레그램 API를 활용해서
#           아래 post() 메소드로 정보(데이터)를 주고 받을 수 있도록 해야한다.
@app.post("/chat")
# 텔레그램 챗봇의 모든 기능을 실행할 수 있는 함수 
async def chat(request: Request):
    # 텔레그램 채팅방에서 사용자가 채팅 입력 
    # ->? 해당 채팅에 대한 정보가 텔레그램 API webhook 메소드 통해서
    # 해당 FastAPI 웹서버 URL 주소 "/chat"로 넘어오고 ->
    # 함수 chat 실행 -> print 함수 호출 -> 텔레그램 채팅 정보가 터미널창에 출력
    telegramrequest = await request.json()
    # 텔레그램 채팅 정보 터미널창에 출력
    # 텔레그램 채팅 정보 "연결이 잘 되었나요?"가 아래처럼 json 데이터 형식으로 출력
    # {'update_id': 250682837, 'message': {'message_id': 5, 
    #                                      'from': {'id': 8000253838, 'is_bot': False, 'first_name': '민재', 'last_name': '전', 'language_code': 'ko'}, 
    #                                      'chat': {'id': 8000253838, 'first_name': '민재', 'last_name': '전', 'type': 'private'}, 
    #                                      'date': 1738729567, 
    #                                      'text': '연결이 잘 되었나요?'}}
    print(telegramrequest)   
    return  0 