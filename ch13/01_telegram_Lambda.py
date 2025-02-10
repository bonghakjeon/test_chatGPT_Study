# 가상환경 폴더 "ch13_env" 생성 터미널 명령어
# python -m venv ch13_env

# 가상환경 폴더 "ch13_env" 활성화 터미널 명령어
# ch13_env\Scripts\activate.bat

# 아마존 웹서비스(AWS)
# 클라우드 워치(CloudWatch) 서비스란?

# 아마존 웹서비스(AWS) 람다 함수 "lambda_handler"가
# 호출되는 모든 로그를 저장하고 관리하는 기능이다.

# 해당 로그를 통해 실제 코드가 작동되고 있는지 확인할 수 있고 에러도 확인하고 디버깅 또한 할 수 있다.

# 아마존 웹서비스(AWS)
# 클라우드 워치(CloudWatch) 서비스 사용 방법

# 1. 아마존 웹서비스(AWS) 람다(Lanbda) 화면 들어와서
# -> 함수 "inflearn_Telegram" 들어오기
# -> 화면 하단 탭 "모니터링" 버튼 클릭

# 2. "Monitor" 화면 이동 -> 해당 화면에서 마우스 스크롤 아래로 이동 -> 항목 "CloudWatch Logs" 아래에 보면
# 아마존 웹서비스(AWS) 람다 함수 "lambda_handler"가
# 호출됐던 모든 로그가 시간 순으로 정리되어 출력된다.

# 텔레그램 채팅방에서 사용자가 질문(또는 그림 생성 요청) 입력될 때마다
# 텔레그램 서버 -> 아마존 웹서비스(AWS) API Gateway 주소로 
# 사용자가 질문(또는 그림 생성 요청)이 전달될 수 있도록 
# 텔레그램 API "setWebhook" 사용한 연결 방법
# 1. 구글 크롬(Chrome) 웹브라우저에 아래와 같은 URL 주소 형식 입력 및 엔터
# (형식) https://api.telegram.org/bot<토큰>/setWebhook?url=<아마존 웹서비스(AWS) API Gateway URL 주소>
# (예) https://api.telegram.org/bot7717605195:AAHJGNKRR_aK_dG0HELQUBu1WeEsclERRb0/setWebhook?url=https://9qfl81l1ng.execute-api.ap-northeast-2.amazonaws.com/inflearn_Telegram

# 2. 구글 크롬(Chrome) 웹브라우저에 json 데이터 출력 
# -> 항목 "description"에 매핑된 값이 "Webhook was set" 이라고 출력되면
# -> 텔레그램 채팅방에서 사용자가 질문(또는 그림 생성 요청) 입력될 때마다
#    텔레그램 서버 -> 아마존 웹서비스(AWS) API Gateway 주소 연결 완료
# {"ok":true,"result":true,"description":"Webhook was set"}

# 3. 2번 처럼 텔레그램 채팅방에서 사용자가 질문(또는 그림 생성 요청) 입력될 때마다
#    텔레그램 서버 -> 아마존 웹서비스(AWS) API Gateway 주소 연결 완료되면 
#    기존에 ngrok 사용하여 setWebhook 처리한 URL 주소 "https://api.telegram.org/bot7717605195:AAHJGNKRR_aK_dG0HELQUBu1WeEsclERRb0/setWebhook?url=https://7839-14-52-67-173.ngrok-free.app/chat"
#    는 setWebhook 처리가 해제된다.
#    왜냐면 setWebhook은 채팅방에 단 하나의 URL 주소만 setWebhook 처리해주기 때문이다.
#    즉, 동시에 두 개의 URL 주소를 연결 안 해준다.


