# 비쥬얼스튜디오 코드(VSCode)
# streamlit 터미널 실행 명령어
# streamlit run 03_chatGPTvsBard_app.py

##### 기본 정보 입력 #####
# Streamlit 패키지 추가
import streamlit as st
# OpenAI 패키지 추가
import openai
# Bard 패키지 추가 
from bardapi import Bard
# from gemini import Gemini # (구)Bard, (현)Gemini 패키지 추가

##### 기능 구현 함수 정리#####
# ChatGPT
# ChatGPT 한테 질문하는 함수 
def askGpt(prompt):
    messages_prompt = [{"role": "system", "content": prompt}]
    # 프로그램상에서 사용자가 ChatGPT 모델 종류를 직접 고를 수 있도록 model=st.session_state["model"] 설정 
    response = openai.ChatCompletion.create(model=st.session_state["model"], messages=messages_prompt)

    system_message = response["choices"][0]["message"]

    # ChatGPT 최종 답변(system_message["content"]) 리턴 
    # ChatGPT 한테 질문을 완성하는데 사용한 토큰(response["usage"]["completion_tokens"]) 비용 리턴 
    # ChatGPT 한테 질문을 하는데 사용된 토큰(response["usage"]["prompt_tokens"]) 비용 리턴 
    return system_message["content"], response["usage"]["completion_tokens"], response["usage"]["prompt_tokens"]

# (구)Bard, (현)Gemini
# (구)Bard, (현)Gemini 한테 질문하는 함수 
def askBard(prompt):
    # 프로그램상에서 사용자에게 입력받은 (구)Bard, (현)Gemini 토큰을 session_state에 저장할 수 있도록 token=st.session_state["Bard_TK"] 설정 
    bard = Bard(token=st.session_state["Bard_TK"],timeout=120)
    result = bard.get_answer(prompt)
    # (구)Bard, (현)Gemini 답변을 3가지로 받을 수 있도록 아래처럼 설정 
    return result["choices"][0]["content"],result["choices"][1]["content"], result["choices"][2]["content"] 

