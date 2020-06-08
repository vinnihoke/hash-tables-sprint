#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

class TripList:
    def __init__(self):
        self.head = None
        self.storage = []
        self.length = 0

    def add_to_head(self, node):
        self.storage.insert(0, node)
        self.length += 1

    def add_to_tail(self, node):
        self.storage.append(node)
        self.length += 1


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    layovers = TripList()
    organized_flights = []

    for t in tickets:
        if t.source == "NONE":
            layovers.add_to_head(t)
            # organized_flights.insert(0, t.destination)
        if layovers.storage[layovers.length - 1].destination == t.source:
            layovers.add_to_tail(t)
            organized_flights.append(t.source)
        if t.destination == "NONE":
            layovers.add_to_tail(t)
            organized_flights.append(t.destination)
    return organized_flights



ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
            ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]
print(reconstruct_trip(tickets, len(tickets)))