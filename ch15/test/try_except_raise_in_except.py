# TODO : 파이썬 예외처리(Python Exception) 기능 구현 (2025.02.28 minjae)
# 참고 URL - https://docs.python.org/ko/3.6/tutorial/errors.html
# 참고 2 URL - https://dojang.io/mod/page/view.php?id=2400
# 참고 3 URL - https://loklee9.tistory.com/117
# 참고 4 URL - https://youtu.be/M63Y_Sdu71k?si=Dyay0l1ZYRMIBiP1

# 현재 예외를 다시 발생시키기
# 이번에는 try except에서 처리한 예외를 다시 발생시키는 방법입니다. 
# except 안에서 raise를 사용하면 현재 예외를 다시 발생시킵니다(re-raise).
# 다음은 함수 three_multiple 코드 블록의 예외를 다시 발생시킨 뒤 
# 상위 코드 블록에서 예외를 처리합니다.
# C# throw; 와 비슷한 기능이다.

# three_multiple 함수 안에서 발생한 예외를 함수 안의 except에서 한 번 처리하고, 
# raise로 예외를 다시 발생시켜서 상위 코드 블록으로 넘겼습니다. 
# 그다음에 함수 바깥의 except에서 예외를 처리했습니다. 이런 방식으로 같은 예외를 계속 처리해줄 수 있습니다.
# 참고로 raise만 사용하면 같은 예외를 상위 코드 블록으로 넘기지만 raise에 다른 예외를 지정하고 에러 메시지를 넣을 수도 있습니다.

def three_multiple():
    try:
        x = int(input('3의 배수를 입력하세요: '))
        if x % 3 != 0:                                 # x가 3의 배수가 아니면
            raise Exception('3의 배수가 아닙니다.')     # 예외를 발생시킴
        print(x)
    except Exception as e:                             # 함수 안에서 예외를 처리함
        print('three_multiple 함수에서 예외가 발생했습니다.', e)
        raise    # raise로 함수 three_multiple의 현재 예외를 다시 발생시켜서 함수 three_multiple 호출한 상위 코드 블록으로 넘김
 
try:
    three_multiple()
except Exception as e:                                 # 하위 코드 블록에서 예외가 발생해도 변수 e에다 넣고 아래 코드 실행됨
    print('스크립트 파일에서 예외가 발생했습니다.', e)