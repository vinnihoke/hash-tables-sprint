def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    # Store the key as the value at index

    # x = limit - key
        # x is negative? Fail

    # key + x == limit ?
        # Match if true
        # Fail otherwise

    store = {}
    result = []
    
    for i in range(length):
        w = weights[i]
        store[w] = limit - w
        if store[w] >= 0 and w + store[w] == limit:
            if store[w] in weights:
                result.insert(0, i)

    if len(result) > 1:
        return result
    else:
        return None



weights = [12, 6, 7, 14, 19, 3, 0, 25, 40]
length = len(weights)
limit = 7

print(get_indices_of_item_weights(weights, length, limit))
