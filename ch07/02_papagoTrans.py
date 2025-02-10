# 가상환경 폴더 "ch07_env" 생성 터미널 명령어
# python -m venv ch07_env

# 가상환경 폴더 "ch07_env" 활성화 터미널 명령어
# ch07_env\Scripts\activate.bat

# 파파고 API 지원 종료 안내 [24.2.29.예정]
# 등록일2023-12-07||조회수46593||
# Papago API를 이용해주셔서 감사드립니다.
# Papago 번역 서비스는 번역 품질 향상을 위한 끊임없는 연구를 진행하고 있으며, 네이버 개발자센터에서는 기계번역 서비스인 Papago를 NMT(Neural Machine Translation) API와 언어감지API 두 가지 상품으로 제공하고 있습니다.
# 안정적인 서비스 제공을 위해 개발자 센터를 통해 제공하던 Papago 서비스를 중단하고 네이버 클라우드 플랫폼으로 일원화해 제공하고자 합니다.
# 아래와 같은 일정으로 개발자센터 내 Papago 서비스 제공이 종료될 예정이니, 이용에 참고 부탁드립니다.
# [개발자센터 > Papago번역 API 서비스 종료]
# ▶ 서비스 종료 일정 : 2024년 2월 29일
# ▶ 종료 대상 서비스 : Papago NMT API 및 Papago 언어감지API
# [네이버클라우드 > Papago 번역 서비스 안내]
# ▶ Papago 번역 API 상품 안내 : https://www.ncloud.com/product/aiService/papagoTranslation
# ▶ 네이버 클라우드 플랫폼 > 가입 진행
# : https://auth.ncloud.com/join?from=ncp_home
# 네이버 개발자센터를 통해 Papago 서비스를 이용해주시는 모든 고객분들에게 다시 한 번 감사의 말씀을 전합니다.
# 최고의 번역 품질을 제공해드릴 수 있도록 더욱 노력하겠습니다.
# 참고 URL - https://developers.naver.com/notice/article/14501
import requests

PAPAGO_ID = "ID 입력" 
PAPAGO_PW = "Password 입력" 

def papago_translate(text):
     
    data = {'text' : text,
            'source' : 'en',
            'target': 'ko'}

    url = "https://openapi.naver.com/v1/papago/n2mt"
    header = {"X-Naver-Client-Id":PAPAGO_ID,
              "X-Naver-Client-Secret":PAPAGO_PW}

    response = requests.post(url, headers=header, data=data)
    rescode = response.status_code

    if(rescode==200):
        send_data = response.json()
        trans_data = (send_data['message']['result']['translatedText'])
        return trans_data
    else:
        print("Error Code:" , rescode)



text ="GPT-4 is more creative and collaborative than ever before. It can generate, edit, and iterate with users on creative and technical writing tasks, such as composing songs, writing screenplays, or learning a user??s writing style."

result = papago_translate(text)
print(result)