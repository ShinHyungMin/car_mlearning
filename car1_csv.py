# csv 파일에 무작위로 키를 생성해서 저장
import random

# 연봉대비 차 값 비율을 계산해서 레이블을 리턴하는 함수
def calc_salarycar(s, c):
    cs = c / s
    if 0.5 <= cs <= 0.7:
        return "general"
    elif cs > 0.7:
        return "overspending"
    else:
        return "reasonable consumption"


# 출력 파일 준비하기
fp = open("salarycar.csv", "w", encoding="utf-8")
fp.write("salary,car,label\r\n")

# 무작위로 데이터 생성하기
cnt = {"general":0, "overspending":0, "reasonable consumption":0}
for i in range(20000):
    s = random.randint(3500, 5500)          # 30대 평균연봉 4500 기준으로 +- 1000만원
    c = random.randint(1200, 8000)         # 소형차부터 외제차 가격까지 랜덤으로.
    label = calc_salarycar(s, c)
    # print(f"신장 : {h} \t 몸무게 : {w} \t 결과 : {label}")
    cnt[label] = cnt[label] + 1
    fp.write("{0},{1},{2}\r\n".format(s, c, label))
fp.close()
# print(cnt)
print("csv 파일 생성 완료", cnt)





