import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from myConvexHull import myConvexHull

#load data
iris = datasets.load_iris()
wine = datasets.load_wine()
b_cancer = datasets.load_breast_cancer()

#create a DataFrame
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['Target'] = pd.DataFrame(iris.target)

wine_df = pd.DataFrame(wine.data, columns=wine.feature_names)
wine_df['Target'] = pd.DataFrame(wine.target)

bc_df = pd.DataFrame(b_cancer.data, columns=b_cancer.feature_names)
bc_df['Target'] = pd.DataFrame(b_cancer.target)

print("Convex Hull for Linear Separability Dataset ")
print("Choose dataset to be use")
print("1. Iris")
print("2. Wine")
print("3. Breast Cancer")
choice = int(input("Datased to be used: "))
if(choice == 1):
    data = iris
    used_df = iris_df
    print("\n")
    print("Which atribute to compare ?")
    print("1. Sepal Width vs Sepal Length")
    print("2. Petal width vs Petal Length")
    iris_atribute = int(input("Atribut to be compare: "))
    if(iris_atribute == 1):
        title = "Sepal Width vs Sepal Length"
        index_1 = 0
        index_2 = 1
    elif(iris_atribute == 2):
        title = "Petal width vs Petal Length"
        index_1 = 2
        index_2 = 3
    else:
        print("\nSorry only those two")
        exit()
elif(choice == 2):
    data = wine
    used_df = wine_df
    print("\n")
    print("Which atribute to compare ?")
    print("1. Alcohol vs Malic_acid")
    print("2. Malic_acid vs Ash")
    wine_atribute = int(input("Atribut to be compare: "))
    if(wine_atribute == 1):
        title = "Alcohol vs Malic_acid"
        index_1 = 0
        index_2 = 1
    elif(wine_atribute == 2):
        title = "Malic_acid vs Ash"
        index_1 = 1
        index_2 = 2
    else:
        print("\nSorry only those two")
        exit()
elif(choice == 3):
    data = b_cancer
    used_df = bc_df
    print("\n")
    print("Which atribute to compare ?")
    print("1. Radius vs Texture")
    print("2. Texture vs Perimeter")
    bc_atribute = int(input("Atribut to be compare: "))
    if(bc_atribute == 1):
        title = "Radius vs Texture"
        index_1 = 0
        index_2 = 1
    elif(bc_atribute == 2):
        title = "Texture vs Perimeter"
        index_1 = 1
        index_2 = 2
    else:
        print("\nSorry only those two")
        exit()
else:
    print("Sorry there are no other dataset")
    exit()

#Visualisation on convex hull implementasion using iris data set
import matplotlib.pyplot as plt
plt.figure(figsize = (10, 6))
colors = ['b','r','g']
plt.title(title)
#choose which atribute to be test
plt.xlabel(data.feature_names[index_1])
plt.ylabel(data.feature_names[index_2])
for i in range(len(data.target_names)):
    bucket = used_df[used_df['Target'] == i]
    bucket = bucket.iloc[:,[index_1,index_2]].values
    hull = myConvexHull(bucket)
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
    for j in range(len(hull)-1):
        plt.plot((hull[j][0], hull[j+1][0]), (hull[j][1], hull[j+1][1]), colors[i])
plt.legend()
plt.show()
