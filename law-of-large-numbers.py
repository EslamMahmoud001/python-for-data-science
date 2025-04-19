# Xn -> E(x) when n -> inf
# The Law of Large Numbers states that as the number of trials increases, the sample mean will converge to the expected value.

import numpy as np
from numpy.random import randn

mean = 0
std = 1
expexpected_value = 68.2
N = [10, 100, 1000, 10000, 100000]
answer = []

for n in N:
    count = 0
    for i in randn(n):
        if i > -1 and i < 1:
            count += 1
    answer.append(count / n)   

print("Sample Mean: ", answer)


