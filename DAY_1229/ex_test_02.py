# ---------------------------------------------------------------
# [실습 1] 임의의 숫자 데이터 7개를 저장한 리스트를 생성
#         리스트에 원소를 하나씩 화면에 출력하세요.
# ---------------------------------------------------------------
nums = [12, 23, 37, 45, 59, 60, 78]
print(nums[0], nums[1], nums[2], nums[3], nums[4], nums[5], nums[6], sep = '\n')
print()

# ---------------------------------------------------------------
# [실습 2] 아래 리스트에서 원소를 화면에 한 줄에 한 개씩 출력하세요.
# ---------------------------------------------------------------
datas = [ [10, 20], [40, 50], [70, 80, 90]]
print(datas[0][0], datas[0][1], datas[1][0], datas[1][1], datas[2][0], datas[2][1], sep = '\n')
print()

# ---------------------------------------------------------------
# [실습 3]  좋아하는 계절과 월(month)을 입력 받은 후 각각 변수에
#          저장하세요. 변수명은 season, month 입니다.
#          input() 함수는 1개만 사용 하세요.
# ---------------------------------------------------------------

season_month = input('좋아하는 계절과 월 : ')
season = season_month.split()[0]
month = season_month.split()[1]
print()
# ---------------------------------------------------------------
# [실습 4] 1~20으로 구성된 정수 리스트를 생성하세요.
#         * 3의 배수 인덱스에 해당하는 정수만 출력하세요.
#         * 3의 배수 인덱스에 해당하는 정수의 합계를 출력하세요.
# ---------------------------------------------------------------

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(nums[::3][0]-1)
print(nums[::3][1]-1)
print(nums[::3][2]-1)
print(nums[::3][3]-1)
print(nums[::3][4]-1)
print(nums[::3][5]-1)
print(nums[::3][6]-1)
print()
print(sum(nums[::3]))
