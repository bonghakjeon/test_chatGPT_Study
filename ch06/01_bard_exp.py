# 비쥬얼스튜디오 코드(VSCode)
# streamlit 터미널 실행 명령어
# streamlit run 01_bard_exp.py

from gemini import Gemini

cookies = {
    "__Secure-1PSID" : "g.a000rghfMQ2AKm7_0LcfWGnUAncDNJettjWP63J9HCrW4-7nF0MVzVzlaNQ3_ahCliCRiVnYTgACgYKAd8SARESFQHGX2Miu_7udkIg-n3tHty5AyB4rBoVAUF8yKqXxFjSPwkeHlqfORCrSjEx0076"
}
# client = Gemini(auto_cookies=True)
client = Gemini(cookies=cookies, timeout=30)

response = client.generate_content("LG 트윈스에 대해 설명해줘")
print(response.payload)
