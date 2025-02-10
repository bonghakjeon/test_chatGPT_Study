from fastapi import Request, FastAPI   # FastAPI 패키지 "fastapi" 불러오기 

app = FastAPI()   # FastAPI 클래스 객체 app 생성 

# 위에서 생성한 객체 app 이라는 웹서버에 
# HTTP 통신 get() 메소드에 인자 "/" 전달 후 
# -> get() 메소드 호출시 메인 주소("/")로 접속 진행
# -> root 함수 실행 
@app.get("/")
async def root():
    # 크롬(Chrome) 웹브라우저 상에서 
    # URL 주소 "http://127.0.0.1:8000/"로 접속을 했을 때, 
    # 웹브라우저상에서 아래와 같은 메시지({"message": "kakaoTest"}) 출력
    return {"message": "kakaoTest"}

# 위에서 생성한 객체 app 이라는 웹서버에 
# HTTP 통신 post() 메소드에 인자 "/chat/" 전달 후 
# -> post() 메소드 호출시 메인 주소 하위 주소("/chat/")로 접속 진행
# -> chat 함수 실행 -> 카카오톡 서버와 연결 진행
# 주의사항 - 일반 HTTP 통신 GET 방식으로 구글 크롬 웹브라우저 URL 접속하면 
#           (URL 주소 "http://127.0.0.1:8000/chat/) 아래와 같은 오류 메시지 출력
#           "405 Method Not Allowed"
#           왜냐면 post() 메소드로 호출하기 때문에 
#           구글 크롬 웹브라우저 URL 접속시에는 GET 방식이 아닌
#           POST 방식으로 접근해야 하기 때문이다.
#           하여 해당 오류를 해결하려면 ngrok와 카카오톡 챗봇관리자 센터를 활용해서
#           아래 post() 메소드로 정보(데이터)를 주고 받을 수 있도록 해야한다.
@app.post("/chat/")
# 카카오톡 채팅방에 사용자가 채팅을 새로 입력했을 때
# 카카오톡 챗봇의 모든 기능을 실행할 수 있는 함수 chat
# 사용자가 채팅을 새로 입력했을 때 새로운 입력에 대한 정보를
# 매개변수 request로 인자를 전달 받는다.
async def chat(request: Request):
    # 카카오톡 채팅방에서 사용자가 채팅 입력 
    # -> 해당 채팅에 대한 정보가 카카오톡 챗봇관리자 센터를 활용해서 
    # 카카오톡 서버 -> ngrok 프로그램을 지나서 -> 해당 FastAPI 웹서버 URL 주소 "/chat/"로 넘어오고 ->
    # 함수 chat 실행 -> print 함수 호출 -> 카카오톡 채팅 정보가 터미널창에 출력
    
    # 카카오톡 채팅에서 날라온 채팅 정보를 json 데이터 형태로 정리해서 변수 kakaorequest에 저장
    kakaorequest = await request.json()
    # 카카오톡 채팅 정보 터미널창에 출력
    # 카카오톡 채팅 정보 "연결이 잘 되었나요?"가 아래처럼 json 데이터 형식으로 출력
    # {'update_id': 250682837, 'message': {'message_id': 5, 
    #                                      'from': {'id': 8000253838, 'is_bot': False, 'first_name': '민재', 'last_name': '전', 'language_code': 'ko'}, 
    #                                      'chat': {'id': 8000253838, 'first_name': '민재', 'last_name': '전', 'type': 'private'}, 
    #                                      'date': 1738729567, 
    #                                      'text': '연결이 잘 되었나요?'}}
    print(kakaorequest)
    return 

# 카카오톡에서 챗봇 생성 방법
# 1. 카카오 비즈니스 홈페이지 접속
# 참고 URL - https://business.kakao.com/

# *** "채널관리자센터" 화면 이동하는 방법 *** 
# 참고 - 카카오 비즈니스 홈페이지 상단 탭 "채널" 클릭 
# -> "내 채널" 화면 이동해서 채널 이름 "Test_ImagineBuilder" 클릭 
# -> "채널 관리자센터" 이동 

