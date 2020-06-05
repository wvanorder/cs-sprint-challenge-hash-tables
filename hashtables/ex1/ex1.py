def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    for i in range(length):
        cache[weights[i]] = i

    for weight in weights:
        pair = limit - weight
        if pair not in cache:
            continue
        else:
            if weight > pair:
                return [cache[weight], cache[pair]]
            else:
                return [cache[pair], cache[weight]]


    return None

weights = [ 4, 6, 10, 15, 16 ]
length = 5
limit = 21

get_indices_of_item_weights(weights, 5, 21)
