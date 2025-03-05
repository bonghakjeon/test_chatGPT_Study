# TODO : 파이썬 예외처리(Python Exception) 기능 구현 (2025.02.28 minjae)
# 참고 URL - https://docs.python.org/ko/3.6/tutorial/errors.html
# 참고 2 URL - https://dojang.io/mod/page/view.php?id=2400
# 참고 3 URL - https://loklee9.tistory.com/117
# 참고 4 URL - https://youtu.be/M63Y_Sdu71k?si=Dyay0l1ZYRMIBiP1

try:
    for i in range(1, int(input('숫자를 입력하세요~: '))+1):
        print(i)
except Exception as e:   # 예외가 발생했을 때 변수 e에다 넣고 아래 코드 실행됨
    print('잘못된 값을 입력하셨습니다')
    print(e)