# 카카오톡 챗봇 채널 웹사이트
# 참고 URL - https://pf.kakao.com/_sNBsn

# 가상환경 폴더 "ch15_env" 생성 터미널 명령어
# python -m venv ch15_env

# 가상환경 폴더 "ch15_env" 활성화 터미널 명령어
# ch15_env\Scripts\activate.bat

# 아마존 웹서비스(AWS)
# 클라우드 워치(CloudWatch) 서비스란?

# 아마존 웹서비스(AWS) 람다 함수 "lambda_handler"가
# 호출되는 모든 로그를 저장하고 관리하는 기능이다.

# 해당 로그를 통해 실제 코드가 작동되고 있는지 확인할 수 있고 에러도 확인하고 디버깅 또한 할 수 있다.

# 아마존 웹서비스(AWS)
# 클라우드 워치(CloudWatch) 서비스 사용 방법

# 1. 아마존 웹서비스(AWS) 람다(Lanbda) 화면 들어와서
# -> 함수 "inflearn_kakao" 들어오기
# -> 화면 하단 탭 "모니터링" 버튼 클릭

# 2. "Monitor" 화면 이동 -> 해당 화면에서 마우스 스크롤 아래로 이동 -> 항목 "CloudWatch Logs" 아래에 보면
# 아마존 웹서비스(AWS) 람다 함수 "lambda_handler"가
# 호출됐던 모든 로그가 시간 순으로 정리되어 출력된다.

# 카카오톡 채팅방에서 사용자가 질문(또는 그림 생성 요청) 입력될 때마다
# 카카오톡 서버 -> 아마존 웹서비스(AWS) API Gateway 주소로 
# 사용자가 질문(또는 그림 생성 요청)이 전달될 수 있도록 
# 카카오톡 채널관리자에서 해당 카카오챗봇 채널의 URL 주소 변경 및 배포한다.

# 2. 카카오톡 채팅방에서 사용자가 질문(또는 그림 생성 요청) 입력될 때마다
#    카카오톡 서버 -> 아마존 웹서비스(AWS) API Gateway 주소 연결 완료되면 
#    기존에 ngrok 사용하여 기존에 등록한 카카오챗봇 채널의 URL 주소 등록 처리가 해제된다.
#    즉, 동시에 두 개의 URL 주소를 연결 안 해준다.


# 람다(lambda) 함수 소스파일 "lambda_function.py" 열고 -> 화면 좌측 버튼 "Test" 클릭 
# -> 컴파일 실행시 아래 "OUTPUT - Execution Results" 탭 화면 출력되고
# 아래 응답값(Response) -> 오류 메시지("errorMessage") "Unable to import module 'lambda_function': No module named 'openai'"가 출력되는
# 이유는 안타깝게도 아마존 웹서비스(AWS) 람다(lambda) 에서는 pip 명령어 사용해서 손쉽게 OpenAI 패키지 "openai"를 설치할 수 있는 도구가 없어서 발생한 오류이다.
# 대신에 패키지 코드를 파일 형식으로 직접 업로드해서 패키지를 사용할 수는 있다.
# 하여 OpenAI 패키지 코드를 다운 받아서 압축을 해서 람다(lambda) 함수 안에 업데이트 해야한다.
# 알집 압축 파일(python.zip)안에 해당 OpenAI 패키지 코드가 저장되어 있고,
# 해당 압축 파일은 파일 경로("D:\bhjeon\test_chatGPT\ch15" 폴더 -> "python.zip")에 존재한다.
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
#    -> "열기" 팝업 화면 출력 -> 파일 경로("D:\bhjeon\test_chatGPT\ch15" 폴더 -> "python.zip") 이동 -> .zip 파일(python.zip) 클릭 -> 버튼 "열기(O)" 클릭 
# 4. 항목 "호환 아키텍쳐 - 선택 사항"에 "x86_64" 체크 -> 항목 "호환 런타임 - 선택 사항"에 값 "Python 3.11" 체크 -> 버튼 "생성" 클릭
# 5. 계층 생성 완료 -> 다시 아마존 웹서비스(AWS) 람다(Lambda) 함수 "inflearn_kakao" 들어와서 항목 "함수 개요" 안에 속한 버튼 "Layers" 클릭
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
# -> 화면 좌측 버튼 "Deploy (Ctrl+Shift+U)" 클릭 -> 화면 상단 메시지 "함수 inflearn_kakao이(가) 업데이트되었습니다." 출력
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
# 실제 카카오톡 채팅방으로 부터 넘어오는 채팅의 정보가 
# 아래 JSON 데이터 양식의 "evnet" 파라미터를 통해 받을 수 있다.       
# event : {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
# context : LambdaContext([aws_request_id=a15e368c-ebb2-430f-b32f-43db66d78c74,log_group_name=/aws/lambda/inflearn_kakao,log_stream_name=2025/02/06/[$LATEST]a8b0d48d3249452390205752bbba2a82,function_name=inflearn_kakao,memory_limit_in_mb=128,function_version=$LATEST,invoked_function_arn=arn:aws:lambda:ap-northeast-2:980921720325:function:inflearn_kakao,client_context=None,identity=CognitoIdentity([cognito_identity_id=None,cognito_identity_pool_id=None])])
# END RequestId: a15e368c-ebb2-430f-b32f-43db66d78c74
# REPORT RequestId: a15e368c-ebb2-430f-b32f-43db66d78c74	Duration: 1.27 ms	Billed Duration: 2 ms	Memory Size: 128 MB	Max Memory Used: 33 MB	Init Duration: 72.23 ms

# Request ID: a15e368c-ebb2-430f-b32f-43db66d78c74


# 참고 사항
# 구현하고자 하는 카카오톡 챗봇 서비스 프로그램으로 부터
# 정보가 넘어오는 json 데이터 양식이 있다면 
# 해당 팝업화면 항목 "Event JSON" 부분에 아래처럼 작성하면 
# 따로 카카오톡 서버와 연결하지 않고도 람다(lambda) 함수 환경 안에서도
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

    
###### 기본 정보 설정 단계 #######
# 참고사항
# 아마존 웹서비스(AWS) 활용할 때에는 FastAPI 개발자 로컬 웹서버를 따로 생성할 필요가 없으니까
# 패키지 "from fastapi import Request, FastAPI"를 불러올 필요가 없다.

import json     # 카카오톡 서버로부터 받은 json 데이터 처리하기 위해 패키지 json 불러오기 
import openai   # OPENAI 패키지 openai 불러오기 (ChatGPT, DALLE.2 사용)
import threading  # 프로그램 안에서 동시에 작업하는 멀티스레드 구현하기 위해 패키지 "threading" 불러오기
import time   # ChatGPT 답변 시간 계산하기 위해 패키지 "time" 불러오기
import queue as q   # 자료구조 queue(deque 기반) 이용하기 위해 패키지 "queue" 불러오기
import os   # 답변 결과를 테스트 파일로 저장할 때 경로 생성해야 해서 패키지 "os" 불러오기

# OpenAI API KEY
# 테스트용 카카오톡 챗봇 채팅방에서 
# ChatGPT와 통신하기 위해 OpenAI API 키 입력
# 아마존 웹서비스(AWS) 함수 lambda_handler -> 환경변수로 저장한 OpenAI API 키 'OPENAI_API' 불러오기
openai.api_key = os.environ['OPENAI_API']

###### 메인 함수 단계 #######

