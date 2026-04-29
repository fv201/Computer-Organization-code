table = [2, 2, 2, 2]
ghr = 0

branches = [
    (1, 1),
    (1, 0),
    (1, 1),
    (1, 1)
]

for pc, act in branches:
    idx = pc ^ ghr
    counter = table[idx]

    if counter >= 2:
        predict = 1
    else:
        predict = 0

    print("PC:", pc)
    print("Index:", idx)
    print("Prediction:", predict)
    print("Actual:", act)

    if act == 1 and table[idx] < 3:
        table[idx] += 1
    elif act == 0 and table[idx] > 0:
        table[idx] -= 1

    ghr = act

    print("Updated table:", table)
    print("Updated GHR:", ghr)
