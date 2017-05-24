from django.test import TestCase
from _Serializer.serializer import Serializer as S

class TestSerializer(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        pass

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

    # def test_serialized_datetime_returns_datetime(self):
    #     pass
    #
    # def test_serialized_list_of_datetimes_returns_list_of_datetimes(self):
    #     pass
    #
    # def test_serialized_dict_of_datetimes_returns_list_of_datetimes(self):
    #     pass
