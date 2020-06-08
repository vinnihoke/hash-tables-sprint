def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    length = len(arrays)
    iteration = 0
    result = []
    store = {}

    while iteration is not length:
        for e in arrays[iteration]:
            if e not in store:
                store[e] = 1
            else:
                if store[e] is not iteration + 1:
                    store[e] += 1
        iteration += 1

    for key, value in store.items():
        if value == length:
            result.append(key)

    return result





if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
