import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch


plt.rcParams['axes.unicode_minus'] = False  # 负值显示

df = pd.read_csv('Fortune 500 2017 - Fortune 500.csv', encoding='utf-8', engine='python')  # 解决中文乱码
remove_columns =['Rank','Employees','Website','Hqlocation','Hqaddr','Hqcity','Hqzip', 'Hqtel',
                 'Hqstate','Hqaddr','Ceo','Ceo-title', 'Address', 'Ticker','Sector','Industry',
                 'Fullname', 'Revenues', 'Revchange','Prftchange','Totshequity']
df = df.drop(columns= remove_columns,axis = 1)



name = df['Title'].values.reshape(df['Title'].values.shape[0], 1)  # 提取数据并转置
datax = df['Profits'].values.reshape(df['Profits'].values.shape[0], 1)
datay = df['Assets'].values.reshape(df['Assets'].values.shape[0], 1)
print(name)
print(datax)
print(datay)

# fig1 = plt.figure(figsize=(10, 10))  # 新建画布
# ax = fig1.add_subplot(1, 1, 1)
# ax.scatter(datax, datay, marker='*', color='c', label='3', s=30)  # 绘制散点图
# ax.set_title("Distribution point map")
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')  # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
# ax.spines['bottom'].set_position(('data', 0))  # 指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
# ax.spines['left'].set_position(('data', 0))
# # 为点添加标签
# for i in range(50):
#     ax.text(datax[i], datay[i], df['Title'].values[i], fontsize=1, color="r", style="italic")
# plt.show()
# plt.close()
# # 生成点与点之间的距离矩阵, 这里用的欧氏距离: euclidean
# # X：根据什么来聚类，这里结合总体情况 Profits 与平均情况 Assets 两者
# disMat = sch.distance.pdist(X=df[['Profits', 'Assets']], metric='euclidean')
# # 进行层次聚类: 计算距离的方法使用 ward 法
# Z = sch.linkage(disMat, method='ward')
# # 将层级聚类结果以树状图表示出来并保存
# # 需要手动添加标签。
# # P = sch.dendrogram(Z, labels=name)
# P = sch.dendrogram(Z, labels=df.Title.tolist())
# plt.show()
