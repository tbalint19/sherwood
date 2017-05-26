from _Jobs.ranker import Ranker

class UserTicketMock:

    def __init__(self, pk, points):
        self.result = points
        self.id = pk
        self.rank = None

    def __lt__(self, other):
        if self.result == other.result:
            return self.id > other.id
        return self.result > other.result

    def save(self):
        pass
