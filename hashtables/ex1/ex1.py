def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    d = dict()
    if length >= 2:
        # store index by weight for each item in the dictionary
        for i in range(0,len(weights)):
            d[weights[i]] = i
    
        # loop through 
        for i in range(0,len(weights)):
            # subtract the weights from the limit
            dif = limit-weights[i]
            # if the difference is in our dictionary, return it
            if dif in d:
                # return the indices
                return (d[dif], i)

    return None
