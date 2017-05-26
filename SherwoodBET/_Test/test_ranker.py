from django.test import TestCase
from _Jobs.ranker import Ranker
import random

class UserTicketMock:

    def __init__(self, pk, points):
        self.result = points
        self.id = pk
        self.rank = None
        self.payoff = None

    def __lt__(self, other):
        if self.result == other.result:
            return self.id > other.id
        return self.result < other.result

    def save(self):
        pass

class TestRanker(TestCase):

    def test_ranker_returns_usertickets(self):
        user_tickets = [UserTicketMock(x, random.randint(0, 1000)) for x in range(10)]
        ranker = Ranker(user_tickets)
        result = ranker.rank()
        self.assertEqual(len(result), len(user_tickets))
