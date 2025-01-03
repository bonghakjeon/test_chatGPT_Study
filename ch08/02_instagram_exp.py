# 파이썬 패키지 PIL 불러오기 
from pathlib import Path  # 파이썬 패키지 pathlib의 Path 클래스 불러오기 
from instagrapi import Client   # 파이썬 패키지 instagrapi의 Client 클래스 불러오기 
from PIL import Image 

# 사용자의 인스타그램 아이디와 패스워드를 변수 USER_ID, USER_PASSWORD에 저장하기 
USER_ID = "instagram ID"
USER_PASSWORD = "Password!"

# 이미지 사이즈 변환(resize)
# 아래와 같은 코드를 추가해서 이미지 사이즈 변환하는 이유는
# instagrapi를 통해서 인스타그램에 사진을 업로드하려면
# 사진이 정사각형 모양만 업로드가 된다.
# 하여 이렇게 억지가 인스타그램에 업로드 하고자 하는 사진을 불러와서 (Image.open())
# 이미지 사이즈를 재정의(변환 - image.resize) 해준다.
image = Image.open("instaimg.jpg") # 인스타에 업로드 하고자 하는 사진 이미지 파일 "instaimg.jpg" 불러오기(열기) 
image = image.convert("RGB") 
new_image = image.resize((1080, 1080)) # 인스타에 업로드 하고자 하는 사진 사이즈 1080 * 1080 변환
new_image.save("new_picture.jpg") # 위에서 사이즈 변환된 사진 이미지를 새로운 파일("new_picture.jpg")로 저장 

# 인스타그램 로그인
cl = Client()   # Client 클래스 객체 cl 생성 
cl.login(USER_ID, USER_PASSWORD)   # cl.login 함수 사용해서 인스타그램 로그인 진행 

# 사진 가져오기 
# 위에서 사이즈 변환 사진 이미지 파일("new_picture.jpg")의 경로를 변수 phot_path에 저장 
phot_path = "new_picture.jpg"
phot_path = Path(phot_path)
print(phot_path)

# 업로드하기 
# 함수 cl.photo_upload에 아래 2가지 인자 전달하기 
# 1. 인스타로 업로드 하고자 하는 사이즈 변환 사진 이미지 파일 ("new_picture.jpg") 경로 변수(phot_path)
# 2. 같이 업로드할 텍스트 "hello this is a test from instagrapi"
cl.photo_upload(phot_path, "hello this is a test from instagrapi")