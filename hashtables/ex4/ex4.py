def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    store = {}
    result = []
    for num in a:
        store[num] = num

    for key, value in store.items():
        if key in store and key * -1 in store:
            if key < 0:
                if key * -1 in result:
                    pass
                else:
                    result.append(key * -1)
            
            

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
    print(has_negatives([-1, -2, 1, 3, 4, 5, -5, 6, 6, 7, -7]))
