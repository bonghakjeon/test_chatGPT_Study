# 비쥬얼스튜디오 코드(VSCode)
# streamlit 터미널 실행 명령어
# streamlit run 01_bard_exp.py

from bardapi import Bard

# token = 'Bard token'
token = 'g.a000rghfMZ-WFMlpzKFo3opaYIvFIIcSAm3K0VvAmYIFCZcugiWFfcBszmnwXSkca_4BGkT9QwACgYKAc4SARESFQHGX2MiV9FB27mbo-9pzv93wRS4ChoVAUF8yKoOVqd-qyGxM9SPSoXVUIpY0076'
bard = Bard(token=token,timeout=30)
result = bard.get_answer("LG 트윈스에 대해 설명해줘")
print(result)


# from gemini import Gemini # (구)Bard, (현)Gemini 패키지 추가

# cookies = {
#     "__Secure-1PSID" : "g.a000rghfMQ2AKm7_0LcfWGnUAncDNJettjWP63J9HCrW4-7nF0MVzVzlaNQ3_ahCliCRiVnYTgACgYKAd8SARESFQHGX2Miu_7udkIg-n3tHty5AyB4rBoVAUF8yKqXxFjSPwkeHlqfORCrSjEx0076"
# }
# # client = Gemini(auto_cookies=True)
# client = Gemini(cookies=cookies, timeout=30)

# response = client.generate_content("LG 트윈스에 대해 설명해줘")
# print(response.payload)
