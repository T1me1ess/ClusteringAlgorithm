import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv('Fortune 500 2017 - Fortune 500.csv', encoding='utf-8')
remove_columns =['Rank','Employees','Website','Hqlocation','Hqaddr','Hqcity','Hqzip', 'Hqtel',
                 'Hqstate','Hqaddr','Ceo','Ceo-title', 'Address', 'Ticker','Sector','Industry',
                 'Fullname', 'Revenues', 'Revchange','Prftchange','Totshequity']
df = df.drop(columns= remove_columns,axis = 1)
print(df.columns)
with open('data_new.csv') as csvfile:
    reader = csv.reader(csvfile)
    print(type(reader))

data = pd.read_csv('data_new.csv', encoding='utf-8')
with open('news_data.txt', 'a+', encoding='utf-8') as f:
    for line in data.values:
        f.write((str(line[0]) + ',' + str(line[1]) + '\n'))
x = []
f = open('news_data.txt', 'r')
#Method1 library from SKlearn KMeans
for line in f:
    x.append(np.array(line.split(','), dtype = np.string_).astype(np.float64))

kmeans = KMeans(n_clusters = 3, random_state = 0).fit(x)

colors = ['red', 'green', 'blue']

for i, cluster in enumerate(kmeans.labels_):
    plt.scatter(x[i][0], x[i][1], color=colors[cluster])
plt.show()

#Method2 General algorithm of KMeans
# k = 3
# rnd = 0
# ROUND_LIMIT = 10
# THRESHOLD = 1e-10
# datas = []
# clusters = []
#
# for line in f:
#     datas.append(np.array(line.split(','), dtype = np.string_).astype(np.float64))
#
# mean_vectors = random.sample(datas, k)
#
# while True:
#     rnd += 1
#     change = 0
#     clusters = []
#     for i in range(k):
#         clusters.append([])
#     for melon in datas:
#         c = np.argmin(
#             list(map( lambda vec: np.linalg.norm(melon - vec, ord = 2), mean_vectors))
#         )
#         clusters[c].append(melon)
#
#     for i in range(k):
#         new_vector = np.zeros((1,2))
#         for melon in clusters[i]:
#             new_vector += melon
#         new_vector /= len(clusters[i])
#
#         change += np.linalg.norm(mean_vectors[i] - new_vector, ord = 2)
#         mean_vectors[i] = new_vector
#
#     if rnd > ROUND_LIMIT or change < THRESHOLD:
#         break
#
# print('最终迭代%d轮'%rnd)
#
# colors = ['red', 'green', 'blue']
#
# for i, col in zip(range(k), colors):
#     for melon in clusters[i]:
#         plt.scatter(melon[0], melon[1], color = col)
#
# plt.show()
#
