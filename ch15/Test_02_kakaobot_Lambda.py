# 아마존 웹서비스(AWS) 다중인증(MFA는 Multi-Factor Authentication) 등록 방법 및 모바일 어플 Google Authenticator 설치 및 사용 방법 
# 참고 URL - https://happy-jjang-a.tistory.com/223

###### 기본 정보 설정 단계 #######
# 참고사항
# 아마존 웹서비스(AWS) 활용할 때에는 FastAPI 개발자 로컬 웹서버를 따로 생성할 필요가 없으니까
# 패키지 "from fastapi import Request, FastAPI"를 불러올 필요가 없다.

import json         # 카카오톡 서버로부터 받은 json 데이터 처리하기 위해 패키지 json 불러오기 
import openai       # OPENAI 패키지 openai 불러오기 (ChatGPT, DALLE.2 사용)
import threading    # 프로그램 안에서 동시에 작업하는 멀티스레드 구현하기 위해 패키지 "threading" 불러오기
import time         # ChatGPT 답변 시간 계산하기 위해 패키지 "time" 불러오기
import queue as q   # 자료구조 queue(deque 기반) 이용하기 위해 패키지 "queue" 불러오기
import os           # 답변 결과를 테스트 파일로 저장할 때 경로 생성해야 해서 패키지 "os" 불러오기

# 폴더 "commons" 소스파일 
from commons import autodesk_helper  # 1. Autodesk 제품 전용 도움말 텍스트 "autodesk_helper" 불러오기
from commons import box_helper       # 2. 상상진화 BOX 제품 전용 도움말 텍스트 "box_helper" 불러오기
from commons import account_helper   # 3. 계정&제품배정 문의 전용 도움말 텍스트 "account_helper" 불러오기
from commons import chatbot_helper   # 카카오 챗봇 전용 도움말 텍스트 "chatbot_helper" 불러오기

# 폴더 "modules" 소스파일 
from modules import kakao            # 카카오 API 전용 모듈 "kakao" 불러오기 
from modules import logger           # 로그 설정 전용 모듈 "logger" 불러오기 
from modules import openAI           # OpenAI 전용 모듈 "openAI" 불러오기 
from modules import openAI_logger    # OpenAI 리턴 값 로그 작성 모듈 "openAI_logger" 불러오기
from modules import chatbot_logger   # 카카오 챗봇 로그 작성 모듈 "chatbot_logger" 불러오기
from modules import pdf              # PDF 전용 모듈 "pdf" 불러오기
from modules import text             # TEXT 전용 모듈 "text" 불러오기

from enum import Enum   # Enum 열거형 구조체 사용하기 위해 패키지 "enum" 불러오기 

# 데이터 유효성 검사 
# Enum 열거형 구조체 클래스 
# 참고 URL - https://wikidocs.net/105486
# 참고 2 URL - https://docs.python.org/ko/3.9/library/enum.html#functional-api
class EnumValidator(Enum):
    NONE = 0        # 데이터 존재 안 함.
    EXISTENCE = 1   # 데이터 존재함.

# 로그 초기 설정 
bot_logger = logger.configureLogger(chatbot_helper._openai_objname)

# PDF 파일(Autodesk, Box, Account)에 작성된 청크(chunk) 단위 텍스트 가져오기 
# autodesk_chunks = pdf.getChunksFromPDF(autodesk_helper._autoCAD_2024_Kor_PDF_Filepath) 
# box_chunks = pdf.getChunksFromPDF(box_helper._revitBOX_2024_Kor_PDF_Filepath)
# account_chunks = pdf.getChunksFromPDF(account_helper._change_account_password_PDF_Filepath) 

# 중간보고 LOT 용도 - TEXT 파일(Autodesk, Box, Account)에 작성된 모든 텍스트 가져오기 
autoCAD_2024_kor_response = text.getResponseFromText(autodesk_helper._autoCAD_2024_kor_TEXT_Filepath) 
revitBOX_2024_response = text.getResponseFromText(box_helper._revitBOX_2024_TEXT_Filepath)
change_account_password_response = text.getResponseFromText(account_helper._change_account_password_TEXT_Filepath) 


# level1 - '/level1' 버튼 리스트 (텍스트 + 메세지) 
consultBtnList = [ chatbot_helper._autodeskProduct, 
                   chatbot_helper._boxProduct, 
                   chatbot_helper._askAccount ]   

