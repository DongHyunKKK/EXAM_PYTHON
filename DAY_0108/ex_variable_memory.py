# -----------------------------------------------------------
# 참조형 변수 => 데이터의 주소 저장
# -----------------------------------------------------------
num = 12
print(f'num => {id(num)}, {type(num)}')

num = 3.
print(f'num => {id(num)}, {type(num)}')

num = 'Good'
print(f'num => {id(num)}, {type(num)}')

num1 = []
print(f'num1 => {id(num1)}, {type(num1)}')

num2 = [11, 22.1]
print(f'num => {id(num)}, {type(num)}')
print(f'num[0] => {id(num2[0])}, {type(num2[0])}')
print(f'num[1] => {id(num2[1])}, {type(num2[1])}')

# 값 변경
num2[0] = 100
print(f'num2 => {num2} : {id(num2)}, {type(num2)}')
print(f'num2[0] => {num2[0]} : {id(num2[0])}, {type(num2[0])}')

# 리스트를 다른 리스트로 변경
num1 = num2
print(f'num1 => {id(num1)}, {type(num1)}')
print(f'num2 => {id(num2)}, {type(num2)}')