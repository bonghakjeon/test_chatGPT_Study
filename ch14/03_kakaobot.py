###### 기본 정보 설정 단계 #######
# FastAPI 패키지 "fastapi" 불러오기
# Request 패키지 불러오기 
from fastapi import Request, FastAPI # 개발자 로컬 PC 비동기 웹서버 구현시 필요
import openai   # OPENAI 패키지 openai 불러오기 (ChatGPT, DALLE.2 사용)
import threading  # 프로그램 안에서 동시에 작업하는 멀티스레드 구현하기 위해 패키지 "threading" 불러오기
import time   # ChatGPT 답변 시간 계산하기 위해 패키지 "time" 불러오기
import queue as q   # 자료구조 queue(deque 기반) 이용하기 위해 패키지 "queue" 불러오기
import os   # 답변 결과를 테스트 파일로 저장할 때 경로 생성해야 해서 패키지 "os" 불러오기

# OpenAI API KEY
# 테스트용 카카오톡 챗봇 채팅방에서 
# ChatGPT와 통신하기 위해 OpenAI API 키 입력
API_KEY = "API_key"
openai.api_key = API_KEY

###### 기능 구현 단계 #######
# 카카오톡 챗봇 프로그램을 구동하는데 필요한 모든 기능 함수화 해서
# 아래 2가지 함수에서 사용할 수 있도록 정리 
# 메인 함수 "mainChat", 답변/사진 요청 및 응답 확인 함수 "responseOpenAI"
# 메인 함수 

# 메세지 전송 (카카오톡 서버로 텍스트 전송)
# ChatGPT의 답변을 카카오톡 서버로 답변 전송 전용 JSON 형태(Format)의 데이터로 전달하기 위한 함수
# 카카오톡 채팅방에 보낼 메시지를 매개변수 bot_response에 input으로 받기(인자로 전달)
def textResponseFormat(bot_response):
    # 카카오톡 채팅방에 보낼 메시지가 저장된 매개변수 bot_response를
    # 아래 json 형태(Format)에서 항목 'outputs' -> 항목 "simpleText" -> "text"안에 매개변수 bot_response을 넣어서
    # 변수 responsedp 저장하기 
    response = {'version': '2.0', 
                'template': {
                    'outputs': [{"simpleText": {"text": bot_response}}], 
                    'quickReplies': []
                }
               }
    return response  # 카카오톡 서버로 답변 전송하기 위해 답변 전송 전용 JSON 형태(Format)의 데이터가 저장된 변수 response 리턴  

# 사진 전송 (카카오톡 서버로 사진 전송)
# DALLE.2가 생성한 그림 URL 주소를 카카오톡 서버로 이미지 전송 전용 JSON 형태(Format)의 데이터로 전달하기 위한 함수
# 카카오톡 채팅방에 보낼 DALLE.2가 생성한 그림 URL 주소를 
# 매개변수 bot_response에 input으로 받기(인자로 전달)
# DALLE.2가 그림을 생성할 때 input으로 넣은 프롬프트 문자열을 
# 매개변수 prompt에 input으로 받기(인자로 전달)
def imageResponseFormat(bot_response,prompt):
    output_text = prompt+"내용에 관한 이미지 입니다"
    # 카카오톡 채팅방에 보낼 DALLE.2가 생성한 그림 URL 주소가 저장된 매개변수 bot_response를
    # 아래 json 형태(Format)에서 항목 'outputs' -> 항목 "simpleImage" -> "imageUrl"안에 매개변수 bot_response을 넣어서
    # 변수 responsedp 저장하기 
    response = {'version': '2.0', 'template': {
    'outputs': [{"simpleImage": {"imageUrl": bot_response,"altText":output_text}}], 'quickReplies': []}}
    return response   # 카카오톡 서버로 DALLE.2가 생성한 그림 URL 주소 전송하기 위해  이미지 전송 전용 JSON 형태(Format)의 데이터가 저장된 변수 response 리턴  

