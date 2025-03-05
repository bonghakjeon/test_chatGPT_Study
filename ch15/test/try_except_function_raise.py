# TODO : 파이썬 예외처리(Python Exception) 기능 구현 (2025.02.28 minjae)
# 참고 URL - https://docs.python.org/ko/3.6/tutorial/errors.html
# 참고 2 URL - https://dojang.io/mod/page/view.php?id=2400
# 참고 3 URL - https://loklee9.tistory.com/117
# 참고 4 URL - https://youtu.be/M63Y_Sdu71k?si=Dyay0l1ZYRMIBiP1

# three_multiple 함수는 안에 try except가 없는 상태에서 raise로 예외를 발생시켰습니다. 
# 이렇게 되면 함수 바깥에 있는 except에서 예외가 처리됩니다. 
# 즉, 예외가 발생하더라도 현재 코드 블록에서 처리해줄 except가 없다면 except가 나올 때까지 계속 상위 코드 블록으로 올라갑니다.
# 만약 함수 바깥에도 처리해줄 except가 없다면 코드 실행은 중지되고 에러가 표시됩니다. 
# 다음은 파이썬 셸에서 직접 three_multiple 함수를 호출했으므로 except가 없는 상태입니다.
# >>> three_multiple()
# 3의 배수를 입력하세요: 5 (입력)
# Traceback (most recent call last):
#   File "<pyshell#5>", line 1, in <module>
#     three_multiple()
#   File "C:\project\try_except_function_raise.py", line 4, in three_multiple
#     raise Exception('3의 배수가 아닙니다.')    # 예외를 발생시킴
# Exception: 3의 배수가 아닙니다.


def three_multiple():
    x = int(input('3의 배수를 입력하세요: '))
    if x % 3 != 0:                                 # x가 3의 배수가 아니면
        raise Exception('3의 배수가 아닙니다.')     # 예외를 발생시킴
    print(x)                                       # 현재 함수 안에는 except가 없으므로
                                                   # 예외를 함수 three_multiple 호출한 상위 코드 블록으로 넘김
 
try:
    three_multiple()
except Exception as e:                             # 하위 코드 블록(함수 three_multiple 안의 로직)에서 예외가 발생해도 변수 e에다 넣고 아래 코드 실행됨
    print('예외가 발생했습니다.', e)