# 람다(lambda)가 실행명령을 받았을 때, 실행되는 메인함수 lambda_handler
# 파이썬 또는 C/C++ 프로그래밍 언어에서 main 함수와 같은 역할을 한다.
# 또한 해당 함수는 event, context 라는 파라미터를 매개변수로 전달 받는다.
# 메인 함수
def lambda_handler(event, context):

    # 답변/그림 응답 제한시간 3.5초내에 답변/그림이 완성이 됐는지 여부를 저장하기 위한 변수 run_flag 선언 및 초기화
    # 변수 run_flag 값이 True면 "답변/그림이 응답 제한시간 3.5초내에 완성" 의미
    # 변수 run_flag 값이 False면  "답변/그림이 응답 제한시간 3.5초 초과 및 미완성" 의미
    run_flag = False
    start_time = time.time()   # 답변/그림 응답시간 계산하기 위해 답변/그림을 시작하는 시간을 변수 start_time에 저장 

    # 카카오 정보 저장
    # json.loads 함수 호출 하여 JSON 문자열 -> Dictionary 객체 변환 처리 및
    # Dictionary 객체를 변수 result에 저장 
    # JSON 문자열 (예) '{"name": "홍길동", "birth": "0525", "age": 30}'
    # Dictionary 객체 (예) {'name': '홍길동', 'birth': '0525', 'age': 30}
    # 참고 URL - https://wikidocs.net/126088 
    # 카카오톡 채팅방 채팅 정보가 event 파라미터를 통해서 람다(lambda) 함수 lambda_handler 로 넘어온다.
    # event['body'] - 카카오톡 채팅방 채팅 정보가 들어있는 변수이다.
    kakaorequest = json.loads(event['body'])
    
    # 응답 결과를 저장하기 위한 텍스트 파일(/tmp/botlog.txt) 생성
    # 아마존 웹서비스(AWS) 람다(Lambda)에서는 람다(Lambda) 서버에서
    # 임시로 파일을 저장할 수 있다.
    # 단, 주의할 점은 람다(Lambda) 서버에서 임시로 텍스트 파일(/tmp/botlog.txt)을 저장할 때는
    # 폴더 "tmp"안에 자동으로 저장이 된다.
    # 하여 반드시 임시로 저장할 텍스트 파일(/tmp/botlog.txt)의 경로를 
    # 아래처럼 "/tmp/botlog.txt" 지정해야 한다.
    filename = "/tmp/botlog.txt"
    # 만약에 해당 텍스트 파일 (/tmp/botlog.txt)이 없다면  
    if not os.path.exists(filename):
        # open 함수 사용하여 해당 텍스트 파일 (/tmp/botlog.txt) 쓰기모드("w")로 생성 
        with open(filename, "w") as f:
            f.write("")   # 처음에는 아무 것도 없는 값으로 해당 텍스트 파일(/tmp/botlog.txt) 초기화 
    # 만약에 해당 텍스트 파일 (/tmp/botlog.txt)이 있다면 
    else:
        print("File Exists")   # print 함수 호출하여 지금 현재 파일이 있다고 메시지 "File Exists" 출력 

    # 답변 생성 함수 실행
    # ChatGPT 답변과 DALLE.2가 그려준 그림의 URL 주소를 
    # 변수 response_queue에 저장하고 해당 변수에 저장된 값을
    # 카카오톡 채팅방에 답변으로 전송할 때마다 .get() 메서드를 활용해서 
    # 자료(데이터)를 꺼내서 사용한다.
    # 큐 자료구조 클래스 q.Queue를 객체 response_queue 생성 및 초기화
    # 여기서 자료구조 큐는 리스트와 비슷하게 여러 자료(데이터)를 쌓을 수 있는 자료 구조 형태이다.
    # 자료구조 큐에서 알아야 할 메서드는 2가지가 있다.
    # .put() 메서드 - 큐에 자료(데이터)를 차곡차곡 저장하는 기능
    # .get() 메서드 - 큐에 가장 먼저 저장된 자료부터 하나씩 꺼낼 수 있는 기능
    #                .get() 메서드 사용해서 저장된 자료(데이터)를 꺼내면 해당 자료(데이터)는 큐에서 자동으로 삭제 처리 
    response_queue = q.Queue()   #.put(), .get()
    # 패키지 "threading"을 활용해서 
    # 멀티스레드 작업스레드 객체 request_respond 생성 및 함수 responseOpenAI를 실행한다.
    # 패키지 "threading"을 이용해 request_respond.start() 함수 호출
    # -> 함수 responseOpenAI를 실행하면
    # 해당 함수 responseOpenAI가 끝날 때 까지 기다리지 않고
    # 바로 아래 답변 생성 시간 체크 소스코드 (while (time.time() - start_time < 3.5):)가 실행된다.
    request_respond = threading.Thread(target=responseOpenAI,
                                        args=(kakaorequest, response_queue,filename))
    request_respond.start()

    # 답변 생성 시간 체크
    # 패키지 "threading"을 이용해서 
    # 위에서는 함수 responseOpenAI를 실행하여
    # ChatGPT 답변과 DALLE.2가 그려준 그림을 요청하는 동시에
    # 밑에서는 답변이 오는 시간을 측정할 수 있다.
    # 시작시간(start_time)으로 부터 응답 제한시간 3.5초가 지날 때까지 while문 반복
    # 응답 제한시간(3.5초) = 현재시간(time.time()) - 시작시간(start_time) 
    while (time.time() - start_time < 3.5):
        # 시작시간(start_time)으로 부터 응답 제한시간 3.5초가 지날 때까지
        # 0.1초에 한번씩 큐 자료구조 response_queue에 답변/그림이 담겨 있는지 확인
        # 만약 시작시간(start_time)으로 부터 
        # 응답 제한시간 3.5초내로 답변/그림이 생성된 경우(조건문 if not response_queue.empty(): 만족한 경우(True))
        if not response_queue.empty():
            # 3.5초 안에 답변이 완성되면 바로 값 리턴
            # 시작시간(start_time)으로 부터 응답 제한시간 3.5초 안에 답변/그림이 완성(생성)되면 바로 값 리턴
            # 자료구조 response_queue에 저장된 답변/그림을 꺼내서 변수 response에 저장  
            response = response_queue.get()
            run_flag= True   # 변수 run_flag 값 True 할당 "답변/그림이 응답 제한시간 3.5초내에 완성" 의미
            break   # while 반복문 종료 
        # 안정적인 구동을 위한 딜레이 타임 설정
        # 아래처럼 time.sleep(0.01) 호출하여 0.01초씩 딜레이 타임을 주지 않으면
        # 너무 빨리 돌아서 카카오 챗봇 프로그램이 가끔 종료되는 현상이 발생한다.
        # 하여 카카오 챗봇 프로그램의 안정적인 구동을 위해서
        # time.sleep(0.01) 함수를 호출한다.
        time.sleep(0.01)

    # 3.5초 내 답변이 생성되지 않을 경우
    # (위의 while문의 조건문 if not response_queue.empty(): 만족하지 않은 경우)
    # (조건문 if run_flag== False: 만족한 경우)
    # 시작시간(start_time)으로 부터 응답 제한시간 3.5초 안에 답변이 완성(생성)되지 않은 경우
    if run_flag== False:     
        response = timeover()   # 함수 timeover 호출 및 시간 지연 안내메시지 및 버튼 생성하는 json 포맷 데이터 리턴을 해줘서 최종적으로 변수 response에 저장 

    # 카카오톡 서버로 json 형태의 데이터(response 포함) 리턴
    return{
        'statusCode':200,
        'body': json.dumps(response),
        'headers': {
            'Access-Control-Allow-Origin': '*',
        }
    }