##### 메인 함수 #####
def main():
    # 프로그램 제목(page_title="ChatGPT vs Bard 비교 프로그램") 정하기 
    st.set_page_config(
        page_title="ChatGPT vs Bard 비교 프로그램",
        layout="wide")

    # 프로그램(st.title('ChatGPT vs Bard 비교 프로그램🤜🤛')) 이름 정하기
    st.title('ChatGPT vs Bard 비교 프로그램🤜🤛')
    st.markdown('---') # markdown 사용해서 구분선 생성(st.markdown('---'))

    # 프로그램에서 어떤 이벤트가 발생해도 정보를 잃지 않고 유지할 3가지 session_state 지정하기 
    # session_state 초기화 코드 
    # 1. "model" - 사용자가 언어모델 중에 선택할 언어모델을 저장하는 session_state
    if "model" not in st.session_state:
        st.session_state["model"] = ""
    # 2. "OPENAI_API" - OPENAI API 키를 의미
    if "OPENAI_API" not in st.session_state:
        st.session_state["OPENAI_API"] = ""
    # 3. "Bard_TK" - (구)Bard, (현)Gemini 토큰 의미 
    if "Bard_TK" not in st.session_state:
        st.session_state["Bard_TK"] = ""

    # 사이드바 생성 
    with st.sidebar:
        # st.text_input 사용해서 OpenAI API 키 입력받기
        open_apikey = st.text_input(label='OPENAI API 키', placeholder='Enter Your API Key', value='',type='password') 
        if open_apikey:
            # 입력받은 OpenAI API 키를 st.session_state의 key "OPENAI_API"에 매핑되는 값으로 저장 
            st.session_state["OPENAI_API"] = open_apikey 
            # 입력받은 OpenAI API 키를 변수 openai.api_key에 저장 
            openai.api_key = open_apikey

        #OpenAI 모델 선정하기
        # st.radio 사용해서 OpenAI 모델을 선택할 수 있는 라디오 버튼 객체 생성 
        # 라디오 버튼 label "GPT 모델" 설정 
        # 라디오 버튼 종류(options)는 'gpt-4', 'gpt-3.5-turbo' 2가지 설정 
        st.session_state["model"] = st.radio(label="GPT 모델",options=['gpt-4', 'gpt-3.5-turbo'])
        st.markdown('---') # markdown 사용해서 구분선 생성(st.markdown('---'))
        
        # (구)Bard, (현)Gemini 토큰받기
        # st.text_input 사용해서 (구)Bard, (현)Gemini 토큰 입력받기 
        bard_token = st.text_input(label='Bard Token 키', placeholder='Enter Your Bard Token', value='',type='password')
        if bard_token:
            # 입력받은 (구)Bard, (현)Gemini 토큰을 st.session_state의 key "Bard_TK"에 매핑되는 값으로 저장 
            st.session_state["Bard_TK"] = bard_token

    # 프롬프트 입력 받기
    # 사용자에게 프롬프트 입력 받기 
    # st.header 사용해서 "프롬프트를 입력하세요" 화면 출력  
    st.header("프롬프트를 입력하세요")
    # st.text_input 사용해서 사용자에게 질문 입력 받기 
    # 사용자가 입력한 질문은 변수 prompt에 저장 
    prompt = st.text_input(" ")
    st.markdown('---')   # markdown 사용해서 구분선 생성(st.markdown('---'))

    #결과 출력
    # ChatGPT, (구)Bard, (현)Gemini 2가지로 
    # 사용자의 질문에 대한 결과값을 화면으로 출력하기에
    # 아래처럼 st.columns(2) 사용해서 세로로 화면 영역을 2가지(col1, col2)로 나누기 
    # col1 - ChatGPT
    # col2 - (구)Bard, (현)Gemini
    col1, col2 = st.columns(2)
    # ChatGPT 답변을 화면에 출력하는 공간 
    # 아래 구현된 코드는 사용자에게 질문(프롬프트)를 입력 받았을 시에만 코드 실행 
    with col1: 
        st.header("ChatGPT")
        # 사용자에게 받은 질문이 변수 prompt에 입력된 경우
        if prompt:
            # OpenAI의 API키(st.session_state["OPENAI_API"])를 입력받았을 때에만 해당 if절 안의 코드 실행
            if st.session_state["OPENAI_API"]:
                # 사용자의 질문이 담긴 변수 prompt를 askGpt 함수의 파라미터로 넣어서 
                # ChatGPT로 부터 온 최종 답변을 변수 result에 담기 
                # 질문을 완성하는데 소모한 토큰 비용 변수 completion_token에 담기 
                # 질문을 하는데 소모한 토큰 비용 변수 prompt_token에 담기 
                result, completion_token,prompt_token  = askGpt(prompt)
                st.markdown(result) # st.markdown 사용해서 ChatGPT로 부터 온 최종 답변 화면 출력 
                
                # 사용자가 한 질문을 통해서 소모된 전체 비용 계산 
                # 사용자가 선택한 언어 모델 "gpt-3.5-turbo", "gpt-4"에 따라서 비용이 다르기 때문에
                # 아래처럼 if ~ else절로 구현 
                # st.session_state["model"]에 저장된 언어 모델이 "gpt-3.5-turbo"인 경우 
                if st.session_state["model"] == "gpt-3.5-turbo":
                    # 언어 모델이 "gpt-3.5-turbo"인 상태에서 소모된 전체 비용 계산
                    # 질문을 완성하는데 소모된 토큰(completion_token)은 1,000 토큰당 0.02 달러 계산됨
                    # 질문 하는데 소모된 토큰(prompt_token)은 1,000 토큰당 0.015 달러 계산됨
                    total_bill = (completion_token*0.02+prompt_token*0.015)*0.001
                    
                    # 총 사용 토큰(completion_token+prompt_token), 전체 비용(total_bill) 웹 화면 출력 
                    st.info(f"총 사용 토큰 : {(completion_token+prompt_token)}")
                    st.info(f"금액 : {total_bill}$") # 계산된 금액은 달러($) 기준이다.

                # st.session_state["model"]에 저장된 언어 모델이 "gpt-4"일 경우 
                else:
                    # 언어 모델이 "gpt-4"인 상태에서 소모된 전체 비용 계산
                    total_bill = (completion_token*0.06+prompt_token*0.03)*0.001
                    
                    st.info(f"총 사용 토큰 : {(completion_token+prompt_token)}")
                    st.info(f"금액 : {total_bill}$")
            else:
                st.info("OpenAI API 키를 입력하세요")

    # (구)Bard, (현)Gemini 답변을 화면에 출력하는 공간
    with col2:
        st.header("Bard")
        # 사용자에게 받은 질문이 변수 prompt에 입력된 경우
        if prompt:
            # (구)Bard, (현)Gemini 토큰 (st.session_state["Bard_TK"])를 입력받았을 때에만 해당 if절 안의 코드 실행
            if st.session_state["Bard_TK"]:
                # 사용자의 질문이 담긴 변수 prompt를 askBard 함수의 파라미터로 넣어서 
                # (구)Bard, (현)Gemini로 부터 온 최종 답변 3가지를 
                # 변수 result1, result2, result3에 담기 
                result1, result2, result3 = askBard(prompt)
                # st.markdown 사용해서 (구)Bard, (현)Gemini로 부터 온 최종 답변 3가지 화면에 출력 
                # st.markdown 사용하면 마크다운 문법을 사용해서 화면상에 데이터 출력(시각화) 가능 
                st.markdown("### 답변1")
                st.markdown(result1[0])
                st.markdown("### 답변2")
                st.markdown(result2[0])
                st.markdown("### 답변3")
                st.markdown(result3[0])
            else:
                st.info("Bard Token을 입력하세요")

if __name__=="__main__":
    main()