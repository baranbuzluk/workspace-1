import matplotlib.pyplot as plt
import pandas as pd

# Loading ve slicing dataframe
#   BEGIN
csv_dframe = pd.read_csv('../datas/musteriler.csv')  # No,Cinsiyet,Yas,Hacim,Maas
x_datas_np = csv_dframe.iloc[:, 3:].values  # Hacim,Maas
# print(x_datas_np)

#   END

# Clustering the data
#   BEGIN
from sklearn.cluster import KMeans

k_means = KMeans(init='k-means++', n_clusters=3)
k_means.fit(x_datas_np)
print(k_means.cluster_centers_)
#   END

# The case when the number of n_clusters changes
#   BEGIN
results = list()
for i in range(1, 11):
    k_means = KMeans(init='k-means++', n_clusters=i, random_state=12)
    k_means.fit(x_datas_np)
    results.append(k_means.inertia_)

plt.plot(range(1, 11), results)
plt.show()
#   END