# 2. 카카오 비즈니스 홈페이지에서 카카오톡 채널 생성 진행 
# 1) 회원가입 및 로그인 진행 (카카오 계정 - wjsqhd2@naver.com)
# 2) 회원가입 및 로그인 완료시 카카오 비즈니스 홈페이지 우측 상단 버튼 "내 비즈니스" 클릭
# 3) "내 비즈니스" 화면 이동 -> 화면 좌측 상단 탭 "채널" 클릭 -> 버튼 "채널" 클릭 -> 화면 이동 -> 화면 하단 텍스트 "새로운 채널을 만들어보세요" 밑에 버튼 "새 채널만들기" 클릭
# 4) "비즈니스 채널 개설하기" 화면 이동 -> 사업자등록번호가 없으므로 화면 우측 중앙 "사업자등록번호가 없으신가요?" 클릭 -> 팝업화면 "사업자 번호가 없는 경우" 출력 -> 팝업화면 우측 하단 버튼 "일반채널 개설하기" 클릭
# 5) "채널 개설하기" 화면 이동 -> 프로필 사진 이미지 파일 등록 -> 채널 이름 "Test_ImagineBuilder" 등록 -> 검색용 아이디 "imbu_chatbot" 등록 -> 소개글 "상상진화 테스트 챗봇 프로그램" 등록 -> 카테고리 정보 "IT" "정보통신/SW" 등록 -> 버튼 "완료" 클릭
#    -> 팝업화면 "채널 개설을 위해 입력한 정보가 정확한가요?" 출력 -> 버튼 "네, 입력한 정보로 개설하겠습니다." 클릭 
# 6) "채널 개설이 완료되었습니다." 화면 이동 -> 버튼 "채널관리자센터로 이동" 클릭
# 7) "채널관리자센터" 화면 이동 -> 해당 화면 마우스 스크롤 아래로 내려서 화면 우측 하단 항목 "프로필 설정" 바로 밑에 "채널 공개" 및 "검색 허용" 둘다 (기존) OFF -> (변경) ON 처리 진행
# 8) "채널관리자센터" 화면 좌측 탭 "친구 모으기" 클릭 -> 버튼 "채널 홍보" 클릭 -> "홍보하기" 화면 이동
# 9) "홍보하기" 화면에 항목 "카카오톡에서 내 채널을 검색할 수 없는 상태예요. 검색 공개로 변경할까요?" 우측 버튼 "네, 변경합니다" 클릭 -> 팝업화면 "카카오톡에서 프로필, 소식이 검색됩니다." 출력 -> 버튼 "확인" 클릭 -> 팝업화면 "카카오톡에서 프로필/소식이 검색됩니다." 출력 -> 버튼 "확인" 클릭
# 10) "홍보하기" 화면 리본탭 "채널홈" 클릭 -> 화면 우측 중앙 항목 "내 채널홈" 아래 항목 "링크 복사하기" 아래 URL 주소 "http://pf.kakao.com/_sNBsn" 우측 버튼 "복사하기" 클릭
# 11) 10)번에서 복사한 카카오챗봇 프로그램 채널 URL 주소 메모장에 적어놓기 -> 카카오톡 채널 생성 완료

# 3. 카카오 비즈니스 홈페이지에서 카카오톡 채널 안에서 사용할 챗봇 계정 생성 진행
# 1) "카카오비즈니스" 화면 좌측 상단 탭 "채널" 클릭 -> 버튼 "챗봇" 클릭  
# 2) "다양한 봇 서비스를 만들어보세요!" 출력 -> 버튼 "채널 챗봇 만들기" 클릭 -> 버튼 "카카오톡 챗봇(카카오톡 채널 기반 챗봇)" 클릭
#    -> 팝업화면 "카카오톡 챗봇 생성" 출력 -> 항목 "카카오톡 챗봇 이름 설정" 옆에 챗봇 이름 "TestImbuChatBot" 입력 -> 버튼 "확인" 클릭
# 3) "카카오비즈니스" 화면 좌측 상단 탭 "채널" 다시 클릭 -> 버튼 "챗봇" 다시 클릭
#    -> 화면 "내 챗봇1" 이동 -> 항목 "봇이름" 밑에 2)번에서 생성한 챗봇 이름 "TestImbuChatBot" 클릭 
# 4) 새로 생성한 "TestImbuChatBot" 챗봇 관리자 센터 화면 이동 -> 카카오톡 챗봇 계정 생성 완료 


