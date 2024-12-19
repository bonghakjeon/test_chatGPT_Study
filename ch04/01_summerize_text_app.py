##### 기본 정보 불러오기 #####
##### (프로그램 개발할 때 패키지 정보 불러와서 정리) #####
##### (때에 따라서는 프로그램에 필요한 다른 API들의 키나 토큰들을 정리) #####
# Streamlit 패키지 추가
import streamlit as st   # streamlit 패키지 -> Elias(앨리아스) st 로 불러오기 
# OpenAI 패키지 추가
import openai   # openai 패키지 불러오기 

##### 기능 구현 함수 #####
##### 프로그램 내에서 ChatGPT한테 물어보거나 번역을 지시한다거나 하는 
##### 그러한 기능들을 깔끔하게 함수화해서 정리  
def askGpt(prompt):
    messages_prompt = [{"role": "system", "content": prompt}]
    response = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=messages_prompt)
    gptResponse = response["choices"][0]["message"]["content"]
    return gptResponse

##### 메인 함수 #####
##### 패키지 streamlit을 활용해서 프로그램의 UI를 작성하고 
##### 기능 구현 함수 "askGpt" 호출해서 프로그램이 동작하게 하는 메인 코드가 작성된 함수 
def main():

if __name__=="__main__":
    main()