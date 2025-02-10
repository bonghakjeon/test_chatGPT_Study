# 가상환경 폴더 "ch09_env" 생성 터미널 명령어
# python -m venv ch09_env

# 가상환경 폴더 "ch09_env" 활성화 터미널 명령어
# ch09_env\Scripts\activate.bat

# OpenAI API 터미널 설치 명령어 
# pip install openai==0.28.1

# 랭체인(langchain) 공식 문서 
# 참고 URL - https://python.langchain.com/docs/integrations/chat/openai/
# 참고 2 URL - https://python.langchain.com/api_reference/openai/index.html

# 랭체인(langchain) 프레임워크 터미널 설치 명령어
# (X) pip install langchain
# (O) pip install -U langchain-community

# 유튜브 대본 api 터미널 설치 명령어
# pip install youtube_transcript_api 

# 유튜브 대본(스크립트) 번역할 동영상 URL 주소
# 참고 URL - https://www.youtube.com/watch?v=Pn-W41hC764 

# OpenAI에서 텍스트의 토큰수를 세어야 될 때 사용하는 패키지 "tiktoken" 설치하기 
# pip install tiktoken


# 영어 -> 한글 구글 번역 패키지 "googletrans" 터미널 설치 명령어
# pip install googletrans==3.1.0a0

# 유튜브 대본(스크립트) 불러오기
# 랭체인(langchain) 프레임워크 안에 YoutubeLoader 불러오기 
from langchain.document_loaders import YoutubeLoader

# 함수 YoutubeLoader.from_youtube_url 대본을 불러오고 싶은 유튜브 URL 주소값을 인자로 전달 
loader = YoutubeLoader.from_youtube_url("https://www.youtube.com/watch?v=Pn-W41hC764")
transcript = loader.load() # 인스턴스 loader의 인스턴스 메소드 load() 사용해서 대본 추출 

# 랭체인(langchain) 프레임워크 사용해서 긴 글(내용) 요약하기 
# Max Token 이상의 긴 글(내용)을 요약하는 방법은?
# 글을 쪼개서 요약을 진행하면 된다.
# Max Token 이상의 긴 글(내용)을 요약 순서 
# 1. 랭체인(langchain) 프레임워크 사용해서 전체 문서를 일정 크기(Max Token 보다 작은 크기)로 분할 
# 2. 1번에서 분할한 각각의 문서를 ChatGPT한테 각각 요약 요청 
# 3. 랭체인(langchain) 프레임워크 사용해서 2번에서 요약한 각각의 문서 내용 취합 -> ChatGPT한테 최종 요약 요청
# 4. ChatGPT가 최종 요약한 요약본 문서 화면 출력 (데이터 시각화)

# 주의사항 - 가끔 글이 너무 길이서 분할하였는데, 
# 분할한 문서 덩어리가 1000개, 2000개 이상 나오고 
# 1000개, 2000개의 요약본을 다 더했는데 그것마저도 ChatGPT의 Max Token을 초과할 수 있다.
# 그럴 때는 위의 1~4번 과정을 다시 반복 한다.
# 이렇게 아무리 긴 글(내용)이어도 몇 번의 요약을 거치면
# 결국은 최종 요약본을 만들 수가 있다.
# 다만 이 과정을 거칠 때마다 API 요금은 각각 지불된다.
# 왜냐하면 ChatGPT는 소모된 토큰 기준으로 요금이 요금을 부과하기 때문이다.
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chat_models import ChatOpenAI

