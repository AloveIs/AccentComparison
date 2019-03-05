import lstm_fcn
from get_data import get_data
import pickle

history = []
test_acc = []
for i in range (10):
	X_train, X_val, X_test, y_train, y_val, y_test = get_data("skane", "west", balance = True)
	model = lstm_fcn.generate_model(X_train.shape[1])
	hist, acc = lstm_fcn.train_model(model, X_train, X_val, X_test, y_train, y_val, y_test)
	history.append(hist)
	test_acc.append(acc)
	with open(r"danish_skane.pickle", "wb") as f:
		pickle.dump(history, f)
	with open(r"danish_skane_test_acc.pickle", "wb") as f:
		pickle.dump(test_acc, f) 