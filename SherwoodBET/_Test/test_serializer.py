from django.test import TestCase
from _Serializer.serializer import Serializer as S
from datetime import datetime
from django.contrib.auth.models import User
from App_Profile.models import Profile, Account
from App_Game.models import *

class TestSerializePrimitives(TestCase):

    def test_serialized_string_returns_string(self):
        string = "bela"
        self.assertEqual(string, S.serialize(string))

    def test_serialized_integer_returns_integer(self):
        integer = 15
        self.assertEqual(integer, S.serialize(integer))

    def test_serialized_boolean_returns_boolean(self):
        boolean = True
        self.assertEqual(boolean, S.serialize(boolean))

    def test_serialized_dict_of_floats_returns_list_of_floats(self):
        floatings = {'b': 1.5, 'c': 1.6}
        self.assertEqual(floatings, S.serialize(floatings))

    def test_serialized_none_returns_none(self):
        none = None
        self.assertEqual(none, S.serialize(none))

    def test_serialized_datetime_returns_datetime(self):
        dt = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
        self.assertEqual(dt.isoformat(), S.serialize(dt))

class TestSerializeProfileModels(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = Profile.objects.create_profile("bela", "be@la.hu", "123456Ab", None)

    def setUp(self):
        self.maxDiff = None

    def test_user_returns_dict_from_user(self):
        self.assertEqual("bela", S.serialize(self.__class__.user)['username'])
        self.assertEqual("be@la.hu", S.serialize(self.__class__.user)['email'])

    def test_profile_returns_dict_from_profile(self):
        data = {
            'id': self.__class__.user.profile.id,
            'user': 'bela',
            'rank': 'newbie',
            'email_sent': False,
            'email_attempted': False,
            'annual_points': 0,
            'monthly_points': 0,
            'is_confirmed': False,
            'confirmation_code': self.__class__.user.profile.confirmation_code}
        self.assertEqual(data, S.serialize(self.__class__.user.profile))

    def test_account_returns_dict_from_account(self):
        data = {
            'id': self.__class__.user.account.id,
            'user': 'bela',
            'real_money': 0,
            'game_money': 1000}
        self.assertEqual(data, S.serialize(self.__class__.user.account))

class TestSerializeGameModels(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.player = Profile.objects.create_profile("Kazmer12", "kaz@mer.hu", "123456Ab", None)
        cls.barca = Team(name="F.C. Barcelona", short_name="FC Barca", stadium="Camp Nou")
        cls.barca.save()
        cls.rmadird = Team(name="Real Madrid C.F.", short_name="R Madrid", stadium="Bernabeu")
        cls.rmadird.save()
        deadline = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
        cls.barca_real = Match(home_team_obj=cls.barca, away_team_obj=cls.rmadird, deadline=deadline)
        cls.barca_real.save()
        cls.final_result = Event(name="Final result")
        cls.final_result.save()
        cls.barca_real_final_result = MatchEvent(match_obj=cls.barca_real, event_obj=cls.final_result)
        cls.barca_real_final_result.save()
        cls.PD15_collection = Collection(number=171819, title="PD 15th round", intro="Play it!")
        cls.PD15_collection.save()
        cls.barca_real_final_result_on_PD15_collection = MatchEventOfCollection(
            match_event_obj=cls.barca_real_final_result, collection_obj=cls.PD15_collection)
        cls.barca_real_final_result_on_PD15_collection.save()
        cls.PD15_collection_with_1_euro = RaceTicket(
            collection_obj=cls.PD15_collection, is_professional=True, bet_amount=1)
        cls.PD15_collection_with_1_euro.save()
        cls.user_ticket_of_kazmer = UserTicket(race_ticket_obj=cls.PD15_collection_with_1_euro, user_obj=cls.player)
        cls.user_ticket_of_kazmer.save()
        cls.bet_on_barca_real_from_kazmer = Bet(
            match_event_obj=cls.barca_real_final_result, user_ticket_obj=cls.user_ticket_of_kazmer)
        cls.bet_on_barca_real_from_kazmer.save()

    def setUp(self):
        self.maxDiff = None

    def test_serialize_team(self):
        data = {'name': "F.C. Barcelona", 'short_name': "FC Barca", 'stadium': "Camp Nou", 'id': self.__class__.barca.id}
        serialized = S.serialize(self.__class__.barca)
        self.assertEquals(data, serialized)

    def test_serialize_match(self):
        data = {'away_team': 'R Madrid', 'deadline': '2005-06-01T13:33:00', 'home_team': 'FC Barca',
            'link': '', 'id': self.__class__.barca_real.id, 'league': 'Friendly', 'round': "", 'status': "Upcoming"}
        serialized = S.serialize(self.__class__.barca_real)
        self.assertEquals(data, serialized)

    def test_serialize_event(self):
        data = {'name': "Final result", 'id': self.__class__.final_result.id}
        serialized = S.serialize(self.__class__.final_result)
        self.assertEquals(data, serialized)

    def test_serialize_match_event(self):
        data = {'match': "FC Barca - R Madrid", 'event': "Final result",
            'id': self.__class__.barca_real_final_result.id, 'result': None, 'details': None}
        serialized = S.serialize(self.__class__.barca_real_final_result)
        self.assertEquals(data, serialized)

    def test_serialize_collection(self):
        data = {'is_deep_analysis': False, 'intro': 'Play it!', 'status': "Hidden",
            'number': 171819, 'title': 'PD 15th round'}
        serialized = S.serialize(self.__class__.PD15_collection)
        self.assertEquals(data, serialized)

    def test_serialize_match_event_of_collection(self):
        data = {'collection': '#171819: PD 15th round',
            'id': self.__class__.barca_real_final_result_on_PD15_collection.id,
            'match_event': 'FC Barca - R Madrid / Final result'}
        serialized = S.serialize(self.__class__.barca_real_final_result_on_PD15_collection)
        self.assertEquals(data, serialized)

    def test_serialize_race_ticket(self):
        data = {'collection': '#171819: PD 15th round', 'id': self.__class__.PD15_collection_with_1_euro.id,
            'is_professional': True, 'bet_amount': 1, 'number_of_competitors': 0}
        serialized = S.serialize(self.__class__.PD15_collection_with_1_euro)
        self.assertEquals(data, serialized)

    def test_serialize_user_ticket(self):
        data = {'id': self.__class__.user_ticket_of_kazmer.id, 'paid': False,
            'payoff': None, 'points': 1, 'race_ticket': '#171819: PD 15th round / 1', 'rank': None, 'user': 'Kazmer12'}
        serialized = S.serialize(self.__class__.user_ticket_of_kazmer)
        self.assertEquals(data, serialized)

    def test_serialize_bet(self):
        data = {'away': 0, 'draw': 0, 'home': 0, 'id': self.__class__.bet_on_barca_real_from_kazmer.id,
            'match_event': 'FC Barca - R Madrid / Final result', 'result': 1,
            'user_ticket': "Kazmer12's #171819: PD 15th round / 1"}
        serialized = S.serialize(self.__class__.bet_on_barca_real_from_kazmer)
        self.assertEquals(data, serialized)

class TestSerializeCollections(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user1 = Profile.objects.create_profile("bela", "be@la.hu", "123456Ab", None)
        cls.user2 = Profile.objects.create_profile("lajos", "la@jos.hu", "123456Ab", None)
        cls.user3 = Profile.objects.create_profile("kazmer", "kaz@mer.hu", "123456Ab", None)

    def setUp(self):
        self.maxDiff = None

    def test_serialized_list_of_strings_returns_list_of_strings(self):
        strings = ["bela", "lajos", "kazmer"]
        self.assertEqual(strings, S.serialize(strings))

    def test_serialized_dict_of_strings_returns_list_of_strings(self):
        strings = {'b': "bela", 'l': "lajos", 'k': "kazmer"}
        self.assertEqual(strings, S.serialize(strings))

    def test_serialized_list_of_integers_returns_list_of_integers(self):
        integers = [15, 16]
        self.assertEqual(integers, S.serialize(integers))

    def test_serialized_dict_of_integers_returns_list_of_integers(self):
        integers = {'b': 15, 'c': 16}
        self.assertEqual(integers, S.serialize(integers))

    def test_serialized_float_returns_float(self):
        floating = 1.5
        self.assertEqual(floating, S.serialize(floating))

    def test_serialized_list_of_floats_returns_list_of_floats(self):
        floatings = [1.5, 1.6]
        self.assertEqual(floatings, S.serialize(floatings))

    def test_serialized_list_of_booleans_returns_list_of_booleans(self):
        booleans = [True, False]
        self.assertEqual(booleans, S.serialize(booleans))

    def test_serialized_dict_of_booleans_returns_list_of_booleans(self):
        booleans = {'b': True, 'c': False}
        self.assertEqual(booleans, S.serialize(booleans))

    def test_serialized_list_of_nones_returns_list_of_nones(self):
        nones = [None, None]
        self.assertEqual(nones, S.serialize(nones))

    def test_serialized_dict_of_nones_returns_list_of_nones(self):
        nones = {'b': None, 'c': None}
        self.assertEqual(nones, S.serialize(nones))

    def test_serialized_list_of_datetimes_returns_list_of_datetimes(self):
        dts = [
            datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p'),
            datetime.strptime('Jun 1 2015  1:33PM', '%b %d %Y %I:%M%p')]
        self.assertEqual([dt.isoformat() for dt in dts], S.serialize(dts))

    def test_serialized_dict_of_datetimes_returns_list_of_datetimes(self):
        dts = {
            'b': datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p'),
            'c': datetime.strptime('Jun 1 2015  1:33PM', '%b %d %Y %I:%M%p')}
        self.assertEqual({
            'b': datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p').isoformat(),
            'c': datetime.strptime('Jun 1 2015  1:33PM', '%b %d %Y %I:%M%p').isoformat()}, S.serialize(dts))

    def test_list_of_users_returns_list_of_dicts_of_users(self):
        users = [self.__class__.user1, self.__class__.user2, self.__class__.user3]
        self.assertEqual("bela", S.serialize(users)[0]['username'])
        self.assertEqual("be@la.hu", S.serialize(users)[0]['email'])
        self.assertEqual("lajos", S.serialize(users)[1]['username'])
        self.assertEqual("la@jos.hu", S.serialize(users)[1]['email'])
        self.assertEqual("kazmer", S.serialize(users)[2]['username'])
        self.assertEqual("kaz@mer.hu", S.serialize(users)[2]['email'])

    def test_dict_of_users_returns_dict_of_dicts_of_users(self):
        users = {'bela': self.__class__.user1, 'lajos': self.__class__.user2, 'kazmer': self.__class__.user3}
        self.assertEqual("bela", S.serialize(users)['bela']['username'])
        self.assertEqual("be@la.hu", S.serialize(users)['bela']['email'])
        self.assertEqual("lajos", S.serialize(users)['lajos']['username'])
        self.assertEqual("la@jos.hu", S.serialize(users)['lajos']['email'])
        self.assertEqual("kazmer", S.serialize(users)['kazmer']['username'])
        self.assertEqual("kaz@mer.hu", S.serialize(users)['kazmer']['email'])
