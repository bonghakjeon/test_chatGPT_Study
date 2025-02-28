# TODO : 파이썬 예외처리(Python Exception) 기능 구현 (2025.02.28 minjae)
# 유튜브 참고 URL - https://youtu.be/M63Y_Sdu71k?si=frcOwEpjNA7C1n3p
# 참고 URL - https://docs.python.org/ko/3.6/tutorial/errors.html
# 참고 2 URL - https://dojang.io/mod/page/view.php?id=2400
# 참고 3 URL - https://loklee9.tistory.com/117
# 참고 4 URL - https://youtu.be/M63Y_Sdu71k?si=Dyay0l1ZYRMIBiP1

# 특정 오류(예외) 감지하는 예외처리(try: ~ except:) 코드 구현
try:   # try: 문 안에는 어떤 오류가 발생할 수 있는 여지가 있는 내용이 들어가 있는 코드가 실행된다.
    # 파이썬 파일 "01-input.py" 컴파일 실행시 
    # input 함수 사용해서 문자열 "나이를 입력하세요." 출력되고
    # 사용자가 나이를 입력하면 
    # 입력한 나이는 문자열 -> int로 형변환 처리 및 변수 age에 할당 
    # 주의사항 - 사용자가 나이를 입력할 때 숫자를 입력한다는 보장이 없고, 일반 텍스트로 입력해서 오류가 발생할 수 있다.
    # 오류 메시지 (예시) ValueError: invalid literal for int() with base 10: 'ㅁㅇㄴㄹ'
    age = int(input("나이를 입력하세요.")) 

    # 파이썬 파일 "01-input.py" 컴파일 실행시 
    # input 함수 사용해서 문자열 "나이를 입력하세요." 출력되고
    # 사용자가 이름을 입력 -> 함수 encode 호출해서 아스키("ascii") 형태로 인코딩 처리 후 변수 ename에 저장 
    ename = input("영문 이름을 입력하세요.").encode("ascii")
# 사용자가 이름을 한글로 입력 후 함수 encode 호출해서 아스키("ascii") 형태로 인코딩 처리 오류(예외) 발생시 print()문 호출하여 오류 메시지 출력 
# 주의사항 - 한글 이름의 경우 아스키("ascii") 형태로 인코딩 처리 불가하여 UnicodeEncodeError 오류 발생함.
except UnicodeEncodeError:   
    # 오류 메시지 (예시) - Traceback (most recent call last):
    # File "<stdin>", line 1, in <module>
    # UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-4: ordinal not in range(128)
    print("이름은 영문으로 작성해야 합니다.")
except ValueError: # 사용자가 "나이를 입력하세요." 옆에 숫자가 아닌 문자열 입력 시 ValueError: 오류 발생함.
    # 오류 메시지 (예시) - Traceback (most recent call last):
    # File "<stdin>", line 1, in <module>
    # ValueError: invalid literal for int() with base 10: 'ㅁㅁㅁㅁ'
    print("나이를 정수 형태로 입력하세요.")