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

""""""

print("Hello World")  # 콘솔창에 문자열 "Hello World" 출력 

"""
import logging  # 로깅 함수 호출

​1. instance 설정 - log(로그) instance 설정
2. formatter 생성 - log(로그)를 저장(작성/기록)할 포맷(format) 지정 
3. handler 생성 - log(로그)를 담을 수 있는 핸들러(handler) 생성 (log(로그)를 콘솔창에 출력 할건지? 아니면 파일에 저장 할건지? 이런 저장하는 핸들러(handler) 생성하기)
4. handler에 formatter 지정 - 2번에서 지정한 포맷(format)을 핸들러(handler)에 지정
5. 입력받는 instance에 handler 추가 - 4번에서 지정한 포맷(format)을 핸들러(handler)에 지정한 이후 해당 핸들러(handler)를 log(로그) instance에 추가하여 "입력받는 값"을 핸들러(콘솔 또는 파일)로 가져올 수 있도록 또 설정하기 
6. 기록할 log level 지정 - 로그 레벨 지정 (DEBUG, INFO, WARNING, ERROR, CRICTICAL)
7. log 함수 선 호출 - 아래에 구현한 함수 log() 선호출  
8. log 기록 - 원하는 지점에 로그 기록하기 
"""

"""
# 로그 포맷(format) formatter
|     이름    |   포멧           |   설명   |
| asctime     | %(asctime)s     | 날짜 시간, ex) 2021.04.10 11:21:48,162
| created     | %(created)f     | 생성 시간 출력
| filename    | %(filename)s    | 파일명
| funcName    | %(funcName)s    | 함수명
| levelname   | %(levelname)s   | 로그 레벨(DEBUG, INFO, WARNING, ERROR, CRITICAL)
| levelno     | %(levelno)s     | 로그 레벨을 수치화해서 출력(10, 20, 30, …)
| lineno      | %(lineno)d      | 소스의 라인 넘버
| module      | %(module)s      | 모듈 이름
| msecs       | %(msecs)d       | 로그 생성 시간에서 밀리세컨드 시간 부분만 출력
| message     | %(message)s     | 로그 메시지
| name        | %(name)s        | 로그 이름
| pathname    | %(pathname)s    | 소스 경로
| process     | %(process)d     | 프로세스(Process) ID
| processName | %(processName)s | 프로세스 이름
| thread      | %(thread)d      | Thread ID
| threadName  | %(threadName)s  | Thread Name

"""

"""
# 로그 레벨 종류 
|   Level   |   Value   |   When to use
|   DEBUG   |     10    | (주로 문제 해결을 할때 필요한) 자세한 정보. - 개발 과정에서 오류 원인 파악하고자 할 때 사용
|   INFO    |     20    | 작업이 정상적으로 작동하고 있다는 메시지. 
|  WARNING  |     30    | 예상하지 못한 일이 발생하거나, 발생 가능한 문제점을 명시. (e.g 'disk space low') 작업은 정상적으로 진행.
|   ERROR   |     40    | 프로그램이 함수를 실행하지 못 할 정도의 심각한 문제.
| CRICTICAL |     50    | 프로그램이 동작할 수 없을 정도의 심각한 문제. 
"""

# 1~7 까지는 복붙해 두고,
# 8만 Log 남기고 싶은 부분에 추가하여 사용

# Logging 모듈은 파이썬 기본 라이브러리 중 하나로 콘솔에 출력할 뿐만 아니라 파일 형태로 로그를 생성 할 수 있습니다.
import logging
import time

def log():
    # Logging 모듈은 파이썬 기본 라이브러리 중 하나로 콘솔에 출력할 뿐만 아니라 파일 형태로 로그를 생성 할 수 있습니다.
    # import logging

    # 1. logger instance 설정 - logger의 이름(__name__)을 명시해서 logger instance 설정하기 
    logger = logging.getLogger(__name__)

    # 2. formatter 생성 (로그 작성/출력/저장에 사용할 날짜 + 로그 메시지)
    # 로그 기록 포맷(format) 예시 - [2025-03-06 10:53:33]
    # formatter = logging.Formatter('[%(asctime)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    formatter = logging.Formatter('[%(asctime)s] %(filename)s %(funcName)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    # 3. handler 생성(설정) (streamHandler : 콘솔 출력용 // fileHandler : 파일 기록용)
    streamHandler = logging.StreamHandler()
    fileHandler = logging.FileHandler("server.log")           # 로그를 기록할 파일 이름(경로) "server.log" 지정 (파일 이름은 다른 것으로 변경해도 된다.)
    # fileHandler = logging.FileHandler("botlog.txt")         # 로그를 기록할 파일 이름(경로) "botlog.txt" 지정 (파일 이름은 다른 것으로 변경해도 된다.)
    # fileHandler = logging.FileHandler("/tmp/botlog.txt")    # 로그를 기록할 파일 이름(경로) "/tmp/botlog.txt" 지정 (파일 이름은 다른 것으로 변경해도 된다.)

    # 4. logger instance에 formatter 설정(할당) (각각의 Handler에 formatter 설정 적용)
    streamHandler.setFormatter(formatter)
    fileHandler.setFormatter(formatter)

    # 5. logger instance(logger)에 handler 추가 (addHandler) (입력받는 log에 handler 사용)
    logger.addHandler(streamHandler)
    logger.addHandler(fileHandler)

    # 6. 기록할 로그 레벨(log level) 지정하기 - DEBUG 로그(level=logging.DEBUG)는 로그 레벨(log level) 중 가장 낮은 레벨(level)이다.
    logger.setLevel(level=logging.DEBUG)    # INFO 레벨로 지정하면, INFO 레벨보다 낮은 DEBUG 로그는 무시함.
                                            # Python의 기본 logging 시스템의 레벨은 WARNING으로 설정되어 있음.
                                            # 따라서 특별한 설정을 하지 않으면, WARNING 레벨 이상만 기록됨. (WARNING 레벨보다 낮은 로그들은 무시하고 콘솔창 또는 파일에 기록되지 않음.)

    # 설정된 log setting 반환 - setting 완료된(설정 완료된) logger instance "logger" 반환
    return logger

# 7. log 함수 선 호출 (함수를 한번만 호출해 놓으면, 이후에 logger.debug("메시지") 형식으로 필요 시마다 간단하게 로그를 기록할 수 있음.
logger=log()

def test():
    logger.info("==========TEST INFO==========")
    logger.warning("==========TEST WARNING==========")
    logger.error("==========TEST ERROR==========")
    logger.critical("==========TEST CRITICAL==========")

# test()

# 8. log 기록
# 프로그램 시작 시간 기록 - (콘솔창 + 파일 모두 기록)
logger.debug("==========PROGRAM START==========")

for i in range(1, 10):
    print(i)
    time.sleep(1)   # 1초 대기
    if i == 5:  # 변수 i에 저장된 값이 5인 경우
        logger.debug("5th number has been passed!!")   # DEBUG 로그 기록 로그 내용 한글 번역 "5번째 숫자를 지났다!!"

# logger.info("==========TEST INFO==========")
# logger.warning("==========TEST WARNING==========")
# logger.error("==========TEST ERROR==========")
# logger.critical("==========TEST CRITICAL==========")

# 프로그램 종료 시간 기록 - (콘솔창 + 파일 모두 기록)
logger.debug("==========PROGRAM FINISH==========")