# level2 - 서브 카테고리 버튼 리스트 (텍스트 + 메세지)
subCatBtnList = [ chatbot_helper._askInst, ]

# level3 - 1. Autodesk 제품 설치 문의 버튼 리스트 - label(텍스트) + 메세지(텍스트)
autodeskInstBtnList = [ (autodesk_helper._autoCAD, autodesk_helper._autoCAD_Msg), 
                        (autodesk_helper._revit, autodesk_helper._revit_Msg), 
                        (autodesk_helper._navisworks_Manage, autodesk_helper._navisworks_Manage_Msg), 
                        (autodesk_helper._navisworks_Simulate, autodesk_helper._navisworks_Simulate_Msg), 
                        (autodesk_helper._civil_3D, autodesk_helper._civil_3D_Msg), 
                        (autodesk_helper._advance_Steel, autodesk_helper._advance_Steel_Msg), 
                        (autodesk_helper._inventor, autodesk_helper._inventor_Msg), 
                        (autodesk_helper._3ds_Max, autodesk_helper._3ds_Max_Msg), 
                        (autodesk_helper._maya, autodesk_helper._maya_Msg), 
                        (chatbot_helper._seeMore, chatbot_helper._seeMore) ]

# level3 - 더보기 버튼 텍스트 리스트  - label(텍스트) + 메세지(텍스트)
autodeskSeeMoreBtnList = [ (autodesk_helper._fusion, autodesk_helper._fusion_Msg), 
                           (autodesk_helper._infraWorks, autodesk_helper._infraWorks_Msg), 
                           (autodesk_helper._twinmotion, autodesk_helper._twinmotion_Msg),  
                           (autodesk_helper._dwgTrueView, autodesk_helper._dwgTrueView_Msg),  
                           (autodesk_helper._navisworks_Converter, autodesk_helper._navisworks_Converter_Msg) ]

# level4 - 1. Autodesk 제품 버전 Language Pack 메세지(텍스트) 리스트 
autodeskInstLangPackVerMsgList = [ autodesk_helper._autoCAD_Msg, 
                                   autodesk_helper._revit_Msg, 
                                   autodesk_helper._navisworks_Manage_Msg, 
                                   autodesk_helper._navisworks_Simulate_Msg, 
                                   autodesk_helper._civil_3D_Msg, 
                                   autodesk_helper._advance_Steel_Msg, 
                                   autodesk_helper._inventor_Msg, 
                                   autodesk_helper._3ds_Max_Msg, 
                                   autodesk_helper._infraWorks_Msg ]

# level4 - 1. Autodesk 제품 버전 Language Pack 버튼 리스트 (텍스트 + 메시지)
autodeskInstLangPackVerBtnList = [ (chatbot_helper._2026, chatbot_helper._ver, autodesk_helper._langPack), 
                                   (chatbot_helper._2025, chatbot_helper._ver, autodesk_helper._langPack), 
                                   (chatbot_helper._2024, chatbot_helper._ver, autodesk_helper._langPack), 
                                   (chatbot_helper._2023, chatbot_helper._ver, autodesk_helper._langPack) ]

# level4 - 1. Autodesk 제품 버전 메세지(텍스트) 리스트 
autodeskInstVerMsgList = [ autodesk_helper._maya_Msg, autodesk_helper._twinmotion_Msg, autodesk_helper._navisworks_Converter_Msg ]

# level4 - 1. Autodesk 제품 버전 버튼 리스트 (텍스트 + 메시지)
autodeskInstVerBtnList = [ (chatbot_helper._2026, chatbot_helper._ver), 
                           (chatbot_helper._2025, chatbot_helper._ver), 
                           (chatbot_helper._2024, chatbot_helper._ver), 
                           (chatbot_helper._2023, chatbot_helper._ver) ]

# level4 - 1. Autodesk 제품 설치 방법 (버전 X)
# autodeskInstMsgList = [ autodesk_helper._fusion_Msg, autodesk_helper._dwgTrueView_Msg ]

# level5 - 1. Autodesk 제품 설치 언어 
autodeskInstLangBtnList = [ autodesk_helper._kor, autodesk_helper._eng ]

