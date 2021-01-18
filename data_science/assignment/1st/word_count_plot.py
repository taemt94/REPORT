import sys
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

n = [int(word_counts.split('\t')[1].rstrip('\n')) for word_counts in sys.stdin]
k = range(1, 1001)

plt.plot(k, n)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('log(k)')
plt.ylabel('log(n)')
plt.title("Zipf's law")
plt.grid()

plt.savefig('h01_김태산_20143211_plot.png', dpi=150)

'''
지프의 법칙 n = c * (k ** (-s))에서 양변에 로그를 취하면
log(n) = -s * log(k) + log(c)이므로 log(k)의 log(n)에 대한 선형 모델입니다.
따라서 이를 선형회귀 모델(LinearRegression)에 대입하여 모델을 학습시킨 후
모델의 편향 intercept와 가중치 coef를 통해 log(c)와 -s 값을 구하였습니다.
c에 지수 계산을 하고 -s에 절댓값 취하여 c와 s 값을 구하였습니다.
'''
log_k = np.log(np.array([[x for x in k]]).reshape(-1, 1))
log_n = np.log(np.array([[y for y in n]]).reshape(-1, 1))

lin_reg = LinearRegression()
lin_reg.fit(log_k, log_n)

print(f"s: {abs(lin_reg.coef_[0][0])}")
print(f"c: {np.exp(lin_reg.intercept_)[0]}")
