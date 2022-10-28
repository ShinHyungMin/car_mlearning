import matplotlib.pyplot as plt
import pandas as pd

table = pd.read_csv("salarycar.csv", index_col=2)
# print(table)

# 그래프 그리기
fig = plt.figure()
# 1, 1, 1 => 1*1 그리드, 첫번째 서블 플롯
ax = fig.add_subplot(1, 1, 1)

# 데이터 프레임으로부터 특정 컬럼의 값 가져오기
# 데이터 프레임 인덱싱 방법
# df.loc["row", "column"]
g = table.loc["general"]
o = table.loc["overspending"]
r = table.loc["reasonable consumption"]

# 서브 플롯 전용 - 지정한 레이블을 임의의 색으로 칠하기
def scatter(label, color):
    data = table.loc[label]
    # 해당하는서브플롯.scatter(x축위치, y축위치)
    # ax.scatter(59, 194)
    ax.scatter(data["salary"], data["car"], c=color, label=label)

scatter("general", "yellow")
scatter("overspending", "red")
scatter("reasonable consumption", "green")

ax.legend()     # 범례(데이터 종류를 나타내는 텍스트) 표시
plt.savefig("salarycar.png")     # 이미지 저장