# 람다(lambda) 함수 소스파일 "lambda_function.py" 열고 -> 화면 좌측 버튼 "Test" 클릭 
# -> 컴파일 실행시 아래 "OUTPUT - Execution Results" 탭 화면 출력되고
# 아래 응답값(Response) -> 오류 메시지("errorMessage") "Unable to import module 'lambda_function': No module named 'openai'"가 출력되는
# 이유는 안타깝게도 아마존 웹서비스(AWS) 람다(lambda) 에서는 pip 명령어 사용해서 손쉽게 OpenAI 패키지 "openai"를 설치할 수 있는 도구가 없어서 발생한 오류이다.
# 대신에 패키지 코드를 파일 형식으로 직접 업로드해서 패키지를 사용할 수는 있다.
# 하여 OpenAI 패키지 코드를 다운 받아서 압축을 해서 람다(lambda) 함수 안에 업데이트 해야한다.
# 알집 압축 파일(python.zip)안에 해당 OpenAI 패키지 코드가 저장되어 있고,
# 해당 압축 파일은 파일 경로("D:\bhjeon\test_chatGPT\ch13" 폴더 -> "python.zip")에 존재한다.
# 해당 압축 파일을 아마존 웹서비스(AWS) 람다(Lambda)에 업로드하면 람다(lambda) 함수 소스파일 "lambda_function.py" 안에서도 
# OpenAI 패키지를 사용할 수 있다.
# Response:
# {
#   "errorMessage": "Unable to import module 'lambda_function': No module named 'openai'", # 오류 메시지 출력 
#   "errorType": "Runtime.ImportModuleError",
#   "requestId": "",
#   "stackTrace": []
# }

# 람다(lambda) 함수 소스파일 "lambda_function.py" 
# OpenAI 패키지 파일("python.zip") 아마존 웹서비스(AWS) 람다(Lambda)에 업로드 방법
# 1. 아마존 웹서비스(AWS) 람다(Lambda) 화면 좌측 상단 햄버거 모양 버튼 클릭 -> 화면 좌측 내비게이션바 출력 -> 항목 "추가 리소스" 하단 "계층" 클릭
# 2. 화면 "계층" 출력 -> 화면 우측 버튼 "계층 생성" 클릭 
# 3. 화면 "계층 생성" 출력 -> 항목 "이름"에 값 "openai_311" 입력 -> ".zip 파일 업로드" 체크 -> 버튼 "업로드" 클릭 
#    -> "열기" 팝업 화면 출력 -> 파일 경로("D:\bhjeon\test_chatGPT\ch13" 폴더 -> "python.zip") 이동 -> .zip 파일(python.zip) 클릭 -> 버튼 "열기(O)" 클릭 
# 4. 항목 "호환 아키텍쳐 - 선택 사항"에 "x86_64" 체크 -> 항목 "호환 런타임 - 선택 사항"에 값 "Python 3.11" 체크 -> 버튼 "생성" 클릭
# 5. 계층 생성 완료 -> 다시 아마존 웹서비스(AWS) 람다(Lambda) 함수 "inflearn_Telegram" 들어와서 항목 "함수 개요" 안에 속한 버튼 "Layers" 클릭
# 6. 화면 하단 항목 "계층" 이동 -> 버튼 "Add a layer" 클릭 
# 7. "계층 추가" 화면 이동 -> 항목 "계층 선택" 하단 "사용자 지정 계층" 클릭 
#    -> 항목 "사용자 지정 계층"에 5번에서 생성한 계층인 "openai_311" 클릭 -> 버튼 "추가" 클릭 
# 8. OpenAI 패키지 파일("python.zip") 아마존 웹서비스(AWS) 람다(Lambda)에 업로드 완료 

# 람다(lambda) 함수 lambda_handler 동작 제한시간 설정 변경 방법
# 람다(lambda) 함수 lambda_handler의 동작 제한시간은 기본 3초로 설정되어 있다.
# 함수 동작시간이 3초를 넘어가면 작동을 멈추게 된다.
# 하지만 ChatGPT의 답변 생성 속도와 DALLE.2의 그림 생성 속도는 3초로는 많이 부족하다.
# 하여 아래 방법 처럼 람다(lambda) 함수 lambda_handler 동작 제한시간 설정을 변경하면 된다.
# 1. 해당 소스파일 위 탭 "구성" 클릭 -> 화면 좌측 버튼 "일반 구성" 클릭 -> "일반 구성" 화면 출력 -> 화면 우측 버튼 "편집" 클릭
# 2. "기본 설정 편집" 화면 이동 -> 항목 "제한 시간" (기존) 0분 3초 -> (변경) 1분 0초 -> 버튼 "저장" 클릭 
# 3. 람다(lambda) 함수 lambda_handler 동작 제한시간 설정 변경 완료

