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
from modules import kakao # 폴더 "modules" -> 카카오 API 전용 모듈 "kakao" 불러오기 
from modules import logger # 폴더 "modules" -> 로그 설정 전용 모듈 "logger" 불러오기 

botLogger=logger.configureLogger()

# OpenAI API KEY
# 테스트용 카카오톡 챗봇 채팅방에서 
# ChatGPT와 통신하기 위해 OpenAI API 키 입력
# 아마존 웹서비스(AWS) 함수 lambda_handler -> 환경변수로 저장한 OpenAI API 키 'OPENAI_API' 불러오기
openai.api_key = os.environ['OPENAI_API']

imagineBuilderList = ['/level1', '1. 제품 설치파일 문의', '2. 네트워크 라이선스', '3. 계정&제품배정 문의', 'AutoDesk 제품 버전 문의', '레빗 버전 문의', 'AutoDesk 제품 설치 언어', '/level5'] 
infoIndex = 0   # '/level1' 인덱스 
installerIndex = 1   # '1. 제품 설치파일 문의' 인덱스
licenseIndex = 2   # '2. 네트워크 라이선스' 인덱스
accountIndex = 3   # '3. 계정&제품배정 문의' 인덱스
autoDeskVersionIndex = 4   # 'AutoDesk 제품 버전 문의' 인덱스
revitVersionIndex = 5   # '레빗 버전 문의' 인덱스
languageIndex = 6   # 'AutoDesk 제품 설치 언어' 인덱스 
answerIndex = 7   # '/level5' 인덱스 


# TODO : 파이썬 현재 실행 중인 함수 이름 가져오기 기능 구현 (2025.03.05 minjae)
# 참고 URL - https://stackoverflow.com/questions/4492559/how-to-get-current-function-into-a-variable
# 참고 2 URL - https://gist.github.com/andyxning/3a747afd02ab52483666

# ★파이썬 logging 모듈(라이브러리) 사용해서 카카오챗봇의 로그 기록 작성 및
#   아마존 웹서비스(AWS) 람다(Lambda) 함수 CloudWatch에 작성한 로그 기록 보관하기 
# TODO : event['body'] - 카카오톡 채팅방 채팅 정보가 들어있는 변수 사용 및 
#        파이썬 logging 모듈(라이브러리) 사용해서 카카오챗봇의 로그 기록 작성 기능 구현하기 (2025.02.21 minjae)
# 유튜브 참고 URL - https://youtu.be/KmTzw7Hqlw4?si=yjN4X3VUoNSJ6od2
# 참고 URL - https://blog.naver.com/sangja84/222970140189
# 참고 2 URL - https://velog.io/@goo-gy/CloudWatch%EC%97%90%EC%84%9C-Lambda-%EB%A1%9C%EA%B7%B8-%ED%99%95%EC%9D%B8%ED%95%98%EA%B8%B0
# 참고 3 URL - https://asleea88.medium.com/aws-%EB%9E%8C%EB%8B%A4-%EB%A1%9C%EA%B7%B8-%EC%9E%98-%EB%82%A8%EA%B8%B0%EA%B3%A0-%EC%B6%94%EC%A0%81%ED%95%98%EA%B8%B0-aws-lambda-logging-f097dddbbc52
# 참고 4 URL - https://jibinary.tistory.com/338
# 참고 5 URL - https://docs.python.org/ko/3/library/logging.html
# 참고 6 URL - https://wikidocs.net/84432
# 참고 7 URL - https://docs.python.org/ko/3.13/howto/logging.html

###### 메인 함수 단계 #######

