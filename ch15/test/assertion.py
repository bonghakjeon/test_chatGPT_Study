# TODO : 파이썬 예외처리(Python Exception) 기능 구현 (2025.02.28 minjae)
# 참고 URL - https://docs.python.org/ko/3.6/tutorial/errors.html
# 참고 2 URL - https://dojang.io/mod/page/view.php?id=2400
# 참고 3 URL - https://loklee9.tistory.com/117
# 참고 4 URL - https://youtu.be/M63Y_Sdu71k?si=Dyay0l1ZYRMIBiP1

# assert로 예외 발생시키기
# 예외를 발생시키는 방법 중에는 assert를 사용하는 방법도 있습니다. 
# assert는 지정된 조건식이 거짓일 때 AssertionError 예외를 발생시키며 조건식이 참이면 그냥 넘어갑니다. 
# 보통 assert는 나와서는 안 되는 조건을 검사할 때 사용합니다.
# 다음은 3의 배수가 아니면 예외 발생, 3의 배수이면 그냥 넘어갑니다.
# assert는 디버깅 모드에서만 실행됩니다. 
# 특히 파이썬은 기본적으로 디버깅 모드이며(__debug__의 값이 True) 
# assert가 실행되지 않게 하려면 python에 -O 옵션을 붙여서 실행합니다(영문 대문자 O).

x = int(input('3의 배수를 입력하세요: '))
assert x % 3 == 0, '3의 배수가 아닙니다.'    # 3의 배수가 아니면 예외 발생, 3의 배수이면 그냥 넘어감
print(x)

