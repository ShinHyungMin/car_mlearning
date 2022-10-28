from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import pandas as pd

# 연봉과 자동차 csv 파일로부터 읽기
table = pd.read_csv("salarycar.csv")

# 컬렴(열)을 자르고 정규화하기
label = table["label"]
s = table["salary"] / 5500   # 최대 5500만원 가정
c = table["car"] / 8000   # 최대 8000만원 가정

# concat : 여러개의 동일 형태 데이터 프레임을 합치기
# axis = 0인 경우, 세로(위+아래) 병합
# axis = 1인 경우, 가로(왼쪽+오른쪽) 병합
wh = pd.concat([s, c], axis=1)

# 학습데이터와 테스트 데이터 분할(75%, 25%)
# test_size : 테스트 데이터 셋 비율
# shuffle : 데이터를 섞을지 여부 설정
train_data, test_data, train_label, test_label = \
    train_test_split(wh, label, test_size=0.25, shuffle=True)
# 학습
clf = svm.SVC()
clf.fit(train_data, train_label)

# 예측
predict = clf.predict(test_data)

# 결과
ac_score = metrics.accuracy_score(test_label, predict)
print(f"정확도 : {ac_score}")
