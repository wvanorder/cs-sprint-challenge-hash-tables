def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []
    for i in a:
        if abs(i) not in cache:
            cache[abs(i)] = 1
        else:
            cache[abs(i)] +=1
    
    for kvp in cache:
        if cache[kvp] > 1:
            result.append(kvp)


    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
