# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# パラメータ設定
mu = 0        # 平均
sigma = 1     # 標準偏差

# x軸データ生成
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)

# 正規分布（確率密度関数）
y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-((x - mu)**2) / (2 * sigma**2))

# 描画
plt.figure(figsize=(8, 5))
plt.plot(x, y, label=f'N({mu}, {sigma}^2)')
plt.title('Normal Distribution')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.grid()
plt.legend()

# 保存
plt.savefig("normal_distribution.png")