# 아마존 웹서비스(AWS) 람다(lambda) 함수에서 작동하는 메인함수 lambda_handler 코드 작성 
# 아래 메인함수 lambda_handler의 코드를 수정한다고 해서 바로 람다(lambda) 함수에 반영이 되는게 아니라
# 메인함수 lambda_handler의 코드 수정 -> 단축키 Ctrl + s 누르고 -> 소스코드 변경사항 저장 
# -> 화면 좌측 버튼 "Deploy (Ctrl+Shift+U)" 클릭 -> 화면 상단 메시지 "함수 inflearn_Telegram이(가) 업데이트되었습니다." 출력
# -> 람다(lambda) 함수에 반영된다.

# 람다(lambda) 함수 테스트 방법
# 참고사항 - "Create new test event" 팝업 화면은 메인함수 lambda_handler의 코드를 테스트할 때, 
# 함수에 전달되는 파라미터인 event 변수에 담을 정보를 작성하는 팝업 화면이다.
# 화면 좌측 버튼 "Test (Ctrl+Shift+I)" 클릭 -> 팝업화면 "Select test event" 출력 -> 버튼 "Create new test event" 클릭
# -> "Create new test event" 팝업 화면 출력 
# -> 항목 "Event Name"에 "test" 입력 -> 버튼 "Save" 클릭
# -> 메세지 "Test event is saved successfully." 출력 
# -> 다시 화면 좌측 "test" 버튼 클릭 
# -> 화면 하단 "OUTPUT - Execution Results" 탭 화면 출력
# -> "test" 이벤트 코드 실행 결과 아래처럼 출력 
# Status: Succeeded
# Test Event Name: test

# 람다(lambda) 함수 lambda_handler 실행되었을 때의 
# 리턴값이 그대로 
# return {
#     'statusCode': 200,
#     'body': json.dumps('Hello from Lambda!')
# }
# 아래 "Response"로 똑같이 출력
# Response:
# {
#   "statusCode": 200,
#   "body": "\"Hello from Lambda!\""
# }

# 람다(lambda) 함수 lambda_handler 실행한 결과 
# print 함수 호출해서 event, context 라는 파라미터에 
# 들어온 정보 출력된 결과를 
# 아래 항목 "Function Logs:"로 출력 
# Function Logs:
# START RequestId: a15e368c-ebb2-430f-b32f-43db66d78c74 Version: $LATEST
# 아래처럼 "event" 파라미터에 새로 생성한 test event "test"에서 
# 항목 "Event JSON"에서 작성한 JSON 데이터 양식이 그대로 출력
# 참고사항 
# 람다(lambda) 함수 lambda_handler 안에 메인코드 작성할 때,
# 새로 생성한 test event "test"가 아니라
# 실제 텔레그램 채팅방으로 부터 넘어오는 채팅의 정보가 
# 아래 JSON 데이터 양식의 "evnet" 파라미터를 통해 받을 수 있다.       
# event : {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
# context : LambdaContext([aws_request_id=a15e368c-ebb2-430f-b32f-43db66d78c74,log_group_name=/aws/lambda/inflearn_Telegram,log_stream_name=2025/02/06/[$LATEST]a8b0d48d3249452390205752bbba2a82,function_name=inflearn_Telegram,memory_limit_in_mb=128,function_version=$LATEST,invoked_function_arn=arn:aws:lambda:ap-northeast-2:980921720325:function:inflearn_Telegram,client_context=None,identity=CognitoIdentity([cognito_identity_id=None,cognito_identity_pool_id=None])])
# END RequestId: a15e368c-ebb2-430f-b32f-43db66d78c74
# REPORT RequestId: a15e368c-ebb2-430f-b32f-43db66d78c74	Duration: 1.27 ms	Billed Duration: 2 ms	Memory Size: 128 MB	Max Memory Used: 33 MB	Init Duration: 72.23 ms