# 가상환경 폴더 "ch14_env" 생성 터미널 명령어
# python -m venv ch14_env

# 가상환경 폴더 "ch14_env" 활성화 터미널 명령어
# ch14_env\Scripts\activate.bat

# fastapi 터미널 설치 명령어
# pip install fastapi 

# 주의사항 
# 1. FastAPI 패키지 "fastapi" 단독으로는 웹개발을 할 수 없다.
#    하여 아래처럼 비동기(async - await) 웹서버 생성하는 유비콘 패키지 "uvicorn[standard]"를 추가로 터미널 설치 진행 
#    pip install "uvicorn[standard]"
# 2. 비동기(async - await) 웹서버 생성하는 유비콘 패키지 "uvicorn[standard]"를 사용하는 파이썬 파일의 경우 
#     일반 파이썬 파일을 터미널에서 실행하는 명령어(python 01_kakaobot_server.py)를 
#     그대로 쓰면 파일 안에 있는 FastAPI 서버(FastAPI 클래스 객체 app)가 생성 불가하다.
#     하여 비동기(async - await) 웹서버 생성하는 유비콘 패키지 "uvicorn[standard]"를 사용하는 파이썬 파일은
#     아래와 같은 명령어를 입력 해야만 해당 파일 안에 있는 FastAPI 서버(FastAPI 클래스 객체 app)가 생성된다.
#     uvicorn 01_kakaobot_server:app --reload
# 터미널 명령어 "uvicorn 01_kakaobot_server:app --reload" 입력 및 엔터 
# -> FastAPI 서버(FastAPI 클래스 객체 app)가 정상적으로 생성되면
#    터미널창에 아래와 같은 안내메시지(INFO)가 출력된다.
#    해당 안내메시지(INFO) 중 "http://127.0.0.1:8000" 문자열은
#    FastAPI 서버 로컬 PC URL 주소를 의미한다.
# INFO:     Will watch for changes in these directories: ['D:\\bhjeon\\test_chatGPT\\ch14']
# INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
# INFO:     Started reloader process [13104] using WatchFiles
# INFO:     Started server process [13684]
# INFO:     Waiting for application startup.
# INFO:     Application startup complete.

# 카카오톡 서버와 통신할 개발자 PC에서 실행시키는 FastAPI 로컬 서버 구현

# ngrok 역할?
# 외부에서 개발자 로컬 PC로 접속할 수 있는 URL 주소가 필요하다.
# ngrok는 개발자 로컬 PC에서 생성한 서버 개발 환경을
# 외부 서버에서도(전세계 어디 서버에서도) 접속할 수 있도록 공유해주는 서비스이다.
# 즉, 외부에서 개발자 로컬 PC로 접속할 수 있는 URL 주소를 발급해준다.
# 또한 서로 다른 네트워크(텔레그램 서버와 개발자 PC에서 실행시키는 FastAPI 로컬 서버)를
# 연결 해주는 통로의 역할을 하는 게이트웨이와 비슷한 역할이다.
# ngrok 웹사이트
# 참고 URL - https://ngrok.com/ 

# 게이트웨이 용어 설명
# 참고 URL - https://ko.wikipedia.org/wiki/%EA%B2%8C%EC%9D%B4%ED%8A%B8%EC%9B%A8%EC%9D%B4

# ngrok 응용 프로그램 실행 방법
# 1) 비쥬얼스튜디오코드(VSCode) 실행 
#    -> 유비콘 패키지 "uvicorn[standard]"를 사용하는 파이썬 파일 "01_kakaobot_server.py" 또는 "08_telegramebot.py" 열기
#    -> OpenAI API 키 값 입력 
#    -> 터미널창 열어서 명령어 "uvicorn 01_kakaobot_server:app --reload" 입력 및 엔터 
#    -> FastAPI 서버(FastAPI 클래스 객체 app)가 정상적으로 생성 완료

