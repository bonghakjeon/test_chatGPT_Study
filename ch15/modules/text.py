# TEXT 파일 전용 모듈

import os   # 파일 존재 여부 확인해야 해서 패키지 "os" 불러오기
from modules import chatbot_logger   # 폴더 "modules" -> 카카오 챗봇 로그 작성 모듈 "chatbot_logger" 불러오기

# TEXT 파일에 작성된 모든 텍스트 가져오기 
def getResponseFromText(filepath):
    # 해당 경로에 TEXT 파일 존재하는 경우 
    # 참고 URL - https://wikidocs.net/14304
    # 참고 2 URL - https://wikidocs.net/256287
    if True == os.path.exists(filepath):
        # TEXT 파일에 작성된 모든 텍스트 가져오기
        # with 문 사용해서 TEXT 파일 자동으로 열고(open) 닫기(close)
        # 참고 URL - https://wikidocs.net/26
        with open(filepath, "r") as file:
            response = file.read()
            chatbot_logger.log_write(chatbot_logger._info, "TEXT 파일에 작성된 모든 텍스트", response)
    # 해당 경로에 PDF 파일 존재 안 하는 경우
    else: 
        response = ''
        chatbot_logger.log_write(chatbot_logger._info, "TEXT 파일 존재 안 함.", response)

    return response