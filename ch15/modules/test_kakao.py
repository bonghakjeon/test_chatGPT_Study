from commons import chatbot_helper   # 폴더 "commons" -> 카카오 챗봇 전용 도움말 텍스트 "chatbot_helper" 불러오기

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