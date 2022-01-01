import pandas as pd

from nltk.tokenize import word_tokenize as wt
from sklearn.feature_extraction.text import CountVectorizer

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

stopword = ['so', 'sau', 'sinh', 'sao', 
			'luong', 'lam',
			'cua', 'cach', 'cham', 'can', 'co', 'cong', 
			'tuong', 'tinh', 'the', 'thi',  
			'duong', 'de', 'do', 
			'bao', 'bang', 'bat', 'buoc', 'bi',
			'nhieu', 'nhung', 'nhu', 'nao', 'nhan', 'neu',
			'khi', 'khong', 'kem', 
			'phai', 
			'gi', 'gom',
			'ai',
			'vien',
			'xet', 
			]

dataset = pd.read_csv("dataset.csv")			

data = []

for i in range(dataset.shape[0]):
	question = dataset.iloc[i, 0]
	
	tokenize_question = wt(question)

	question_processed = []
	for word in tokenize_question:
		if word not in set(stopword):
			question_processed.append(word)

	question_text = " ".join(question_processed)
	data.append(question_text)


matrix = CountVectorizer(max_features = 1000)
X = matrix.fit_transform(data).toarray()
y = dataset.iloc[:,1]

X_train, X_test, y_train, y_test = train_test_split(X, y)

k_range = range(1, 26)
scores = {}
scores_list = []
"""
for k in k_range:
	knn = KNeighborsClassifier(n_neighbors = k, algorithm = 'ball_tree', leaf_size = 30, metric = 'minkowski', metric_params = None, n_jobs = 1, p = 2, weights = 'distance')
	knn.fit(X_train, y_train)
	y_pred = knn.predict(X_test)
	scores[k] = metrics.accuracy_score(y_test, y_pred)
	scores_list.append(metrics.accuracy_score(y_test, y_pred))


import matplotlib.pyplot as plt
plt.plot(k_range, scores_list)
plt.xlabel('Value of k for KNN')
plt.ylabel('Testing Accuracy')
plt.show()
"""
knn = KNeighborsClassifier(n_neighbors = 2, algorithm = 'ball_tree', leaf_size = 30, metric = 'minkowski', metric_params = None, n_jobs = 1, p = 2, weights = 'distance')
knn.fit(X_train, y_train)
question_input = "xin chao, ban la ai"
newData_Unseen = matrix.transform([question_input].toarray())
print(newData_Unseen.getnnz()) # new kq <= 2 => cau hoi khong co trong tap du lieu 
# nho bo sung phan nay vao ham main.py
