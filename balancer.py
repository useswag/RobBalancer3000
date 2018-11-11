from sklearn import svm
import random
import numpy as np

TRAINING_DATA_SIZE = 500

class Balancer(object):
    def __init__(self):
        self.regr = svm.SVC(kernel='linear')
        train_x, train_y = self.generate_training_data()
        self.regr.fit(train_x, train_y)

    def generate_training_data(self):
        train_x = []
        train_y = []
        for n in range(TRAINING_DATA_SIZE):
            x = np.array([random.randint(0, 10) for m in range(10)])
            train_x.append(x)
            train_y.append(sum(x))
        return train_x, train_y

    def total(self, transactions):
        return self.regr.predict(transactions.reshape(1,-1))