import pandas as pd  # data processing -> CSV file I/O
import numpy as np  # linear algebra
from scipy import spatial
import matplotlib.pyplot as plt  # for data visualization
# from sklearn.neighbors import KNeighborsClassifier


class KNearestNeighbors:
    def __init__(self, k) -> None:
        self.k = k

    def __init__(self, k, x_data, y_data) -> None:
        self.k = k
        self.x_data = x_data
        self.y_data = y_data

    def set_k(self, k) -> None:
        self.k = k

    def set_data(self, x_data, y_data) -> None:
        self.x_data = x_data
        self.y_data = y_data

    def get_distance(self, target_x, target_y) -> None:
        self.distances = []

        for i in self.x_data:
            distance = np.sqrt(
                ((target_x - self.x_data[i]) ** 2) +
                ((target_y - self.y_data[i]) ** 2)
            )
            self.distances.append(distance)

    def predict(self, target_x, target_y) -> int:

        return 0


# load dataset CSV file
DATA_SET_URL = 'https://raw.githubusercontent.com/whitestorm2346/neural-network/main/train.csv'
pd_df = pd.read_csv(DATA_SET_URL)

# data frame for entity name and ID
pd_df0 = 0

# data frame for attributes
pd_df1 = 0

# convert to 0s and 1s based on the attribute values
pd_df1 = pd_df.iloc[:, [0, 2]]

# merge pd_df0 and pd_df1 data frame
pd_df2 = pd.concat([pd_df0, pd_df1], axis=1, sort=False)

df_array = pd_df2.to_numpy()

carDict = {}

for d in df_array:
    pass

nearest_k = 0  # k個最接近你的鄰居
selected_id = 0

print("")

neighbors = []

for neighbor in neighbors:
    print(
        str(neighbor[0]) + " | "
        + carDict[neighbor[0]][0] + " | "
        + str(neighbor[1])
    )

# https://godamber.blogspot.com/2019/07/pythoncolab.html(資料集讀取方式，若同學使用colab以外的編譯器需自行搜尋CSV檔案讀取方法)
# https://ithelp.ithome.com.tw/articles/10269826?sc=iThelpR(簡易KNN(有使用套件))
# https://www.w3schools.com/python/python_ml_knn.asp(簡易KNN(有使用套件，且有圖示))
# https://www.kaggle.com/code/prashant111/knn-classifier-tutorial/notebook(比較正規的KNN資料分析，較難)
