###### 기능 구현 단계 #######
# 카카오톡 챗봇 프로그램을 구동하는데 필요한 모든 기능 함수화 해서
# 파이썬 스크립트 파일(01_kakaobot_Lambda.py)에 속한 
# 메인 함수 "lambda_handler" -> 답변/사진 요청 및 응답 확인 함수 "responseOpenAI"에서 사용할 수 있도록 정리 

from commons import autodesk_helper  # 폴더 "commons" -> 1. Autodesk 제품 전용 도움말 텍스트 "autodesk_helper" 불러오기
from commons import box_helper       # 폴더 "commons" -> 2. 상상진화 BOX 제품 전용 도움말 텍스트 "box_helper" 불러오기
from commons import account_helper   # 폴더 "commons" -> 3. 계정&제품배정 문의 전용 도움말 텍스트 "account_helper" 불러오기
from commons import chatbot_helper   # 폴더 "commons" -> 카카오 챗봇 전용 도움말 텍스트 "chatbot_helper" 불러오기

# 메세지 전송 (카카오톡 서버로 텍스트 전송)
# def textResponseFormat(bot_response):
#     response = {'version': '2.0', 'template': {
#     'outputs': [{"simpleText": {"text": bot_response}}], 'quickReplies': []}}
#     return response   

# 텍스트 메세지 전송 (카카오톡 서버로 텍스트 전송)
# 카카오톡 채팅방에 보낼 메시지를 매개변수 message에 input으로 받기(인자로 전달)
def simple_textResponseFormat(message):
    # 카카오톡 채팅방에 보낼 메시지가 저장된 매개변수 message를
    # 아래 json 형태(Format)에서 항목 'outputs' -> 항목 "simpleText" -> "text"안에 매개변수 message를 넣어서
    # 변수 response에 저장하기 
    response = {
        'version': '2.0', 
        'template': {
            'outputs': [
                {
                    "simpleText": {
                        "text": message
                    }
                }
            ], 
            'quickReplies': []
        }
    }
    return response   # 카카오톡 서버로 답변 전송하기 위해 답변 전송 전용 JSON 형태(Format)의 데이터가 저장된 변수 response 리턴 

# 그림 전송 (카카오톡 서버로 그림 전송)
# def imageResponseFormat(bot_response, prompt):
def image_ResponseFormat(bot_response, prompt):
    output_text = prompt+"내용에 관한 이미지 입니다"
    response = {
        'version': '2.0', 
        'template': {
            'outputs': [
                {
                    "simpleImage": {
                        "imageUrl": bot_response,
                        "altText": output_text
                    }
                }], 
                'quickReplies': []
        }
    }
    return response   

# 오류 메세지 전송 (카카오톡 서버로 텍스트 전송)
# 오류 발생시 카카오톡 서버로 오류 메시지 전송 전용 JSON 형태(Format)의 데이터로 전달하기 위한 함수
# 카카오톡 채팅방에 보낼 메시지를 매개변수 errorMessage에 input으로 받기(인자로 전달)
def error_textResponseFormat(errorMessage):
    # 카카오톡 채팅방에 보낼 메시지가 저장된 매개변수 errorMessage를
    # 아래 json 형태(Format)에서 항목 'outputs' -> 항목 "simpleText" -> "text"안에 매개변수 errorMessage을 넣어서
    # 변수 response에 저장하기 
    response = {
        'version': '2.0', 
        'template': {
            'outputs': [
                {
                    "simpleText": {
                        "text": errorMessage
                    }
                }
            ], 
            'quickReplies': []
        }
    }
    return response   # 카카오톡 서버로 답변 전송하기 위해 답변 전송 전용 JSON 형태(Format)의 데이터가 저장된 변수 response 리턴    

