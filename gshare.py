
table = [2, 2, 2, 2]   # prediction table (2 = weakly taken)
ghr = 0                # last branch result

# (pc, actual result)
branches = [
    (1, 1),
    (1, 0),
    (1, 1),
    (1, 1)
]

for b in branches:
    pc = b[0]
    actual = b[1]

    # get index using xor
    idx = pc ^ ghr

    counter = table[idx]

    # make prediction
    if counter >= 2:
        pred = 1
    else:
        pred = 0

    print("index:", idx)
    print("pred:", pred, "actual:", actual)

    # update counter
    if actual == 1:
        if counter < 3:
            table[idx] += 1
    else:
        if counter > 0:
            table[idx] -= 1

    # update history
    ghr = actual

    print("table now:", table)
    print("ghr:", ghr)
    print()