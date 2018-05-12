import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform
from scipy.cluster import hierarchy


data=pd.read_excel('D:/Jupyter/Data/metro.xlsx')
names=data['Название']
data=data.set_index(names)
distance=data['Расстояние м']
openYear=data['Год открытия']
passFlow=data['Пассажиропоток']
depth=data['Глубина заложения']

dist=squareform(pdist(data, metric='cityblock')) #Манхеттенская метрика
#dist=pdist(data, metric='euclidean') #Евклидова метрика
#dist=pdist(data, metric='seuclidean') #квадрат Евклидовой метрики

cluster=hierarchy.linkage(dist, method='single') #ближний сосед
#cluster=hierarchy.linkage(dist, method='complete') #дальний сосед
#cluster=hierarchy.linkage(dist, method='centroid') #центроидный
#cluster=hierarchy.linkage(dist, method='ward') #алгоритм Уорда

def hierarchy_draw(Z, level):
    """Рисуем дендрограмму и сохраняем её"""
    plt.figure()
    hierarchy.dendrogram(Z, color_threshold=level, leaf_font_size=5, count_sort=True)
    plt.show()
    
#hierarchy.dendrogram(cluster, labels=data.index, leaf_font_size=5, count_sort=True)
df=pd.DataFrame(dist, columns=np.arange(0,30)) #делаем дата-фрейм чтоб удобнее было читать
print('Матрица расстояний: \n',df)
hierarchy_draw(cluster, 300) #рисуем дендрограмму

"""fig=plt.figure()
ax = Axes3D(fig)
ax.scatter(cluster[:,0], cluster[:,1], cluster[:,2], c='g', marker='^')
plt.xlabel('1 элемент')
plt.ylabel('2 элемент')
plt.title('Диаграмма рассеяния')"""