# 2) 텔레그램 응용 프로그램 실행 

# 3) PC 바탕 화면 -> ngrok 바로가기 아이콘 더블 클릭
# ngrok 바로가기 아이콘 존재하지 않으면 아래 파일경로 들어가서 ngrok 응용 프로그램 실행
# 파일 경로 - "C:\Users\bhjeon\Desktop\회사_업무_및_공부_자료\상상진화 회사 업무\AI 챗봇_개발\텔레그램_카카오_챗봇_ngrok_실행_프로그램" -> 응용 프로그램 ngrok

# 4) ngrok 전용 터미널창 출력 
#    -> 아래 명령어 "ngrok authtoken 2sZKZBZ9stzdWgsAPcHt9JtrNzN_5QpYosiEkadfnfffAvsvn" 입력 및 엔터 
# (명령어 형식) ngrok authtoken <Your token>
# (명령어 예시) ngrok authtoken 2sZKZBZ9stzdWgsAPcHt9JtrNzN_5QpYosiEkadfnfffAvsvn

# 5) 4)번의 토큰 번호 입력이 잘 되었을 경우 터미널창에 아래와 같은 메시지 출력
# Authtoken saved to configuration file: C:\Users\bhjeon\AppData\Local/ngrok/ngrok.yml

# 6) ngrok 응용 프로그램 터미널창에 명령어 "ngrok http 8000" 입력 및 엔터 
#    -> 외부 서버에서도 개발자 로컬 PC로 접속할 수 있는 URL 주소 생성 
# 참고사항 
# - 위에 명령어 중 "8000"이 뜻하는 바는 개발자 로컬 PC안에 포트(Port) 번호를 의미함.
# - 파이썬 파일 "01_kakaobot_server.py"을 유비콘 패키지 "uvicorn[standard]"를 사용하여 FastAPI 웹서버를 생성해 놓은 상태이다.
#   FastAPI 서버 로컬 PC URL 주소는 "http://127.0.0.1:8000" 이다.
#   해당 URL 주소 중 "http://127.0.0.1"은 개발자의 로컬 PC를 의미하며,
#   "8000"은 개발자의 로컬 PC 안에서 몇동 몇호, 즉 예를들어 105동 105호가 "8000"을 뜻한다.
#   하여 개발자의 로컬 PC 안에 "8000"이라는 포트(Port) 번호 안에 
#   새로 생성한 FastAPI 웹서버를 오픈한 것을 의미한다.
#   즉, ngrok 응용 프로그램 터미널창에서 명령어 "ngrok http 8000" 입력 및 엔터를 치면
#   외부 서버에서도 개발자 로컬 PC에 있는 포트(Port) 번호 "8000"에 있는
#   새로 생성한 FastAPI 웹서버에 접속할 수 있는 URL 주소를 생성해준다.

# 7) ngrok 응용 프로그램 터미널창에 아래와 같은 메시지가 출력되면
#    이제 외부 서버에서도 개발자 로컬 PC로 접속할 수 있는 FastAPI 웹서버 URL 주소 생성 완료.
#    아래에 출력된 메시지 중 외부 서버에서도 개발자 로컬 PC로 접속할 수 있는 
#    FastAPI 웹서버 URL 주소 (예) "https://1835-14-52-67-173.ngrok-free.app" 
#    로 외부 서버에서 접속을 하면 
#    개발자 로컬 PC에 포트(Port) 번호 "8000"로 접속이 가능("http://localhost:8000")하다는 것을 의미한다.
# 주의사항 - ngrok 응용 프로그램 터미널창에 URL 주소 "https://1835-14-52-67-173.ngrok-free.app" 
#           복사하려고 단축키 Ctrl + C 키를 누르면 ngrok 응용 프로그램이 종료된다.(Ctrl+C to quit)
#           하여 절대 단축키 Ctrl + C 키를 누르지 말고 마우스로 해당 URL 주소를 드래그 한 후 
#           키보드 단축키 Ctrl + Insert 키를 눌러서 해당 URL 주소를 복사 및 메모장에 저장한다.
# (예) 터미널창에 출력되는 메시지 예시
# ngrok    (Ctrl+C to quit)                                                                                                                                                                                   
# Sign up to try new private endpoints https://ngrok.com/new-features-update?ref=private                                                                                                                                                                                                                                                                                
# Session Status                online                                                                                                                                               
# Account                       minjaejeon0827@gmail.com (Plan: Free)                                                                                                                
# Version                       3.19.1                                                                                                                                               
# Region                        Japan (jp)                                                                                                                                           
# Latency                       36ms                                                                                                                                                 
# Web Interface                 http://127.0.0.1:4040                                                                                                                                
# Forwarding                    https://1835-14-52-67-173.ngrok-free.app -> http://localhost:8000                                                                                                                                                                                                                                                                       
# Connections                   ttl     opn     rt1     rt5     p50     p90                                                                                                                                        
#                               0       0       0.00    0.00    0.00    0.00     