# level1 텍스트 카드 (카카오톡 서버로 텍스트 전송)
# 상담시간 안내
def level1_consult_textCardResponseFormat(consultBtnList):
    consultButtons = []
    # 상담시간 안내 3가지 버튼 텍스트 및 메세지 추가 
    for consultLabel in consultBtnList:
        consultButtons.append({
            "action": "message",
            "label": consultLabel,
            "messageText": consultLabel
        })
        
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "textCard": {
                        "title": chatbot_helper._consultTitle,
                        "description": chatbot_helper._consultDescription,
                        "buttons": consultButtons
                    }
                }
            ],
            "quickReplies": []
        }
    }
    # TODO : 함수 level1_textCardResponseFormat 로직 수정 예정 (2025.03.05 minjae)
    # 함수 len 사용하여 testButtons 배열 안에 존재하는 요소의 갯수가 0보다 큰경우
    # ----- if len(testButtons) > 0:
    #     response["template"]["buttons"] = testButtons

    return response


# level2 텍스트 카드 (카카오톡 서버로 텍스트 전송)
# 상담유형 안내
def level2_textCardResponseFormat(userRequest_Msg, level2BtnList):
    subCatButtons = []
    # 상담유형 안내 버튼 텍스트 및 메세지 추가 
    for subCatLabel in level2BtnList:
        subCatButtons.append({
            "action": "message",
            "label": subCatLabel,
            "messageText": f"{userRequest_Msg} {subCatLabel}"
        })
        
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "textCard": {
                        "title": chatbot_helper._subCatTitle,
                        "description": chatbot_helper._selectInfo,
                        "buttons" : subCatButtons
                    }
                }
            ],
            "quickReplies": []
        }
    }
    # TODO : 함수 level2_textCardResponseFormat 로직 수정 예정 (2025.03.05 minjae)
    # 함수 len 사용하여 testButtons 배열 안에 존재하는 요소의 갯수가 0보다 큰경우
    # ----- if len(testButtons) > 0:
    #     response["template"]["buttons"] = testButtons

    return response

# level2 바로가기 그룹 전송 (카카오톡 서버로 텍스트 전송)
# 3. 계정&제품배정 문의
def level2_account_quickRepliesResponseFormat(accountBtnList):
    accountQuickReplies = []
    # 3. 계정&제품배정 문의 10가지 버튼 텍스트 및 메세지 추가 
    for (accountLabel, accountMsg) in accountBtnList:
        messageText = f"{account_helper._commandType} {accountMsg}"
        accountQuickReplies.append({
            "action": "message",
            "label": accountLabel,
            "messageText": messageText
        })

    response = {
        "version": "2.0", 
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": chatbot_helper._selectInfo
                    }
                }
            ], 
            "quickReplies": accountQuickReplies
        }
    }
    # TODO : 함수 level3_autodesk_quickRepliesResponseFormat 로직 수정 예정 (2025.03.21 minjae)
    # 함수 len 사용하여 testQuick 배열 안에 존재하는 요소의 갯수가 0보다 큰경우
    # ----- if len(testQuick) > 0:
    #     response["template"]["quickReplies"] = testQuick
    return response

# level3 바로가기 그룹 전송 (카카오톡 서버로 텍스트 전송)
# 1. Autodesk 제품 설치 문의
def level3_autodesk_quickRepliesResponseFormat(autodeskInstBtnList):
    autodeskQuickReplies = []
    # 1. Autodesk 제품 설치 문의 버튼 텍스트 및 메세지 추가 
    for (autodeskInstLabel, autodeskInstMsg) in autodeskInstBtnList:
        # TODO : 파이썬 삼항 연산자 사용하여 버튼 텍스트 메시지 변수 messageText에 값 할당 기능 구현 (2025.03.28 minjae)
        # 참고 URL - https://wikidocs.net/20701
        # 파이썬 삼항 연산자 사용하여 버튼이 "Fusion", "DWGTrueView"일 경우 안내할 버전이 없으므로 값 f"{autodesk_helper._commandType} {autodeskInstMsg} {chatbot_helper._softwareInstMethod}" 할당
        messageText = f"{autodesk_helper._commandType} {autodeskInstMsg} {chatbot_helper._softwareInstMethod}" if autodesk_helper._fusion_Msg == autodeskInstMsg or autodesk_helper._dwgTrueView_Msg == autodeskInstMsg else autodeskInstMsg
        autodeskQuickReplies.append({
            "action": "message",
            "label": autodeskInstLabel,
            "messageText": messageText
        })
        
    response = {
        "version": "2.0", 
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": chatbot_helper._selectInfo
                    }
                }
            ], 
            "quickReplies": autodeskQuickReplies
        }
    }
    # TODO : 함수 level3_autodesk_quickRepliesResponseFormat 로직 수정 예정 (2025.03.21 minjae)
    # 함수 len 사용하여 testQuick 배열 안에 존재하는 요소의 갯수가 0보다 큰경우
    # ----- if len(testQuick) > 0:
    #     response["template"]["quickReplies"] = testQuick
    return response