# Request ID: a15e368c-ebb2-430f-b32f-43db66d78c74


# 참고 사항
# 구현하고자 하는 텔레그램 챗봇 서비스 프로그램으로 부터
# 정보가 넘어오는 json 데이터 양식이 있다면 
# 해당 팝업화면 항목 "Event JSON" 부분에 아래처럼 작성하면 
# 따로 텔레그램 서버와 연결하지 않고도 람다(lambda) 함수 환경 안에서도
# 테스트를 해서 디버깅이 가능하다. 
# import json

# 람다(lambda)가 실행명령을 받았을 때, 실행되는 메인함수 lambda_handler
# 파이썬 또는 C/C++ 프로그래밍 언어에서 main 함수와 같은 역할을 한다.
# 또한 해당 함수는 event, context 라는 파라미터를 매개변수로 전달 받는다.
# def lambda_handler(event, context):
#     # TODO implement
#     # event, context에 어떤 정보가 들어오는지 확인
#     # event, context 출력 
#     print("event :", event)
#     print("context :", context)

#     return {
#         'statusCode': 200,
#         'body': json.dumps('Hello from Lambda!')
#     }


import urllib3   # HTTP 통신을 하기위해 파이썬 기본 내장 패키지(함수) urllib3 불러오기
import json      # 텔레그램 서버로부터 받은 json 데이터 처리하기 위해 패키지 json 불러오기 
import openai    # OPENAI 패키지 openai 불러오기 
import os
# FastAPI 패키지 "fastapi" / Request 패키지를 사용하지 않고
# 주석처리 하는 이유는 따로 개발자 PC FastAPI 로컬 서버를 생성할 필요 없이
# AWS 람다(Lambda) 함수 lambda_handler를 바로 호출하면 되기 때문에 
# 더이상 FastAPI 패키지 "fastapi" / Request 패키지가 필요 없기 때문이다.
# FastAPI 패키지 "fastapi" 불러오기
# Request 패키지 불러오기 
# from fastapi import Request, FastAPI

# 아마존 웹서비스(AWS) 함수 lambda_handler -> 환경변수로 저장한 텔레그램 채팅방 토큰 'TELE_TOKEN' 불러오기 
# 텔레그램 채팅방 토큰값 - 7717605195:AAHJGNKRR_aK_dG0HELQUBu1WeEsclERRb0
BOT_TOKEN = os.environ['TELE_TOKEN'] 
# 아마존 웹서비스(AWS) 함수 lambda_handler-> 환경변수로 저장한 OpenAI API 키 'OPENAI_API' 불러오기
openai.api_key = os.environ['OPENAI_API']

