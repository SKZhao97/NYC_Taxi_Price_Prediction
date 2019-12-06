import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import glob
import numpy as np

def normalization(data):
	data_np = data.values #returns a numpy array
	min_max_scaler = preprocessing.MinMaxScaler()
	x_scaled = min_max_scaler.fit_transform(data_np)
	X_train_nor = pd.DataFrame(x_scaled)
	return X_train_nor

def process_data(file_name):
	print(file_name)
	pd_data = pd.read_csv(file_name)
	return pd_data

def get_data():
	subdirname = './test/'
	depthfiles = glob.glob(subdirname + '*.csv');
	frames = [process_data(f) for f in depthfiles]
	result = pd.concat(frames)
	return result

def clean_data():
	cols = [2,3,5,6,10,11,12,13]
	Y_cols = [10]
	data = pd.read_csv('./taxi_01.csv', usecols=cols)
	# Y_data = pd.read_csv('./taxi_01.csv', usecols=Y_cols)
	print(data.columns)
	# Y_data = data['total_amount']
	# X_data = data.drop(['total_amount'], axis=1)

	data.to_csv ('./data.csv', index = None, header=True)
	# Y_data.to_csv ('./labels_data.csv', index = None, header=True)

def get_train_test():
	# data = get_data()
	data = pd.read_csv('./year_data.csv')
	# Y_data = pd.read_csv('./taxi_01.csv', usecols=Y_cols)
	print(data.columns)
	train, test = train_test_split(data, test_size=0.2)

	Y_train = train['total_amount']
	X_train = train.drop(['total_amount'], axis=1)

	Y_test = test['total_amount']
	X_test = test.drop(['total_amount'], axis=1)
	# print(X_train.head())
	return (X_train,Y_train, X_test, Y_test)

def mean_absolute_percentage_error(y_true, y_pred): 
    # y_true, y_pred = check_arrays(y_true, y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100
