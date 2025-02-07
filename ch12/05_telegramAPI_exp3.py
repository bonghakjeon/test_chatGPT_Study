# 웹훅이란?
# 텔레그램 API의 getUpdates 메소드와 비슷한 기능으로 
# 텔레그램 채팅방에서 새로운 채팅이 생성될 때마다
# 자동으로 우리의 서버로 채팅 메시지나 채팅 정보를 전송 해주는 기능이다.

# 테스트용 텔레그램 챗봇 채팅방에 이미지 보내기 

import urllib3   # HTTP 통신을 하기위해 파이썬 기본 내장 패키지(함수) urllib3 불러오기 - 아마존 웹서비스(AWS)에서 사용하기 용이하다.
import json   # 텔레그램 서버로부터 받은 json 데이터 처리하기 위해 패키지 json 불러오기 

# 테스트용 텔레그램 챗봇 채팅방에서 
# HTTP 통신하기 위한 고유 토큰 번호 문자열을 변수 BOT_TOKEN에 할당 
# BOT_TOKEN = 'Token'
BOT_TOKEN = '7717605195:AAHJGNKRR_aK_dG0HELQUBu1WeEsclERRb0'

# 테스트용 텔레그램 챗봇 채팅방 아이디 - "8000253838"

# 텔레그램 채팅방에 이미지 보내기
# 아래 sendPhoto 함수 호출시
# ChatGPT - DALL.E 2가 그려주고 최종 생성된 이미지 URL 주소를 
# 인자로 전달하여 텔레그램 채팅방에 이미지 보내는 것도 가능함.
def sendPhoto(chat_id, image_url):
    # 변수 data에 채팅방에 전송할 이미지 URL 주소가 담긴
    # JSON 포맷 데이터 저장 
    # ('chat_id' - 이미지 전송할 채팅방 아이디 / 'text' - 채팅방으로 전송할 이미지 URL 주소)
    data = {
        'chat_id': chat_id,
        'photo': image_url,
    }
    # 라이브러리(패키지) urllib3의 PoolManager 클래스 객체 http 생성
    http = urllib3.PoolManager()
    # 텔레그램 채팅방에 이미지 보내기 위해
    # 텔레그램 API의 sendPhoto 메소드 활용한 HTTP 통신 요청 문자열 사용
    # "https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    # 텔레그램 채팅방에 이미지 보내기 위한 
    # 용도이기 때문에 HTTP Request(요청) - POST 방식 으로 진행 
    # HTTP POST 요청하여 채팅방에 전송할 이미지 URL 주소가 담긴 변수(data)를 추가로 저장 
    # http.request 함수 호출시 'POST', url, fields=data 3가지 인자 전달 
    response = http.request('POST',url ,fields=data)
    # 텔레그램 채팅방에 전송한 이미지 정보 및 
    # 텔레그램 서버에서 채팅방으로 이미지를 잘 전송했다고 
    # 이미지를 전송한 행위에 대한 정보 아래처럼 리턴 
    # json.loads 함수 호출 하여 JSON 문자열 -> Dictionary 객체 변환 처리 
    # JSON 문자열 (예) '{"name": "홍길동", "birth": "0525", "age": 30}'
    # Dictionary 객체 (예) {'name': '홍길동', 'birth': '0525', 'age': 30}
    # 참고 URL - https://wikidocs.net/126088 
    return json.loads(response.data.decode('utf-8'))

# 텔레그램 채팅방에 이미지 보내기 위해 
# 함수 sendPhoto 호출시 
# 채팅방 아이디 "8000253838", 
# 이미지 URL 주소 "https://wikibook.co.kr/images/cover/l/9791158394608.jpg" 인자로 전달 
result = sendPhoto(8000253838,"https://wikibook.co.kr/images/cover/l/9791158394608.jpg")

# 텔레그램 채팅방에 전송한 이미지 정보 및 
# 텔레그램 서버에서 채팅방으로 이미지를 잘 전송했다고 
# 이미지를 전송한 행위에 대한 정보 터미널창 출력 
# 터미널창에 출력된 정보 설명
# 'first_name': 'Telegrambot' (채팅방 개설할 때 지정했던 이름)
# 'first_name': '민재', 'last_name': '전' (채팅방 안에서 이미지를 전송받은 사람의 정보)
# 'photo' (방금 전 채팅방으로 전송한 이미지 정보 - 'file_id', 'file_unique_id', 'file_size', 'width', 'height')
# {'ok': True, 'result': {'message_id': 4, 
#                         'from': {'id': 7717605195, 'is_bot': True, 'first_name': 'Telegrambot', 'username': 'testinflearnGPTAPI_bot'}, 
#                         'chat': {'id': 8000253838, 'first_name': '민재', 'last_name': '전', 'type': 'private'}, 
#                         'date': 1738647676, 
#                         'photo': [{'file_id': 'AgACAgQAAxkDAAMEZ6GofD3rkjvAdg52lNh2o6XCUpwAAnWxMRsVazVTA5dGvaULBgMBAAMCAANzAAM2BA', 'file_unique_id': 'AQADdbExGxVrNVN4', 'file_size': 1412, 'width': 69, 'height': 90}, 
#                                   {'file_id': 'AgACAgQAAxkDAAMEZ6GofD3rkjvAdg52lNh2o6XCUpwAAnWxMRsVazVTA5dGvaULBgMBAAMCAANtAAM2BA', 'file_unique_id': 'AQADdbExGxVrNVNy', 'file_size': 15880, 'width': 245, 'height': 320}, 
#                                   {'file_id': 'AgACAgQAAxkDAAMEZ6GofD3rkjvAdg52lNh2o6XCUpwAAnWxMRsVazVTA5dGvaULBgMBAAMCAAN4AAM2BA', 'file_unique_id': 'AQADdbExGxVrNVN9', 'file_size': 24982, 'width': 460, 'height': 600}]}}
print(result)   # 변수 result에 할당된 값 터미널창 출력