# 람다(lambda)가 실행명령을 받았을 때, 실행되는 메인함수 lambda_handler
# 파이썬 또는 C/C++ 프로그래밍 언어에서 main 함수와 같은 역할을 한다.
# 또한 해당 함수는 event, context 라는 파라미터를 매개변수로 전달 받는다.
def lambda_handler(event, context):
    
    # json.loads 함수 호출 하여 JSON 문자열 -> Dictionary 객체 변환 처리 및
    # Dictionary 객체를 변수 result에 저장 
    # JSON 문자열 (예) '{"name": "홍길동", "birth": "0525", "age": 30}'
    # Dictionary 객체 (예) {'name': '홍길동', 'birth': '0525', 'age': 30}
    # 참고 URL - https://wikidocs.net/126088 
    # 텔레그램 채팅방 정보가 event 파라미터를 통해서 람다(lambda) 함수 lambda_handler 로 넘어온다.
    # event['body'] - 텔레그램 채팅방 정보가 들어있는 변수이다.
    result = json.loads(event['body'])
    
    # 텔레그램을 통해 입력받은 채팅 정보(메시지)가
    # 챗봇(['from']['is_bot'])이 입력한 메시지가 아닌 경우 
    # 즉, 사람이 입력한 메시지인 경우 의미
    if not result['message']['from']['is_bot']:

        # 메세지를 보낸 사람의 chat ID 
        # 텔레그램 채팅방에서 채팅 메시지를 입력한 사용자에게
        # 회신을 하기 위해서 사용자의 아이디(['message']['chat']['id'])를 변수 chat_id에 저장 
        chat_id = str(result['message']['chat']['id'])

        # 해당 메세지의 ID
        # 텔레그램 채팅방에서 채팅 메시지를 입력한 사용자에게
        # 회신을 하기 위해서 채팅 메세지의 아이디(['message']['message_id']))를 변수 msg_id에 저장 
        # 변수 msg_id에 채팅 메세지의 아이디를 저장하는 이유는
        # 사용자가 텔레그램 챗봇이 미처 답변을 하기 전에 
        # 다른 질문을 연달아 넣을 수도 있기 때문이다.
        # 그럴 경우 각각의 채팅 메시지에 회신을 하기 위해서
        # 해당 채팅 메시지의 아이디(['message']['message_id']))를 
        # 아래와 같이 저장을 해야한다.
        msg_id = str(int(result['message']['message_id']))

        # 만약 그림 생성을 요청하면
        # 만약 텔레그램 채팅방에 사용자가 입력한 메시지 안에
        # '/img'란 문자열이 포함되어 있으면,  
        # 즉, DALLE.2에게 그림 생성을 요청한 경우 
        if '/img' in result['message']['text']:
            # "/img"란 문자열만 공백("")으로 변환(replace) 처리 하고 
            # DALLE.2에게 그림 생성을 요청한 프롬프트(Prompt) 내용만 발췌하여 변수 prompt에 저장
            prompt = result['message']['text'].replace("/img", "")
            # DALL.E 2로부터 생성한 이미지 URL 주소 받기
            # getImageURLFromDALLE 함수 호출시 위의 변수 prompt 인자로 전달하여
            # DALL.E 2에게 그림 생성 요청 및 생성한 이미지 URL 주소 받기
            # DALL.E 2가 생성한 이미지의 URL 주소를 변수 bot_response에 저장하기 
            bot_response = getImageURLFromDALLE(prompt)
            # 이미지 텔레그램 방에 보내기
            # sendPhoto 함수 호출시 위의 변수 3가지
            # chat_id, bot_response, msg_id 인자로 전달하여
            # 텔레그램 채팅방에 DALL.E 2가 생성한 이미지 전송 처리
            # 이 때 위에 있는 변수 chat_id, msg_id를 활용해서
            # 채팅 메시지를 입력한 사용자와 해당 메시지에게
            # 직접 이미지 전송 처리함.
            print(sendPhoto(chat_id,bot_response, msg_id))
        # 만약 chatGPT의 답변을 요청하면
        # 만약 텔레그램 채팅방에 사용자가 입력한 메시지 안에
        # '/ask'란 문자열이 포함되어 있으면,  
        # 즉, ChatGPT에게 답변을 요청한 경우 
        if '/ask' in result['message']['text']:
            # "/ask"란 문자열만 공백("")으로 변환(replace) 처리 하고 
            # ChatGPT에게 질문한 프롬프트(Prompt) 내용만 발췌하여 변수 prompt에 저장
            prompt = result['message']['text'].replace("/ask", "")
            # ChatGPT로부터 답변 받기
            # getTextFromGPT 함수 호출시 위의 변수 prompt 인자로 전달하여
            # ChatGPT에게 질문을 하고 답변 받기
            # ChatGPT에게 받은 답변을 변수 bot_response에 저장하기 
            bot_response = getTextFromGPT(prompt)
            # 답변 텔레그램 방에 보내기
            # sendMessage 함수 호출시 위의 변수 3가지
            # chat_id, bot_response, msg_id 인자로 전달하여
            # 텔레그램 채팅방에 ChatGPT에게 받은 답변 전송 처리
            # 이 때 위에 있는 변수 chat_id, msg_id를 활용해서
            # 채팅 메시지를 입력한 사용자와 해당 메시지에게
            # 직접 ChatGPT에게 받은 답변 전송 처리함.
            print(sendMessage(chat_id, bot_response,msg_id))
    
    return 0