# 람다(lambda)가 실행명령을 받았을 때, 실행되는 메인함수 lambda_handler
# 파이썬 또는 C/C++ 프로그래밍 언어에서 main 함수와 같은 역할을 한다.
# 또한 해당 함수는 event, context 라는 파라미터를 매개변수로 전달 받는다.
# 메인 함수
def lambda_handler(event, context):
    try:
        run_flag = False
        start_time = time.time()   # 답변/그림 응답시간 계산하기 위해 답변/그림을 시작하는 시간을 변수 start_time에 저장 

        # 카카오 정보 저장
        # json.loads 함수 호출 하여 JSON 문자열 -> Dictionary 객체 변환 처리 및
        # Dictionary 객체를 변수 kakaorequest에 저장 
        # JSON 문자열 (예) '{"name": "홍길동", "birth": "0525", "age": 30}'
        # Dictionary 객체 (예) {'name': '홍길동', 'birth': '0525', 'age': 30}
        # 참고 URL - https://wikidocs.net/126088 
        # 카카오톡 채팅방 채팅 정보가 event 파라미터를 통해서 람다(lambda) 함수 lambda_handler 로 넘어온다.
        # event['body'] - 카카오톡 채팅방 채팅 정보가 들어있는 변수이다.
        kakaorequest = json.loads(event['body'])

        filename = "/tmp/botlog.txt"
        if not os.path.exists(filename):
            with open(filename, "w") as f:
                f.write("")  
        else:
            print("File Exists")   # print 함수 호출하여 지금 현재 파일이 있다고 메시지 "File Exists" 출력 

        # 테스트 로그 기록 
        botLogger.info("[테스트] 사용자 입력 채팅 정보 - %s" %event['body'])
        # botLogger.info("[테스트2] 사용자 입력 채팅 정보 - %s" %kakaorequest)
        # botLogger.error('챗봇 로그 오류 테스트 : ')

        response_queue = q.Queue()   #.put(), .get()

        request_respond = threading.Thread(target=responseOpenAI,
                                            args=(kakaorequest, response_queue,filename))
        request_respond.start()

    except Exception as e:   # 하위 코드 블록에서 예외가 발생해도 변수 e에다 넣고 아래 코드 실행됨
        # pass
        # 테스트 오류 로그 기록  
        errorMessage = str(e)  # str() 함수 사용해서 Exception 클래스 객체 e를 문자열로 변환 및 오류 메시지 변수 errorMessage에 할당 (문자열로 변환 안할시 카카오 챗봇에서 스킬서버 오류 출력되면서 챗봇이 답변도 안하고 장시간 멈춤 상태 발생.)
        botLogger.error('[테스트] 오류 - %s' %errorMessage)
    finally:   # 예외 발생 여부와 상관없이 항상 마지막에 실행할 코드
        while(time.time() - start_time < 3.5):
            if not response_queue.empty():
                response = response_queue.get()
                run_flag= True   
                break   
            time.sleep(0.01)

        if run_flag == False:     
            response = timeover()   

        # 테스트 로그 기록
        responseMessage = json.dumps(response)
        botLogger.info("[테스트] 챗봇 답변 채팅 정보 - %s" %responseMessage)

        # 카카오톡 서버로 json 형태의 데이터(response 포함) 리턴
        return {
            'statusCode':200,
            'body': json.dumps(response),
            'headers': {
                'Access-Control-Allow-Origin': '*',
            }
        }