# 8) "카카오비즈니스" 홈페이지 이동(참고 URL - https://business.kakao.com/) 
#    -> 카카오 계정 로그인 -> "카카오비즈니스" 화면 좌측 상단 탭 "채널" 클릭 -> 버튼 "챗봇" 클릭
#    -> 화면 "내 챗봇1" 이동 -> 항목 "봇이름" 밑에 2)번에서 생성한 챗봇 이름 "TestImbuChatBot" 클릭 
#    -> 새로 생성한 "TestImbuChatBot" 챗봇 관리자 센터 화면 이동 
#    -> 챗봇 관리자 센터 화면 좌측 탭 "스킬" 클릭 -> "스킬 목록" 클릭
#    -> "스킬 목록" 화면 이동 -> 버튼 "생성" 클릭

# 9) "스킬명을 입력해주세요" 화면 이동 -> 화면 상단 "스킬명을 입력해주세요"에 스킬명을 "kakaobot" 입력
#    -> 항목 "설명"에 내용 작성 생략 -> 항목 "URL"에 7)번에서 ngrok 응용 프로그램으로 생성한 
#       외부 서버에서도 개발자 로컬 PC로 접속할 수 있는 
#       FastAPI 웹서버 URL 주소(https://1835-14-52-67-173.ngrok-free.app) 뒤에 "/chat/" 붙인 
#       URL 주소(https://1835-14-52-67-173.ngrok-free.app/chat/)를 항목 "URL"에 입력하기
#    -> "스킬명을 입력해주세요" 화면 우측 상단 "기본 스킬로 설정" 체크
#    -> 버튼 "저장" 클릭 -> 해당 화면 마우스 스크롤 아래로 내려서 항목 "스킬 테스트" 이동 
#    -> 해당 "스킬 테스트" 항목은 카카오톡 서버와 연결이 잘 됐는지 확인할 수 있는 기능 "JSON"이 있다.
#    -> 해당 "JSON" 에서 작성된 양식은 카카오톡 서버 -> 개발자 로컬 PC FastAPI 서버로 
#       채팅 정보를 줄 때 전송하는 JSON 데이터 양식과 동일하다. 
#    -> 하여 해당 "JSON" 데이터를 가지고 디버깅 하면서 스킬 테스트를 진행할 수 있다.
#       해당 "JSON" 우측 하단 버튼 "스킬서버로 전송" 클릭
#    -> "스킬서버로 전송" 기능이 잘 실행되었는지 확인하려면
#       비쥬얼 스튜디오 코드 돌아와서 FastAPI 개발자 로컬 PC 비동기 웹서버 파이썬 파일(01_kakaobot_server.py)
#       @app.post("/chat/") 메서드 호출 -> async def chat(request: Request): 함수 실행 
#       -> 코드 kakaorequest = await request.json() 실행 ->  
#       print(kakaorequest) 함수 호출하여 터미널창에서 아래와 같은 결과가 출력되면 
#       "스킬서버로 전송" 기능이 잘 실행되었다는 것을 확인할 수 있다.
#       하여 해당 결과를 통하여 카카오톡 챗봇(카카오톡 서버)과 
#       FastAPI 개발자 로컬 PC 비동기 웹서버 파이썬 파일(01_kakaobot_server.py)이
#       연결이 아주 잘 되는 것을 확인할 수 있다.   
# {'intent': {
#             'id': 'qj4nick9o33seydhqobmj65t', 
#             'name': '블록 이름'
#            }, 
#  'userRequest': {'timezone': 'Asia/Seoul', 'params': {'ignoreMe': 'true'}, 
#  'block': {'id': 'qj4nick9o33seydhqobmj65t', 'name': '블록 이름'}, 
#  'utterance': '발화 내용', 
#  'lang': None, 
#  'user': {'id': '662293', 'type': 'accountId', 'properties': {}}}, 
#  'bot': {'id': '67a961ce1e098a447d574fe7', 
#  'name': '봇 이름'}, 
#  'action': {'name': 'vkjjc0ckza', 'clientExtra': None, 'params': {}, 
#  'id': 'o4yb2t6sg90zxh7qmnc8l85y', 'detailParams': {}}
# }       
# INFO: 219.249.231.42:0 - "POST /chat/ HTTP/1.1" 200 OK