###### 기능 함수 구현 단계 ######

# 메세지 전송
# 텔레그램 채팅방에 ChatGPT의 답변을 채팅 메시지로 보내기
# ChatGPT의 답변을 아래 sendMessage 함수를 호출하여
# 텔레그램 채팅방에 채팅 메시지 보내는 것도 가능함.
def sendMessage(chat_id, text,msg_id):
    # 변수 data에 채팅방에 전송할 채팅 메시지가 담긴
    # JSON 포맷 데이터 저장 
    # 'chat_id' - 텍스트 전송할 채팅방 아이디 
    # 'text' - 채팅방으로 전송할 채팅 메시지 내용
    # 'reply_to_message_id' - 사용자가 보낸 메세지 아이디
    data = {
        'chat_id': chat_id,
        'text': text,
        'reply_to_message_id': msg_id
    }
    # 라이브러리(패키지) urllib3의 PoolManager 클래스 객체 http 생성
    http = urllib3.PoolManager()
    # 텔레그램 채팅방에 채팅 메시지 보내기 위해
    # 텔레그램 API의 sendMessage 메소드 활용한 HTTP 통신 요청 문자열 사용
    # "https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    # 텔레그램 채팅방에 채팅 메시지 보내기 위한 
    # 용도이기 때문에 HTTP Request(요청) - POST 방식 으로 진행 
    # HTTP POST 요청하여 채팅방에 전송할 채팅 메시지가 담긴 변수(data)를 추가로 저장 
    # http.request 함수 호출시 'POST', url, fields=data 3가지 인자 전달 
    response = http.request('POST',url ,fields=data)
    # 텔레그램 채팅방에 보낸 채팅 메시지 정보 아래처럼 리턴 
    # json.loads 함수 호출 하여 JSON 문자열 -> Dictionary 객체 변환 처리 
    # JSON 문자열 (예) '{"name": "홍길동", "birth": "0525", "age": 30}'
    # Dictionary 객체 (예) {'name': '홍길동', 'birth': '0525', 'age': 30}
    # 참고 URL - https://wikidocs.net/126088 
    return json.loads(response.data.decode('utf-8'))

# 사진 전송
# 텔레그램 채팅방에 ChatGPT - DALL.E 2가 생성한 이미지 보내기
# 아래 sendPhoto 함수 호출시
# ChatGPT - DALL.E 2가 그려주고 최종 생성된 이미지 URL 주소를 
# 인자로 전달하여 텔레그램 채팅방에 이미지 보내는 것도 가능함.
def sendPhoto(chat_id, image_url,msg_id):
    # 변수 data에 채팅방에 전송할 이미지 URL 주소가 담긴
    # JSON 포맷 데이터 저장 
    # 'chat_id' - 이미지 전송할 채팅방 아이디 
    # 'text' - 채팅방으로 전송할 이미지 URL 주소
    # 'reply_to_message_id' - 사용자가 보낸 메세지 아이디
    data = {
        'chat_id': chat_id,
        'photo': image_url,
        'reply_to_message_id': msg_id
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

# OpenAI API 사용해서 사용자가 ChatGPT에게 질문하고
# ChatGPT로 부터 답변받기
# 텔레그램 채팅방 안에서 사용자가 텔레그램 챗봇(ChatGPT)에게 질문을 하면
# 질문의 내용이 변수 messages로 input돼서 해당 함수 getTextFromGPT 실행
def getTextFromGPT(messages):   # ChatGPT한테 질문을 하게 될 프롬프트(messages)를 함수 getTextFromGPT에 input으로 받기 
    # 텔레그램 챗봇(ChatGPT)에게 질문을 할때는 
    # 아래와 같은 시스템 프롬프트(System Prompt - [{"role": "system", "content": 'You are a thoughtful assistant. Respond to all input in 25 words and answer in korea'}])와 함께 질문
    # 시스템 프롬프트의 내용("content": 'You are a thoughtful assistant. Respond to all input in 25 words and answer in korea')이 
    # 의미하는 뜻은 "넌 훌륭한 도우미고 답변은 25자 내외로 한국어로 해줘." 이다.
    # 이렇듯 텔레그램 챗봇(ChatGPT)의 답변의 뉘앙스(응답 스타일)를 변경하고 싶은 경우 
    # 시스템 프롬프트의 내용("content": 'You are a thoughtful assistant. Respond to all input in 25 words and answer in korea')을
    # 개발자의 요구사항에 맞게 변경하면 된다.
    # ChatGPT API에서 요구하는 프롬프트(messages) input 양식으로 변경 및 변경한 input 양식을 변수 messages_prompt에 저장 
    # messages_prompt = [{"role": "system", "content": 'You are a thoughtful assistant. Respond to all input in 25 words and answer in korea'}]
    messages_prompt = [{"role": "system", "content": 'You are a thoughtful assistant. Respond to all input in 100 words and answer in korea'}]
    messages_prompt += [{"role": "user", "content": messages}]  

    # openai.ChatCompletion.create 함수 파라미터 "messages"에 messages_prompt 저장 
    # 함수 openai.ChatCompletion.create 호출 결과 최종적으로 ChatGPT API를 통해서 받은 응답을
    # response라는 변수에 저장 
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages_prompt)
    # response에서 ChatGPT의 응답 메시지 부분만 발췌를 해서(response["choices"][0]["message"])
    # 변수 system_message에 저장
    system_message = response["choices"][0]["message"]
    return system_message["content"]   # ChatGPT의 응답 메시지에 속한 답변 내용 부분(system_message["content"])만 발췌 및 리턴

