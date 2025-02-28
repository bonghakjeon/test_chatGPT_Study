# TODO : 파이썬 예외처리(Python Exception) 기능 구현 (2025.02.28 minjae)
# 유튜브 참고 URL - https://youtu.be/M63Y_Sdu71k?si=frcOwEpjNA7C1n3p
# 참고 URL - https://docs.python.org/ko/3.6/tutorial/errors.html
# 참고 2 URL - https://dojang.io/mod/page/view.php?id=2400
# 참고 3 URL - https://loklee9.tistory.com/117
# 참고 4 URL - https://youtu.be/M63Y_Sdu71k?si=Dyay0l1ZYRMIBiP1

# 오류(예외) 발생시 아래 코드 무한 반복 처리
while True:
    # 예외처리(try: ~ except:) 구현 
    try:   # try: 문 안에는 어떤 오류가 발생할 수 있는 여지가 있는 내용이 들어가 있는 코드가 실행된다.
        # 파이썬 파일 "01-input.py" 컴파일 실행시 
        # input 함수 사용해서 문자열 "나이를 입력하세요." 출력되고
        # 사용자가 나이를 입력하면 
        # 입력한 나이는 문자열 -> int로 형변환 처리 및 변수 age에 할당 
        # 주의사항 - 사용자가 나이를 입력할 때 숫자를 입력한다는 보장이 없고, 일반 텍스트로 입력해서 오류가 발생할 수 있다.
        # 오류 메시지 (예시) ValueError: invalid literal for int() with base 10: 'ㅁㅇㄴㄹ'
        age = int(input("나이를 입력하세요."))
    
        if age > 18:   # 변수 age에 저장된 값이 18보다 큰경우 
            print("성인 입니다.")   # "성인 입니다." 출력 후 해당 파이썬 파일 "01-input.py" 프로그램 실행 종료  
        break
    except:   # 오류(예외) 발생시 print()문 호출하여 오류 메시지 출력 
        print("알 수 없는 문자입니다.") 
 
