#-*-coding:utf-8-*- 
import pandas as pd 

# 如果csv文件无列标题,即第一行为数据
# 参数加 header = None声明无标题 
# 或加 names = [str1,str2,str3,...]自定义标题
view = pd.read_csv('user_view.txt',names=['uid','sid','date'])
v2 = pd.read_csv('extra_user_view.txt',names=['uid','sid','date'])

# 合并两个数据
view = view.append(v2,ignore_index=True)
del v2
# 按date排序
view = view.sort_values(by='date')
view.to_csv('view_sorted.txt',index=False)

pay = pd.read_csv('user_pay.txt',names=['uid','sid','date'])
pay = pay.sort_values(by='date')
paydate = pay[pay['date']>='2016-02-01 00:00:00']
pay.to_csv('pay_sorted.txt',index=False)
