from random import choice

n_dice = 16
die_outcomes = range(1,7)
n_trials = 300
scale = 1

def stemnleaf(L, scale = 1.0):
    LoL = [None] * 10
    for i in range(len(LoL)):
        LoL[i] = [0] * 10
    ## load
    for e in L:
        ones = e % 10
        tens = int((e - ones) / 10)
        LoL[tens][ones] += 1
    ##print
    for i in range(len(LoL)):
        print(str(i) + ': ', end='')
        for j in range(len(LoL[i])):
            print(str(j) * int(LoL[i][j] * scale), end='')
        print()

# Set up variates.

trials = []
for t in range(n_trials):
    dice_in_trial = [choice(die_outcomes) for d in range(n_dice)]
    trials.append(sum(dice_in_trial))

# Print.

stemnleaf(trials, scale=scale)
