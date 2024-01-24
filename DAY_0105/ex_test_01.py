# -------------------------------------------------------------------------
# [실습 1] 두 개의 정수를 입력 받은 후 사칙 연산 수행 결과를 반환하는 기능의 함수를 정의
# 함수이름 : fourCalc
# 매개변수 : n1, n2
# 반환결과 :사칙 연산 결과
# -------------------------------------------------------------------------

def fourCalc(n1, n2):
    return n1+n2, n1-n2, n1*n2, n1/n2 if n2 else '0으로 나눌 수 없음'

fourCalc(5,2)
# -------------------------------------------------------------------------
# [실습 2] 문자열을 16진수 코드 값으로 변환 후 반환하는 함수를 정의
#         함수이름 : getCode
#         매개변수 : message
#         반환결과 : str
# -------------------------------------------------------------------------
def getCode(message):
    ret = ''
    for msg in message:
        ret += hex(ord(msg))  # hex의 반환 값의 타입은 str이다.
    return ret
print(getCode('love'))