# 함수 RecursiveCharacterTextSplitter 사용해서 인스턴스 text_splitter 생성
# 함수 RecursiveCharacterTextSplitter 파라미터 
# 1) "chunk_size"는 각각의 분할한 문서의 사이즈를 뜻한다.
# 2) "chunk_overlap"은 문서를 분할할 때 앞에 문서와 뒤에 문서의 내용을 겹치게(Overlap) 해서 분할할 수 있다.
#    "chunk_overlap" 값이 0인 경우 문서의 내용을 겹치지 않고 (Not Overlap)
#     텍스트가 쪼개진다.
text_splitter = RecursiveCharacterTextSplitter(chunk_size=4000, chunk_overlap=0)
# 인스턴스 메서드 text_splitter.split_documents 사용해서 
# 해당 메서드 안에 위에서 추출한 유튜브 대본(스크립트)가 들어있는 변수 transcript를 인자로 전달
text = text_splitter.split_documents(transcript)

# 함수 RecursiveCharacterTextSplitter 파라미터 
# chunk_size를 4천으로 설정한 경우 문서는 2개의 덩어리로 출력 
print('유튜브 문서(대본) 갯수 : ' + str(len(text))) # 텍스트 변수 text의 문서(대본) 갯수 구하기 

# print(text[0])   # 첫번째 유튜브 문서(대본) 내용 
# print(text[1])   # 두번째 유튜브 문서(대본) 내용

# 랭체인(langchain) 프레임워크 안에서 사용할
# ChatGPT 언어 모델 설정하기 
llm = ChatOpenAI(temperature=0,
                 openai_api_key="API 키 입력",
                 max_tokens=3000,
                 model_name="gpt-3.5-turbo",
                 request_timeout=120)

# 요약에 사용할 프롬프트 작성 
# PromptTemplate 메소드 사용하여 프롬프트를 일종의 템플릿을 갖춰서 작성할 수 있도록 함.
# 각각의 분할된 문서 조각을 요약 및 요청하는 프롬프트이다.
# 각각의 chunck 를 요약하기
prompt = PromptTemplate(
    # 아래 시스템 프롬프트 문자열 "각각의 분할된 문서들을 요약해줘" 작성  
    template="""Summarize the youtube video whose transcript is provided within backticks \
    ```{text}```
    """, input_variables=["text"]
)

# 요약된 내용들을 취합하여 다시한번 요약하기 
combine_prompt = PromptTemplate(
    # 아래 시스템 프롬프트 문자열 "유튜브 대본(스크립트) 요약한 것을 조합해서 다시 한번 8개에서 10개 사이로 문장을 요약해줘" 작성  
    template="""Combine all the youtube video transcripts  provided within backticks \
    ```{text}```
    Provide a concise summary between 8 to 10 sentences.
    """, input_variables=["text"]
)


# 함수 load_summarize_chain 파라미터 
# 1. ChatGPT 언어 모델 인스턴스 llm
# 2. 각각의 분할된 대본을 요청할 때 사용하는 프롬프트 map_prompt=prompt
# 3. 최종적으로 분할되어 있는 요약된 내용들을 조합해서 최종 요약본을 작성할 때 사용하는 프롬프트 combine_prompt=combine_prompt
# 인스턴스 chain 생성 
chain = load_summarize_chain(llm, 
                             chain_type="map_reduce", 
                             verbose=False, 
                             map_prompt=prompt, 
                             combine_prompt=combine_prompt)

# 유튜브 대본(스크립트) 요약 시작하기 
# 인스턴스 메서드 chain.run(text) 실행해야 유튜브 대본(스크립트) 요약이 시작된다.
# 유튜브 대본(스크립트) 요약을 진행할 변수 text를
# 인스턴스 메서드 chain.run(text) 파라미터로 넣고 
# 유튜브 대본(스크립트) 요약 시작하여 해당 요약한 결과를 output에 넣기
output = chain.run(text)

print(output)   # 유튜브 대본(스크립트) 요약한 결과 출력


from googletrans import Translator

# 함수 영어 -> 한글로 번역
def google_trans(messages):
    google = Translator()
    result = google.translate(messages, dest="ko")

    return result.text

# 유튜브 대본(스크립트) 요약본 영어 -> 한글로 번역 실행 
result = google_trans(output)
print(result)