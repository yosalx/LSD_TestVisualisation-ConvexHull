import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from convexhull import myConvexHull

#load data
iris = datasets.load_iris()
wine = datasets.load_wine()
b_cancer = datasets.load_breast_cancer()

#create a DataFrame
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['Target'] = pd.DataFrame(iris.target)

wine_df = pd.DataFrame(iris.data, columns=iris.feature_names)
wine_df['Target'] = pd.DataFrame(iris.target)

bc_df = pd.DataFrame(iris.data, columns=iris.feature_names)
bc_df['Target'] = pd.DataFrame(iris.target)

#Visualisation on convex hull implementasion using iris data set
import matplotlib.pyplot as plt
plt.figure(figsize = (10, 6))
colors = ['b','r','g']
plt.title('petal width vs petal length')

#choose which atribute to be test
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
for i in range(len(iris.target_names)):
    bucket = iris_df[iris_df['Target'] == i]
    bucket = bucket.iloc[:,[0,1]].values
    hull = myConvexHull(bucket)
    plt.scatter(bucket[:, 0], bucket[:, 1], label=iris.target_names[i])
    for j in range(len(hull)-1):
        plt.plot((hull[j][0], hull[j+1][0]), (hull[j][1], hull[j+1][1]), colors[i])
plt.legend()
plt.show()