# 답변/사진 요청 및 응답 확인 함수
# 메인함수 mainChat에서 패키지 "threading"을 통해서 사용하고 있는
# 멀티스레드(작업스레드) 함수 responseOpenAI
# 사용자의 채팅을 분석해서 
# ChatGPT에게 답변을 받거나 DALLE.2에게 그림을 받는 기능을 수행한다.
def responseOpenAI(request,response_queue,filename):
    # 사용자가 버튼을 클릭하여 답변 완성 여부를 다시 봤을 시
    # 사용자가 기다리다가 버튼('생각 다 끝났나요?')을 클릭하면 카카오톡 채팅방에 
    # 마치 사용자가 입력한 것처럼 '생각 다 끝났나요?' 라는 메세지가 출력된다.
    # 해당 메시지 '생각 다 끝났나요?'는 함수 timeover 몸체 안에서 json 형태(Format)
    # 항목 "quickReplies" -> 항목 "messageText"에 "생각 다 끝났나요?"로 작성 했다.
    # request["userRequest"]["utterance"] 의미?
    # 사용자가 카카오톡 채팅방에 사용자의 채팅이 입력됐을 때
    # 카카오톡 서버에서 카카오 챗봇으로 보내주는
    # json 형태(Format)을 보면 이해할 수 있다.
    # json 형태(Format) 항목 "userRequest" -> 항목 "utterance" 안에 
    # 사용자의 채팅 내용이 포함되어 있다.
    # 하여 사용자의 채팅 내용이(request["userRequest"]["utterance"])이 '생각 다 끝났나요?'인 경우 
    # 즉 사용자가 버튼('생각 다 끝났나요?')을 클릭한 경우  
    if '생각 다 끝났나요?' in request["userRequest"]["utterance"]:
        # 텍스트 파일('/tmp/botlog.txt') 열기
        # open 함수 호출하여 응답 제한시간(3.5초) 초과한 시점에 저장된 
        # ChatGPT 답변 또는 DALLE.2에서 받은 그림의 URL 주소를 
        # 임시로 저장한 텍스트 파일을 불러와서 (f)
        # 텍스트 파일('/tmp/botlog.txt')에 저장된 내용을 꺼내서 .put 메서드 활용해서 큐 자료구조 response_queue에 저장  
        with open(filename) as f:
            last_update = f.read()   # 해당 텍스트 파일(f)에 저장된 ChatGPT 답변 또는 DALLE.2에서 받은 그림의 URL 주소 읽어오기
        # 텍스트 파일 내 저장된 정보가 있을 경우
        if len(last_update.split())>1:
            kind = last_update.split()[0]  
            # 해당 텍스트 파일('/tmp/botlog.txt')에 저장돤 정보(데이터)가 DALLE.2가 생성한 이미지 URL 정보(데이터)인 경우 
            if kind == "img":
                # 변수 prompt는 DALLE.2한테 그림을 그려달라고 요청하는 프롬프트(prompt) 문자열이 저장된 변수이다.
                # 변수 bot_res는 DALLE.2가 생성한 그림 URL 주소 문자열이 저장된 변수이다.
                bot_res, prompt = last_update.split()[1],last_update.split()[2]
                # 함수 imageResponseFormat에 해당 변수 bot_res, prompt에 저장된 값을 인자로 전달하고
                # 해당 함수 imageResponseFormat 실행 결과 리턴된 값을 put 메서드 활용해서 큐 자료구조 response_queue에 저장 
                response_queue.put(imageResponseFormat(bot_res,prompt))
            # 해당 텍스트 파일('/tmp/botlog.txt')에 저장된 정보(데이터)가 ChatGPT 답변인 경우 
            else:
                # 변수 bot_res는 ChatGPT 답변 문자열이 저장된 변수이다.
                bot_res = last_update[4:]
                print(bot_res)
                # 함수 textResponseFormat에 해당 변수 bot_res에 저장된 값을 인자로 전달하고 
                # 해당 함수 textResponseFormat 실행 결과 리턴된 값을 put 메서드 활용해서 큐 자료구조 response_queue에 저장 
                response_queue.put(textResponseFormat(bot_res))
            dbReset(filename)   # 함수 dbReset 실행하여 텍스트 파일('/tmp/botlog.txt')에 저장된 ChatGPT 답변 또는 DALLE.2에서 받은 그림의 URL 주소 초기화 

    # 이미지 생성을 요청한 경우
    # 만약 그림 생성을 요청하면
    # 만약 카카오톡 채팅방에 사용자가 입력한 메시지 안에
    # '/img'란 문자열이 포함되어 있으면,  
    # 즉, DALLE.2에게 그림 생성을 요청한 경우 
    elif '/img' in request["userRequest"]["utterance"]:
        dbReset(filename)   # 함수 dbReset 실행하여 텍스트 파일('/tmp/botlog.txt')에 저장된 ChatGPT 답변 또는 DALLE.2에서 받은 그림의 URL 주소 초기화
        # replace 메서드 호출하여 텍스트 메시지 안에 "/img" 란 단어를 
        # 공백("")으로 변경한 나머지 사용자의 질문 내용 프롬프트 문자열을 추출해서 변수 prompt에 저장 
        prompt = request["userRequest"]["utterance"].replace("/img", "")
        # 함수 getImageURLFromDALLE 호출하여 DALLE.2에게 그림 생성 요청을 해서
        # 최종적으로 DALLE.2가 생성한 그림의 URL주소를 변수 bot_res에 저장 
        bot_res = getImageURLFromDALLE(prompt)
        # 함수 imageResponseFormat에 변수 bot_res,prompt를 인자로 전달하여 
        # DALLE.2가 생성한 그림 URL 주소값이 포함되어 카카오톡 서버로 전송할 그림 생성 전용 json 형태(Format)를 작성 및 리턴 
        # put 메서드 호출하여 최종적으로 큐 자료구조 response_queue에 저장함.
        response_queue.put(imageResponseFormat(bot_res,prompt))
        # DALLE.2가 생성한 그림 URL 주소 정보를 텍스트 파일('/tmp/botlog.txt') 변수 save_log에 저장함 
        # 변수 save_log에 저장하는 이유는 그림을 그리는게 응답 제한시간 3.5초 내로 완료가 안 됐으면
        # 우선은 DALLE.2가 생성한 그림 URL 주소를 텍스트 파일('/tmp/botlog.txt')에 임시로 저장을 해놓기 위해서 
        # 변수 save_log 선언 및 DALLE.2가 생성한 그림 URL 주소 할당 후 
        # 텍스트 파일('/tmp/botlog.txt')에 임시로 저장함.
        save_log = "img"+ " " + str(bot_res) + " " + str(prompt)
        with open(filename, 'w') as f:
            f.write(save_log)

    # ChatGPT 답변을 요청한 경우
    # 만약 chatGPT의 답변을 요청하면
    # 만약 카카오톡 채팅방에 사용자가 입력한 메시지 안에
    # '/ask'란 문자열이 포함되어 있으면,  
    # 즉, ChatGPT에게 답변을 요청한 경우 
    elif '/ask' in request["userRequest"]["utterance"]:
        dbReset(filename)   # 함수 dbReset 실행하여 텍스트 파일('/tmp/botlog.txt')에 저장된 ChatGPT 답변 또는 DALLE.2에서 받은 그림의 URL 주소 초기화

        # replace 메서드 호출하여 텍스트 메시지 안에 "/ask" 란 단어를 
        # 공백("")으로 변경한 나머지 사용자의 질문 내용 프롬프트 문자열을 추출해서 변수 prompt에 저장 
        prompt = request["userRequest"]["utterance"].replace("/ask", "")
        # 함수 getTextFromGPT 호출하여 ChatGPT에게 질문 요청을 해서
        # 최종적으로 ChatGPT의 답변을 변수 bot_res에 저장 
        bot_res = getTextFromGPT(prompt)
        # 함수 imageResponseFormat에 변수 bot_res를 인자로 전달하여 
        # ChatGPT의 답변이 포함되어 카카오톡 서버로 전송할 ChatGPT의 답변 전용 json 형태(Format)를 작성 및 리턴 
        # put 메서드 호출하여 최종적으로 큐 자료구조 response_queue에 저장함.
        response_queue.put(textResponseFormat(bot_res))
        print(bot_res)
        # ChatGPT의 답변 정보를 텍스트 파일('/tmp/botlog.txt') 변수 save_log에 저장함 
        # 변수 save_log에 저장하는 이유는 ChatGPT의 답변을 얻는데 응답 제한시간 3.5초 내로 완료가 안 됐으면
        # 우선은 ChatGPT의 답변을 텍스트 파일('/tmp/botlog.txt')에 임시로 저장을 해놓기 위해서 
        # 변수 save_log 선언 및 ChatGPT의 답변 내용 할당 후 
        # 텍스트 파일('/tmp/botlog.txt')에 임시로 저장함.
        save_log = "ask"+ " " + str(bot_res)

        with open(filename, 'w') as f:
            f.write(save_log)

    # TODO : 추후 필요시 시작 웹페이지(start.html) 구현 예정 (2025.02.18 minjae)
    # 시작페이지(start.html) 출력 요청한 경우
    # 만약 시작페이지(start.html) 웹페이지 출력을 요청하면
    # 만약 카카오톡 채팅방에 사용자가 입력한 메시지 안에
    # '/start'란 문자열이 포함되어 있으면,  
    # 즉, 시작페이지(start.html) 웹페이지 출력을 요청한 경우 
    elif '/start' in request["userRequest"]["utterance"]:
        # response_queue.put(textCardResponseFormat())
        # TODO : 파이썬 문법 pass 사용하여 해당 elif 조건문 로직이 실행되지 않고 무시 되도록 구현 (2025.02.20 minjae)
        # 참고 URL - https://docs.python.org/ko/3.13/tutorial/controlflow.html
        pass 

    # level1 텍스트 카드
    elif '/level1' in request["userRequest"]["utterance"]:
        dbReset(filename)   # 함수 dbReset 실행하여 텍스트 파일('/tmp/botlog.txt')에 save_log = "level1"+ " " + "테스트" 초기화
        response_queue.put(level1textCardResponseFormat())

        # 텍스트 파일('/tmp/botlog.txt')에 임시로 저장함.
        save_log = "level1"+ " " + "테스트"

        with open(filename, 'w') as f:
            f.write(save_log)

    # level2 바로가기 그룹
    elif '/level2' in request["userRequest"]["utterance"]:
        dbReset(filename)   # 함수 dbReset 실행하여 텍스트 파일('/tmp/botlog.txt')에 save_log = "level2"+ " " + "테스트" 초기화
        response_queue.put(level2quickRepliesResponseFormat())

        # 텍스트 파일('/tmp/botlog.txt')에 임시로 저장함.
        save_log = "level2"+ " " + "테스트"

        with open(filename, 'w') as f:
            f.write(save_log)

    # level3 텍스트 카드
    elif '/level3' in request["userRequest"]["utterance"]:
        dbReset(filename)   # 함수 dbReset 실행하여 텍스트 파일('/tmp/botlog.txt')에 save_log = "level3"+ " " + "테스트" 초기화
        response_queue.put(level3textCardResponseFormat())

        # 텍스트 파일('/tmp/botlog.txt')에 임시로 저장함.
        save_log = "level3"+ " " + "테스트"

        with open(filename, 'w') as f:
            f.write(save_log)

    # level4 텍스트 카드
    elif '/level4' in request["userRequest"]["utterance"]:
        dbReset(filename)   # 함수 dbReset 실행하여 텍스트 파일('/tmp/botlog.txt')에 save_log = "level4"+ " " + "테스트" 초기화
        response_queue.put(level4textCardResponseFormat())

        # 텍스트 파일('/tmp/botlog.txt')에 임시로 저장함.
        save_log = "level4"+ " " + "테스트"

        with open(filename, 'w') as f:
            f.write(save_log)

    # level5 텍스트 카드 + 텍스트
    elif '/level5' in request["userRequest"]["utterance"]:
        dbReset(filename)   # 함수 dbReset 실행하여 텍스트 파일('/tmp/botlog.txt')에 save_log = "level5"+ " " + "테스트" 초기화
        response_queue.put(level5textCardResponseFormat())

        # 텍스트 파일('/tmp/botlog.txt')에 임시로 저장함.
        save_log = "level5"+ " " + "테스트"

        with open(filename, 'w') as f:
            f.write(save_log)

            
    # 아무 답변 요청이 없는 채팅일 경우
    # 카카오톡 채팅방의 사용자의 입력이 버튼('생각 다 끝났나요?')을 클릭한 경우도 아니고
    # DALLE.2에게 그림 생성 요청한 것도 아니고
    # ChatGPT의 답변을 요청한 것도 아닌 경우 
    else:
        # 기본 response 값
        # 아래처럼 그냥 내용 자체가 없는 깡통 json 형태(Format)의 정보(데이터)를 변수 base_response 에 저장
        base_response = {'version': '2.0', 'template': {'outputs': [], 'quickReplies': []}}
        # json 형태(Format)의 정보(데이터)가 저장된 변수 base_response 를 
        # put 메서드 활용해서 큐 자료구조 response_queue에 저장 
        response_queue.put(base_response)