# level3 텍스트 카드 (카카오톡 서버로 텍스트 전송)
# 2. 상상진화 BOX 제품 설치 문의
def level3_box_textCardResponseFormat(boxInstBtnList):
    boxInstButtons = []
    # 2. 상상진화 BOX 제품 설치 문의 3가지 버튼 텍스트 및 메세지 추가 
    for (boxInstLabel, boxInstMsg) in boxInstBtnList:
        # TODO : 파이썬 삼항 연산자 사용하여 버튼 텍스트 메시지 변수 messageText에 값 할당 기능 구현 (2025.03.28 minjae)
        # 참고 URL - https://wikidocs.net/20701
        # 파이썬 삼항 연산자 사용하여 버튼이 'CAD BOX', 'Energy BOX'일 경우 안내할 버전이 없으므로 값 f"{box_helper._commandType} {boxInstMsg} {chatbot_helper._softwareInstMethod}" 할당
        messageText = f"{box_helper._commandType} {boxInstMsg} {chatbot_helper._softwareInstMethod}" if box_helper._autoCADBOX_Msg == boxInstMsg or box_helper._energyBOX_Msg == boxInstMsg else boxInstMsg
        boxInstButtons.append({
            "action": "message",
            "label": boxInstLabel,
            "messageText": messageText
        })

    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "textCard": {
                        "title": "",
                        "description": chatbot_helper._selectInfo,
                        "buttons" : boxInstButtons
                    }
                }
            ],
            "quickReplies": []
        }
    }

    # TODO : 함수 level3_box_textCardResponseFormat 로직 수정 예정 (2025.03.05 minjae)
    # 함수 len 사용하여 testButtons 배열 안에 존재하는 요소의 갯수가 0보다 큰경우
    # ----- if len(testButtons) > 0:
    #     response["template"]["buttons"] = testButtons
    return response


# level4 바로가기 그룹 전송 (카카오톡 서버로 텍스트 전송)
# level4 - 1. Autodesk 제품 버전 Language Pack 
def level4_autodeskInstLangPackVer_quickRepliesResponseFormat(userRequest_Msg, autodeskInstLangPackVerBtnList):
    autodeskInstLangPackVerQuickReplies = []
    # level4 - 1. Autodesk 제품 버전 Language Pack 버튼 텍스트 및 메세지 추가 
    for (autodeskInstLangPackVerLabel, ver, langPack) in autodeskInstLangPackVerBtnList:
        autodeskInstLangPackVerQuickReplies.append({
            "action": "message",
            "label": autodeskInstLangPackVerLabel,
            "messageText": f"{autodesk_helper._commandType} {userRequest_Msg} {autodeskInstLangPackVerLabel} {ver} {langPack}"
        })

    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": chatbot_helper._selectVersion
                    }
                }
            ],
            "quickReplies": autodeskInstLangPackVerQuickReplies
        }
    }

    # TODO : 함수 level4_autodeskInstLangPackVer_quickRepliesResponseFormat 로직 수정 예정 (2025.03.05 minjae)
    # 함수 len 사용하여 testButtons 배열 안에 존재하는 요소의 갯수가 0보다 큰경우
    # ----- if len(testButtons) > 0:
    #     response["template"]["buttons"] = testButtons
    return response

