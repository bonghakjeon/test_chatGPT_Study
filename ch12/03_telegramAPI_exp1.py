# 가상환경 폴더 "ch12_env" 생성 터미널 명령어
# python -m venv ch12_env

# 가상환경 폴더 "ch12_env" 활성화 터미널 명령어
# ch12_env\Scripts\activate.bat

# 파이썬 파일 "03_telegramAPI_exp1.py" 터미널 실행 명령어
# python 03_telegramAPI_exp1.py

# 파이썬 파일 "03_telegramAPI_exp1.py" 실행시 
# 오류 메시지 ModuleNotFoundError: No module named 'urllib3'
# 해결하기 위해 파이썬 기본 내장 패키지(라이브러리) - "urllib3" 삭제 및 
# 버전 1.26.18 설치 진행 
# 참고 URL - https://heidong.tistory.com/278
# 1) pip uninstall urllib3
# 2) pip install urllib3==1.26.18

# 텔레그램 PC 프로그램 다운로드 방법
# 참고 URL - https://m.blog.naver.com/voramines/223163473669

# 텔레그램 PC 프로그램 다운로드 사이트
# 다운로드 URL - https://desktop.telegram.org/

# 텔레그램 모바일 어플 언어 "한국어" 변경 방법
# 참고 URL - https://lifenourish.tistory.com/2165

# JSON 데이터 보기 편하게 해주는 jsonformatter 사이트 
# 참고 URL - https://jsonformatter.curiousconcept.com/

# 텔레그램 전용 API 사이트 
# 참고 URL - https://core.telegram.org/

# 텔레그램 API의 HTTP 통신 요청시 필요한 URL 양식 :
# https://api.telegram.org/bot{BOT_TOKEN}/METHOD_NAME
# - 텔레그램 채팅방에 입력된 채팅 메시지나 채팅 정보 확인 HTTP 통신 요청 URL :
# https://api.telegram.org/bot{BOT_TOKEN}/getUpdates
# - 메시지 전송 HTTP 통신 요청 URL :
# https://api.telegram.org/bot{BOT_TOKEN}/sendMessage
# - 사진 전송 HTTP 통신 요청 URL :
# https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto

# 웹훅이란?
# 텔레그램 API의 getUpdates 메소드와 비슷한 기능으로 
# 텔레그램 채팅방에서 새로운 채팅이 생성될 때마다
# 자동으로 우리의 서버로 채팅 메시지나 채팅 정보를 전송 해주는 기능이다.

import urllib3   # HTTP 통신을 하기위해 파이썬 기본 내장 패키지(함수) urllib3 불러오기 - 아마존 웹서비스(AWS)에서 사용하기 용이하다.
import json   # 텔레그램 서버로부터 받은 json 데이터 처리하기 위해 패키지 json 불러오기 

# 테스트용 텔레그램 챗봇 채팅방에서 
# HTTP 통신하기 위한 고유 토큰 번호 문자열을 변수 BOT_TOKEN에 할당 
# BOT_TOKEN = 'Token'
BOT_TOKEN = '7717605195:AAHJGNKRR_aK_dG0HELQUBu1WeEsclERRb0'

# 텔레그램 채팅방에 입력된 채팅 메시지나 채팅 정보 확인
def get_updates():
    # 라이브러리(패키지) urllib3의 PoolManager 클래스 객체 http 생성
    http = urllib3.PoolManager()
    # 텔레그램 채팅방에 입력된 채팅 메시지나 채팅 정보 확인 하기 위해
    # 텔레그램 API의 getUpdates 메소드 활용한 HTTP 통신 요청 문자열 사용
    # "https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
    # 단순히 텔레그램 채팅방에 입력된 채팅 메시지나 채팅 정보 확인하기 위한
    # 용도이기 때문에 HTTP Request(요청) - GET 방식 으로 진행 
    response = http.request('GET', url)   # HTTP Request(요청) - GET 방식
    # 텔레그램 채팅방의 현재 채팅 메시지나 채팅 정보 아래처럼 리턴 
    # json.loads 함수 호출 하여 JSON 문자열 -> Dictionary 객체 변환 처리 
    # JSON 문자열 (예) '{"name": "홍길동", "birth": "0525", "age": 30}'
    # Dictionary 객체 (예) {'name': '홍길동', 'birth': '0525', 'age': 30}
    # 참고 URL - https://wikidocs.net/126088 
    return json.loads(response.data.decode('utf-8'))

# Get the latest updates
# 텔레그램 채팅방의 현재 채팅 메시지나 채팅 정보가 
# 아래처럼 리턴되서 변수 updates에 저장 
updates = get_updates()

# 텔레그램 채팅방에서 주고받은 채팅 메시지나 채팅 정보는
# 'result' 라는 변수 안에서 저장되서 json 데이터 형식으로 출력 가능
# 'result' 라는 변수안에 속한 정보
# 'id' - 채팅방 아이디 "8000253838" (텔레그램 API 사용하여 텍스트를 전송하거나 사진 파일을 전송할 때 필요함.)
# 'from' - 채팅을 보낸 사람 정보 
# 'chat' - 채팅을 쓴 사람 정보 
# 'text' - 채팅방에서 주고받은 채팅 내용 (예) "안녕하세요"
# {'ok': True, 'result': [{'update_id': 250682836, 'message': {'message_id': 2, 'from': {'id': 8000253838, 'is_bot': False, 'first_name': '민재', 'last_name': '전', 'language_code': 'ko'}, 'chat': {'id': 8000253838, 'first_name': '민재', 'last_name': '전', 'type': 'private'}, 'date': 1738637137, 'text': '안녕하세요'}}]}

# 텔레그램 채팅방에서 주고받은 채팅 메시지나 채팅 정보가 없는 경우 
# print(updates) 호출시 터미널 창에 아래처럼 빈결과('result': [])로 출력 
# {'ok': True, 'result': []}

# 텔레그램 채팅방에서 주고받은 채팅 메시지나 채팅 정보가 "안녕하세요"가 입력된 경우 
# {'ok': True, 'result': [{'update_id': 250682836, 'message': {'message_id': 2, 'from': {'id': 8000253838, 'is_bot': False, 'first_name': '민재', 'last_name': '전', 'language_code': 'ko'}, 'chat': {'id': 8000253838, 'first_name': '민재', 'last_name': '전', 'type': 'private'}, 'date': 1738637137, 'text': '안녕하세요'}}]}
print(updates)   # 변수 updates에 할당된 값 터미널창 출력