###### 기능 구현 단계 #######
# 카카오톡 챗봇 프로그램을 구동하는데 필요한 모든 기능 함수화 해서
# 아래 2가지 함수에서 사용할 수 있도록 정리 
# 메인 함수 "mainChat", 답변/그림 요청 및 응답 확인 함수 "responseOpenAI"
# 메인 함수 

# level1 텍스트 카드 (카카오톡 서버로 텍스트 전송)
def level1textCardResponseFormat():
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "textCard": {
                        "title": "[상담시간 안내]",
                        "description": "월~금요일 : 9시~18시\n주말, 공휴일 : 상담불가",
                        "buttons": [
                            {
                                "action": "message",
                                "label": "1. Autodesk 제품 설치파일 문의",
                                "messageText": "[구현 예정!] 1. Autodesk 제품 설치파일 문의"
                            },
                            {
                                "action": "message",
                                "label": "2. 상상진화 BOX 설치파일 문의",
                                "messageText": "[구현 예정!] 2. 상상진화 BOX 설치파일 문의"
                            },
                            {
                                "action": "message",
                                "label": "3. 네트워크 라이선스 오류",
                                "messageText": "[구현 예정!] 3. 네트워크 라이선스 오류"
                            },
                            {
                                "action": "message",
                                "label": "4. 오토데스크 계정 및 제품 배정 문의",
                                "messageText": "[구현 예정!] 4. 오토데스크 계정 및 제품 배정 문의"
                            }
                        ]
                    }
                }
            ],
            "quickReplies": []
        }
    }
    return response

# level2 바로가기 그룹 전송 (카카오톡 서버로 텍스트 전송)
def level2quickRepliesResponseFormat():
    response = {
        'version': '2.0', 
        'template': {
            'outputs': [
                {
                    "simpleText" : {
                        "text": "안내가 필요한 항목을 선택해주세요"
                    }
                }
            ], 
            "quickReplies": [
                {
                    "action": "message",
                    "label": "1. AUTOCAD",
                    "messageText": "[구현 예정!] 1. AUTOCAD"
                },
                {
                    "action": "message",
                    "label": "2. Revit",
                    "messageText": "[구현 예정!] 2. Revit"
                },
                {
                    "action": "message",
                    "label": "3. Navisworks",
                    "messageText": "[구현 예정!] 3. Navisworks"
                },
                {
                    "action": "message",
                    "label": "4. Civil 3D",
                    "messageText": "[구현 예정!] 4. Civil 3D"
                },
                {
                    "action": "message",
                    "label": "5. InfraWorks",
                    "messageText": "[구현 예정!] 5. InfraWorks"
                },
                {
                    "action": "message",
                    "label": "6. Advanced Steel",
                    "messageText": "[구현 예정!] 6. Advanced Steel"
                },
                {
                    "action": "message",
                    "label": "7. AutoCAD DWG True Viewer (CAD 뷰어)",
                    "messageText": "[구현 예정!] 7. AutoCAD DWG True Viewer (CAD 뷰어)"
                },
                {
                    "action": "message",
                    "label": "8. Navisworks Exporter",
                    "messageText": "[구현 예정!] 8. Navisworks Exporter"
                },
                {
                    "action": "message",
                    "label": "9. Revit Content Library (레빗 라이브러리)",
                    "messageText": "[구현 예정!] 9. Revit Content Library (레빗 라이브러리)"
                }
            ]
        }
    }
    return response

# level3 텍스트 카드 (카카오톡 서버로 텍스트 전송)
def level3textCardResponseFormat():
    response = {
        'version': '2.0', 
        'template': {
            'outputs': [
                {
                    "textCard": {
                        "title": "버전을 선택해주세요",
                        "description": "level3 테스트",
                        "buttons": [
                            {
                                "action": "message",
                                "label": "2022",
                                "messageText": "[구현 예정!] 2022버전"
                            },
                            {
                                "action": "message",
                                "label": "2023",
                                "messageText": "[구현 예정!] 2023버전"
                            },
                            {
                                "action": "message",
                                "label": "2024",
                                "messageText": "[구현 예정!] 2024버전"
                            },
                            {
                                "action": "message",
                                "label": "2025",
                                "messageText": "[구현 예정!] 2025버전"
                            }
                        ]
                    }
                }
            ], 
            'quickReplies': []
        }
    }
    return response

