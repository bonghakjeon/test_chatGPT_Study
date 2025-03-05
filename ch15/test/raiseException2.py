# TODO : 파이썬 raise 문법 사용하여 강제로 예외처리(Python Exception) 기능 구현 (2025.02.28 minjae)
# 참고 - C#의 throw new Exception('강제로 예외처리'); 와 같은 기능이다.
# 참고 URL - https://docs.python.org/ko/3.6/tutorial/errors.html
# 참고 2 URL - https://dojang.io/mod/page/view.php?id=2400
# 참고 3 URL - https://loklee9.tistory.com/117
# 참고 4 URL - https://youtu.be/M63Y_Sdu71k?si=Dyay0l1ZYRMIBiP1


try:
    raise Exception('spam', 'eggs')
except Exception as e:   # 예외가 발생했을 때 변수 e에다 넣고 아래 코드 실행됨
    print(type(e))    # the exception instance
    print(e.args)     # arguments stored in .args
    print(e)          # __str__ allows args to be printed directly,
                      # but may be overridden in exception subclasses
    x, y = e.args     # unpack args
    print('x =', x)
    print('y =', y)