# level4 바로가기 그룹 전송 (카카오톡 서버로 텍스트 전송)
# level4 - 1. Autodesk 제품 버전 
def level4_autodeskInstVer_quickRepliesResponseFormat(userRequest_Msg, autodeskInstVerBtnList):
    autodeskInstVerQuickReplies = []
    # level4 - 1. Autodesk 제품 버전 (Language Pack X) 버튼 텍스트 및 메세지 추가 
    for (autodeskInstVerLabel, ver) in autodeskInstVerBtnList:
        autodeskInstVerQuickReplies.append({
            "action": "message",
            "label": autodeskInstVerLabel,
            "messageText": f"{autodesk_helper._commandType} {userRequest_Msg} {autodeskInstVerLabel} {ver} {chatbot_helper._softwareInstMethod}"
        })

    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": chatbot_helper._selectVersion
                    }
                }
            ],
            "quickReplies": autodeskInstVerQuickReplies
        }
    }

    # TODO : 함수 level4_autodeskInstVer_textCardResponseFormat 로직 수정 예정 (2025.03.05 minjae)
    # 함수 len 사용하여 testButtons 배열 안에 존재하는 요소의 갯수가 0보다 큰경우
    # ----- if len(testButtons) > 0:
    #     response["template"]["buttons"] = testButtons
    return response

# level4 바로가기 그룹 전송 (카카오톡 서버로 텍스트 전송)
# level4 - 2. 상상진화 BOX 제품 버전 (1. Revit BOX만 해당)
def level4_boxInstVer_quickRepliesResponseFormat(userRequest_Msg, boxInstVerBtnList):
    boxInstVerQuickReplies = []
    # 2. 상상진화 BOX 제품 버전 (1. Revit BOX만 해당) 6가지 버튼 텍스트 및 메세지 추가 
    for (boxInstVerLabel, ver) in boxInstVerBtnList:
        boxInstVerQuickReplies.append({
            "action": "message",
            "label": boxInstVerLabel,
            "messageText": f"{box_helper._commandType} {userRequest_Msg} {boxInstVerLabel} {ver} {chatbot_helper._softwareInstMethod}"
        })

    response = {
        "version": "2.0", 
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": chatbot_helper._selectVersion
                    }
                }
            ], 
            "quickReplies": boxInstVerQuickReplies
        }
    }
    # TODO : 함수 level4_boxInstVer_quickRepliesResponseFormat 로직 수정 예정 (2025.03.21 minjae)
    # 함수 len 사용하여 testQuick 배열 안에 존재하는 요소의 갯수가 0보다 큰경우
    # ----- if len(testQuick) > 0:
    #     response["template"]["quickReplies"] = testQuick
    return response

# level5 텍스트 카드 (카카오톡 서버로 텍스트 전송)
# level5 - 1. Autodesk 제품 설치 언어
def level5_autodeskInstLang_textCardResponseFormat(userRequest_Msg, autodeskInstLangBtnList):
    autodeskInstLangButtons = []
    # level5 - 1. Autodesk 제품 설치 언어 버튼 텍스트 및 메세지 추가 
    for autodeskInstLangLabel in autodeskInstLangBtnList:
        autodeskInstLangButtons.append({
            "action": "message",
            "label": autodeskInstLangLabel,
            "messageText": f"{userRequest_Msg} {autodeskInstLangLabel} {chatbot_helper._softwareInstMethod}"
        })

    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "textCard": {
                        "title": "",
                        "description": chatbot_helper._selectLang,
                        "buttons" : autodeskInstLangButtons
                    }
                }
            ],
            "quickReplies": []
        }
    }

    # TODO : 함수 level5_autodeskInstLang_textCardResponseFormat 로직 수정 예정 (2025.03.05 minjae)
    # 함수 len 사용하여 testButtons 배열 안에 존재하는 요소의 갯수가 0보다 큰경우
    # ----- if len(testButtons) > 0:
    #     response["template"]["buttons"] = testButtons
    return response