# level4 텍스트 카드 (카카오톡 서버로 텍스트 전송)
def level4textCardResponseFormat():
    response = {
        'version': '2.0', 
        'template': {
            'outputs': [
                {
                    "textCard": {
                        "title": "설치 언어를 선택해주세요",
                        "description": "level4 테스트",
                        "buttons": [
                            {
                                "action": "message",
                                "label": "한국어",
                                "messageText": "[구현 예정!] 한국어"
                            },
                            {
                                "action": "message",
                                "label": "English",
                                "messageText": "[구현 예정!] English"
                            }
                        ]
                    }
                }
            ], 
            'quickReplies': []
        }
    }
    return response

# level5 텍스트 카드 + 텍스트 (카카오톡 서버로 텍스트 전송)
def level5textCardResponseFormat():
    response = {
        'version': '2.0', 
        'template': {
            'outputs': [
                {
                    "textCard": {
                        "title": "아래 링크를 클릭해주세요",
                        "description": "level5 테스트",
                        "buttons": []
                    }
                },
                {   
                    "simpleText" : {
                        "text": "https://www.autodesk.com/support/download-install"
                    }
                }
            ], 
            'quickReplies': []
        }
    }
    return response


# 메세지 전송 (카카오톡 서버로 텍스트 전송)
# ChatGPT의 답변을 카카오톡 서버로 답변 전송 전용 JSON 형태(Format)의 데이터로 전달하기 위한 함수
# 카카오톡 채팅방에 보낼 메시지를 매개변수 bot_response에 input으로 받기(인자로 전달)
def textResponseFormat(bot_response):
    # 카카오톡 채팅방에 보낼 메시지가 저장된 매개변수 bot_response를
    # 아래 json 형태(Format)에서 항목 'outputs' -> 항목 "simpleText" -> "text"안에 매개변수 bot_response을 넣어서
    # 변수 responsedp 저장하기 
    response = {'version': '2.0', 'template': {
    'outputs': [{"simpleText": {"text": bot_response}}], 'quickReplies': []}}
    return response   # 카카오톡 서버로 답변 전송하기 위해 답변 전송 전용 JSON 형태(Format)의 데이터가 저장된 변수 response 리턴  

# 그림 전송 (카카오톡 서버로 그림 전송)
# DALLE.2가 생성한 그림 URL 주소를 카카오톡 서버로 이미지 전송 전용 JSON 형태(Format)의 데이터로 전달하기 위한 함수
# 카카오톡 채팅방에 보낼 DALLE.2가 생성한 그림 URL 주소를 
# 매개변수 bot_response에 input으로 받기(인자로 전달)
# DALLE.2가 그림을 생성할 때 input으로 넣은 프롬프트 문자열을 
# 매개변수 prompt에 input으로 받기(인자로 전달)
def imageResponseFormat(bot_response,prompt):
    output_text = prompt+"내용에 관한 이미지 입니다"
    # 카카오톡 채팅방에 보낼 DALLE.2가 생성한 그림 URL 주소가 저장된 매개변수 bot_response를
    # 아래 json 형태(Format)에서 항목 'outputs' -> 항목 "simpleImage" -> "imageUrl"안에 매개변수 bot_response을 넣어서
    # 변수 response에 저장하기 
    response = {'version': '2.0', 'template': {
    'outputs': [{"simpleImage": {"imageUrl": bot_response,"altText":output_text}}], 'quickReplies': []}}
    return response   # 카카오톡 서버로 DALLE.2가 생성한 그림 URL 주소 전송하기 위해  이미지 전송 전용 JSON 형태(Format)의 데이터가 저장된 변수 response 리턴 

# ChatGPT또는 DALLE.2의 답변(응답)이 3.5초 초과시 
# 지연 안내 메세지 + 버튼 생성
# 답변 시간이 지연되면 지연 안내 메시지를 보내고
# 답변을 다시 요청하기 위해서 FastAPI 비동기 웹서버에서 버튼 생성 요청하여 카카오톡 서버로 전달
# 카카오톡 서버에 버튼 생성 요청하기 위하여 버튼 생성 전용 JSON 형태(Format)의 데이터로 전달
def timeover():
    # 카카오톡 채팅방에 보낼 안내메시지는 
    # 아래 json 형태(Format)에서 항목 "outputs" -> 항목 "simpleText" -> 항목 "text" 안에 안내메시지 텍스트 "아직 제가 생각이 끝나지 않았어요🙏🙏\n잠시후 아래 말풍선을 눌러주세요👆" 저장
    # 카카오톡 채팅방에 보낼 생성할 버튼은
    # 아래 json 형태(Format)에서 항목 "quickReplies" 
    # -> 항목 "action"에 "message" 작성 
    # -> 항목 "label"에 "생각 다 끝났나요?🙋" 작성 (버튼 안에 들어가는 label)
    # -> 항목 "messageText"에 "생각 다 끝났나요?" 작성 (사용자가 이 버튼을 클릭했을 때 카카오톡 채팅방에 출력되는 입력 메시지)
    
    # 카카오톡 채팅방에 보낼 안내메시지, 생성할 버튼을 
    # 전용 json 형태(Format)의 데이터를 변수 response에 저장 
    response = {"version":"2.0","template":{
      "outputs":[
         {
            "simpleText":{
               "text":"아직 제가 생각이 끝나지 않았어요??\n잠시후 아래 말풍선을 눌러주세요?"
            }
         }
      ],
      "quickReplies":[
         {
            "action":"message",
            "label":"생각 다 끝났나요??",
            "messageText":"생각 다 끝났나요?"
         }]}}
    return response   # 카카오톡 서버로 지연 안내메시지 + 생성할 버튼 전송하기 위해 JSON 형태(Format)의 데이터가 저장된 변수 response 리턴  

# ChatGPT에게 질문/답변 받기
# OpenAI API 사용해서 사용자가 ChatGPT에게 질문하고
# ChatGPT로 부터 답변받기
# 카카오톡 채팅방 안에서 사용자가 카카오톡 챗봇(ChatGPT)에게 질문을 하면
# 질문의 내용이 변수 prompt로 input돼서 해당 함수 getTextFromGPT 실행
def getTextFromGPT(prompt):   # ChatGPT한테 질문을 하게 될 프롬프트(prompt)를 함수 getTextFromGPT에 input으로 받기
    # 카카오톡 챗봇(ChatGPT)에게 질문을 할때는 
    # 아래와 같은 시스템 프롬프트(System Prompt - [{"role": "system", "content": 'You are a thoughtful assistant. Respond to all input in 25 words and answer in korea'}])와 함께 질문
    # 시스템 프롬프트의 내용("content": 'You are a thoughtful assistant. Respond to all input in 25 words and answer in korea')이 
    # 의미하는 뜻은 "넌 훌륭한 도우미고 답변은 25자 내외로 한국어로 해줘." 이다.
    # 이렇듯 카카오톡 챗봇(ChatGPT)의 답변의 뉘앙스(응답 스타일)를 변경하고 싶은 경우 
    # 시스템 프롬프트의 내용("content": 'You are a thoughtful assistant. Respond to all input in 25 words and answer in korea')을
    # 개발자의 요구사항에 맞게 변경하면 된다.
    # ChatGPT API에서 요구하는 프롬프트(prompt) input 양식으로 변경 및 변경한 input 양식을 변수 messages_prompt에 저장 
    # messages_prompt = [{"role": "system", "content": 'You are a thoughtful assistant. Respond to all input in 25 words and answer in korea'}] 
    messages_prompt = [{"role": "system", "content": 'You are a thoughtful assistant. Respond to all input in 300 words and answer in korea'}]
    messages_prompt += [{"role": "user", "content": prompt}]

    # openai.ChatCompletion.create 함수 파라미터 "messages"에 messages_prompt 저장 
    # 함수 openai.ChatCompletion.create 호출 결과 최종적으로 ChatGPT API를 통해서 받은 응답을
    # response라는 변수에 저장 
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages_prompt)
    # response에서 ChatGPT의 응답 메시지 부분만 발췌를 해서(response["choices"][0]["message"])
    # 변수 system_message에 저장
    message = response["choices"][0]["message"]["content"]
    return message   # ChatGPT의 응답 메시지에 속한 답변 내용 부분(system_message["content"])만 발췌 및 리턴

