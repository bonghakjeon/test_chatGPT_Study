###### 기능 구현 단계 #######
# 카카오톡 챗봇 프로그램을 구동하는데 필요한 모든 기능 함수화 해서
# 파이썬 스크립트 파일(01_kakaobot_Lambda.py)에 속한 
# 메인 함수 "lambda_handler" -> 답변/사진 요청 및 응답 확인 함수 "responseOpenAI"에서 사용할 수 있도록 정리 

# 오류 메세지 전송 (카카오톡 서버로 텍스트 전송)
# 오류 발생시 카카오톡 서버로 오류 메시지 전송 전용 JSON 형태(Format)의 데이터로 전달하기 위한 함수
# 카카오톡 채팅방에 보낼 메시지를 매개변수 errorMessage에 input으로 받기(인자로 전달)
def errorTextResponseFormat(errorMessage):
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
def level1textCardResponseFormat():
    # TODO : 함수 level1textCardResponseFormat 로직 수정 예정 (2025.03.05 minjae)
    # ----- # TODO : 바로 아래 소스코드는 파이썬 스크립트 파일 "D:\minjae\test_BotProject\05.카카오톡\04-kakao-money.py" -> 함수 "get_exchange_from_won"의 로직을 참고 하여 구현함 (2025.03.04 minjae)
    # ----- testButtons = []
    # ----- for test in testButtonList:
    #     testButtons.append({
    #         "action": "message",
    #         "label": f"{test}",
    #         "messageText": f"[구현 예정!] {test}"
    #     })
        
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "textCard": {
                        "title": "[상담시간 안내]",
                        "description": "▶ 기술지원문의\n월~금요일: 오전 9시 ~ 오후 6시\n주말, 공휴일: 휴무",
                        "buttons": [
                            {
                                "action": "message",
                                "label": "1. 제품 설치파일 문의",
                                "messageText": "1. 제품 설치파일 문의"
                            },
                            {
                                "action": "message",
                                "label": "2. 네트워크 라이선스",
                                "messageText": "2. 네트워크 라이선스"
                            },
                            {
                                "action": "message",
                                "label": "3. 계정&제품배정 문의",
                                "messageText": "3. 계정&제품배정 문의"
                            }
                        ]
                    }
                }
            ],
            "quickReplies": []
        }
    }
    # TODO : 함수 level1textCardResponseFormat 로직 수정 예정 (2025.03.05 minjae)
    # 함수 len 사용하여 testButtons 배열 안에 존재하는 요소의 갯수가 0보다 큰경우
    # ----- if len(testButtons) > 0:
    #     response["template"]["buttons"] = testButtons

    return response

# level2 바로가기 그룹 전송 (카카오톡 서버로 텍스트 전송)
# 1. 제품 설치파일 문의
def level2InstallerquickRepliesResponseFormat(messageTextAutoDesk, messageTextRevit):
    # TODO : 함수 level2InstallerquickRepliesResponseFormat 로직 수정 예정 (2025.03.05 minjae)
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
                        "text": "안내가 필요한 항목을 선택해주세요."
                    }
                }
            ], 
            "quickReplies": [
                {
                    "action": "message",
                    "label": "1. 오토캐드",
                    "messageText": f"{messageTextAutoDesk}"
                },
                {
                    "action": "message",
                    "label": "2. 레빗",
                    "messageText": f"{messageTextAutoDesk}"
                },
                {
                    "action": "message",
                    "label": "3. 나비스웍스",
                    "messageText": f"{messageTextAutoDesk}"
                },
                {
                    "action": "message",
                    "label": "4. Civil 3D",
                    "messageText": f"{messageTextAutoDesk}"
                },
                {
                    "action": "message",
                    "label": "5. CADBOX",
                    "messageText": f"[구현 예정!] 5. CADBOX"
                },
                {
                    "action": "message",
                    "label": "6. RevitBOX",
                    "messageText": f"{messageTextRevit}"
                },
                {
                    "action": "message",
                    "label": "7. EnergyBOX",
                    "messageText": f"[구현 예정!] 7. EnergyBOX"
                },
                {
                    "action": "message",
                    "label": "8. DWGTrueView",
                    "messageText": f"[구현 예정!] 8. DWGTrueView"
                },
                {
                    "action": "message",
                    "label": "9. 레빗->나비스웍스",
                    "messageText": f"{messageTextRevit}"
                },
                {
                    "action": "message",
                    "label": "10. 레빗 라이브러리",
                    "messageText": f"{messageTextRevit}"
                }
            ]
        }
    }

    # TODO : 함수 level2InstallerquickRepliesResponseFormat 로직 수정 예정 (2025.03.05 minjae)
    # 함수 len 사용하여 testQuick 배열 안에 존재하는 요소의 갯수가 0보다 큰경우
    # ----- if len(testQuick) > 0:
    #     response["template"]["quickReplies"] = testQuick
    return response

# level2 바로가기 그룹 전송 (카카오톡 서버로 텍스트 전송)
# 2. 네트워크 라이선스
def level2NetworkquickRepliesResponseFormat():
    # TODO : 함수 level2NetworkquickRepliesResponseFormat 로직 수정 예정 (2025.03.05 minjae)
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
                        "text": "안내가 필요한 항목을 선택해주세요."
                    }
                }
            ], 
            "quickReplies": [
                {
                    "action": "message",
                    "label": "1. 상상정보통 다운로드",
                    "messageText": "[구현 예정!] 1. 상상정보통 다운로드"
                },
                {
                    "action": "message",
                    "label": "2. 체크아웃 시간 초과",
                    "messageText": "[구현 예정!] 2. 체크아웃 시간 초과"
                },
                {
                    "action": "message",
                    "label": "3. -4,132,0 오류",
                    "messageText": "[구현 예정!] 3. -4,132,0 오류"
                },
                {
                    "action": "message",
                    "label": "4. 0,0,0 오류",
                    "messageText": "[구현 예정!] 4. 0,0,0 오류"
                },
                {
                    "action": "message",
                    "label": "5. -15,570,0오류",
                    "messageText": "[구현 예정!] 5. -15,570,0오류"
                },
                {
                    "action": "message",
                    "label": "6. 라이센싱 에러 조치",
                    "messageText": "[구현 예정!] 6. 라이센싱 에러 조치"
                },
                {
                    "action": "message",
                    "label": "7. 라이선스 매니저 오류",
                    "messageText": "[구현 예정!] 7. 라이선스 매니저 오류"
                },
                {
                    "action": "message",
                    "label": "8. FlexNet 창 발생",
                    "messageText": "[구현 예정!] 8. FlexNet 창 발생"
                },
                {
                    "action": "message",
                    "label": "9. 라이선스 유형 변경",
                    "messageText": "[구현 예정!] 9. 라이선스 유형 변경"
                },
                {
                    "action": "message",
                    "label": "10. 기타 문의",
                    "messageText": "[구현 예정!] 10. 기타 문의"
                }
            ]
        }
    }

    # TODO : 함수 level2NetworkquickRepliesResponseFormat 로직 수정 예정 (2025.03.05 minjae)
    # 함수 len 사용하여 testQuick 배열 안에 존재하는 요소의 갯수가 0보다 큰경우
    # ----- if len(testQuick) > 0:
    #     response["template"]["quickReplies"] = testQuick
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
                        "text": "안내가 필요한 항목을 선택해주세요."
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
                        "text": "버전을 선택해주세요."
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
                            }
                        ]
                    }
                }
            ],
            "quickReplies": []
        }
    }
    return response