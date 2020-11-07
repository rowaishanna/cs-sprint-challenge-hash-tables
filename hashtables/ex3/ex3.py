def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # create a dictionary
    d = dict()
    # find how many arrays we have
    count = len(arrays)

    # loop through the list of arrays
    for array in arrays:
        # loop through each array
        for value in array:
            # if the value is not in the dictionary
            if value not in d:
                d[value] = 1
            # if the value is in the dictionary
            else:
                d[value] += 1

    # create an empty list to hold the result
    result = []
    # search the dictionary for the intersecting values
    for number, occurences in d.items():
        # if there is a number that intersects all the given arrays
        if occurences == count:
            # add it to our result
            result.append(number)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