# DALLE.2에게 질문/그림 URL 받기
# 생성된 그림의 URL 주소 받기
# 카카오톡 채팅방 안에서 사용자가 카카오톡 챗봇(ChatGPT)에게 그림 생성을 요청하면
# 요청한 내용이 변수 messages로 input돼서 해당 함수 getImageURLFromDALLE 실행
# DALLE.2 주의사항 
# 1. 특정 유명인 (예) 도널드 트럼프, 바이든 등등… 을 그림 그려달라고 요청 시 오류 발생 
#    참고 URL - https://community.openai.com/t/your-request-was-rejected-as-a-result-of-our-safety-system-your-prompt-may-contain-text-that-is-not-allowed-by-our-safety-system/285641
#    1번 오류 발생시 위의 ChatGPT로 부터 답변받기 함수 "getTextFromGPT" 몸체 안 변수 "messages_prompt"에 할당되는 시스템 프롬프트 문자열(항목 "content") 아래처럼 변경 후 컴파일 빌드 다시 실행 필요 
# (변경 전) messages_prompt = [{"role": "system", "content": 'You are a thoughtful assistant. Respond to all input in 25 words and answer in korea'}]
# (변경 후) messages_prompt = [{"role": "system", "content": 'You are a thoughtful assistant. Respond to all input in 100 words and answer in korea'}]
# 2. 영어가 아닌 한글로 그림 그려달라고 요청 시 요청사항과 전혀 다른 그림으로 그려줌.
# 3. 사용자가 그림 그려달라고 요청시 시간이 소요됨 (간단한 그림은 몇초 단위 / 복잡한 그림은 그 이상 시간 소요)
def getImageURLFromDALLE(prompt):
    # 사용자가 DALLE.2에게 그림 생성을 요청한 내용이 
    # 문자열로 저장된 변수 messages를 
    # 함수 openai.Image.create 에 전달하여 이미지 생성
    # 생성한 이미지에 대한 정보를 변수 response에 저장 
    # DALLE.2로 생성한 이미지의 사이즈(size)를 "512x512"로 설정
    response = openai.Image.create(prompt=prompt,n=1,size="512x512")
    # 이미지를 다운받을 수 있는 이미지 URL 주소(response['data'][0]['url'])를
    # 변수 image_url에 저장 
    image_url = response['data'][0]['url']
    return image_url   # 이미지를 다운받을 수 있는 이미지 URL 주소 리턴 

# 텍스트파일 초기화
# 메인 함수 "mainChat", 답변/그림 요청 및 응답 확인 함수 "responseOpenAI"
# 해당 2가지 함수에서 3.5초 이후에 생성된 답변 및 그림 URL 주소를 
# 임시로 텍스트 파일에 저장 -> 해당 텍스트 파일에 저장된 정보는
# 추후에 사용자가 버튼("생각 다 끝났나요?🙋")을 클릭해서 
# 답변 및 그림 URL 주소를 요청하면
# 해당 답변 및 그림 URL 주소를 전송한 후에는 해당 텍스트 파일은 필요가 없다.
# 이 때 해당 함수 dbReset를 호출하여 저장된 텍스트 파일를 초기화 해준다.
def dbReset(filename):
    with open(filename, 'w') as f:
        f.write("")

# 주의사항 
# 비동기(async - await) 웹서버 생성하는 유비콘 패키지 "uvicorn[standard]"를 사용하는 파이썬 파일의 경우 
# 일반 파이썬 파일을 터미널에서 실행하는 명령어(python 03_kakaobot.py)를 
# 그대로 쓰면 파일 안에 있는 FastAPI 서버(FastAPI 클래스 객체 app)가 생성 불가하다.
# 하여 비동기(async - await) 웹서버 생성하는 유비콘 패키지 "uvicorn[standard]"를 사용하는 파이썬 파일은
# 아래와 같은 명령어를 입력 해야만 해당 파일 안에 있는 FastAPI 서버(FastAPI 클래스 객체 app)가 생성된다.
# uvicorn 03_kakaobot:app --reload


# ngrok 역할?
# 외부에서 개발자 로컬 PC로 접속할 수 있는 URL 주소가 필요하다.
# ngrok는 개발자 로컬 PC에서 생성한 서버 개발 환경을
# 외부 서버에서도(전세계 어디 서버에서도) 접속할 수 있도록 공유해주는 서비스이다.
# 즉, 외부에서 개발자 로컬 PC로 접속할 수 있는 URL 주소를 발급해준다.
# 또한 서로 다른 네트워크(카카오톡 서버와 개발자 PC에서 실행시키는 FastAPI 로컬 서버)를
# 연결 해주는 통로의 역할을 하는 게이트웨이와 비슷한 역할이다.
# ngrok 웹사이트
# 참고 URL - https://ngrok.com/ 

# 게이트웨이 용어 설명
# 참고 URL - https://ko.wikipedia.org/wiki/%EA%B2%8C%EC%9D%B4%ED%8A%B8%EC%9B%A8%EC%9D%B4

# ngrok 응용 프로그램 실행 방법
# 1) 비쥬얼스튜디오코드(VSCode) 실행 
#    -> 유비콘 패키지 "uvicorn[standard]"를 사용하는 파이썬 파일 "03_kakaobot.py" 또는 "08_telegramebot.py" 열기
#    -> OpenAI API 키 값 입력 
#    -> 터미널창 열어서 명령어 "uvicorn 03_kakaobot:app --reload" 입력 및 엔터 
#    -> FastAPI 서버(FastAPI 클래스 객체 app)가 정상적으로 생성 완료

# 2) 카카오톡 응용 프로그램 실행 

# 3) PC 바탕 화면 -> ngrok 바로가기 아이콘 더블 클릭
# ngrok 바로가기 아이콘 존재하지 않으면 아래 파일경로 들어가서 ngrok 응용 프로그램 실행
# 파일 경로 - "C:\Users\bhjeon\Desktop\회사_업무_및_공부_자료\상상진화 회사 업무\AI 챗봇_개발\카카오톡_카카오_챗봇_ngrok_실행_프로그램" -> 응용 프로그램 ngrok

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
# - 파이썬 파일 "03_kakaobot.py"을 유비콘 패키지 "uvicorn[standard]"를 사용하여 FastAPI 웹서버를 생성해 놓은 상태이다.
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
#    FastAPI 웹서버 URL 주소 (예) "https://c84e-14-52-67-173.ngrok-free.app" 
#    로 외부 서버에서 접속을 하면 
#    개발자 로컬 PC에 포트(Port) 번호 "8000"로 접속이 가능("http://localhost:8000")하다는 것을 의미한다.
# 주의사항 - ngrok 응용 프로그램 터미널창에 URL 주소 "https://c84e-14-52-67-173.ngrok-free.app" 
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
# Latency                       37ms                                                                                                                                                 
# Web Interface                 http://127.0.0.1:4040                                                                                                                                
# Forwarding                    https://c84e-14-52-67-173.ngrok-free.app -> http://localhost:8000                                                                                                                                                                                                                                                                       
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
#       FastAPI 웹서버 URL 주소(https://c84e-14-52-67-173.ngrok-free.app) 뒤에 "/chat/" 붙인 
#       URL 주소(https://c84e-14-52-67-173.ngrok-free.app/chat/)를 항목 "URL"에 입력하기
#    -> "스킬명을 입력해주세요" 화면 우측 상단 "기본 스킬로 설정" 체크
#    -> 버튼 "저장" 클릭 -> 해당 화면 마우스 스크롤 아래로 내려서 항목 "스킬 테스트" 이동 
#    -> 해당 "스킬 테스트" 항목은 카카오톡 서버와 연결이 잘 됐는지 확인할 수 있는 기능 "JSON"이 있다.
#    -> 해당 "JSON" 에서 작성된 양식은 카카오톡 서버 -> 개발자 로컬 PC FastAPI 서버로 
#       채팅 정보를 줄 때 전송하는 JSON 데이터 양식과 동일하다. 
#    -> 하여 해당 "JSON" 데이터를 가지고 디버깅 하면서 스킬 테스트를 진행할 수 있다.
#       해당 "JSON" 우측 하단 버튼 "스킬서버로 전송" 클릭
#    -> "스킬서버로 전송" 기능이 잘 실행되었는지 확인하려면
#       비쥬얼 스튜디오 코드 돌아와서 FastAPI 개발자 로컬 PC 비동기 웹서버 파이썬 파일(03_kakaobot.py)
#       @app.post("/chat/") 메서드 호출 -> async def chat(request: Request): 함수 실행 
#       -> 코드 kakaorequest = await request.json() 실행 ->  
#       print(kakaorequest) 함수 호출하여 터미널창에서 아래와 같은 결과가 출력되면 
#       "스킬서버로 전송" 기능이 잘 실행되었다는 것을 확인할 수 있다.
#       하여 해당 결과를 통하여 카카오톡 챗봇(카카오톡 서버)과 
#       FastAPI 개발자 로컬 PC 비동기 웹서버 파이썬 파일(03_kakaobot.py)이
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


