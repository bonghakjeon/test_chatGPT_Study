# 가상환경 폴더 "ch07_env" 생성 터미널 명령어
# python -m venv ch07_env

# 가상환경 폴더 "ch07_env" 활성화 터미널 명령어
# ch07_env\Scripts\activate.bat

# TODO : DeepL API 신용카드 등록 오류로 인하여 DeepL API 키 발급 실패함. (2025.01.02 jbh)
# DeepL 파이썬 오픈 소스 패키지 deepl 
# 터미널 설치 명령어
# pip install deepl==1.15.0
import deepl

auth_key = "API Key"  # Replace with your key
translator = deepl.Translator(auth_key)

text ="GPT-4 is more creative and collaborative than ever before. It can generate, edit, and iterate with users on creative and technical writing tasks, such as composing songs, writing screenplays, or learning a user??s writing style."

result = translator.translate_text(text, target_lang="KO")
print(result.text)