# TODO : 파이썬 예외처리(Python Exception) 기능 구현 (2025.02.28 minjae)
# 참고 URL - https://docs.python.org/ko/3.6/tutorial/errors.html
# 참고 2 URL - https://dojang.io/mod/page/view.php?id=2400
# 참고 3 URL - https://loklee9.tistory.com/117
# 참고 4 URL - https://youtu.be/M63Y_Sdu71k?si=Dyay0l1ZYRMIBiP1

try:
    x = int(input('3의 배수를 입력하세요: '))
    if x % 3 != 0:                                # x가 3의 배수가 아니면
        raise Exception('3의 배수가 아닙니다.')    # 예외를 발생시킴
    print(x)
except Exception as e:                            # 예외가 발생했을 때 변수 e에다 넣고 아래 코드 실행됨
    print('예외가 발생했습니다.', e)