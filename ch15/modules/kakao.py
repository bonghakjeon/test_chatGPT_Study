###### 기능 구현 단계 #######
# 카카오톡 챗봇 프로그램을 구동하는데 필요한 모든 기능 함수화 해서
# 파이썬 스크립트 파일(01_kakaobot_Lambda.py)에 속한 
# 메인 함수 "lambda_handler" -> 답변/사진 요청 및 응답 확인 함수 "responseOpenAI"에서 사용할 수 있도록 정리 

from commons import autodesk_helper  # 폴더 "commons" -> 1. Autodesk 제품 전용 도움말 텍스트 "autodesk_helper" 불러오기
from commons import box_helper       # 폴더 "commons" -> 2. 상상진화 BOX 제품 전용 도움말 텍스트 "box_helper" 불러오기
from commons import chatbot_helper   # 폴더 "commons" -> 카카오 챗봇 전용 도움말 텍스트 "chatbot_helper" 불러오기

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

# level1 텍스트 카드 (카카오톡 서버로 텍스트 전송)
# 상담시간 안내
def level1_textCardResponseFormat(level1ButtonList):
    level1Buttons = []
    # 상담시간 안내 3가지 버튼 텍스트 및 메세지 추가 
    for level1Button in level1ButtonList:
        level1Buttons.append({
            "action": "message",
            "label": level1Button,
            "messageText": level1Button
        })
        
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "textCard": {
                        "title": "[상담시간 안내]",
                        "description": "▶ 기술지원문의\n월~금요일: 오전 9시 ~ 오후 6시\n주말, 공휴일: 휴무",
                        "buttons": level1Buttons
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
def level2_textCardResponseFormat(userRequest_Msg, level2ButtonList):
    level2Buttons = []
    # 상담유형 안내 버튼 텍스트 및 메세지 추가 
    for level2Button in level2ButtonList:
        level2Buttons.append({
            "action": "message",
            "label": level2Button,
            "messageText": f"{userRequest_Msg} {level2Button}"
        })
        
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "textCard": {
                        "title": "상담 유형",
                        "description": chatbot_helper._selectInfo,
                        "buttons" : level2Buttons
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

# level3 바로가기 그룹 전송 (카카오톡 서버로 텍스트 전송)
# 1. Autodesk 제품 설치 문의
def level3_autodesk_quickRepliesResponseFormat(autodeskInstButtonList):
    autodeskQuickReplies = []
    # 1. Autodesk 제품 설치 문의 버튼 텍스트 및 메세지 추가 
    for autodeskInstButton in autodeskInstButtonList:
        # TODO : 파이썬 삼항 연산자 사용하여 버튼 텍스트 메시지 변수 messageText에 값 할당 기능 구현 (2025.03.28 minjae)
        # 참고 URL - https://wikidocs.net/20701
        # 파이썬 삼항 연산자 사용하여 버튼이 "10. Fusion", "13. DWGTrueView"일 경우 안내할 버전이 없으므로 값 f"{autodesk_helper._brandName} {autodeskInstButton} {chatbot_helper._softwareInstMethod}" 할당
        messageText = f"{autodesk_helper._brandName} {autodeskInstButton} {chatbot_helper._softwareInstMethod}" if autodesk_helper._fusion == autodeskInstButton or autodesk_helper._dwgTrueView == autodeskInstButton else autodeskInstButton
        autodeskQuickReplies.append({
            "action": "message",
            "label": autodeskInstButton,
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
def level3_box_textCardResponseFormat(boxInstButtonList):
    boxInstButtons = []
    # 2. 상상진화 BOX 제품 설치 문의 3가지 버튼 텍스트 및 메세지 추가 
    for boxInstButton in boxInstButtonList:
        # TODO : 파이썬 삼항 연산자 사용하여 버튼 텍스트 메시지 변수 messageText에 값 할당 기능 구현 (2025.03.28 minjae)
        # 참고 URL - https://wikidocs.net/20701
        # 파이썬 삼항 연산자 사용하여 버튼이 '2. CAD BOX', '3. Energy BOX'일 경우 안내할 버전이 없으므로 값 f"{box_helper._brandName} {boxInstButton} {chatbot_helper._softwareInstMethod}" 할당
        messageText = f"{box_helper._brandName} {boxInstButton} {chatbot_helper._softwareInstMethod}" if box_helper._autoCADBOX == boxInstButton or box_helper._energyBOX == boxInstButton else boxInstButton
        boxInstButtons.append({
            "action": "message",
            "label": boxInstButton,
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


# level3 바로가기 그룹 전송 (카카오톡 서버로 텍스트 전송)
# 3. 계정&제품배정 문의
def level3_account_quickRepliesResponseFormat(accountButtonList):
    accountQuickReplies = []
    # 3. 계정&제품배정 문의 10가지 버튼 텍스트 및 메세지 추가 
    for accountButton in accountButtonList:
        accountQuickReplies.append({
            "action": "message",
            "label": accountButton,
            "messageText": accountButton
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


# level4 텍스트 카드 (카카오톡 서버로 텍스트 전송)
# level4 - 1. Autodesk 제품 버전 Language Pack 
def level4_autodeskInstLangPackVer_textCardResponseFormat(userRequest_Msg, autodeskInstLangPackVerButtonList):
    autodeskInstLangPackVerButtons = []
    # level4 - 1. Autodesk 제품 버전 Language Pack 버튼 텍스트 및 메세지 추가 
    for (autodeskInstLangPackVerButton, ver, langPack) in autodeskInstLangPackVerButtonList:
        autodeskInstLangPackVerButtons.append({
            "action": "message",
            "label": autodeskInstLangPackVerButton,
            "messageText": f"{autodesk_helper._brandName} {userRequest_Msg} {autodeskInstLangPackVerButton} {ver} {langPack}"
        })

    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "textCard": {
                        "title": "",
                        "description": chatbot_helper._selectVersion,
                        "buttons" : autodeskInstLangPackVerButtons
                    }
                }
            ],
            "quickReplies": []
        }
    }

    # TODO : 함수 level4_autodeskInstLangPackVer_textCardResponseFormat 로직 수정 예정 (2025.03.05 minjae)
    # 함수 len 사용하여 testButtons 배열 안에 존재하는 요소의 갯수가 0보다 큰경우
    # ----- if len(testButtons) > 0:
    #     response["template"]["buttons"] = testButtons
    return response

# level4 텍스트 카드 (카카오톡 서버로 텍스트 전송)
# level4 - 1. Autodesk 제품 버전 
def level4_autodeskInstVer_textCardResponseFormat(userRequest_Msg, autodeskInstVerButtonList):
    autodeskInstVerButtons = []
    # level4 - 1. Autodesk 제품 버전 (Language Pack X) 버튼 텍스트 및 메세지 추가 
    for (autodeskInstVerButton, ver) in autodeskInstVerButtonList:
        autodeskInstVerButtons.append({
            "action": "message",
            "label": autodeskInstVerButton,
            "messageText": f"{autodesk_helper._brandName} {userRequest_Msg} {autodeskInstVerButton} {ver} {chatbot_helper._softwareInstMethod}"
        })

    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "textCard": {
                        "title": "",
                        "description": chatbot_helper._selectVersion,
                        "buttons" : autodeskInstVerButtons
                    }
                }
            ],
            "quickReplies": []
        }
    }

    # TODO : 함수 level4_autodeskInstVer_textCardResponseFormat 로직 수정 예정 (2025.03.05 minjae)
    # 함수 len 사용하여 testButtons 배열 안에 존재하는 요소의 갯수가 0보다 큰경우
    # ----- if len(testButtons) > 0:
    #     response["template"]["buttons"] = testButtons
    return response

