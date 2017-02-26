#-*-coding:utf-8-*- 
import pandas as pd 
import numpy as np

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

shop = pd.read_csv('shop_info.txt',names=['sid','city','locid','per_pay','score','cmt','level','c1','c2','c3'])
shop.to_csv('shop.txt',index = False)


pay = pd.read_csv('user_pay.txt',names=['uid','sid','date'])
pay = pay.sort_values(by='date')
pay['sid'] = pay['sid'].astype(int)
pay['uid'] = pay['uid'].astype(int)
pay.to_csv('pay_sorted.txt',index=False)


date = set()
for i in pay['date']:
	date.add(i[0:-9])

# payment per day
ppd = np.zeros((len(date),2000))
dic = {}
for i in range(len(date)):
	dic[date[i]] = i

plist = pay.as_matrix()

def creatPpd(plist):
	global ppd,dic
	ppd[dic[plist[2][0:-9]]][plist[1]-1] = ppd[dic[plist[2][0:-9]]][plist[1]-1] + 1

map(creatPpd,plist)

pd.DataFrame(ppd,index=date,columns=range(1,2001)).to_csv('pay_per_day.txt')

# 下次读取时，由于第0列为index
# 加参数index_col=0
ppd = pd.read_csv('pay_per_day.txt',index_col=0)