# 10) "챗봇 관리자센터" 화면 좌측 상단 버튼 "시나리오" 클릭 
#     -> "시나리오" 화면 이동 -> 버튼 "+ 시나리오" 클릭 -> "시나리오" 화면 좌측 탭 "기본 시나리오" 하단 버튼 "폴백 블록" 클릭
#     -> "블록 이름을 입력해주세요" 출력 -> 항목 "파라미터 설정" 우측 체크 박스 "스킬 검색/선택" 클릭 -> 위에서 생성했던 스킬인 "kakaobot" 클릭
#     -> "시나리오" 화면 마우스 스크롤 아래로 내려서 항목 "봇 응답" 아래 
#        말풍선 형태 항목 "첫번째 응답 -텍스트형"의 
#        하위 항목 "+ 응답 추가 (0/3)" 아래에 있는 버튼 "스킬데이터" 클릭
#     -> 항목 "봇 응답" 아래에 있던 말풍선 형태 항목 "첫번째 응답 -텍스트형"이 사라지고 
#        항목 "봇 응답" 아래에 "스킬데이터 사용"만 출력되면 -> 버튼 "저장" 클릭
#     -> "스킬데이터" 저장 완료
#     "스킬데이터" 저장 완료되었다는 의미는 카카오톡 챗봇에서의 모든 기능을 방금 생성한 카카오봇 스킬
#     즉 카카오봇 스킬은 FastAPI 개발자 로컬 PC서버와 연결이 되어있다.
#     오직 FastAPI 개발자 로컬 PC서버 통해서만 카카오 챗봇이 모든 답변을 하겠다는 뜻으로 이해하면 된다.

# 11) 10)번까지 생성한(스킬데이터 저장 포함) 카카오 챗봇을 카카오톡 채널에 지정하려면 아래와 같이 한다.
#     -> "챗봇 관리자센터" 화면 좌측 버튼 "설정" 클릭 
#     -> "설정" 화면 이동 -> 항목 "기본 정보" 하단 하위 항목 "카카오톡 채널 연결" 옆에 버튼 "운영 채널 선택하기" 클릭 
#     -> 팝업화면 "운영 채널 연결" 출력 -> 맨 처음 단계에서 생성한 카카오톡 채널명 "Test_ImagineBuilder" 클릭
#     -> "설정" 화면 우측 상단 버튼 "저장" 클릭
#     -> 팝업화면 "배포를 진행하시겠습니까?" 출력 -> 버튼 "이동" 클릭

# 12) "배포" 화면 이동 -> "배포" 화면 우측 상단 "배포" 클릭
#     -> 팝업화면 "배포를 진행하시겠습니까?" 출력 -> 버튼 "배포" 클릭 
#     -> 처음 단계부터 지금까지 카카오 챗봇에 설정한 모든 사항들이 이제서야
#        외부 사용자들이 카카오 챗봇을 사용할 수 있도록 최종 배포 완료

