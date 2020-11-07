# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    d = dict()
    # loop through the files
    for path in files:
        # split the path at /
        path2 = path.split('/')
        # loop through path
        for word in path2:
            # if the word is not in the dictionary
            if word not in d:
                # create a list with the path in it
                l = [path]
                # add it to the dict
                d[word] = l
            # if the word is in the dictionary
            else:
                # append the path to the existing list
                d[word].append(path)
    
    # create a list to hold our results
    result = []
    # loop through queries
    for querie in queries:
        if querie in d:
            # loop through the paths
            for path in d[querie]:
                result.append(path)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