# level3 - 2. 상상진화 BOX 제품 설치 문의 버튼 리스트 (텍스트 + 메세지)
boxInstBtnList = [ (box_helper._revitBOX, box_helper._revitBOX_Msg), 
                   (box_helper._autoCADBOX, box_helper._autoCADBOX_Msg), 
                   (box_helper._energyBOX, box_helper._energyBOX_Msg) ]

# level4 - 2. 상상진화 BOX 제품 버전 (1. Revit BOX만 해당)
boxInstVerBtnList = [ (chatbot_helper._2026, chatbot_helper._ver), 
                      (chatbot_helper._2025, chatbot_helper._ver), 
                      (chatbot_helper._2024, chatbot_helper._ver), 
                      (chatbot_helper._2023, chatbot_helper._ver), 
                      (chatbot_helper._2022, chatbot_helper._ver), 
                      (chatbot_helper._2021, chatbot_helper._ver) ]

# level4 - 2. 상상진화 BOX 제품 버전 메세지(텍스트) 리스트 
# TODO : 2. 상상진화 BOX 제품 버전 대상에 1. Revit BOX만 포함되어 있지만 추후 필요시 버전 대상 제품 추가 예정 (2025.04.08 minjae)
boxInstVerMsgList = [ box_helper._revitBOX_Msg, ]

# level4 - 2. 상상진화 BOX 설치 방법 (버전 X)
# boxInstMsgList = [ box_helper._autoCADBOX_Msg, box_helper._energyBOX_Msg ]

# level3 - 3. 계정&제품배정 문의 버튼 리스트 - label(텍스트) + 메세지(텍스트)
accountBtnList = [ (account_helper._accountCreation, account_helper._accountCreation_Msg), 
                   (account_helper._forgetPassword, account_helper._forgetPassword_Msg), 
                   (account_helper._availableProduct, account_helper._availableProduct_Msg), 
                   (account_helper._newMember_assignProduct, account_helper._newMember_assignProduct_Msg), 
                   (account_helper._currentMember_removeProduct, account_helper._currentMember_removeProduct_Msg), 
                   (account_helper._manageUserGroup, account_helper._manageUserGroup_Msg), 
                   (account_helper._expirationDate_contractDetail, account_helper._expirationDate_contractDetail_Msg), 
                   (account_helper._redesignateManager, account_helper._redesignateManager_Msg), 
                   (account_helper._usageReport, account_helper._usageReport_Msg), 
                   (account_helper._anyQuestion, account_helper._anyQuestion_Msg) ]

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

        filename = chatbot_helper._botlog_filepath
        # if not os.path.exists(filename):
        if False == os.path.exists(filename):
            dbReset(filename)
        else:
            # print("File Exists")   # print 함수 호출하여 지금 현재 파일이 있다고 메시지 "File Exists" 출력 
            # chatbot_logger.log_write 함수 호출하여 지금 현재 파일이 있다고 메시지 "File Exists" 로그 기록 
            chatbot_logger.log_write(chatbot_logger._info, "파일 존재 여부", "File Exists")

        # 테스트 로그 기록 
        # chatbot_logger._info("[테스트] 사용자 입력 채팅 정보 - %s" %event['body'])
        chatbot_logger.log_write(chatbot_logger._info, "[테스트] 사용자 입력 채팅 정보", event['body'])

        response_queue = q.Queue()   #.put(), .get()

        request_respond = threading.Thread(target=responseChatbot,
                                           args=(kakaorequest, response_queue,filename))
        request_respond.start()

    except Exception as e:   # 하위 코드 블록에서 예외가 발생해도 변수 e에다 넣고 아래 코드 실행됨
        # pass
        # 테스트 오류 로그 기록  
        error_Msg = str(e)  # str() 함수 사용해서 Exception 클래스 객체 e를 문자열로 변환 및 오류 메시지 변수 error_Msg에 할당 (문자열로 변환 안할시 카카오 챗봇에서 스킬서버 오류 출력되면서 챗봇이 답변도 안하고 장시간 멈춤 상태 발생.)
        # chatbot_logger._error('[테스트] 오류 - %s' %error_Msg)
        chatbot_logger.log_write(chatbot_logger._error, "[테스트] 오류", error_Msg)
    finally:   # 예외 발생 여부와 상관없이 항상 마지막에 실행할 코드
        # 시간 3.5초 이내인 경우 
        while(time.time() - start_time < 3.5):
            if not response_queue.empty():
                response = response_queue.get()
                run_flag= True   
                break   
            time.sleep(0.01)

        # 시간 5초 초과한 경우 
        if False == run_flag:     
            response = kakao.timeover_quickRepliesResponseFormat(chatbot_helper._doneThinking)   

        # 테스트 로그 기록
        responseMessage = json.dumps(response)
        # chatbot_logger._info("[테스트] 챗봇 답변 채팅 정보 - %s" %responseMessage)
        chatbot_logger.log_write(chatbot_logger._info, "[테스트] 챗봇 답변 채팅 정보", responseMessage)

        # 카카오톡 서버로 json 형태의 데이터(response 포함) 리턴
        return {
            'statusCode':200,
            'body': json.dumps(response),
            'headers': {
                'Access-Control-Allow-Origin': '*',
            }
        }
    