# ChatGPT또는 DALLE.2의 답변(응답)이 3.5초 초과시 
# 지연 안내 메세지 + 버튼 생성
# 답변 시간이 지연되면 지연 안내 메시지를 보내고
# 답변을 다시 요청하기 위해서 FastAPI 비동기 웹서버에서 버튼 생성 요청하여 카카오톡 서버로 전달
# 카카오톡 서버에 버튼 생성 요청하기 위하여 버튼 생성 전용 JSON 형태(Format)의 데이터로 전달
def timeover():
    # 카카오톡 채팅방에 보낼 안내메시지는 
    # 아래 json 형태(Format)에서 항목 "outputs" -> 항목 "simpleText" -> 항목 "text" 안에 안내메시지 텍스트 "아직 제가 생각이 끝나지 않았어요🙏🙏\n잠시후 아래 말풍선을 눌러주세요👆" 저장
    # 카카오톡 채팅방에 보낼 생성할 버튼은
    # 아래 json 형태(Format)에서 항목 "quickReplies" 
    # -> 항목 "action"에 "message" 작성 
    # -> 항목 "label"에 "생각 다 끝났나요?🙋" 작성 (버튼 안에 들어가는 label)
    # -> 항목 "messageText"에 "생각 다 끝났나요?" 작성 (사용자가 이 버튼을 클릭했을 때 카카오톡 채팅방에 출력되는 문구)
    
    # 카카오톡 채팅방에 보낼 안내메시지, 생성할 버튼을 
    # 전용 json 형태(Format)의 데이터를 변수 response에 저장 
    response = {"version":"2.0","template":{
      "outputs":[
         {
            "simpleText":{
               "text":"아직 제가 생각이 끝나지 않았어요🙏🙏\n잠시후 아래 말풍선을 눌러주세요👆"
            }
         }
      ],
      "quickReplies":[
         {
            "action":"message",
            "label":"생각 다 끝났나요?🙋",
            "messageText":"생각 다 끝났나요?"
         }]}}
    return response   # 카카오톡 서버로 지연 안내메시지 + 생성할 버튼 전송하기 위해 JSON 형태(Format)의 데이터가 저장된 변수 response 리턴  

# ChatGPT에게 질문/답변 받기
# OpenAI API 사용해서 사용자가 ChatGPT에게 질문하고
# ChatGPT로 부터 답변받기
# 카카오톡 채팅방 안에서 사용자가 카카오톡 챗봇(ChatGPT)에게 질문을 하면
# 질문의 내용이 변수 prompt로 input돼서 해당 함수 getTextFromGPT 실행
def getTextFromGPT(prompt):   # ChatGPT한테 질문을 하게 될 프롬프트(prompt)를 함수 getTextFromGPT에 input으로 받기 
    # 카카오톡 챗봇(ChatGPT)에게 질문을 할때는 
    # 아래와 같은 시스템 프롬프트(System Prompt - [{"role": "system", "content": 'You are a thoughtful assistant. Respond to all input in 25 words and answer in korea'}])와 함께 질문
    # 시스템 프롬프트의 내용("content": 'You are a thoughtful assistant. Respond to all input in 25 words and answer in korea')이 
    # 의미하는 뜻은 "넌 훌륭한 도우미고 답변은 25자 내외로 한국어로 해줘." 이다.
    # 이렇듯 카카오톡 챗봇(ChatGPT)의 답변의 뉘앙스(응답 스타일)를 변경하고 싶은 경우 
    # 시스템 프롬프트의 내용("content": 'You are a thoughtful assistant. Respond to all input in 25 words and answer in korea')을
    # 개발자의 요구사항에 맞게 변경하면 된다.
    # ChatGPT API에서 요구하는 프롬프트(prompt) input 양식으로 변경 및 변경한 input 양식을 변수 messages_prompt에 저장 
    # messages_prompt = [{"role": "system", "content": 'You are a thoughtful assistant. Respond to all input in 25 words and answer in korea'}]
    messages_prompt = [{"role": "system", "content": 'You are a thoughtful assistant. Respond to all input in 25 words and answer in korea'}]
    messages_prompt += [{"role": "user", "content": prompt}]
    
    # openai.ChatCompletion.create 함수 파라미터 "messages"에 messages_prompt 저장 
    # 함수 openai.ChatCompletion.create 호출 결과 최종적으로 ChatGPT API를 통해서 받은 응답을
    # response라는 변수에 저장 
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages_prompt)
    # response에서 ChatGPT의 응답 메시지 부분만 발췌를 해서(response["choices"][0]["message"])
    # 변수 system_message에 저장
    message = response["choices"][0]["message"]["content"]
    return message   # ChatGPT의 응답 메시지에 속한 답변 내용 부분(system_message["content"])만 발췌 및 리턴