# 카카오톡 챗봇의 콘셉
# 카카오톡 챗봇의 기본 구조는 텔레그램 챗봇과 동일하게
# 아래처럼 4가지 구조로 나뉜다.
# 1) 기본 정보 설정 단계
# 2) 기능 함수 구현 단계
# 3) 서버 생성 단계
# 4) 메인 함수 구현 단계 
# 전체적인 구조는 텔레그램 챗봇과 동일하지만
# 4) 메인 함수 구현 단계 부분이 텔레그램 챗봇보다 훨씬 복잡하다.
# 이유는 카카오톡 서버 응답이 5초를 넘어가면 답변을 차단하기 때문이다.
# 이게 무슨 뜻인가 하면 카카오톡 채팅방에 사용자가 질문을 하면
# 해당 질문에 대한 답변을 카카오 챗봇이 해주는데
# 해당 챗봇이 5초 안에 답변을 하지 않으면 카카오톡 서버에서 답변을 차단한다.
# 카카오톡 채팅방에 채팅을 입력하고 챗봇 서버에서 OpenAI 서버로 
# ChatGPT에게 응답 또는 DALLE.2 에게 그림을 요청하고 그림 생성이 완료된 응답을
# 다시 한번 카카오톡 서버로 전송해야 하는데 5초라는 시간은 너무 짧고 가혹하다.
# ChatGPT의 응답은 어느 정도 커버가 가능하지만 
# DALLE.2의 경우는 그림 생성이 대부분 5초를 넘어가서
# 사실 5초 안에 답변 하는게 불가하다.
# 그러면 5초 안에 답변을 하지 않고 기다리고 있다가
# 답변이 다 완료된 후에 그냥 보내주면 되잖아요? 라고 생각할 순 있지만
# 카카오톡 챗봇 시스템은 텔레그램 처럼 언제 어느 시점에서나
# 카카오톡 챗봇이 사용자에게 메시지 전송을 할수 있는게 아니다
# 카카오톡 챗봇은 오직 사용자의 입력에 대한 답장만 가능하다.
# 그 답장을 5초를 넘어가면은 그 답장마저 못하고 차단된다.
# 카카오톡 채팅방 보면 카카오 플러스 채널이 굉장히 많은데
# 해당 카카오 플러스 채널들이 사용자에게 가끔씩 광고 메시지를 전송한다.
# 해당 광고 메시지는 카카오톡 채널 창에 메시지를 보내지 않았는데
# 알아서 광고 메시지를 사용자에게 보낸다.
# 이런 식으로 카카오톡 채널에서 사용자의 입력에 대한 답장이 아니라
# 임의로 채널에 있는 챗봇이 사용자에게 메시지를 보내는 것은 전부 유료 서비스이다.
# 즉, 각 회사들은 사용자한테 광고성 메시지를 보낼 때 다 돈을 내고 보내는 것이다.
# 단, 우리가 개발하는 카카오 챗봇 프로그램은 그렇게 돈을 내면서 까지 구현할 필요는 없고
# 사용자의 질문에 대한 답변 즉 무료로 사용자의 질문에 대한 답변을 5초 안에만 하면 된다.
# 하지만 5초 안에 답변을 하는 것은 불가능하기 때문에 해당 문제를 해결해야 한다.
# 해당 문제를 해결하는 방법은 아래처럼 2가지이다.
# 1. 카카오 "챗봇 관리자센터" -> "도움말" 들어가서 답변 응답시간을 늘려달라고 요청 
# (카카오 자체 심사 과정 통과하는 경우만 답변 응답시간 늘려줌)
# 2. 소스코드를 추가로 구현하여 사용자에게 일정 시간이 지난 후 다시 요청 받기
# 2번 소스코드 추가 구현 설명
# 상황 설명 
# 5초 안에 사용자에게 답변(텍스트, 그림) 받는 상황이다.
# 예를들어 사용자가 카카오 챗봇에게 그림 그려달라고 요청을 한 시점이 있다.
# 해당 시점 부터 OpenAI가 생성한 그림을 카카오 챗봇이 받는 시점이 3.5초 이내면 
# 바로 카카오 챗봇이 사용자에게 그림을 보낼 수 있다.
# 여기서 기준을 3.5초로 정한 이유는 
# 카카오 챗봇 -> 카카오톡 서버로 전송하는 시간을 대략 1.5초 정도로
# 여유롭게 확보를 하기 위해서 정한 기준이다.
# 이 경우에는 개발자가 따로 별도의 코드를 작성하지 않아도 
# 5초 안에 답변이 나가기 때문에 개발자가 별도로 코드를 작성할 필요가 없다.
# 하지만 문제는 다음과 같이 3.5초 이내로 OpenAI-DALLE.2로 부터 
# 그림을 전달받지 못하는 경우이다.
# 좀더 설명하자면 사용자가 카카오 챗봇에게 그림을 요청했고
# 그림이 생성되서 카카오톡 서버로 그림을 전송해주는 시점이 3.5초를 넘어갔다.
# 또는 그림이 생성되는 과정만 3.5초를 넘어갔다면 
# 개발자가 구현한 FastAPI 로컬 웹서버는 카카오톡 서버로 일단 먼저 "안내메세지"를 보내서 답장한다.
# 아래와 같은 "안내메시지"를 보내서 사용자에게 아래와 같은 추가 기능("버튼[생각 다 끝났나요?]")을 사용할 수 있게 해준다.
# "미안 조금만 기다려줘 지금 그림을 생성중인데 조금 시간이 걸려 내가 너무 미안하니까 대신에 "버튼[생각 다 끝났나요?]"을 하나 만들어 줄게
#  조금 시간이 지난 후에 해당 "버튼[생각 다 끝났나요?]"을 누르면 내가 생성된 그림을 보내줄 거야 라고 "안내메시지"를 보낸다."
# 다시 한번 정리 하자면 사용자가 카카오 챗봇에게 그림을 요청한 시점으로부터 
# 3.5초 내에 OpenAI-DALLE.2로 부터 그림을 받지 못하면은
# 개발자가 구현한 FastAPI 로컬 웹서버는 카카오톡 서버로 아래와 같은 "안내메세지"를 보내야 되는데
# "안내메시지"에는 "버튼[생각 다 끝났나요?]"을 하나 추가해서 보내야 한다.
# "지금 그림 생성을 못했으니까 일정 시간 지난 후에 다시 한번 이 버튼[생각 다 끝났나요?]을 누르면 우리가 완성한 그림을 보내줄거야"
# 라는 안내 메시지를 카카오톡 서버로 보낸다.
# 그렇게 "안내메시지"가 나간 후에 OpenAI-DALLE.2에서는 그림을 이미 다 그리고
# 개발자가 구현한 FastAPI 로컬 웹서버로 그려놓은 그림에 대한 정보를 넘겨준다.
# 그러면 일단 개발자가 구현한 FastAPI 로컬 웹서버에 OpenAI-DALLE.2가 그려놓은 그림을 저장하고 
# 개발자가 구현한 FastAPI 로컬 웹서버에서만 해당 그림을 가지고만 있다.
# 그리고 일정 시간 후에 개발자가 구현한 FastAPI 로컬 웹서버에서 
# 카카오톡 서버로 "안내메시지"와 같이 보내줬던 "버튼[생각 다 끝났나요?]"을 사용자가 보고
# "이제 그림 다 그렸나?" 라고 생각을 하고 "버튼[생각 다 끝났나요?]"을 클릭하면
# "버튼[생각 다 끝났나요?]"을 클릭한 메시지가 개발자가 구현한 FastAPI 로컬 웹서버로 전송되고
# 개발자가 구현한 FastAPI 로컬 웹서버는 사용자가 "버튼[생각 다 끝났나요?]"을 클릭하면
# 개발자가 구현한 FastAPI 로컬 웹서버에서 저장해놓은 
# OpenAI-DALLE.2가 그려놓은 그림을 가지고 와서 
# 사용자에게 카카오챗봇으로 그림을 전송 해주는 시스템이 되겠다.
# 여기서 굳이 버튼[생각 다 끝났나요?]을 만든 이유는 5초 지난 시점 이후에는 
# 개발자가 구현한 FastAPI 로컬 웹서버에서 카카오톡으로 그림을 보낼 수 잇는 방법이 없기 때문이다.
# 다시 한번 사용자에게 버튼[생각 다 끝났나요?]을 클릭하여 입력(이벤트)을 받기 위해서이다.
# 다시 한번 사용자에게 버튼[생각 다 끝났나요?]을 클릭하여 입력(이벤트)을 받으면
# 그 버튼[생각 다 끝났나요?]을 클릭한 입력(이벤트) 시점 부터 5초 이내로 
# 개발자가 구현한 FastAPI 로컬 웹서버에서 답장(그림이 포함된 답장)만 하면 되기 때문에
# 다시 한번 사용자에게 버튼[생각 다 끝났나요?]을 클릭하여 입력(이벤트)을 받기 위해서
# 개발자가 구현한 FastAPI 로컬 웹서버에서 "버튼[생각 다 끝났나요?]"을 생성해서 
# 카카오톡 챗봇 사용자에게 전달을 해주게 되는 것이다.
# 위에서 설명한 기능을 시연 설명을 하면 아래와 같다.
# 1) 카카오톡 채팅방에서 사용자가 "/img 따뜻한 여름 해변" 입력 및 엔터
# 2) 개발자가 구현한 FastAPI 로컬 웹서버가 카카오톡 서버로 아래 "안내메시지"와 "버튼[생각 다 끝났나요?]"을 생성해서 전송함/
# 3) 사용자는 약간의 시간 대략 3초~4초 정도 후에 "버튼[생각 다 끝났나요?]" 클릭
# 4) 개발자가 구현한 FastAPI 로컬 웹서버에서 저장해뒀던 
#    OpenAI-DALLE.2가 그려놓은 그림을 그제서야 카카오 챗봇을 통해서 사용자에게 전달하게 되는 방법이다.
# 5) 그렇게해서 사용자가 "버튼[생각 다 끝났나요?]"을 클릭하면 사용자가 메시지 "생각이 다 끝났나요?" 자동 생성 및 입력 처리
#    -> 카카오 챗봇 입장에서는 마치 "사용자가 생각이 다 끝났나요?" 라는 채팅을 입력한 것으로 인식한다.
#       이렇게 인식하면 카카오 챗봇은 OpenAI-DALLE.2가 그려놓은 그림을 그제서야 
#       사용자에게 전달하게 된다.
# 사실 애초에 카카오 챗봇이 사용자의 입력에 대한 답변 기능만 가능하고
# 사용자의 입력 없이 챗봇이 독단적으로 메시지를 보내는 것을 금지해놨기 때문에
# 위와 같이 복잡하게 구현을 해야한다.
# 이렇게라도 기능을 구현하면 사용자에게 OpenAI-DALLE.2가 그려놓은 그림을 보낼 수 있기 때문에
# 이런 방식으로 카카오 챗봇 프로그램을 구현한다.
# 그런데 이런 방법으로 코드를 구현하려면
# 카카오 챗봇은 동시에 아래 두 가지 작업을 하고 있어야 한다.
# 첫 번째, 3.5초를 카운팅 하면서 카카오 챗봇에게 우선 답장을 하는 작업
# 두 번째, 개발자가 구현한 FastAPI 로컬 웹서버가 OpenAI-DALLE.2가 그려놓은 그림을 받는 작업 
# 다만 잘 알다시피 프로그래밍 작업은 동시에 진행이 안 된다.
# 무조건 순서대로 이 작업이 끝나면 그 다음 작업, 
# 이 작업이 끝나면 그 다음 작업, 또 이 작업이 끝나야 그 다음 작업이 시작된다.
# 조금 더 전문적인 표현을 쓰자면 해당 작업 두가지를 동시에 멀티스레딩이라는 작업을 통해서 
# 일을 처리해야 한다.
# 멀티스레딩이란 동시에 코드에서 병렬적으로 2가지 이상의 여러 가지 작업을 진행하는 것을 뜻한다.
# 하여 파이썬 환경에서 멀티스레딩을 코드로 구현하기 위해 아래 소스코드를 참고 해야 한다.

