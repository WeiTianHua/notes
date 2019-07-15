# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
测试金融相关方法
'''
import numpy as np

# 将1000元以1%的年利率存银行5年, 每年加
# 存100元, 到期后本息一共多少钱?
# 求金融终值 fv
fv = np.fv(0.01, 5, -100, -1000)
print(fv)

# 将多少钱以1%的年利率存入银行5年, 每年
# 加存100元,到期后本息合计fv元.
# 求金融现值 pv
pv = np.pv(0.01, 5, -100, fv)
print(pv)

# 净现值
# 将1000元以1%的年利率存入银行5年, 每年加存
# 100元, 相当于现在要一次性存入多少钱
npv = np.npv(0.01, [-1000, -100,
                    -100, -100, -100, -100])
print(npv)

# 每期支付
# 以1%的利率从银行贷款1000元, 分5年还清.
# 平均每年还多少钱?
pmt = np.pmt(0.01, 5, 1000)
print(pmt)
pmt = np.pmt(0.0441 / 12, 360, 1000000)
print(pmt)

# 以4.41%/12的利率从银行贷款100万元,
# 平均每期还pmt元, 多少年还清?
nper = np.nper(0.0441 / 12, pmt, 1000000)
print(nper)