# DALLE.2에게 질문/그림 URL 받기
# 생성된 그림의 URL 주소 받기
# 카카오톡 채팅방 안에서 사용자가 카카오톡 챗봇(ChatGPT)에게 그림 생성을 요청하면
# 요청한 내용이 변수 messages로 input돼서 해당 함수 getImageURLFromDALLE 실행
# DALLE.2 주의사항 
# 1. 특정 유명인 (예) 도널드 트럼프, 바이든 등등… 을 그림 그려달라고 요청 시 오류 발생 
#    참고 URL - https://community.openai.com/t/your-request-was-rejected-as-a-result-of-our-safety-system-your-prompt-may-contain-text-that-is-not-allowed-by-our-safety-system/285641
#    1번 오류 발생시 위의 ChatGPT로 부터 답변받기 함수 "getTextFromGPT" 몸체 안 변수 "messages_prompt"에 할당되는 시스템 프롬프트 문자열(항목 "content") 아래처럼 변경 후 컴파일 빌드 다시 실행 필요 
# (변경 전) messages_prompt = [{"role": "system", "content": 'You are a thoughtful assistant. Respond to all input in 25 words and answer in korea'}]
# (변경 후) messages_prompt = [{"role": "system", "content": 'You are a thoughtful assistant. Respond to all input in 100 words and answer in korea'}]
# 2. 영어가 아닌 한글로 그림 그려달라고 요청 시 요청사항과 전혀 다른 그림으로 그려줌.
# 3. 사용자가 그림 그려달라고 요청시 시간이 소요됨 (간단한 그림은 몇초 단위 / 복잡한 그림은 그 이상 시간 소요)
def getImageURLFromDALLE(prompt):
    # 사용자가 DALLE.2에게 그림 생성을 요청한 내용이 
    # 문자열로 저장된 변수 messages를 
    # 함수 openai.Image.create 에 전달하여 이미지 생성
    # 생성한 이미지에 대한 정보를 변수 response에 저장 
    # DALLE.2로 생성한 이미지의 사이즈(size)를 "512x512"로 설정
    response = openai.Image.create(prompt=prompt,n=1,size="512x512")
    # 이미지를 다운받을 수 있는 이미지 URL 주소(response['data'][0]['url'])를
    # 변수 image_url에 저장 
    image_url = response['data'][0]['url']
    return image_url   # 이미지를 다운받을 수 있는 이미지 URL 주소 리턴 

# 텍스트파일 초기화
# 메인 함수 "mainChat", 답변/사진 요청 및 응답 확인 함수 "responseOpenAI"
# 해당 2가지 함수에서 3.5초 이후에 생성된 답변 및 그림 URL 주소를 
# 임시로 텍스트 파일에 저장 -> 해당 텍스트 파일에 저장된 정보는
# 추후에 사용자가 버튼("생각 다 끝났나요?🙋")을 클릭해서 
# 답변 및 그림 URL 주소를 요청하면
# 해당 답변 및 그림 URL 주소를 전송한 후에는 해당 텍스트 파일은 필요가 없다.
# 이 때 해당 함수 dbReset를 호출하여 저장된 텍스트 파일를 초기화 해준다.
def dbReset(filename):
    with open(filename, 'w') as f:
        f.write("")

###### 서버 생성 단계 #######
app = FastAPI()   # FastAPI 클래스 객체 app 생성 

