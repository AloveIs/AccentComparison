import lstm_fcn
from get_data import get_data
import pickle

history = []
for i in range (10):
    X_train, X_test, y_train, y_test = get_data("skane", "west", balance = True)
    model = lstm_fcn.generate_model(X_train.shape[1])
    history.append(lstm_fcn.train_model(model, X_train, X_test, y_train, y_test))
    with open(r"west_skane2.pickle", "wb") as f:
        pickle.dump(history, f)