# 카카오 챗봇 답변 요청 및 응답 확인
def responseChatbot(request, response_queue, filename):
    try:
        if False == isValidator():   # 데이터 유효성 검사 결과 오류인 경우
            raise Exception(chatbot_helper._errorTitle + 
                            '사유 : 데이터 유효성 검사 오류.\n'+
                            chatbot_helper._errorSSflex)
        
        chatbot_logger.log_write(chatbot_logger._info, '[테스트] 데이터 유효성 검사 결과', 'OK!')   # 데이터 유효성 검사 결과 성공   
        userRequest_Msg = request["userRequest"]["utterance"]   # 사용자 입력 채팅 정보 가져오기 

        # 시간 5초 초과시 응답 재요청
        if chatbot_helper._doneThinking in userRequest_Msg:
            with open(filename) as f:
                last_update = f.read()  
            if len(last_update.split())>1:
                kind = last_update.split()[0]  
                if kind == "img":
                    bot_res, prompt = last_update.split()[1],last_update.split()[2]
                    response_queue.put(kakao.simple_imageResponseFormat(bot_res,prompt))
                else:
                    bot_res = last_update[4:]

                    # TODO : 아래 주석친 OpenAI 로그 기록 코드 필요시 사용 예정 (2025.03.27 minjae)
                    # openAI_logger.log_write(openAI_logger._info, "시간 5초 초과 후 ChatGPT 텍스트 답변", bot_res)
                    response_queue.put(kakao.simple_textResponseFormat(bot_res))
                dbReset(filename)   

        elif '/img' in userRequest_Msg:
            dbReset(filename)   
            prompt = userRequest_Msg.replace("/img", "")
            bot_res = openAI.getImageURLFromDALLE(prompt)
            response_queue.put(kakao.simple_imageResponseFormat(bot_res,prompt))

            saveLog_Msg = f"img {str(bot_res)} {str(prompt)}"
            dbSave(filename, saveLog_Msg)

        elif '/ask' in userRequest_Msg:
            # TODO : 아래 함수 호출 구간 dbReset(filename) ~ dbSave(filename, saveLog_Msg) 을 간결하게 하기 위해 
            #        함수 dbSetting 구현 및 해당 함수 dbSetting에 파라미터로 카카오 함수(kakao.~~~~~_ResponseFormat())
            #        전달 가능하도록 구현 예정 (2025.04.17 minjae)
            # 참고 URL - https://www.codeit.kr/community/questions/UXVlc3Rpb246NWU1Y2M4NzJjZGQwNzQ1OTAzYWU2NGNk
            dbReset(filename)  
            prompt = userRequest_Msg.replace("/ask", "")
            bot_res = openAI.getMessageFromGPT(prompt)
            response_queue.put(kakao.simple_textResponseFormat(bot_res))

            openAI_logger.log_write(openAI_logger._info, "ChatGPT 텍스트 답변", bot_res)
            saveLog_Msg = f"ask {str(bot_res)}" 
            dbSave(filename, saveLog_Msg)

        elif '/error' in userRequest_Msg:
            saveLog(filename, chatbot_logger._error, "오류 테스트")

            raise Exception(chatbot_helper._errorTitle + 
                            '사유 : 테스트 오류\n' +
                            chatbot_helper._errorSSflex)   # 예외를 발생시킴
        
        # [OpenAI] API 테스트 기능 
        # elif '/openai' in userRequest_Msg:
        #     dbReset(filename)
        #     prompt = userRequest_Msg.replace("/openai", "")  

        #     if autodesk_helper._commandType in prompt:   # Autodesk 제품 설치 방법 
        #         # chunks = autodesk_chunks 
        #         response = autodesk_response
        #     elif box_helper._commandType in prompt:      # 상상진화 BOX 제품 설치 방법 
        #         # chunks = box_chunks
        #         response = box_response
        #     elif account_helper._commandType in prompt:  # 계정&제품배정 문의
        #         # chunks = account_chunks
        #         response = account_response

        #     # 함수 len 사용하여 리스트 객체 chunks 안에 존재하는 요소의 갯수가 0보다 큰 경우
        #     # 함수 len 사용하여 문자열 response 길이가 0보다 큰 경우
        #     # if len(chunks) > 0:
        #     if len(response) > 0:
        #         # bot_res = openAI.getMessageFromChunks(chunks, prompt)
        #         bot_res = response
        #         response_queue.put(kakao.simple_textResponseFormat(bot_res))
        #         openAI_logger.log_write(openAI_logger._info, "", bot_res)

        #         saveLog_Msg = f"openai {str(bot_res)}" 
        #         dbSave(filename, saveLog_Msg)
            
        #     else:
        #         bot_res = ''
        #         openAI_logger.log_write(openAI_logger._error, "", bot_res)

        #         saveLog_Msg = f"openai {str(bot_res)}" 
        #         dbSave(filename, saveLog_Msg)
        
        #         raise Exception(chatbot_helper._errorTitle+
        #                         # '사유 : PDF 파일 기반 텍스트(chunk) 존재 안 함.\n'+
        #                         '사유 : TEXT 파일 존재 안 함.\n'+
        #                         chatbot_helper._errorSSflex)   # 예외를 발생시킴       

        # level1 - 상담시간 안내 or 처음으로
        elif (chatbot_helper._consult in userRequest_Msg
              or chatbot_helper._beginning in userRequest_Msg):
            saveLog(filename, chatbot_logger._info, "level1 - 상담시간 안내 테스트")   
            response_queue.put(kakao.level1_consult_textCardResponseFormat(consultBtnList))

        # level2 - 1. Autodesk 제품 상담 유형 or 2. 상상진화 BOX 제품 상담 유형
        elif (chatbot_helper._autodeskProduct == userRequest_Msg
              or chatbot_helper._boxProduct == userRequest_Msg):
            saveLog(filename, chatbot_logger._info, f"level2 - {userRequest_Msg} 상담 유형 테스트")
            response_queue.put(kakao.level2_textCardResponseFormat(userRequest_Msg, subCatBtnList))

        # level2 - 2. 상상진화 BOX 제품 상담 유형
        # elif chatbot_helper._boxProduct == userRequest_Msg:
        #     saveLog(filename, chatbot_logger._info, f"level2 - {userRequest_Msg} 상담 유형 테스트")
        #     response_queue.put(kakao.level2_textCardResponseFormat(userRequest_Msg, subCatBtnList))

        # level2 - 3. 계정&제품배정 문의
        elif chatbot_helper._askAccount == userRequest_Msg:
            saveLog(filename, chatbot_logger._info, f"level2 - {userRequest_Msg} 테스트")    
            response_queue.put(kakao.level2_account_quickRepliesResponseFormat(accountBtnList))

        # level3 - 1. Autodesk 제품 설치 문의
        elif chatbot_helper._askInst_autodeskProduct == userRequest_Msg:
            saveLog(filename, chatbot_logger._info, f"level3 - {userRequest_Msg} 테스트")
            response_queue.put(kakao.level3_autodesk_quickRepliesResponseFormat(autodeskInstBtnList))

        # level3 - 더보기 1. Autodesk 제품 설치 문의
        elif chatbot_helper._seeMore == userRequest_Msg:
            saveLog(filename, chatbot_logger._info, f"level3 - {userRequest_Msg} {chatbot_helper._askInst_autodeskProduct} 테스트")
            response_queue.put(kakao.level3_autodesk_quickRepliesResponseFormat(autodeskSeeMoreBtnList))

        # level3 - 2. 상상진화 BOX 제품 설치 문의
        elif chatbot_helper._askInst_boxProduct == userRequest_Msg:
            saveLog(filename, chatbot_logger._info, f"level3 - {userRequest_Msg} 테스트")
            response_queue.put(kakao.level3_box_textCardResponseFormat(boxInstBtnList))

        # 1. Autodesk 제품 또는 2. 상상진화 BOX 제품 버전 2026 이상 또는 아직 준비되지 못한 버전
        elif chatbot_helper._2026 in userRequest_Msg: 
            saveLog(filename, chatbot_logger._error, "1. Autodesk 제품 또는 2. 상상진화 BOX 제품 버전 2026 이상 또는 아직 준비되지 못한 버전 테스트")

            raise Exception(chatbot_helper._errorTitle + 
                            '사유 : 제품없음.\n'+
                            '해당 제품군은 아직 준비 중입니다.\n'+
                            '추가 문의 필요시\n'+
                            chatbot_helper._errorSSflex)   # 예외를 발생시킴

        # level4 - 1. Autodesk 제품 버전 Language Pack
        # TODO : 파이썬 in 연산자 사용하여 리스트 객체 "autodeskInstLangPackVerMsgList" 안에 사용자가 클릭한 버튼 텍스트 메시지 (예) 오토캐드 
        #        존재하는 경우 아래 elif 절 로직 실행할 수 있도록 구현 (2025.03.28 minjae) 
        # 참고 URL - https://hun931018.tistory.com/55
        # 참고 2 URL - https://miki3079.tistory.com/40
        # 참고 3 URL - https://cigiko.cafe24.com/python-%EB%A6%AC%EC%8A%A4%ED%8A%B8%EC%9D%98-%EA%B8%B0%EC%B4%88-%EC%97%B0%EC%82%B0%EB%93%A4/
        # 리스트 객체 "autodeskInstLangPackVerMsgList" 내부에 사용자가 클릭한 버튼 텍스트 메시지 "userRequest_Msg = request["userRequest"]["utterance"]" 값 존재하는 경우
        elif userRequest_Msg in autodeskInstLangPackVerMsgList:
            saveLog(filename, chatbot_logger._info, f"level4 - {userRequest_Msg} 테스트")
            response_queue.put(kakao.level4_autodeskInstLangPackVer_quickRepliesResponseFormat(userRequest_Msg, autodeskInstLangPackVerBtnList))

        # level4 - 1. Autodesk 제품 버전
        # TODO : 파이썬 in 연산자 사용하여 리스트 객체 "autodeskInstVerMsgList" 안에 사용자가 클릭한 버튼 텍스트 메시지 (예) 12. Twinmotion
        #        존재하는 경우 아래 elif 절 로직 실행할 수 있도록 구현 (2025.03.28 minjae) 
        # 참고 URL - https://hun931018.tistory.com/55
        # 참고 2 URL - https://miki3079.tistory.com/40
        # 참고 3 URL - https://cigiko.cafe24.com/python-%EB%A6%AC%EC%8A%A4%ED%8A%B8%EC%9D%98-%EA%B8%B0%EC%B4%88-%EC%97%B0%EC%82%B0%EB%93%A4/
        # 리스트 객체 "autodeskInstVerMsgList" 내부에 사용자가 클릭한 버튼 텍스트 메시지 "userRequest_Msg = request["userRequest"]["utterance"]" 값 존재하는 경우
        elif userRequest_Msg in autodeskInstVerMsgList:
            saveLog(filename, chatbot_logger._info, f"level4 - {userRequest_Msg} 테스트")
            response_queue.put(kakao.level4_autodeskInstVer_quickRepliesResponseFormat(userRequest_Msg, autodeskInstVerBtnList))

        # level4 - 2. 상상진화 BOX 제품 버전 
        # TODO : 2. 상상진화 BOX 제품 버전 대상에 1. Revit BOX만 포함되어 있지만 추후 필요시 버전 대상 제품 추가 예정 (2025.04.08 minjae)
        elif userRequest_Msg in boxInstVerMsgList:
            saveLog(filename, chatbot_logger._info, f"level4 - {userRequest_Msg} 테스트")
            response_queue.put(kakao.level4_boxInstVer_quickRepliesResponseFormat(userRequest_Msg, boxInstVerBtnList))

        # level5 - 1. Autodesk 제품 설치 언어 
        # 파이썬 in 연산자 사용하여 사용자가 클릭한 버튼 텍스트 메시지 "userRequest_Msg = request["userRequest"]["utterance"]" 문자열 안에 "autodesk_helper._langPack"이 포함되어 있고 
        # 파이썬 not in 연산자 사용하여 사용자가 클릭한 버튼 텍스트 메시지 "userRequest_Msg = request["userRequest"]["utterance"]" 문자열 안에 "chatbot_helper._softwareInstMethod"이 포함되지 않은 경우 
        elif (autodesk_helper._langPack in userRequest_Msg 
              and chatbot_helper._softwareInstMethod not in userRequest_Msg):
            saveLog(filename, chatbot_logger._info, f"level5 - {userRequest_Msg} 테스트")    
            response_queue.put(kakao.level5_autodeskInstLang_textCardResponseFormat(userRequest_Msg, autodeskInstLangBtnList))

        # [OpenAI] level6 - 1. Autodesk 제품 설치 방법
        elif (autodesk_helper._commandType in userRequest_Msg
              and chatbot_helper._softwareInstMethod in userRequest_Msg): 
            saveLog(filename, chatbot_logger._info, f"level6 - {userRequest_Msg} 테스트")
                
            if (autodesk_helper._autoCAD_Msg in userRequest_Msg 
                and chatbot_helper._2024 in userRequest_Msg 
                and autodesk_helper._kor in userRequest_Msg): 
                response_queue.put(kakao.beginning_quickRepliesResponseFormat(autoCAD_2024_kor_response))
            else:
                response_queue.put(kakao.beginning_quickRepliesResponseFormat("[구현 예정!] " + userRequest_Msg))

            # TODO : 아래 주석친 OpenAI 관련 기능 추후 구현 예정 (2025.04.10 minjae) 
            # result_Msg = openAI.(userRequest_Msg)
            # response_queue.put(kakao.beginning_quickRepliesResponseFormat(result_Msg))

        # [OpenAI] level5 - 2. 상상진화 BOX 제품 설치 방법
        elif (box_helper._commandType in userRequest_Msg
              and chatbot_helper._softwareInstMethod in userRequest_Msg): 
            saveLog(filename, chatbot_logger._info, f"level5 - {userRequest_Msg} 테스트")
    
            if (box_helper._revitBOX_Msg in userRequest_Msg 
                and chatbot_helper._2024 in userRequest_Msg):
                response_queue.put(kakao.beginning_quickRepliesResponseFormat(revitBOX_2024_response))
            else:
                response_queue.put(kakao.beginning_quickRepliesResponseFormat("[구현 예정!] " + userRequest_Msg))

            # TODO : 아래 주석친 OpenAI 관련 기능 추후 구현 예정 (2025.04.10 minjae)
            # result_Msg = openAI.(userRequest_Msg)
            # response_queue.put(kakao.beginning_quickRepliesResponseFormat(result_Msg)) 

        # [OpenAI] level3 - 3. 계정&제품배정 문의
        elif account_helper._commandType in userRequest_Msg: 
            saveLog(filename, chatbot_logger._info, f"level3 - {userRequest_Msg} 테스트")

            # '기타 문의'일 경우 
            if account_helper._anyQuestion_Msg in userRequest_Msg:
                response_queue.put(kakao.beginning_quickRepliesResponseFormat(account_helper._anyQuestion_response))
            # '계정 비밀번호 분실'일 경우 
            elif account_helper._forgetPassword_Msg in userRequest_Msg:
                response_queue.put(kakao.beginning_quickRepliesResponseFormat(change_account_password_response))
            # '기타 문의', '계정 비밀번호 분실' 제외한 다른 문의일 경우
            else:
                response_queue.put(kakao.beginning_quickRepliesResponseFormat("[구현 예정!] " + userRequest_Msg))
                # TODO : 아래 주석친 OpenAI 관련 기능 추후 구현 예정 (2025.04.10 minjae)
                # result_Msg = openAI.(userRequest_Msg)
                # response_queue.put(kakao.beginning_quickRepliesResponseFormat(result_Msg))

        # level4 - 1. Autodesk 제품 버전 X
        # TODO : 파이썬 in 연산자 사용하여 리스트 객체 "autodeskInstMsgList" 안에 사용자가 클릭한 버튼 텍스트 메시지 (예) 'Fusion'
        #        존재하는 경우 아래 elif 절 로직 실행할 수 있도록 구현 (2025.03.28 minjae) 
        # 리스트 객체 "autodeskInstMsgList" 내부에 사용자가 클릭한 버튼 텍스트 메시지 "userRequest_Msg = request["userRequest"]["utterance"]" 값 존재하는 경우
        # elif userRequest_Msg in autodeskInstMsgList:
        #     saveLog(filename, f"level4 - {userRequest_Msg} 테스트")
            
        #     # message = f'{userRequest_Msg} {chatbot_helper._softwareInstMethod}'
        #     # response_queue.put(kakao.simple_textResponseFormat(message))

        else:
            base_response = {'version': '2.0', 'template': {'outputs': [], 'quickReplies': []}}
            response_queue.put(base_response)

    except Exception as e:   # 하위 코드 블록에서 예외가 발생해도 변수 e에다 넣고 아래 코드 실행됨
        # 테스트 오류 로그 기록  
        error_Msg = str(e)  # str() 함수 사용해서 Exception 클래스 객체 e를 문자열로 변환 및 오류 메시지 변수 error_Msg에 할당 (문자열로 변환 안할시 카카오 챗봇에서 스킬서버 오류 출력되면서 챗봇이 답변도 안하고 장시간 멈춤 상태 발생.)
        # chatbot_logger._error('[테스트] 오류 - %s' %error_Msg)
        chatbot_logger.log_write(chatbot_logger._error, "[테스트] 오류", error_Msg)
        response_queue.put(kakao.error_textResponseFormat(error_Msg))
        raise    # raise로 함수 responseChatbot의 현재 예외를 다시 발생시켜서 함수 responseChatbot 호출한 상위 코드 블록으로 넘김

