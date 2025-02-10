# 가상환경 폴더 "ch11_env" 생성 터미널 명령어
# python -m venv ch11_env

# 가상환경 폴더 "ch11_env" 활성화 터미널 명령어
# ch11_env\Scripts\activate.bat

# 파이썬 스크립트 파일 "02_whisper_example.py" 터미널 실행 명령어 
# python 02_whisper_example.py

# STT(Speech-To-Text)란?
# 음성 메시지 분석 -> 텍스트 변환(생성) 해주는 기능
# STT(Speech-To-Text) 기능을 구현하기 위해 Whisper라는 서비스를 사용함.

# Whisper란?
# ChatGPT로 유명한 OpenAI에서 공개한
# 인공지능 모델로 음성 메시지 -> 텍스트 변환(생성) 해주는 STT 기술을 의미한다.
# 약 68만 시간 분량의 방대한 데이터를 학습시켜서
# 영어, 한국어를 포함한 다양한 언어를 인식할 수 있고
# 언어 번역 및 언어 식별 기능이 있다.
# Whisper 모델은 오픈 소스로 공개되어 있다.
# Whisper API는 ChatGPT와 같은 OpenAI API키를 사용한다.
# 현재 공개된 Whisper API는 "whisper-1" 모델이고
# 당연히 Whisper 모델을 사용할 때도 요금이 부과된다.

# Whisper 모델 사용요금 확인 방법
# 1. Whisper 공식 사이트 "https://openai.com/index/whisper/" 접속 
# -> 화면 하단으로 이동 -> 항목 "API" 밑에 "Pricing" 클릭 
# 2. Whisper 모델 "Pricing" 화면 이동 "https://openai.com/api/pricing/" -> 키워드 "Audio models" 검색 
# -> 항목 "Model" 하위 "Whisper"를 찾고 그 옆에 항목 "Usage"에 적혀있는 값은 분당 0.006달러의 요금이 부과된다고 알려준다.

# Whisper 모델 구조 확인할 수 있는 공식 웹사이트
# 참고 URL - https://openai.com/index/whisper/

# Whisper 관련 문서 PDF 파일 웹사이트
# 참고 URL - https://cdn.openai.com/papers/whisper.pdf

import openai  # openai 패키지 불러오기 

#API 키 입력
openai.api_key = "API_key 입력" # OopenAI 패키지의 api 키(openai.api_key)에 사용자가 발급한 API 키 값 입력 
# 녹음파일 열기
# open 함수 사용하여 텍스트로 추출(변환)하고 싶은 
# 음성 파일 "output.mp3"을 Byte 형식으로 불러와서(읽어와서)
# 변수 audio_file에 할당 
# 음성 파일 "output.mp3"을 Byte 형식으로 불러오기(읽어오기) 위해서
# 함수 open에 인자값을 "rb"로 전달 해야함.
audio_file = open("output.mp3", "rb")   
# whisper 모델에 음원파일 전달하기
# openai.Audio.transcribe 함수 사용하여 
# 해당 함수 openai.Audio.transcribe 안에
# 전달 인자로 STT(Speech-To-Text) 기능을 사용할 때 필요한 
# Whisper 모델("whisper-1")을 먼저 전달하고
# 방금 전에 위에서 불러온 음성 파일 변수 audio_file 또한 전달한다.
# 아래 코드 실행으로 음성 파일("output.mp3")에서 텍스트를 추출(변환)해서 
# 변수 transcript에 저장 
transcript = openai.Audio.transcribe("whisper-1", audio_file)
# 결과 보기
# transcript["text"]만 출력하면 음성 파일 "output.mp3"에서 추출(변환)한 텍스트만 출력할 수 있다.
# 출력되는 텍스트 "안녕하세요. 음성비서 프로그램 실습 중입니다."
print(transcript["text"]) 