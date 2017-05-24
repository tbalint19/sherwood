from django.test import TestCase
from _Serializer.serializer import Serializer as S
from datetime import datetime

class TestSerializerPrimitives(TestCase):

    def test_serialized_string_returns_string(self):
        string = "bela"
        self.assertEqual(string, S.serialize(string))

    def test_serialized_list_of_strings_returns_list_of_strings(self):
        strings = ["bela", "lajos", "kazmer"]
        self.assertEqual(strings, S.serialize(strings))

    def test_serialized_dict_of_strings_returns_list_of_strings(self):
        strings = {'b': "bela", 'l': "lajos", 'k': "kazmer"}
        self.assertEqual(strings, S.serialize(strings))

    def test_serialized_integer_returns_integer(self):
        integer = 15
        self.assertEqual(integer, S.serialize(integer))

    def test_serialized_list_of_integers_returns_list_of_integers(self):
        integers = [15, 16]
        self.assertEqual(integers, S.serialize(integers))

    def test_serialized_dict_of_integers_returns_list_of_integers(self):
        integers = {'b': 15, 'c': 16}
        self.assertEqual(integers, S.serialize(integers))

    def test_serialized_boolean_returns_boolean(self):
        boolean = True
        self.assertEqual(boolean, S.serialize(boolean))

    def test_serialized_list_of_booleans_returns_list_of_booleans(self):
        booleans = [True, False]
        self.assertEqual(booleans, S.serialize(booleans))

    def test_serialized_dict_of_booleans_returns_list_of_booleans(self):
        booleans = {'b': True, 'c': False}
        self.assertEqual(booleans, S.serialize(booleans))

    def test_serialized_float_returns_float(self):
        floating = 1.5
        self.assertEqual(floating, S.serialize(floating))

    def test_serialized_list_of_floats_returns_list_of_floats(self):
        floatings = [1.5, 1.6]
        self.assertEqual(floatings, S.serialize(floatings))

    def test_serialized_dict_of_floats_returns_list_of_floats(self):
        floatings = {'b': 1.5, 'c': 1.6}
        self.assertEqual(floatings, S.serialize(floatings))

    def test_serialized_none_returns_none(self):
        none = None
        self.assertEqual(none, S.serialize(none))

    def test_serialized_list_of_nones_returns_list_of_nones(self):
        nones = [None, None]
        self.assertEqual(nones, S.serialize(nones))

    def test_serialized_dict_of_nones_returns_list_of_nones(self):
        nones = {'b': None, 'c': None}
        self.assertEqual(nones, S.serialize(nones))

    def test_serialized_datetime_returns_datetime(self):
        dt = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
        self.assertEqual(dt.isoformat(), S.serialize(dt))

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

class TestSerializerModels(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        pass

    def test_user_returns_dict_from_user(self):
        pass

    def test_list_of_users_returns_list_of_dicts_of_users(self):
        pass

    def test_dict_of_users_returns_dict_of_dicts_of_users(self):
        pass
