# TODO : 파이썬 raise 문법 사용하여 강제로 예외처리(Python Exception) 기능 구현 (2025.02.28 minjae)
# 참고 - C#의 throw new Exception('강제로 예외처리'); 와 같은 기능이다.
# 참고 URL - https://docs.python.org/ko/3.6/tutorial/errors.html
# 참고 2 URL - https://dojang.io/mod/page/view.php?id=2400
# 참고 3 URL - https://loklee9.tistory.com/117
# 참고 4 URL - https://youtu.be/M63Y_Sdu71k?si=Dyay0l1ZYRMIBiP1


# 오류 메시지 (예시)
# An exception flew by!
# Traceback (most recent call last):
#   File "d:\bhjeon\test_chatGPT\ch15\test\raiseException.py", line 5, in <module>
#     raise NameError('HiThere')
# NameError: HiThere
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise