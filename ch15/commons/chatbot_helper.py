# 공통 
# OpenAI Logger 객체 이름 'openai'
_openai_objname = 'openai'  

# 아마존 웹서비스(AWS) 람다 함수(Lambda Function) 
# -> 로그 텍스트 파일("/tmp/botlog.txt") 경로 
_botlog_filepath = '/tmp/botlog.txt'

# (주)상상진화 각 레벨(level)별 처리할 업무 프로세스
_consult = '/level1'
_autodeskProduct = '1. Autodesk 제품'
_boxProduct = '2. 상상진화 BOX 제품'
_askAccount = '3. 계정&제품배정 문의'
_askInst = '설치 문의'
_askInst_autodeskProduct = f'{_autodeskProduct} {_askInst}'
_askInst_boxProduct = f'{_boxProduct} {_askInst}'
_seeMore = '더보기'


# level4, level5 - '1. Autodesk 제품', '2. 상상진화 BOX 제품'
_ver = '버전'
_softwareInstMethod = '설치 방법'
_beginning = '처음으로'

# 버전 종류 
# '1. Autodesk 제품', '2. 상상진화 BOX 제품' 공통 버전 
_2026 = '2026'  
_2025 = '2025'
_2024 = '2024'
_2023 = '2023'

# '2. 상상진화 BOX 제품' 전용 버전 
_2022 = '2022'
_2021 = '2021'

# 폴더 "modules" -> 카카오 API 전용 모듈 "kakao"
_consultTitle = '[상담시간 안내]'
_consultDescription = '▶ 기술지원문의\n월~금요일: 오전 9시 ~ 오후 6시\n주말, 공휴일: 휴무'
_subCatTitle = '상담 유형'
_selectInfo = '안내가 필요한 항목 선택해주세요.'
_selectVersion = '버전을 선택해주세요.'
_selectLang = '설치 언어를 선택해주세요.'
_checkingRequest = '요청사항 확인 중이에요.\n잠시후 아래 말풍선을 눌러주세요.'
_doneThinking = '생각 다 끝났나요?'

# 오류 안내 메시지 (raise Exception)
_errorTitle = '[테스트] [오류 안내]\n'
_errorSSflex = '상상플렉스 커뮤니티\n(https://www.ssflex.co.kr/community/open)\n문의 부탁드립니다.'