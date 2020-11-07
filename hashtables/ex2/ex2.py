#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    d = dict()
    route = []
    # loop through the tickets
    for ticket in tickets:
        # set each key to the source and each value to the destination
        d[ticket.source] = ticket.destination
    
    # find the first flight
    ff = d['NONE']
    # add the first flight to the route
    route.append(ff)
    # loop through until we find the last flight
    while d[ff] is not 'NONE':
        # append the value to the route
        route.append(d[ff])
        # update ff
        ff = d[ff]
    # append the final trip to the list
    route.append(d[ff])
    return route