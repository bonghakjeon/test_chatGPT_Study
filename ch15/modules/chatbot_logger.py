"""
# 로그 레벨 종류 
|   Level   |   Value   |   When to use
|   DEBUG   |     10    | (주로 문제 해결을 할때 필요한) 자세한 정보. - 개발 과정에서 오류 원인 파악하고자 할 때 사용
|   INFO    |     20    | 작업이 정상적으로 작동하고 있다는 메시지. 
|  WARNING  |     30    | 예상하지 못한 일이 발생하거나, 발생 가능한 문제점을 명시. (e.g 'disk space low') 작업은 정상적으로 진행.
|   ERROR   |     40    | 프로그램이 함수를 실행하지 못 할 정도의 심각한 문제.
| CRICTICAL |     50    | 프로그램이 동작할 수 없을 정도의 심각한 문제. 
"""

import inspect
import os   # 함수 log_write 호출한 상위 파일 이름 구해야 해서 패키지 "os" 불러오기
from datetime import datetime


# 로그 레벨 작성
debug = 'debug'
info = 'info'
warning = 'warning'
error = 'error'
crictical = 'crictical'

# 아마존 웹서비스(AWS) 람다 함수(Lambda Funtion) 카카오 챗봇 로그 작성 
def log_write(log_type, content, bot_res):
    # 현재 날짜/시간 구하기
    # TODO : 날짜와 시간을 특정 포맷으로 출력하기 구현 (2025.03.27 minjae)
    # 참고 URL - https://wikidocs.net/269063
    current_time = datetime.now()
    formatted_current_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    # 현재 함수 openai_log_write 호출하는 상위 파일명 가져오기 
    # 참고 URL - https://docs.python.org/ko/3.8/library/inspect.html
	# 참고 2 URL - https://louky0714.tistory.com/144
    # 참고 3 URL - https://wikidocs.net/3717
    current_filepath = inspect.currentframe().f_back.f_code.co_filename
    current_filename = os.path.basename(current_filepath)

    # 현재 함수 openai_log_write 호출하는 상위 함수명 가져오기
    # 참고 URL - https://docs.python.org/ko/3.8/library/inspect.html
    # 참고 2 URL - https://louky0714.tistory.com/144    
    current_function_name = inspect.currentframe().f_back.f_code.co_name

    # 현재 함수 openai_log_write 호출하는 상위 파일 라인번호(라인위치) 가져오기 
    # 참고 URL - https://docs.python.org/ko/3.8/library/inspect.html
    current_lineno = inspect.currentframe().f_back.f_lineno

    print("[Chatbot] [%s] [%s] [%s | %s - L%s] : %s - %s" %(log_type, formatted_current_time, current_filename, current_function_name, current_lineno, content, bot_res))