# 아래와 같이 여러 작업스레드가 동시에 처리되는 것을 멀티스레딩이라고 부른다.
# 사실은 아래처럼 컴퓨터가 실제로 동시에 병렬로 여러 개 작업을 하는게 아니라
# 첫 번째 작업 "Thread1"을 조금 하고 그 다음에 두 번째 작업 "Thread2"을 조금 하고
# 그 다음에 세 번째 작업 "Thread3"을 조금 하고 
# 그리고 그 다음에 또 첫 번째 작업 "Thread1"을 조금 하고
# 그 다음에 두 번째 작업 "Thread2"을 조금 하고
# 이런 식으로 사실은 순서대로 진행을 하는데 
# 처음부터 끝까지 작업을 진행을 하고 다 함께 시작하는게 아니라
# 조금 조금씩 진행을 해서 마치 사용자가 느끼기에는 동시에
# 병렬적으로 여러 작업스레드를 처리하고 있구나라고 느낄 수 있다.
# 이것이 바로 멀티스레딩의 개념이다.

# *** 멀티스레딩 작업스레드 "Thread1", "Thread2", "Thread3" 실행 순서 ***
# 1. 첫 번째 작업 "Thread1" 시작 
# 2. 첫 번째 작업 "Thread1"이 끝나기 전에 두 번째 작업 "Thread2" 시작 
#    (두 번째 작업 "Thread2" 시작이 되면 사실상 첫 번째 작업 "Thread1"과 두 번째 작업 "Thread2"이 동시에 진행되는 상태이다.)
# 3. 두 번째 작업 "Thread2"도 끝나기 전에 세 번째 작업 "Thread3" 시작
#    (세 번째 작업 "Thread3" 시작이 되면 사실상 첫 번째 작업 "Thread1"과 두 번째 작업 "Thread2"과 세 번째 작업 "Thread3"이 동시에 진행되는 상태이다.)
# 4. 첫 번째 작업 "Thread1" 종료 
#    (두 번째 작업 "Thread2"과 세 번째 작업 "Thread3"이 동시에 진행되는 상태이다.)
# 5. 두 번째 작업 "Thread2" 종료 
#    (세 번째 작업 "Thread3"만 진행되는 상태이다.)