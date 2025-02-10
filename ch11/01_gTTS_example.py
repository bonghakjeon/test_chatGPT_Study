# 가상환경 폴더 "ch11_env" 생성 터미널 명령어
# python -m venv ch11_env

# 가상환경 폴더 "ch11_env" 활성화 터미널 명령어
# ch11_env\Scripts\activate.bat

# 나만의 음성비서 프로그램 실행 구조 
# 1. 사용자에게 음성 파일 입력받기 
# 2. OpenAI API Whisper라는 모델 사용하여 
#    사용자에게 입력받은 음성 파일을 텍스트로 변환 
# 3. 텍스트로 변환된 질문은 ChatGPT에게 프롬프트로 입력
# 4. ChatGPT가 텍스트 형태로 답변 
# 5. 마지막으로 ChatGPT에게 답변받은 텍스트는 구글 Translate의 TTS 서비스 API 사용하여
#    다시 음성 파일로 변환 -> 최종적으로 Streamlit 으로 구현한 웹브라우저 화면에서 음성 파일로 소리가 재생

# 파이썬 스크립트 파일 "01_gTTS_example.py" 터미널 실행 명령어 
# python 01_gTTS_example.py

# TTS(Text-To-Speech)란?
# 텍스트 -> 음성 파일 변환 기능

# gTTS란?
# 구글 번역의 음성 재생 기능을 활용한 TTS 서비스이다.
# 구글 클라우드에서 지원하는 유료 TTS 서비스와는 다른 별도의 패키지이다.

# 따라서 별도의 API 키를 입력하지 않아도 패키지만 설치하면 무료로 실행할 수 있다.

# gTTS 무료 TTS 패키지 공식 문서 웹사이트
# 참고 URL - https://gtts.readthedocs.io/en/latest/

# gTTS 무료 TTS 패키지 설치 명령어
# pip install gTTS
from gtts import gTTS   # gTTS 무료 TTS 패키지 불러오기

# gTTS 클래스 객체 tts 생성시 
# 생성자에 들어가는 
# 파라미터 text 안에는 음성으로 변경할 텍스트 "안녕하세요 음성비서 프로그램 실습중입니다." 할당
# 파라미터 lang 안에는 한국어 음성을 생성할 것이기 때문에 텍스트 "ko" 할당 
# ** 주의사항 ** 
# 만약 파라미터 lang 안에 텍스트 "ko" 말고 "en"으로 할당하면
# 영어권 사람이 한국어를 발음 기호를 사용해서 읽는 것처럼
# 안.녕.하.세.요 이런식으로 음성이 자연스럽지 않고 뚝뚝 끊기는 음성 파일이 생성된다.
# 파라미터 lang 안에 텍스트 "ko"로 꼭 할당해야 한다.
tts = gTTS(text="안녕하세요 음성비서 프로그램 실습중입니다.",lang="ko")
tts.save("output.mp3")   # tts.save 함수 사용하여 파일 이름 "output.mp3"을 가진 음성 파일 형태로 저장(생성) 