import random

totalRand = []
rand = []
pickRandNum = 0
amountRand = 0
count = 0

print("**Random Number Generator (1~100)**")
amountRand = int(input('Amount of Random Number-> '))
count = int(input('Amount of Random Number Arrays-> '))

for _ in range(count) :
    rand = []
    while True:
        pickRandNum = random.randint(1, 100)
        if pickRandNum not in rand :
            rand.append(pickRandNum)
        if len(rand) >= amountRand :
            break
    totalRand.append(rand)

for rand in totalRand :
    rand.sort()
    print('Rand -> ', end = ' ')
    for i in range(0, amountRand) :
        print("%2d" %rand[i], end = ' ')
    print()