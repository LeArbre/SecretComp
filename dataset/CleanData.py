#-*-coding:utf-8-*- 
import pandas as pd 
import numpy as np
import pickle

# 如果csv文件无列标题,即第一行为数据
# 参数加 header = None声明无标题 
# 或加 names = [str1,str2,str3,...]自定义标题

# user_view
view = pd.read_csv('user_view.txt',names=['uid','sid','date'])
v2 = pd.read_csv('extra_user_view.txt',names=['uid','sid','date'])

# 合并两个数据
view = view.append(v2,ignore_index=True)
del v2
# # 对字符串数据切片（取0到-9）,将日期精确到天
# view.date = view.date.str.slice(0,-9)
# 按date排序
view = view.sort_values(by='date')
view.to_csv('view_sorted.txt',index=False)

# shop
shop = pd.read_csv('shop_info.txt',names=['sid','city','locid','per_pay','score','cmt','level','c1','c2','c3'])
shop.score = shop.score.fillna(-1)
shop.cmt = shop.cmt.fillna(-1)
shop.c1 = shop.c1.fillna(u'无')
shop.c2 = shop.c2.fillna(u'无')
shop.c3 = shop.c3.fillna(u'无')

city = shop.city.value_counts().index.tolist()
citymap = {city[i]:i for i in range(len(city))}

c1 = shop.c1.value_counts().index.tolist()
c1map = {c1[i]:i for i in range(len(c1))}

c2 = shop.c2.value_counts().index.tolist()
c2map = {c2[i]:i for i in range(len(c2))}

c3 = shop.c3.value_counts().index.tolist()
c3map = {c3[i]:i for i in range(len(c3))}

f = open('maps.pkl','w')
f2 = open('maps.txt','w')
for i in [citymap,c1map,c2map,c3map]:
	f2.writelines("map: \n")
	for j in i:
		f2.writelines(j+" : "+str(i[j])+'\n')
	pickle.dump(i,f)
f.close()
f2.close()

shop.city = shop.apply(lambda x: citymap[x.city],axis=1)
shop.c1 = shop.apply(lambda x: c1map[x.c1],axis=1)
shop.c2 = shop.apply(lambda x: c2map[x.c2],axis=1)
shop.c3 = shop.apply(lambda x: c3map[x.c3],axis=1)
shop = shop.drop('sid',axis=1)
shop = shop.astype(int).as_matrix()
np.save('shop',shop)


# user_pay
pay = pd.read_csv('user_pay.txt',names=['uid','sid','date'])
pay = pay.sort_values(by='date')
pay.to_csv('pay_sorted.txt',index=False)

# 对字符串数据切片（取0到-9）,将日期精确到天
pay.date = pay.date.str.slice(0,-9)
# 日期精确到天
date = list(set(pay.date))
date.sort()
datemap = {date[i]:i for i in range(len(date))}

# DataFrame -> numpy
pay['sid'] = pay['sid'].astype(int)
pay['uid'] = pay['uid'].astype(int)
plist = pay.as_matrix()


# payment per day
sid = shop.sid.astype(int).tolist()
ppd = np.zeros((len(date),len(sid)))

def creatPpd(item):
	global ppd,datemap
	ppd[datemap[item[2]]][item[1]-1] = ppd[datemap[item[2]]][item[1]-1] + 1

# map函数遍历plist
map(creatPpd,plist)

ppd = pd.DataFrame(ppd,index=date,columns=sid)
ppd.to_csv('pay_per_day.txt')
# 下次读取时，由于第0列为index
# 加参数index_col=0
ppd = pd.read_csv('pay_per_day.txt',index_col=0)

# [svc.fit(X_digits[train], y_digits[train]).score(X_digits[test], y_digits[test]) for train, test in kfold] 
