import openai 
# Dalle2 에서 생성한 이미지를 파일 형태로 제공을 하지 않고 인터넷 접속 주소인 URL로 제공을 해준다. 
# 그럼 해당 URL로 접근해서 그 그림을 다운을 받아야 되는데, 
# 이 때, 해당 URL로 접근하기 위해 아래 urllib 패키지를 불러온다.(import)
import urllib 

# TODO : 변수 openai.api_key에 실제 OpenAI API 키 값 입력후 Git push 진행시 
#        오류 메시지 "To push, remove secret from commit(s) or follow this URL to allow the secret." 출력 되므로 실제 OpenAI API 키 값은 제거 처리함 (2025.01.03 jbh)
# 참고 URL - https://velog.io/@nigasa12/secret-key-%EC%9C%A0%EC%B6%9C%EC%82%AC%EA%B3%A0-%EB%B0%A9%EC%A7%80-git-secrets
# 변수 openai.api_key에 OpenAI API 키값을 아래처럼 입력해준다. 
openai.api_key = "OpenAI API 키 값 입력"

# 이미지를 생성하기 위해 함수 openai.Image.create 사용 
# 해당 함수 openai.Image.create 의 전달인자로 아래 3가지가 있다.
# 생성하고자 하는 이미지에 대한 텍스트 문자열을 파라미터 prompt에 할당 
# 총 몇개의 이미지를 생성할지 파라미터 n에 할당 
# 생성하고자 하는 이미지의 사이즈를 파라미터 size에 할당 
response = openai.Image.create(prompt="A futuristic city at night",n=1,size="512x512")
# 주의사항 - 생성하고자 하는 이미지의 사이즈를 키울수록 비용은 더 크게 소모된다.
# size : "256x256", "512x512","1024x1024" 
# price : 0.016$, 0.018$, 0.02$

# Dalle2로 생성한 이미지의 정보를 변수 response에 저장 
# 변수 response 안에서 해당 이미지를 다운받을 수 있는 URL 부분에 접근해서(response['data'][0]['url'])
# 이미지 URL 변수에 저장을 해준다.
image_url = response['data'][0]['url']

# 패키지 urllib -> rllib.request.urlretrieve 활용해서
# 해당 이미지 다운 받을 수 있는 URL 주소(image_url) 접근해서 
# 이미지 다운로드를 받는데, 다운을 받을 때의 파일명은 "test.jpg"로 
# 다운을 받도록 아래처럼 코드 작성한다.
# 파일명 "test.jpg" 다운로드 받은 경로는 가상환경이 설정된 
# 루트 디렉토리 "ch08" 하위에 "test.jpg"로 다운로드 완료된다.
urllib.request.urlretrieve(image_url, "test.jpg")
# 생성하고자 하는 이미지 URL 주소 화면 출력(데이터 시각화)
print(image_url)