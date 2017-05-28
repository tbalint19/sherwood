from django.test import TestCase, tag
from _Jobs.update_standings import Ranker
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
        return self.result > other.result

    def save(self):
        pass

@tag('fast', 'ranker')
class TestRanker(TestCase):

    def test_ranker_returns_usertickets(self):
        user_tickets = [UserTicketMock(x, random.randint(0, 1000)) for x in range(10)]
        ranker = Ranker(user_tickets)
        ranked = ranker.rank()
        self.assertEqual(len(ranked), len(user_tickets))

    def test_ranker_previous_with_better_result_than_latter(self):
        user_tickets = [UserTicketMock(x, random.randint(0, 1000)) for x in range(10)]
        ranker = Ranker(user_tickets)
        ranked = ranker.rank()
        self.assertTrue(ranked[0].result >= ranked[1].result)
        self.assertTrue(ranked[1].result >= ranked[2].result)
        self.assertTrue(ranked[2].result >= ranked[3].result)
        self.assertTrue(ranked[3].result >= ranked[4].result)
        self.assertTrue(ranked[4].result >= ranked[5].result)
        self.assertTrue(ranked[5].result >= ranked[6].result)
        self.assertTrue(ranked[6].result >= ranked[7].result)
        self.assertTrue(ranked[7].result >= ranked[8].result)
        self.assertTrue(ranked[8].result >= ranked[9].result)

    def test_less_than_20_sets_all_payoff_to_1(self):
        user_tickets = [UserTicketMock(x, random.randint(0, 1000)) for x in range(19)]
        ranker = Ranker(user_tickets)
        ranked = ranker.rank()
        self.assertEqual(ranked[0].payoff, 1)
        self.assertEqual(ranked[1].payoff, 1)
        self.assertEqual(ranked[2].payoff, 1)
        self.assertEqual(ranked[3].payoff, 1)
        self.assertEqual(ranked[4].payoff, 1)
        self.assertEqual(ranked[5].payoff, 1)
        self.assertEqual(ranked[6].payoff, 1)
        self.assertEqual(ranked[7].payoff, 1)
        self.assertEqual(ranked[8].payoff, 1)
        self.assertEqual(ranked[9].payoff, 1)
        self.assertEqual(ranked[10].payoff, 1)
        self.assertEqual(ranked[11].payoff, 1)
        self.assertEqual(ranked[12].payoff, 1)
        self.assertEqual(ranked[13].payoff, 1)
        self.assertEqual(ranked[14].payoff, 1)
        self.assertEqual(ranked[15].payoff, 1)
        self.assertEqual(ranked[16].payoff, 1)
        self.assertEqual(ranked[17].payoff, 1)
        self.assertEqual(ranked[18].payoff, 1)

    def test_20_sets_seconds_payoff_to_relevant(self):
        user_tickets = [UserTicketMock(x, random.randint(0, 1000)) for x in range(20)]
        ranker = Ranker(user_tickets)
        ranked = ranker.rank()
        self.assertEqual(ranked[0].payoff, 2)
        self.assertEqual(ranked[1].payoff, 1.9)
        self.assertEqual(ranked[2].payoff, 1.8)
        self.assertEqual(ranked[3].payoff, 1.7)
        self.assertEqual(ranked[4].payoff, 1.6)
        self.assertEqual(ranked[5].payoff, 1.5)
        self.assertEqual(ranked[6].payoff, 1.4)
        self.assertEqual(ranked[7].payoff, 1.3)
        self.assertEqual(ranked[8].payoff, 1.2)
        self.assertEqual(ranked[9].payoff, 1.1)
        self.assertEqual(ranked[10].payoff, 0.9)
        self.assertEqual(ranked[11].payoff, 0.8)
        self.assertEqual(ranked[12].payoff, 0.7)
        self.assertEqual(ranked[13].payoff, 0.6)
        self.assertEqual(ranked[14].payoff, 0.5)
        self.assertEqual(ranked[15].payoff, 0.4)
        self.assertEqual(ranked[16].payoff, 0.3)
        self.assertEqual(ranked[17].payoff, 0.2)
        self.assertEqual(ranked[18].payoff, 0.1)
        self.assertEqual(ranked[19].payoff, 0)

    def test_21_sets_1s_payoff_to_1(self):
        user_tickets = [UserTicketMock(x, random.randint(0, 1000)) for x in range(21)]
        ranker = Ranker(user_tickets)
        ranked = ranker.rank()
        self.assertEqual(ranked[10].payoff, 1)

    def test_39_sets_19s_payoff_to_1(self):
        user_tickets = [UserTicketMock(x, random.randint(0, 1000)) for x in range(39)]
        ranker = Ranker(user_tickets)
        ranked = ranker.rank()
        self.assertEqual(ranked[0].payoff, 2)
        self.assertEqual(ranked[1].payoff, 1.9)
        self.assertEqual(ranked[2].payoff, 1.8)
        self.assertEqual(ranked[3].payoff, 1.7)
        self.assertEqual(ranked[4].payoff, 1.6)
        self.assertEqual(ranked[5].payoff, 1.5)
        self.assertEqual(ranked[6].payoff, 1.4)
        self.assertEqual(ranked[7].payoff, 1.3)
        self.assertEqual(ranked[8].payoff, 1.2)
        self.assertEqual(ranked[9].payoff, 1.1)
        self.assertEqual(ranked[10].payoff, 1)
        self.assertEqual(ranked[11].payoff, 1)
        self.assertEqual(ranked[12].payoff, 1)
        self.assertEqual(ranked[13].payoff, 1)
        self.assertEqual(ranked[14].payoff, 1)
        self.assertEqual(ranked[15].payoff, 1)
        self.assertEqual(ranked[16].payoff, 1)
        self.assertEqual(ranked[17].payoff, 1)
        self.assertEqual(ranked[18].payoff, 1)
        self.assertEqual(ranked[19].payoff, 1)
        self.assertEqual(ranked[20].payoff, 1)
        self.assertEqual(ranked[21].payoff, 1)
        self.assertEqual(ranked[22].payoff, 1)
        self.assertEqual(ranked[23].payoff, 1)
        self.assertEqual(ranked[24].payoff, 1)
        self.assertEqual(ranked[25].payoff, 1)
        self.assertEqual(ranked[26].payoff, 1)
        self.assertEqual(ranked[27].payoff, 1)
        self.assertEqual(ranked[28].payoff, 1)
        self.assertEqual(ranked[29].payoff, 0.9)
        self.assertEqual(ranked[30].payoff, 0.8)
        self.assertEqual(ranked[31].payoff, 0.7)
        self.assertEqual(ranked[32].payoff, 0.6)
        self.assertEqual(ranked[33].payoff, 0.5)
        self.assertEqual(ranked[34].payoff, 0.4)
        self.assertEqual(ranked[35].payoff, 0.3)
        self.assertEqual(ranked[36].payoff, 0.2)
        self.assertEqual(ranked[37].payoff, 0.1)
        self.assertEqual(ranked[38].payoff, 0)

    def test_40_sets_all_payoff_to_relevant(self):
        user_tickets = [UserTicketMock(x, random.randint(0, 1000)) for x in range(40)]
        ranker = Ranker(user_tickets)
        ranked = ranker.rank()
        self.assertEqual(ranked[0].payoff, 2)
        self.assertEqual(ranked[1].payoff, 2)
        self.assertEqual(ranked[2].payoff, 1.9)
        self.assertEqual(ranked[3].payoff, 1.9)
        self.assertEqual(ranked[4].payoff, 1.8)
        self.assertEqual(ranked[5].payoff, 1.8)
        self.assertEqual(ranked[6].payoff, 1.7)
        self.assertEqual(ranked[7].payoff, 1.7)
        self.assertEqual(ranked[8].payoff, 1.6)
        self.assertEqual(ranked[9].payoff, 1.6)
        self.assertEqual(ranked[10].payoff, 1.5)
        self.assertEqual(ranked[11].payoff, 1.5)
        self.assertEqual(ranked[12].payoff, 1.4)
        self.assertEqual(ranked[13].payoff, 1.4)
        self.assertEqual(ranked[14].payoff, 1.3)
        self.assertEqual(ranked[15].payoff, 1.3)
        self.assertEqual(ranked[16].payoff, 1.2)
        self.assertEqual(ranked[17].payoff, 1.2)
        self.assertEqual(ranked[18].payoff, 1.1)
        self.assertEqual(ranked[19].payoff, 1.1)
        self.assertEqual(ranked[20].payoff, 0.9)
        self.assertEqual(ranked[21].payoff, 0.9)
        self.assertEqual(ranked[22].payoff, 0.8)
        self.assertEqual(ranked[23].payoff, 0.8)
        self.assertEqual(ranked[24].payoff, 0.7)
        self.assertEqual(ranked[25].payoff, 0.7)
        self.assertEqual(ranked[26].payoff, 0.6)
        self.assertEqual(ranked[27].payoff, 0.6)
        self.assertEqual(ranked[28].payoff, 0.5)
        self.assertEqual(ranked[29].payoff, 0.5)
        self.assertEqual(ranked[30].payoff, 0.4)
        self.assertEqual(ranked[31].payoff, 0.4)
        self.assertEqual(ranked[32].payoff, 0.3)
        self.assertEqual(ranked[33].payoff, 0.3)
        self.assertEqual(ranked[34].payoff, 0.2)
        self.assertEqual(ranked[35].payoff, 0.2)
        self.assertEqual(ranked[36].payoff, 0.1)
        self.assertEqual(ranked[37].payoff, 0.1)
        self.assertEqual(ranked[38].payoff, 0)
        self.assertEqual(ranked[39].payoff, 0)

    def test_less_than_20_sets_all_payoff_to_1(self):
        user_tickets = [UserTicketMock(x, random.randint(0, 1000)) for x in range(312)]
        ranker = Ranker(user_tickets)
        ranked = ranker.rank()
        self.assertEqual(ranked[0].payoff, 2)
        self.assertEqual(ranked[7].payoff, 2)
        self.assertEqual(ranked[14].payoff, 2)
        self.assertEqual(ranked[15].payoff, 1.9)
        self.assertEqual(ranked[19].payoff, 1.9)
        self.assertEqual(ranked[29].payoff, 1.9)
        self.assertEqual(ranked[30].payoff, 1.8)
        self.assertEqual(ranked[41].payoff, 1.8)
        self.assertEqual(ranked[44].payoff, 1.8)
        self.assertEqual(ranked[45].payoff, 1.7)
        self.assertEqual(ranked[48].payoff, 1.7)
        self.assertEqual(ranked[59].payoff, 1.7)
        self.assertEqual(ranked[60].payoff, 1.6)
        self.assertEqual(ranked[64].payoff, 1.6)
        self.assertEqual(ranked[74].payoff, 1.6)
        self.assertEqual(ranked[75].payoff, 1.5)
        self.assertEqual(ranked[80].payoff, 1.5)
        self.assertEqual(ranked[89].payoff, 1.5)
        self.assertEqual(ranked[90].payoff, 1.4)
        self.assertEqual(ranked[99].payoff, 1.4)
        self.assertEqual(ranked[104].payoff, 1.4)
        self.assertEqual(ranked[105].payoff, 1.3)
        self.assertEqual(ranked[109].payoff, 1.3)
        self.assertEqual(ranked[119].payoff, 1.3)
        self.assertEqual(ranked[120].payoff, 1.2)
        self.assertEqual(ranked[123].payoff, 1.2)
        self.assertEqual(ranked[134].payoff, 1.2)
        self.assertEqual(ranked[135].payoff, 1.1)
        self.assertEqual(ranked[140].payoff, 1.1)
        self.assertEqual(ranked[149].payoff, 1.1)
        self.assertEqual(ranked[150].payoff, 1)
        self.assertEqual(ranked[156].payoff, 1)
        self.assertEqual(ranked[161].payoff, 1)
        self.assertEqual(ranked[162].payoff, 0.9)
        self.assertEqual(ranked[164].payoff, 0.9)
        self.assertEqual(ranked[176].payoff, 0.9)
        self.assertEqual(ranked[177].payoff, 0.8)
        self.assertEqual(ranked[180].payoff, 0.8)
        self.assertEqual(ranked[191].payoff, 0.8)
        self.assertEqual(ranked[192].payoff, 0.7)
        self.assertEqual(ranked[200].payoff, 0.7)
        self.assertEqual(ranked[206].payoff, 0.7)
        self.assertEqual(ranked[207].payoff, 0.6)
        self.assertEqual(ranked[211].payoff, 0.6)
        self.assertEqual(ranked[221].payoff, 0.6)
        self.assertEqual(ranked[222].payoff, 0.5)
        self.assertEqual(ranked[230].payoff, 0.5)
        self.assertEqual(ranked[236].payoff, 0.5)
        self.assertEqual(ranked[237].payoff, 0.4)
        self.assertEqual(ranked[240].payoff, 0.4)
        self.assertEqual(ranked[251].payoff, 0.4)
        self.assertEqual(ranked[252].payoff, 0.3)
        self.assertEqual(ranked[260].payoff, 0.3)
        self.assertEqual(ranked[266].payoff, 0.3)
        self.assertEqual(ranked[267].payoff, 0.2)
        self.assertEqual(ranked[280].payoff, 0.2)
        self.assertEqual(ranked[281].payoff, 0.2)
        self.assertEqual(ranked[282].payoff, 0.1)
        self.assertEqual(ranked[286].payoff, 0.1)
        self.assertEqual(ranked[296].payoff, 0.1)
        self.assertEqual(ranked[297].payoff, 0)
        self.assertEqual(ranked[300].payoff, 0)
        self.assertEqual(ranked[311].payoff, 0)