# 답변/사진 요청 및 응답 확인 함수
def responseOpenAI(request,response_queue,filename):
    try:
        if '생각 다 끝났나요?' in request["userRequest"]["utterance"]:
            with open(filename) as f:
                last_update = f.read()  
            if len(last_update.split())>1:
                kind = last_update.split()[0]  
                if kind == "img":
                    bot_res, prompt = last_update.split()[1],last_update.split()[2]
                    response_queue.put(imageResponseFormat(bot_res,prompt))
                else:
                    bot_res = last_update[4:]
                    print(bot_res)
                    response_queue.put(textResponseFormat(bot_res))
                dbReset(filename)   

        elif '/img' in request["userRequest"]["utterance"]:
            dbReset(filename)   
            prompt = request["userRequest"]["utterance"].replace("/img", "")
            bot_res = getImageURLFromDALLE(prompt)
            response_queue.put(imageResponseFormat(bot_res,prompt))
            save_log = "img"+ " " + str(bot_res) + " " + str(prompt)
            with open(filename, 'w') as f:
                f.write(save_log)

        elif '/ask' in request["userRequest"]["utterance"]:
            dbReset(filename)  
            prompt = request["userRequest"]["utterance"].replace("/ask", "")
            bot_res = getTextFromGPT(prompt)
            response_queue.put(textResponseFormat(bot_res))
            print(bot_res)
            save_log = "ask"+ " " + str(bot_res)

            with open(filename, 'w') as f:
                f.write(save_log)

        elif '/start' in request["userRequest"]["utterance"]:
            pass 

        elif '/error' in request["userRequest"]["utterance"]:
            dbReset(filename)   
            # response_queue.put(kakao.errorTextResponseFormat("오류 테스트"))
            save_log = "오류"+ " " + "테스트"

            with open(filename, 'w') as f:
                f.write(save_log)

            raise Exception('[오류 테스트]\n오류 사유 : 테스트 오류\n문제 해결이 어려울시 상상플렉스 커뮤니티(https://www.ssflex.co.kr/community/open)나\n기술지원번호(02-3474-2263)으로 문의 부탁드립니다.')   # 예외를 발생시킴


        elif imagineBuilderList[infoIndex] in request["userRequest"]["utterance"]:
            dbReset(filename)   
            response_queue.put(kakao.level1textCardResponseFormat())

            save_log = "level1"+ " " + "테스트"

            with open(filename, 'w') as f:
                f.write(save_log)

        elif imagineBuilderList[installerIndex] in request["userRequest"]["utterance"]:
            dbReset(filename)   
            messageTextAutoDesk = imagineBuilderList[autoDeskVersionIndex]  
            messageTextRevit = imagineBuilderList[revitVersionIndex]   
            response_queue.put(kakao.level2InstallerquickRepliesResponseFormat(messageTextAutoDesk, messageTextRevit))

            save_log = "level2"+ " " + "1. 제품 설치파일 문의"

            with open(filename, 'w') as f:
                f.write(save_log)

        elif imagineBuilderList[licenseIndex] in request["userRequest"]["utterance"]:
            dbReset(filename)   
            response_queue.put(kakao.level2NetworkquickRepliesResponseFormat())

            save_log = "level2"+ " " + "2. 네트워크 라이선스"

            with open(filename, 'w') as f:
                f.write(save_log)

        elif imagineBuilderList[accountIndex] in request["userRequest"]["utterance"]:
            dbReset(filename)  
            response_queue.put(kakao.level2AccountquickRepliesResponseFormat())

            save_log = "level2"+ " " + "3. 계정&제품배정 문의"

            with open(filename, 'w') as f:
                f.write(save_log)

        elif imagineBuilderList[autoDeskVersionIndex] in request["userRequest"]["utterance"]:
            dbReset(filename)  
            messageText = imagineBuilderList[languageIndex]  
            response_queue.put(kakao.level3VersionquickRepliesResponseFormat(messageText))

            save_log = "level3"+ " " + "AutoDesk 제품 버전 문의"

            with open(filename, 'w') as f:
                f.write(save_log)

        elif imagineBuilderList[revitVersionIndex]  in request["userRequest"]["utterance"]:
            dbReset(filename)   
            messageText = '레빗 제품 설치 방법 안내'   
            response_queue.put(kakao.level3VersionquickRepliesResponseFormat(messageText))

            # 텍스트 파일('/tmp/botlog.txt')에 임시로 저장함.
            save_log = "level3"+ " " + "레빗 버전 문의"

            with open(filename, 'w') as f:
                f.write(save_log)

        elif imagineBuilderList[languageIndex] in request["userRequest"]["utterance"]:
            dbReset(filename)   
            messageTextKor = '한국어 설치 방법'  
            messageTextEng = '영어 설치 방법'   
            response_queue.put(kakao.level4LanguagetextCardResponseFormat(messageTextKor, messageTextEng))
            
            save_log = "level4"+ " " + "AutoDesk 제품 설치 언어"

            with open(filename, 'w') as f:
                f.write(save_log)

        elif imagineBuilderList[answerIndex] in request["userRequest"]["utterance"]:
            dbReset(filename)   
            response_queue.put(kakao.level5textCardResponseFormat())

            save_log = "level5"+ " " + "테스트"

            with open(filename, 'w') as f:
                f.write(save_log)

        else:
            base_response = {'version': '2.0', 'template': {'outputs': [], 'quickReplies': []}}
            response_queue.put(base_response)

    except Exception as e:   # 하위 코드 블록에서 예외가 발생해도 변수 e에다 넣고 아래 코드 실행됨
        # 테스트 오류 로그 기록  
        errorMessage = str(e)  # str() 함수 사용해서 Exception 클래스 객체 e를 문자열로 변환 및 오류 메시지 변수 errorMessage에 할당 (문자열로 변환 안할시 카카오 챗봇에서 스킬서버 오류 출력되면서 챗봇이 답변도 안하고 장시간 멈춤 상태 발생.)
        botLogger.error('[테스트] 오류 - %s' %errorMessage)
        response_queue.put(kakao.errorTextResponseFormat(errorMessage))
        # 오류 로그 기록 
        raise    # raise로 함수 responseOpenAI의 현재 예외를 다시 발생시켜서 함수 responseOpenAI 호출한 상위 코드 블록으로 넘김


# 메세지 전송 (카카오톡 서버로 텍스트 전송)
def textResponseFormat(bot_response):
    response = {'version': '2.0', 'template': {
    'outputs': [{"simpleText": {"text": bot_response}}], 'quickReplies': []}}
    return response   

# 그림 전송 (카카오톡 서버로 그림 전송)
def imageResponseFormat(bot_response,prompt):
    output_text = prompt+"내용에 관한 이미지 입니다"
    response = {'version': '2.0', 'template': {
    'outputs': [{"simpleImage": {"imageUrl": bot_response,"altText":output_text}}], 'quickReplies': []}}
    return response  

def timeover():
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
    return response   

def getTextFromGPT(prompt):  
    messages_prompt = [{"role": "system", "content": 'You are a thoughtful assistant. Respond to all input in 300 words and answer in korea'}]
    messages_prompt += [{"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages_prompt)

    message = response["choices"][0]["message"]["content"]
    return message   

def getImageURLFromDALLE(prompt):
    response = openai.Image.create(prompt=prompt,n=1,size="512x512")
    image_url = response['data'][0]['url']
    return image_url  

def dbReset(filename):
    with open(filename, 'w') as f:
        f.write("")