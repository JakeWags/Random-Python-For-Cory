from random import randint
num = int(input('Number of times to flip coin: '))
flips = [randint(0,1) for r in range(num)]
results = []
for flip in flips:
        if flip == 0:
            results.append('Heads')
        elif flip == 1:
            results.append('Tails')
print("Heads: " + str(results.count("Heads")) + ", Tails: " + str(results.count("Tails")))