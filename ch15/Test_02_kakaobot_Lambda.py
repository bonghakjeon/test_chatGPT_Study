# 아마존 웹서비스(AWS) 다중인증(MFA는 Multi-Factor Authentication) 등록 방법 및 모바일 어플 Google Authenticator 설치 및 사용 방법 
# 참고 URL - https://happy-jjang-a.tistory.com/223

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
# 비쥬얼스튜디오코드(VSCode) cmd 터미널창에 
# 아래처럼 최신 버전 OpenAI 라이브러리 "openai" 설치 및 함수 "getTextFromGPTNew" 구현 및 사용하기
# pip install openai
OPENAI_KEY = os.environ['OPENAI_API'] 
# OPENAI_KEY = os.getenv("OPENAI_KEY")

# (주)상상진화 각 레벨(level)별 처리할 업무 프로세스 리스트 
imagineBuilderList = [ '/level1', '1. Autodesk 제품', '2. 상상진화 BOX 제품', '3. 계정&제품배정 문의', '1. Autodesk 제품 설치 문의', '더보기', '2. 상상진화 BOX 제품 설치 문의'  ]
level1Index = 0      # '/level1' 인덱스
autodeskIndex = 1    # '1. Autodesk 제품' 인덱스 
boxIndex = 2         # '2. 상상진화 BOX 제품' 인덱스
accountIndex = 3     # '3. 계정&제품배정 문의' 인덱스
autodeskInstIndex = 4       # '1. Autodesk 제품 설치 문의' 인덱스
autodeskSeeMoreIndex = 5    # '더보기' 인덱스
boxInstIndex = 6            # '2. 상상진화 BOX 제품 설치 문의' 인덱스

level1ButtonList = [ '1. Autodesk 제품', '2. 상상진화 BOX 제품', '3. 계정&제품배정 문의' ]   # level1 - '/level1' 버튼 리스트 (텍스트 + 메세지) 
level2ButtonList = [ '설치 문의' ]   # level2 - 서브 카테고리 버튼 리스트 (텍스트 + 메세지)

# level3 - '1. Autodesk 제품 설치 문의' 버튼 리스트 (텍스트 + 메세지)
autodeskInstButtonList = [ '1. 오토캐드', '2. 레빗', '3. 나비스웍스 매니지', '4. 나비스웍스 시뮬레이트', '5. Civil 3D', '6. 어드밴스트 스틸', '7. Inventor', '8. 3ds Max', '9. Maya', '더보기' ]
# level3 - '더보기' 버튼 텍스트 리스트
autodeskSeeMoreButtonList = [ '10. Fusion', '11. InfraWorks', '12. Twinmotion', '13. DWGTrueView', '14. 나비스웍스 변환기' ]
is_autodeskSeeMore = False    # level3 - '더보기' 버튼 클릭 여부 
autodeskInstVersion = '1. Autodesk 제품 버전' # '1. Autodesk 제품 버전' 버튼 메시지 

# level3 - 2. 상상진화 BOX 제품 설치 문의
boxInstButtonList = [ '1. Revit BOX', '2. CAD BOX', '3. Energy BOX' ]
boxInstVersion = '2. 상상진화 BOX 제품 버전'   # '2. 상상진화 BOX 제품 버전' 버튼 메시지