# 13) 12)번에서 최종 배포 완료되었다면 최종 배포한 카카오 챗봇이 있는 대화창을 열어보려면 
#     "챗봇 관리자센터" 화면 좌측 상단 버튼 "kakao business" 클릭 
#     -> "카카오비즈니스 센터 대시보드" 화면 이동 
#     -> 항목 "자산 목록" 하단에 새로 생성했던 카카오톡 채널 "Test_ImagineBuilder" 클릭
#     -> "채널 관리자센터" 화면 이동 -> 해당 화면 좌측 탭 "친구 모으기" 클릭 -> 버튼 "채널 홍보" 클릭
#     -> "홍보하기" 화면 이동 -> 리본탭 "채널홈" 하단 하위 항목 "링크 복사하기" 하단 
#        URL 주소 "http://pf.kakao.com/_sNBsn" 옆에 버튼 "복사하기" 클릭 
#     -> 복사한 URL 주소 "http://pf.kakao.com/_sNBsn"를 구글 크롬(Chrome) 웹브라우저에 붙여넣기 및 엔터
#     -> 새로 생성한 카카오톡 채널 "Test_ImagineBuilder"이 화면상에 출력 
#     -> 해당 화면 우측 상단 버튼 "로봇모양 이모지콘" 클릭 
#     -> 카카오 (모바일/PC) 어플의 해당 카카오톡 채널 "Test_ImagineBuilder"의
#        카카오 챗봇 채팅방으로 이동 및 카카오 챗봇 안내 메시지 "안녕하세요. 무엇을 도와드릴까요?" 출력
#     -> 이제 맨 처음 단계에서 생성한 
#     카카오톡 채널 "Test_ImagineBuilder"에 외부 사용자가 채팅 입력을 하면 
#     그거에 대한 챗봇은 무조건 "TestImbuChatBot"이 대응하여 
#     외부 사용자의 채팅 입력에 대한 답변을 해준다.


# 카카오톡 챗봇 프로그램 실행 순서 
# 1 단계 : FastAPI를 사용해서 개발자 로컬 파이썬 서버(03_kakaobot.py) 실행(생성)
# 2 단계 : ngrok를 활용해서 외부 서버에서 개발자 로컬 PC로 접속하기 위한 URL 주소 발급 받기
# 3 단계 : 카카오톡 챗봇관리자 센터에 접속해서 
#          2 단계에서 발급받은 외부 서버에서 개발자 로컬 PC로 접속하기 위한 URL 주소 저장하여
#          카카오톡 서버와 FastAPI 개발자 로컬 파이썬 서버(03_kakaobot.py) 연결 

# 카카오톡 챗봇 프로그램 실행 순서(요약)
# 1) FastAPI를 활용해 개발자 로컬 PC 서버 생성하기
# 2) ngrok을 활용해 외부에서 개발자 로컬 PC 서버에 접속할 수 있는 URL 주소 생성하기
# 3) 카카오톡 챗봇 관리자 센터에서 카카오톡 서버와 개발자 로컬 PC 서버 연결하기

# 카카오톡 챗봇 프로그램 구조
# 1. 실행파일 - 03_kakaobot.py 
# - 실행파일 - 03_kakaobot.py 먼저 실행
# - FastAPI 파이썬 서버(03_kakaobot.py) 실행(생성)
# - 내부 주소로 실행 (http://localhost:8000/) 
# - 외부 서버에서 접근 불가 

# 2. FastAPI 서버 - 03_kakaobot.py 
# - 주소 별 특정 기능 수행 
# - 기본 연결 확인 "/"
#   http://localhost:8000/
# - 카카오톡 응답 "/chat" (카카오톡 서버로 전송)
#   http://localhost:8000/chat/

# 3. 카카오톡 서버
# - ngrok를 활용해서 외부 서버에서 개발자 로컬 PC로 접속하기 위한 URL 주소 발급 받기
#   카카오톡 챗봇관리자 센터에 접속해서 해당 외부 서버에서 개발자 로컬 PC로 접속 가능 URL 주소 저장 및 
#   카카오톡 서버와 FastAPI 로컬 파이썬 서버(03_kakaobot.py) 연결하기 

