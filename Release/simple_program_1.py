yourname = input("Type Your Name> ") 
#   yourname이라는 변수에다가 자기 자신의 이름을 넣는다 (str 형식)

birthday = input("Type Your 6-digit birthday/year > ") 
#   birthday라는 변수에다가 자기 자신의 6자리 생년월일을 넣는다 (*str 형식* (숫자 int형식이 아니다!))

gender = input("What is your gender? (M/W) > ")
#   gender이라는 변수에다가 자기 자신의 성별을 적는다 (str 형식)

int_b = int(birthday)
#   birthday라는 문자열 변수를 숫자 형식으로 바꾼다 (str -> int)

print(yourname, int_b, gender)
#   yourname, int_b, gender 변수를 출력한다