# 위에서 생성한 객체 app 이라는 웹서버에 
# HTTP 통신 get() 메소드에 인자 "/" 전달 후 
# -> get() 메소드 호출시 메인 주소("/")로 접속 진행
# -> root 함수 실행 
# HTTP 통신 GET 메서드 형태(@app.get("/"))로 
# 개발자 FastAPI 로컬 비동기 웹서버에 메인주소("/")로 접속하면
# 아래 비동기 함수 root 실행
# 개발자 FastAPI 로컬 비동기 웹서버의 로컬 포트(Port)는 8000번으로 디폴트(default)로 설정
# 구글 크롬(Chrome) 웹브라우저에서 URL 주소 "http://localhost:8000/" 접속시
# 아래 비동기 함수 root 실행
@app.get("/")
async def root():
    # 크롬(Chrome) 웹브라우저 상에서 
    # URL 주소 "http://127.0.0.1:8000/"로 접속을 했을 때, 
    # 웹브라우저상에서 아래와 같은 메시지({"message": "kakaoTest"}) 출력
    return {"message": "kakaoTest"}

# 위에서 생성한 객체 app 이라는 웹서버에 
# HTTP 통신 post() 메소드에 인자 "/chat/" 전달 후 
# -> post() 메소드 호출시 메인 주소 하위 주소("/chat/")로 접속 진행
# -> chat 함수 실행 -> 카카오톡 서버와 연결 진행
# 주의사항 - 일반 HTTP 통신 GET 방식으로 구글 크롬 웹브라우저 URL 접속하면 
#           (URL 주소 "http://127.0.0.1:8000/chat/) 아래와 같은 오류 메시지 출력
#           "405 Method Not Allowed"
#           왜냐면 post() 메소드로 호출하기 때문에 
#           구글 크롬 웹브라우저 URL 접속시에는 GET 방식이 아닌
#           POST 방식으로 접근해야 하기 때문이다.
#           하여 해당 오류를 해결하려면 카카오 API를 활용해서
#           아래 post() 메소드로 정보(데이터)를 주고 받을 수 있도록 해야한다.
# HTTP 통신 POST 메서드 형태(@app.post("/chat/"))로 
# 개발자 FastAPI 로컬 비동기 웹서버에 메인주소 + /chat/ 주소("/chat/")로 접속하면
# 아래 비동기 함수 chat 실행
# 개발자 FastAPI 로컬 비동기 웹서버의 로컬 포트(Port)는 8000번으로 디폴트(default)로 설정
# 구글 크롬(Chrome) 웹브라우저에서 URL 주소 "http://localhost:8000/chat/" 접속시
# 아래 비동기 함수 chat 실행
@app.post("/chat/")
# 카카오톡 채팅방에 사용자가 채팅을 새로 입력했을 때
# 챗봇의 모든 기능을 실행할 수 있는 함수 chat
# 사용자가 채팅을 새로 입력했을 때 새로운 입력에 대한 정보를
# 매개변수 request로 인자를 전달 받는다.
async def chat(request: Request):
    # 카카오톡 채팅방에서 사용자가 채팅 입력 
    # -> 해당 채팅에 대한 정보가 카카오톡 서버 -> ngrok 프로그램을 지나서 
    # -> 해당 FastAPI 웹서버 URL 주소 "/chat"로 넘어오고 
    # -> 함수 chat 실행 -> print 함수 호출 -> 카카오톡 채팅 정보가 터미널창에 출력
    # 쉽게 말해서 카카오톡 채팅방에 채팅이 입력될 때마다
    # 해당 chat 함수 실행되서 
    # 카카오톡 챗봇의 모든 기능 실행할 수 있는 메인함수 mainChat이 실행된다.
    # 메인함수 mainChat이 실행될 때는 카카오톡 채팅방에
    # 방금 전에 사용자가 입력한 채팅의 정보가 넘어오면서 메인함수 mainChat이 실행된다.

    # 카카오톡 채팅에서 날라온 채팅 정보를 json 데이터 형태(Format)로 정리(request.json())해서 변수 kakaorequest에 저장
    kakaorequest = await request.json()
    # 사용자의 요청에 맞는 카카오톡 챗봇의 모든 기능 실행할 수 있는 메인함수 mainChat에
    # 위의 변수 kakaorequest를 인자로 전달 
    # 해당 mainChat 함수는 최종적으로 사용자의 요청에 맞는 json 데이터를 반환해서 리턴해준다.
    # 해당 mainChat 함수 실행 결과 리턴된 jsom 데이터가 
    # 비동기 함수 chat에서 또 리턴이 돼서
    # 최종적으로는 카카오톡 서버로 답변 및 DALLE.2가 그려준 그림 URL 주소를 전송해줌.
    return mainChat(kakaorequest)

