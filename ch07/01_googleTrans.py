# 가상환경 폴더 "ch07_env" 생성 터미널 명령어
# python -m venv ch07_env

# 가상환경 폴더 "ch07_env" 활성화 터미널 명령어
# ch07_env\Scripts\activate.bat

# 구글 번역기 파이썬 오픈소스 패키지 googletrans
# 참고 URL - https://pypi.org/project/googletrans/

# 구글 번역기 파이썬 오픈소스 패키지 googletrans
# 터미널 설치 명령어
# pip install googletrans==3.1.0a0
# 구글 번역기 파이썬 오픈소스 패키지 googletrans 의 경우 따로 API 키 발급이 필요 없다.
from googletrans import Translator # 패키지 googletrans에서 Translator 클래스 가져오기 

def google_trans(messages):
    google = Translator() # Translator 클래스 인스턴스 google 생성 
    # 함수 google.translate 사용해서 번역하고자 하는 메시지(messages)를
    # 해당 함수의 첫번째 파라미터로 전달하고
    # 번역을 하고 싶은 언어를 해당 함수의 두번째 파라미터로 전달 
    # 영어 -> 한글로 번역하고자 하면 dest="ko" 라고 두번째 파라미터로 전달한다.
    result = google.translate(messages, dest="ko")

    # 영어 -> 한글로 번역한 결과 result.text 리턴 
    return result.text

# 변수 text에 영어 -> 한글로 번역하고자 하는 메시지 담기 
text ="GPT-4 is more creative and collaborative than ever before. It can generate, edit, and iterate with users on creative and technical writing tasks, such as composing songs, writing screenplays, or learning a user??s writing style."

# 함수 google_trans 호출시 변수 text를 인자로 전달 
result = google_trans(text)
print(result) # 영어 -> 한글로 번역 결과 화면에 데이터 출력 