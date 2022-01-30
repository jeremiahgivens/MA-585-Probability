import numpy
n = 10000  # Run the experiment n times.
outcomes = []  # coin, die
for i in range(n):
    x = numpy.random.choice(numpy.arange(1, 3), p=[.5, .5])  # H = 1, T = 2
    if x == 2:
        y = numpy.random.choice(numpy.arange(1, 5), p=[.4, .3, .2, .1])
    else:
        y = numpy.random.choice(numpy.arange(1, 7), p=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
    outcomes.append([x, y])


targetHit = 0
tot = 0
for i in outcomes:
    if i[1] == 2:
        tot += 1
        if i[0] == 2:
            targetHit += 1

print(targetHit/tot)
print(9/14)
