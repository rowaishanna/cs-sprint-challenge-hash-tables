def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    d = dict()
    # loop through the list
    for value in a:        
        # check to see if the value is positive
        if value > 0:
            # if the value is not in the dictionary
            if value not in d:
                # add it to the dictionary
                d[value] = 1  
    # create an empty list to store the answers
    result = []
    # loop through the inverse of the list
    a = [-1*(value) for value in a]
    for value in a:
        # if the inverted value is in our dictionary
        if value in d:
            # add it to our list
            result.append(value)
    # return the list
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