# OpenAI API 사용해서 사용자가 DALLE.2에게 그림 생성을 요청하고
# 생성된 그림의 URL 주소 받기
# 텔레그램 채팅방 안에서 사용자가 텔레그램 챗봇(ChatGPT)에게 그림 생성을 요청하면
# 요청한 내용이 변수 messages로 input돼서 해당 함수 getImageURLFromDALLE 실행
# DALLE.2 주의사항 
# 1. 특정 유명인 (예) 도널드 트럼프, 바이든 등등… 을 그림 그려달라고 요청 시 오류 발생 
#    참고 URL - https://community.openai.com/t/your-request-was-rejected-as-a-result-of-our-safety-system-your-prompt-may-contain-text-that-is-not-allowed-by-our-safety-system/285641
#    1번 오류 발생시 위의 ChatGPT로 부터 답변받기 함수 "getTextFromGPT" 몸체 안 변수 "messages_prompt"에 할당되는 시스템 프롬프트 문자열(항목 "content") 아래처럼 변경 후 컴파일 빌드 다시 실행 필요 
# (변경 전) messages_prompt = [{"role": "system", "content": 'You are a thoughtful assistant. Respond to all input in 25 words and answer in korea'}]
# (변경 후) messages_prompt = [{"role": "system", "content": 'You are a thoughtful assistant. Respond to all input in 100 words and answer in korea'}]
# 2. 영어가 아닌 한글로 그림 그려달라고 요청 시 요청사항과 전혀 다른 그림으로 그려줌.
# 3. 사용자가 그림 그려달라고 요청시 시간이 소요됨 (간단한 그림은 몇초 단위 / 복잡한 그림은 그 이상 시간 소요)
def getImageURLFromDALLE(messages):   
    # 사용자가 DALLE.2에게 그림 생성을 요청한 내용이 
    # 문자열로 저장된 변수 messages를 
    # 함수 openai.Image.create 에 전달하여 이미지 생성
    # 생성한 이미지에 대한 정보를 변수 response에 저장 
    # DALLE.2로 생성한 이미지의 사이즈(size)를 "512x512"로 설정
    response = openai.Image.create(prompt=messages,n=1,size="512x512")
    # 이미지를 다운받을 수 있는 이미지 URL 주소(response['data'][0]['url'])를
    # 변수 image_url에 저장 
    image_url = response['data'][0]['url']
    return image_url   # 이미지를 다운받을 수 있는 이미지 URL 주소 리턴 
