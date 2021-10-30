# Author Nick Sebasco
# Date: 9/09/2021
# M51 Advanced Python Programming
# Machine Learning - KNN Algorithm from scratch
#

from random import sample
from typing import Callable
from statistics import mode

class CSV:
    def __init__(self, fname, delim=","):
        with open(fname, "r") as f:
            self.data = [i.split(delim) for i in f.readlines() if i.strip() != ""]
        
        self.shape = (len(self.data) - 1, len(self.data[0]))
    
    def ttsplit(self, fraction = 0.9):
        sampled = sample(self.data[1:],len(self.data) - 1)
        pivot = int(fraction * len(sampled))
        return (sampled[:pivot], sampled[pivot:])

    def get_columnNames(self):
        return [i.strip() for i in self.data[0]]

def euclidean(u: list, v: list) -> float:
    '''
    u = [1,2,3]
    v = [3,3,2]

    i = 0
    u[i] = 1
    v[i] = 3

    (1 - 3)^2 = 4
    sqrt(x) = x^1/2
    '''
    t = 0
    for i in range(len(u)):
        t += (u[i] - v[i])**2
    return t**0.5

def knn(distance: Callable, u: list, k: int, data: list):
    dist_label = []
    u = [float(i) for i in u]
    for v in data:
        label = v[0]
        v = [float(i) for i in v[1:]]
        dist = distance(u, v)
        dist_label.append((dist, label))
    
    dist_label.sort(key= lambda x: x[0])
    return mode([i[1] for i in dist_label[0:k]])


csv = CSV("weight-height.csv")
# training/ testing
train, test = csv.ttsplit()


u_X = test[0][1:]
u_Y = test[0][0]

print("test:", u_X)
print("actual label:", u_Y)
prediction = knn(euclidean, u_X, 3, train)
print("predicted: ", prediction)

# Practice Problems:
# ----------------------------------------------------------------------------------
# 1. Determine Accuracy
# Iterate over test set and determine percentage of correct predictions
# Confusion matrix
# 2. Implement a mode function from scratch
# 3. implement a sorting algorithm from scratch
# 4. Find optimal k value
# 5. explore different distance functions
# 6. try new dataset