# level3 - 3. 계정&제품배정 문의
accountButtonList = [ '1. 오토데스크 계정 생성', '2. 계정 비밀번호 분실', '3. 사용가능 제품확인', '4. 신규인원 제품배정', '5. 기존인원 제품제거', '6. 사용자 그룹관리 안내', '7. 만료일 계약내역 확인', '8. 관리자 역할 재지정', '9. 사용량 보고서 확인', '10. 기타 문의' ]

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
            dbReset(filename)
        else:
            print("File Exists")   # print 함수 호출하여 지금 현재 파일이 있다고 메시지 "File Exists" 출력 

        # 테스트 로그 기록 
        botLogger.info("[테스트] 사용자 입력 채팅 정보 - %s" %event['body'])

        response_queue = q.Queue()   #.put(), .get()

        request_respond = threading.Thread(target=responseChatbot,
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
    
# 카카오 챗봇 답변 요청 및 응답 확인
def responseChatbot(request,response_queue,filename):
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

            save_log = f"img {str(bot_res)} {str(prompt)}"
            dbSave(filename, save_log)

        elif '/ask' in request["userRequest"]["utterance"]:
            dbReset(filename)  
            prompt = request["userRequest"]["utterance"].replace("/ask", "")
            bot_res = getTextFromGPT(prompt)
            response_queue.put(textResponseFormat(bot_res))
            print(bot_res)

            save_log = f"ask {str(bot_res)}" 
            dbSave(filename, save_log)

        elif '/error' in request["userRequest"]["utterance"]:
            dbReset(filename)   

            save_log = "오류 테스트"
            dbSave(filename, save_log)

            raise Exception("[테스트] [오류 안내]\n"+
                            "오류 사유 : 테스트 오류\n"+
                            "문제 해결이 어려울시\n"+ 
                            "상상플렉스 커뮤니티(https://www.ssflex.co.kr/community/open)\n"+
                            "혹은 기술지원번호(02-3474-2263)으로 문의 부탁드립니다.")   # 예외를 발생시킴

        # level1 - 상담시간 안내
        elif imagineBuilderList[level1Index] in request["userRequest"]["utterance"]:
            dbReset(filename)   
            response_queue.put(kakao.level1_textCardResponseFormat(level1ButtonList))

            save_log = "level1 - 상담시간 안내 테스트"
            botLogger.info(save_log)
            dbSave(filename, save_log)

        # level2 - 1. Autodesk 제품 상담 유형
        elif imagineBuilderList[autodeskIndex] == request["userRequest"]["utterance"]:
            dbReset(filename)
            type = imagineBuilderList[autodeskIndex]
            response_queue.put(kakao.level2_textCardResponseFormat(type, level2ButtonList))

            save_log = f"level2 - {type} 상담 유형 테스트"
            botLogger.info(save_log)
            dbSave(filename, save_log)

        # level2 - 2. 상상진화 BOX 제품 상담 유형
        elif imagineBuilderList[boxIndex] == request["userRequest"]["utterance"]:
            dbReset(filename)
            type = imagineBuilderList[boxIndex]
            response_queue.put(kakao.level2_textCardResponseFormat(type, level2ButtonList))

            save_log = f"level2 - {type} 상담 유형 테스트"
            botLogger.info(save_log)
            dbSave(filename, save_log)

        # level3 - 1. Autodesk 제품 설치 문의
        elif imagineBuilderList[autodeskInstIndex] == request["userRequest"]["utterance"]:
            dbReset(filename)  
            is_autodeskSeeMore = False    # level3 - '더보기' 버튼 클릭 안 함.
            response_queue.put(kakao.level3_autodesk_quickRepliesResponseFormat(is_autodeskSeeMore, autodeskInstVersion, autodeskInstButtonList))

            save_log = "level3 - 1. Autodesk 제품 설치 문의 테스트"
            botLogger.info(save_log)
            dbSave(filename, save_log)

        # level3 - 더보기 1. Autodesk 제품 설치 문의
        elif imagineBuilderList[autodeskSeeMoreIndex] == request["userRequest"]["utterance"]:
            dbReset(filename)  
            is_autodeskSeeMore = True    # level3 - '더보기' 버튼 클릭함.
            response_queue.put(kakao.level3_autodesk_quickRepliesResponseFormat(is_autodeskSeeMore, autodeskInstVersion, autodeskSeeMoreButtonList))

            save_log = "level3 - 더보기 1. Autodesk 제품 설치 문의 테스트"
            botLogger.info(save_log)
            dbSave(filename, save_log)

        # level3 - 2. 상상진화 BOX 제품 설치 문의
        elif imagineBuilderList[boxInstIndex] == request["userRequest"]["utterance"]:
            dbReset(filename)    
            response_queue.put(kakao.level3_box_textCardResponseFormat(boxInstVersion, boxInstButtonList))

            save_log = "level3 - 2. 상상진화 BOX 제품 설치 문의 테스트"
            botLogger.info(save_log)
            dbSave(filename, save_log)

        # level3 - 3. 계정&제품배정 문의
        elif imagineBuilderList[accountIndex] == request["userRequest"]["utterance"]:
            dbReset(filename)    
            response_queue.put(kakao.level3_account_textCardResponseFormat(accountButtonList))

            save_log = "level3 - 3. 계정&제품배정 문의 테스트"
            botLogger.info(save_log)
            dbSave(filename, save_log)

        # elif imagineBuilderList[boxInstallerIndex] == request["userRequest"]["utterance"]:
        #     dbReset(filename)  
        #     messageTextBOX = imagineBuilderList[boxVersionIndex]    
        #     response_queue.put(kakao.level3BOXquickRepliesResponseFormat(messageTextBOX))

        #     save_log = "level3"+ " " + "상상진화 BOX 제품 설치 문의"

        #     with open(filename, 'w') as f:
        #         f.write(save_log)

        else:
            base_response = {'version': '2.0', 'template': {'outputs': [], 'quickReplies': []}}
            response_queue.put(base_response)

    except Exception as e:   # 하위 코드 블록에서 예외가 발생해도 변수 e에다 넣고 아래 코드 실행됨
        # 테스트 오류 로그 기록  
        errorMessage = str(e)  # str() 함수 사용해서 Exception 클래스 객체 e를 문자열로 변환 및 오류 메시지 변수 errorMessage에 할당 (문자열로 변환 안할시 카카오 챗봇에서 스킬서버 오류 출력되면서 챗봇이 답변도 안하고 장시간 멈춤 상태 발생.)
        botLogger.error('[테스트] 오류 - %s' %errorMessage)
        response_queue.put(kakao.error_textResponseFormat(errorMessage))
        # 오류 로그 기록 
        raise    # raise로 함수 responseOpenAI의 현재 예외를 다시 발생시켜서 함수 responseOpenAI 호출한 상위 코드 블록으로 넘김

# 시간 5초 초과시 응답
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

# 메세지 전송 (카카오톡 서버로 텍스트 전송)
def textResponseFormat(bot_response):
    response = {'version': '2.0', 'template': {
    'outputs': [{"simpleText": {"text": bot_response}}], 'quickReplies': []}}
    return response   

# 그림 전송 (카카오톡 서버로 그림 전송)
def imageResponseFormat(bot_response, prompt):
    output_text = prompt+"내용에 관한 이미지 입니다"
    response = {'version': '2.0', 'template': {
    'outputs': [{"simpleImage": {"imageUrl": bot_response,"altText": output_text}}], 'quickReplies': []}}
    return response  

# ChatGPT 텍스트 응답 
def getTextFromGPT(prompt):  
    messages_prompt = [{"role": "system", "content": 'You are a thoughtful assistant. Respond to all input in 300 words and answer in korea'}]
    messages_prompt += [{"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages_prompt)

    message = response["choices"][0]["message"]["content"]
    return message   

# DALLE2 이미지 응답
def getImageURLFromDALLE(prompt):
    response = openai.Image.create(prompt=prompt,n=1,size="512x512")
    image_url = response['data'][0]['url']
    return image_url  

# 아마존 웹서비스(AWS) 람다 함수(Lambda Function) -> 텍스트 파일("/tmp/botlog.txt")에 적힌 로그(텍스트) 초기화  
def dbReset(filename):
    with open(filename, 'w') as f:
        f.write("")

# 아마존 웹서비스(AWS) 람다 함수(Lambda Function) -> 텍스트 파일("/tmp/botlog.txt")에 적힌 로그(텍스트) 작성  
def dbSave(filename, save_log):
    with open(filename, 'w') as f:
        f.write(save_log)