import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle


with open("danish_skane.pickle", "rb") as f:
	history = pickle.load(f)

n_runs = len(history)
n_epochs = 30

data = np.zeros((n_runs,5,n_epochs))
for i in range(n_runs):
    #history[i].history.pop('lr')
    data[i, :, :] = np.array(pd.DataFrame.from_dict(history[i].history, orient='index'))


p10 = np.percentile(data, 10, axis = 0)
p30 = np.percentile(data, 30, axis = 0)
p50 = np.percentile(data, 50, axis = 0)
p70 = np.percentile(data, 70, axis = 0)
p90 = np.percentile(data, 90, axis = 0)




plt.figure(figsize=(13,5))
plt.subplot(121)
plt.plot(p50[0], color = 'b')
plt.fill_between(range(n_epochs), p10[0], p90[0], color = 'b', alpha =.1)
plt.fill_between(range(n_epochs), p30[0], p70[0], color = 'b', alpha =.3)

plt.plot(p50[2], color = 'r')
plt.fill_between(range(n_epochs), p10[2], p90[2], color = 'r', alpha =.1)
plt.fill_between(range(n_epochs), p30[2], p70[2], color = 'r', alpha =.3)

plt.legend(["val_loss", "loss"])
plt.title("Crossentropy Evolution")
plt.xlabel("Epochs")
plt.ylabel("Loss")



plt.subplot(122)
plt.plot(p50[1], color = 'b')
plt.fill_between(range(n_epochs), p10[1], p90[1], color = 'b', alpha =.1)
plt.fill_between(range(n_epochs), p30[1], p70[1], color = 'b', alpha =.3)

plt.plot(p50[3], color = 'r')
plt.fill_between(range(n_epochs), p10[3], p90[3], color = 'r', alpha =.1)
plt.fill_between(range(n_epochs), p30[3], p70[3], color = 'r', alpha =.3)


plt.legend(["val_acc", "acc"])
plt.title("Accuracy Evolution")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")


plt.show()