# 카카오 챗봇 프로그램 상단에 정의한 
# 변수(문자열, 리스트 객체)에 저장된 데이터 유효성 검사
# 참고 URL - https://chatgpt.com/c/68017acc-672c-8010-8649-7fa39f17d834
def isValidator():
    # 파이썬 함수 len 사용하여 문자열, 리스트 객체 길이 구하기
    # 참고 URL - https://wikidocs.net/215513 
    if (EnumValidator.NONE.value >= len(autoCAD_2024_kor_response) 
        or EnumValidator.NONE.value >= len(revitBOX_2024_response)
        or EnumValidator.NONE.value >= len(change_account_password_response)     
        or EnumValidator.NONE.value >= len(consultBtnList)       
        or EnumValidator.NONE.value >= len(subCatBtnList)
        or EnumValidator.NONE.value >= len(autodeskInstBtnList)
        or EnumValidator.NONE.value >= len(autodeskSeeMoreBtnList)
        or EnumValidator.NONE.value >= len(autodeskInstLangPackVerMsgList) 
        or EnumValidator.NONE.value >= len(autodeskInstLangPackVerBtnList)
        or EnumValidator.NONE.value >= len(autodeskInstVerMsgList)
        or EnumValidator.NONE.value >= len(autodeskInstVerBtnList)        
        or EnumValidator.NONE.value >= len(autodeskInstLangBtnList)        
        or EnumValidator.NONE.value >= len(boxInstBtnList)      
        or EnumValidator.NONE.value >= len(boxInstVerBtnList) 
        or EnumValidator.NONE.value >= len(boxInstVerMsgList)         
        or EnumValidator.NONE.value >= len(accountBtnList)):
        return False   # 데이터 유효성 검사 오류 
        
    return True   # 데이터 유효성 검사 성공

# 아마존 웹서비스(AWS) 람다 함수(Lambda Function) 
# -> 로그 텍스트 파일("/tmp/botlog.txt")에 적힌 로그(텍스트) 초기화 및 작성 
def saveLog(filename, log_level, saveLog_Msg):
    dbReset(filename)   
    chatbot_logger.log_write(log_level, "", saveLog_Msg)
    dbSave(filename, saveLog_Msg)

# 아마존 웹서비스(AWS) 람다 함수(Lambda Function) -> 로그 텍스트 파일("/tmp/botlog.txt")에 적힌 로그(텍스트) 초기화  
def dbReset(filename):
    with open(filename, 'w') as f:
        f.write("")

# 아마존 웹서비스(AWS) 람다 함수(Lambda Function) -> 로그 텍스트 파일("/tmp/botlog.txt")에 적힌 로그(텍스트) 작성  
def dbSave(filename, saveLog_Msg):
    with open(filename, 'w') as f:
        f.write(saveLog_Msg)