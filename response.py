import pandas as pd

def response(dataset, predict):
	answer = dataset.loc[dataset["label"] == predict, "answer"].iloc[0]
	return answer

"""
#test
df = pd.read_csv("response.csv")
predict = 10
output = response(df, predict)	
print(output)
"""