# level4 바로가기 그룹 전송 (카카오톡 서버로 텍스트 전송)
# level4 - 2. 상상진화 BOX 제품 버전 (1. Revit BOX만 해당)
def level4_boxInstVer_quickRepliesResponseFormat(userRequest_Msg, boxInstVerButtonList):
    boxInstVerQuickReplies = []
    # 2. 상상진화 BOX 제품 버전 (1. Revit BOX만 해당) 6가지 버튼 텍스트 및 메세지 추가 
    for (boxInstVerButton, ver) in boxInstVerButtonList:
        boxInstVerQuickReplies.append({
            "action": "message",
            "label": boxInstVerButton,
            "messageText": f"{box_helper._brandName} {userRequest_Msg} {boxInstVerButton} {ver} {chatbot_helper._softwareInstMethod}"
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
def level5_autodeskInstLang_textCardResponseFormat(userRequest_Msg, autodeskInstLangButtonList):
    autodeskInstLangButtons = []
    # level5 - 1. Autodesk 제품 설치 언어 버튼 텍스트 및 메세지 추가 
    for autodeskInstLangButton in autodeskInstLangButtonList:
        autodeskInstLangButtons.append({
            "action": "message",
            "label": autodeskInstLangButton,
            "messageText": f"{userRequest_Msg} {autodeskInstLangButton} {chatbot_helper._softwareInstMethod}"
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

# level2 바로가기 그룹 전송 (카카오톡 서버로 텍스트 전송)
# 3. 계정&제품배정 문의
def level2AccountquickRepliesResponseFormat():
    # TODO : 함수 level2AccountquickRepliesResponseFormat 로직 수정 예정 (2025.03.05 minjae)
    # TODO : 바로 아래 소스코드는 파이썬 스크립트 파일 "D:\minjae\test_BotProject\05.카카오톡\04-kakao-money.py" -> 함수 "get_exchange_from_won"의 로직을 참고 하여 구현함 (2025.03.04 minjae)
    # ----- testQuick = []
    # ----- for test in testList:
    #     testQuick.append({
    #         "action": "message",
    #         "label": f"{test}",
    #         "messageText": f"[구현 예정!] {test}"
    #     })

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
            "quickReplies": [
                {
                    "action": "message",
                    "label": "1. 오토데스크 계정 생성",
                    "messageText": "[구현 예정!] 1. 오토데스크 계정 생성"
                },
                {
                    "action": "message",
                    "label": "2. 계정 비밀번호 분실",
                    "messageText": "[구현 예정!] 2. 계정 비밀번호 분실"
                },
                {
                    "action": "message",
                    "label": "3. 사용가능 제품확인",
                    "messageText": "[구현 예정!] 3. 사용가능 제품확인"
                },
                {
                    "action": "message",
                    "label": "4. 신규인원 제품배정",
                    "messageText": "[구현 예정!] 4. 신규인원 제품배정"
                },
                {
                    "action": "message",
                    "label": "5. 기존인원 제품제거",
                    "messageText": "[구현 예정!] 5. 기존인원 제품제거"
                },
                {
                    "action": "message",
                    "label": "6. 사용자 그룹관리 안내",
                    "messageText": "[구현 예정!] 6. 사용자 그룹관리 안내"
                },
                {
                    "action": "message",
                    "label": "7. 만료일 계약내역 확인",
                    "messageText": "[구현 예정!] 7. 만료일 계약내역 확인"
                },
                {
                    "action": "message",
                    "label": "8. 관리자 역할 재지정",
                    "messageText": "[구현 예정!] 8. 관리자 역할 재지정"
                },
                {
                    "action": "message",
                    "label": "9. 사용량 보고서 확인",
                    "messageText": "[구현 예정!] 9. 사용량 보고서 확인"
                },
                {
                    "action": "message",
                    "label": "10. 기타 문의",
                    "messageText": "[구현 예정!] 10. 기타 문의"
                }
            ]
        }
    }
    # TODO : 함수 level2AccountquickRepliesResponseFormat 로직 수정 예정 (2025.03.05 minjae)
    # 함수 len 사용하여 testQuick 배열 안에 존재하는 요소의 갯수가 0보다 큰경우
    # ----- if len(testQuick) > 0:
    #     response["template"]["quickReplies"] = testQuick
    return response

# level3 바로가기 그룹 전송 (카카오톡 서버로 텍스트 전송)
# AutoDesk 제품 또는 레빗 버전 선택
def level3VersionquickRepliesResponseFormat(messageText):
    # TODO : 함수 level3VersionquickRepliesResponseFormat 로직 수정 예정 (2025.03.05 minjae)
    # TODO : 바로 아래 소스코드는 파이썬 스크립트 파일 "D:\minjae\test_BotProject\05.카카오톡\04-kakao-money.py" -> 함수 "get_exchange_from_won"의 로직을 참고 하여 구현함 (2025.03.04 minjae)
    # ----- testQuick = []
    # ----- for test in testList:
    #     testQuick.append({
    #         "action": "message",
    #         "label": f"{test}",
    #         "messageText": f"[구현 예정!] {test}"
    #     })

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
            "quickReplies": [
                {
                    "action": "message",
                    "label": "2022",
                    "messageText": f"{messageText}"
                },
                {
                    "action": "message",
                    "label": "2023",
                    "messageText": f"{messageText}"
                },
                {
                    "action": "message",
                    "label": "2024",
                    "messageText": f"{messageText}"
                },
                {
                    "action": "message",
                    "label": "2025",
                    "messageText": f"{messageText}"
                }
            ]
        }
    }
    # TODO : 함수 level3VersionquickRepliesResponseFormat 로직 수정 예정 (2025.03.05 minjae)
    # 함수 len 사용하여 testQuick 배열 안에 존재하는 요소의 갯수가 0보다 큰경우
    # ----- if len(testQuick) > 0:
    #     response["template"]["quickReplies"] = testQuick
    return response

# level4 텍스트 카드 (카카오톡 서버로 텍스트 전송)
# 설치언어 선택
def level4LanguagetextCardResponseFormat(messageTextKor, messageTextEng):
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "textCard": {
                        "title": "",
                        "description": "설치 언어를 선택해주세요",
                        "buttons": [
                            {
                                "action": "message",
                                "label": "한국어",
                                "messageText": f"[구현 예정!] {messageTextKor}"
                            },
                            {
                                "action": "message",
                                "label": "English",
                                "messageText": f"[구현 예정!] {messageTextEng}"
                            },
                            {
                                "action": "message",
                                "label": "PDF 테스트",
                                "messageText": "[PDF 테스트]\n" + 
                                               "Revit 한국어 프로그램 설치 방법 확인하시려면\n" + 
                                               "아래 URL 클릭하세요.\n" + 
                                               "https://damassets.autodesk.net/content/dam/autodesk/www/campaigns/AEC-KR-Test-Drive-BIM-Program/fy15-aec-test-drive-bim-interoperability-guide-ko.pdf"
                            }
                        ]
                    }
                }
            ],
            "quickReplies": []
        }
    }
    return response