###### 메인 함수 단계 #######

# 멀티스레드 작업 처리를 해야해서 아래 2가지 함수 구현
# 메인 함수 "mainChat", 답변/사진 요청 및 응답 확인 함수 "responseOpenAI"

# 메인 함수
def mainChat(kakaorequest):

    run_flag = False
    start_time = time.time()

    # 응답 결과를 저장하기 위한 텍스트 파일 생성
    cwd = os.getcwd()
    filename = cwd + '/botlog.txt'
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            f.write("")
    else:
        print("File Exists")    

    # 답변 생성 함수 실행
    response_queue = q.Queue() #.put(), .get()
    request_respond = threading.Thread(target=responseOpenAI,
                                        args=(kakaorequest, response_queue,filename))
    request_respond.start()

    # 답변 생성 시간 체크
    while (time.time() - start_time < 3.5):
        if not response_queue.empty():
            # 3.5초 안에 답변이 완성되면 바로 값 리턴
            response = response_queue.get()
            run_flag= True
            break
        # 안정적인 구동을 위한 딜레이 타임 설정
        time.sleep(0.01)

    # 3.5초 내 답변이 생성되지 않을 경우
    if run_flag== False:     
        response = timeover()

    return response

# 답변/사진 요청 및 응답 확인 함수
def responseOpenAI(request,response_queue,filename):
    # 사용자가 버튼을 클릭하여 답변 완성 여부를 다시 봤을 시
    if '생각 다 끝났나요?' in request["userRequest"]["utterance"]:
        # 텍스트 파일 열기
        with open(filename) as f:
            last_update = f.read()
        # 텍스트 파일 내 저장된 정보가 있을 경우
        if len(last_update.split())>1:
            kind = last_update.split()[0]  
            if kind == "img":
                bot_res, prompt = last_update.split()[1],last_update.split()[2]
                response_queue.put(imageResponseFormat(bot_res,prompt))
            else:
                bot_res = last_update[4:]
                print(bot_res)
                response_queue.put(textResponseFormat(bot_res))
            dbReset(filename)

    # 이미지 생성을 요청한 경우
    elif '/img' in request["userRequest"]["utterance"]:
        dbReset(filename)
        prompt = request["userRequest"]["utterance"].replace("/img", "")
        bot_res = getImageURLFromDALLE(prompt)
        response_queue.put(imageResponseFormat(bot_res,prompt))
        save_log = "img"+ " " + str(bot_res) + " " + str(prompt)
        with open(filename, 'w') as f:
            f.write(save_log)

    # ChatGPT 답변을 요청한 경우
    elif '/ask' in request["userRequest"]["utterance"]:
        dbReset(filename)
        prompt = request["userRequest"]["utterance"].replace("/ask", "")
        bot_res = getTextFromGPT(prompt)
        response_queue.put(textResponseFormat(bot_res))
        print(bot_res)
        save_log = "ask"+ " " + str(bot_res)
        with open(filename, 'w') as f:
            f.write(save_log)
            
    #아무 답변 요청이 없는 채팅일 경우
    else:
        # 기본 response 값
        base_response = {'version': '2.0', 'template': {'outputs': [], 'quickReplies': []}}
        response_queue.put(base_response)