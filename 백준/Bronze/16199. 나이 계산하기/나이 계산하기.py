import sys


birth_year, birth_month, birth_day  = map(int, sys.stdin.readline().strip().split())
current_year, current_month, current_day = map(int, sys.stdin.readline().strip().split())


if (current_month > birth_month) or (current_month == birth_month and current_day >= birth_day):
    man_age = current_year - birth_year
else:
    man_age = current_year - birth_year - 1

# 세는나이 계산
se_age = current_year - birth_year + 1

# 연나이 계산
yeon_age = current_year - birth_year

# 결과 출력
print(man_age)
print(se_age)
print(yeon_age)