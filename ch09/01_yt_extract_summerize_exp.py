# 랭체인 프레임워크 터미널 설치 명령어
# (X) pip install langchain
# (O) pip install -U langchain-community

# 유튜브 대본 api 터미널 설치 명령어
# pip install youtube_transcript_api 


# 랭체인(langchain) 프레임워크 안에 YoutubeLoader 불러오기 
from langchain.document_loaders import YoutubeLoader

# 함수 YoutubeLoader.from_youtube_url 대본을 불러오고 싶은 유튜브 URL 주소값을 인자로 전달 
loader = YoutubeLoader.from_youtube_url("https://www.youtube.com/watch?v=Pn-W41hC764")
transcript = loader.load() # 인스턴스 loader의 인스턴스 메소드 load() 사용해서 대본 추출 
transcript
