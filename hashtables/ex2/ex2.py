#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    itinerary = []
    for ticket in tickets:
        cache[ticket.source] = ticket.destination


    current_ticket = cache["NONE"]
    while current_ticket:
        itinerary.append(current_ticket)

        if cache[current_ticket] == "NONE":
            itinerary.append("NONE")
            current_ticket = None
        else:
            current_ticket = cache[current_ticket]

    return itinerary
