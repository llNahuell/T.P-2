import random

LIKES = [[0]*8 for i in range(8)]
for i in range(len(LIKES)):
    for j in range(len(LIKES)):
        if j != i:
            rng = random.randint(0,1)
        else:
            rng = 0
        LIKES[i][j] = rng
    print(LIKES[i])

