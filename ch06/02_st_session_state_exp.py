# 비쥬얼스튜디오 코드(VSCode)
# streamlit 터미널 실행 명령어
# streamlit run 02_st_session_state_exp.py

##### 기본 정보 불러오기 #####
##### (프로그램 개발할 때 패키지 정보 불러와서 정리) #####
##### (때에 따라서는 프로그램에 필요한 다른 API들의 키나 토큰들을 정리) #####
# Streamlit 패키지 추가
import streamlit as st   # streamlit 패키지 -> Elias(앨리아스) st 로 불러오기 

# 사용자가 숫자를 입력하고 해당 숫자를 누적해서 더하는 프로그램
# 주의사항 - streamlit 패키지를 사용하여 구현한 프로그램은
# 사용자가 버튼을 누르거나 텍스트를 입력할 때마다
# 코드가 처음부터 끝까지 재실행된다.
# 이 과정에서 내부의 모든 변수가 초기화처리 된다.
# 하여 사용자가 숫자를 입력하고 해당 숫자를 누적해서 더하지 못하는 오류가 발생한다.
# 이러한 모든 변수가 초기화 되는 오류를 해결하기 위해 streamlit 패키지 st.session_state 사용해야 한다.
total = 0

# 사용자가 숫자를 입력하고 해당 숫자를 누적해서 더하지 못하는 오류가 발생시
# 이러한 모든 변수가 초기화 되는 오류를 해결하기 위해 streamlit 패키지 st.session_state 사용하는 코드 예시 
# session_state란? (st.session_state)
# session_state는 Python의 Dictionary 형태로 여러 개의 정보를 저장할 수 있다.

# 만약에 "total"이라는 st.session_state가 없다면 
if "total" not in st.session_state:
    st.session_state["total"] = 0 # "total"이라는 st.session_state를 생성 및 0으로 초기화 

num = st.text_input(" ") # st.text_input() 엘리먼트로 입력받은 숫자를 num이라는 변수에 저장 
if num: # num에 입력받은 숫자가 존재하면 
    st.session_state["total"] = st.session_state["total"]+int(num) # st.session_state의 "total" 안에 num에 입력받은 숫자를 int로 형변환한 값을 덧셈하여 누적계산 처리 

st.title(st.session_state["total"])  # 최종적으로 누적된 st.session_state의 "total"안에 저장된 값을 웹브라우저 화면에 시각화 처리 


# 사용자가 숫자를 입력하고 해당 숫자를 누적해서 더하지 못하고
# 모든 변수가 초기화 되는 오류 발생하는 코드 예시 
# num = st.text_input(" ") # st.text_input() 엘리먼트로 입력받은 숫자를 num이라는 변수에 저장 
# if num: # num에 입력받은 숫자가 존재하면 
#     total = total+int(num) # 변수 total에 num에 입력받은 숫자를 int로 형변환한 값을 덧셈하여 누적계산 처리 

# st.title(total) # 최종적으로 누적된 변수 total의 값을 웹브라우저 화면에 시각화 처리 



