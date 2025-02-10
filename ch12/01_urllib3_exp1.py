# 가상환경 폴더 "ch12_env" 생성 터미널 명령어
# python -m venv ch12_env

# 가상환경 폴더 "ch12_env" 활성화 터미널 명령어
# ch12_env\Scripts\activate.bat

# HTTP(Hypertext Transfer Protocol) 통신이란?
# HTTP 통신은 컴퓨터가 인터넷을 통해 서로 통신하는 방식이다.
# 예를들어 구글 크롬(Chrome)과 애플의 사파리(Safari) 같은 웹브라우저와
# 웹서버가 정보를 교환하고 웹서버에서 받은 정보(데이터)를
# 웹브라우저에서 웹페이지로 데이터 시각화해서 표시할 수 있도록 하는 일련의 규칙이다.
# HTTP Request : 웹브라우저 -> 웹서버로 HTTP 요청 
# 요청 형식 - 요청헤더(HTTP URL 주소 + 요청 메서드[요청 유형 - Get 또는 Post / 요청 body 형식 - 양식 데이터 또는 json payload 같은 추가 데이터 포함])
# HTTP Response : 웹서버 -> 웹브라우저로 HTTP 응답
# 응답 형식 - 응답헤더(사용중인 HTTP 버전 + HTTP 상태 결과 코드 + 쿠키 + 캐싱 정보 등등...) 
#           + 웅답 body(HTML + CSS + JavaScript + 이미지 + JSON 데이터 등 실제 콘텐츠가 포함)
# HTTP Response 참고사항
# 1) -2xx-성공 : 200번대의 상태 코드는 대부분 성공 의미
# 2) -3xx-리다이렉션 : 300번대의 상태 코드는 대부분 클라이언트가 이전 주소로 데이터를 요청하여 
#                     서버에서 새 URL로 리다이렉트를 유도하는 경우이다.
# 3) -4xx-클라이언트 에러 : 400번대 상태 코드는 대부분 클라이언트의 코드가 잘못된 경우이다.
# (예) 페이지를 찾을 수 없습니다. (404 NotFound)
#      페이지가 존재하지 않거나, 사용할 수 없는 페이지입니다.
#      입력하신 주소가 정확한지 다시 한번 확인해 주시기 바랍니다.

# HTTP 통신 이해하기 
# 텔레그램 API 활용하려면 텔레그램 서버와 개발자가 구현한 챗봇 서버가
# 인터넷을 통해 대화하는 방법인 HTTP 통신에 대해서 이해가 필요함.
# HTTP 통신에 대한 이론적인 설명과 파이썬 환경에서 HTTP 통신을 할 수 있는
# 파이썬 라이브러리 "urllib3"의 간단한 사용 방법은 아래와 같다.

# 파이썬 환경에서 HTTP 통신하려면
# 파이썬 기본 내장 패키지(라이브러리) - "urllib3"
# 아마존 웹서비스(AWS)에서 챗봇 프로그램을 구현할 때, 
# 다른 패키지를 사용하면 구현하기 복잡하기 때문에 
# 파이썬 기본 내장 패키지(라이브러리) - "urllib3" 사용함.
# HTTP 통신 웹서버 테스트 사이트 URL 주소
# - https://jsonplaceholder.typicode.com/

# 파이썬 파일 "01_urllib3_exp1.py" 터미널 실행 명령어
# python 01_urllib3_exp1.py

# 파이썬 파일 "01_urllib3_exp1.py" 실행시 
# 오류 메시지 ModuleNotFoundError: No module named 'urllib3'
# 해결하기 위해 파이썬 기본 내장 패키지(라이브러리) - "urllib3" 삭제 및 
# 버전 1.26.18 설치 진행 
# 참고 URL - https://heidong.tistory.com/278
# 1) pip uninstall urllib3
# 2) pip install urllib3==1.26.18

# HTTP 통신 Request(요청) 테스트 코드 
import urllib3   # HTTP 통신을 하기위해 파이썬 기본 내장 패키지(함수) urllib3 불러오기 - 아마존 웹서비스(AWS)에서 사용하기 용이하다.

# 라이브러리(패키지) urllib3의 PoolManager 클래스 객체 http 생성
http = urllib3.PoolManager()

# HTTP - GET 방식 Request(요청)할 URL 주소가 담긴 변수 url
url = "https://jsonplaceholder.typicode.com/posts/1"
# http.request 함수 호출시 'GET', url 2가지 인자 전달
response = http.request('GET', url) # HTTP Request(요청) - GET 방식

print(response.data) # HTTP Response(응답) 데이터(response.data) 터미널창 출력


