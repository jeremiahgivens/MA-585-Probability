import numpy as np
from matplotlib import pyplot as plt

num = []
prob = []
trials = 20000

for n in range(1, 100):
    arr = np.arange(n)
    trial_with_at_least_one_correct = 0

    for i in range(trials):
        np.random.shuffle(arr)
        for x in range(len(arr)):
            if arr[x] == x:
                trial_with_at_least_one_correct += 1
                break

    prob.append(trial_with_at_least_one_correct / trials)
    num.append(n)

print(prob)
plt.plot(num, prob)
plt.show()
