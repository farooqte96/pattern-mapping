"""
This is the test script which contains unit tests for all functions of our main script
"""
import unittest
from package.user_input import if_numbers_within_bounds
from package.apply_format import apply_format
from package.modify_string import modify_string
from package.retrieve_message import get_message_of_all_strings, get_message_single_string

#import apply_format
#import retrieve_message

class TestIntegers(unittest.TestCase):

    """
    This class contains test functions to test all functions related to integers
    """
    #Tests for function check_all_positives
    #Test1:
    def test_return_true_if_all_integers_positive(self):
        #Test1: all positive should return True
        integers = [10, 20, 15, 12]
        result = if_numbers_within_bounds(integers)
        self.assertEqual(result, True)

    #Test2:
    def test_return_false_if_zero_in_integers(self):
        integers = [0, 1, 2, 3]
        result = if_numbers_within_bounds(integers)
        self.assertEqual(result, False)

    #Test3
    def test_return_false_if_negative_integers(self):
        integers = [-4, 3, -2, 3]
        result = if_numbers_within_bounds(integers)
        self.assertEqual(result, False)
    #Test4
    def test_return_false_for_big_numbers(self):
        integers = [5, 22, 6666, 765]
        result = if_numbers_within_bounds(integers)
        self.assertEqual(result, False)

class TestStringPatterns(unittest.TestCase):
    """
    This class is used to test functions related to string patterns
    """
    #test5
    def test_pattern_SST_with_5_should_give_SSTSS(self):
        pattern = 'sst'
        integer = 5
        modified_pattern = modify_string(pattern, integer)
        self.assertEqual(modified_pattern, 'SSTSS')

    #test6
    def test_pattern_SST_with_2_should_give_SS(self):
        pattern = 'sst'
        integer = 2
        modified_pattern = modify_string(pattern, integer)
        self.assertEqual(modified_pattern, 'SS')

    #test7
    def test_pattern_SSTTTS_with_9_should_give_SSTTTSSSS(self):
        pattern = 'ssttts'
        integer = 9
        modified_pattern = modify_string(pattern, integer)
        self.assertEqual(modified_pattern, 'SSTTTSSSS')

    #test8
    def test_pattern_SSTTTS_with_20_should_give_SSTTTSSSSSSSSSSSSSSS(self):
        pattern = 'ssttts'
        integer = 20
        modified_pattern = modify_string(pattern, integer)
        self.assertEqual(modified_pattern, 'SSTTTSSSSSSSSSSSSSSS')

    #test9
    def test_pattern_S_with_2_should_give_SS(self):
        pattern = 's'
        integer = 2
        modified_pattern = modify_string(pattern, integer)
        self.assertEqual(modified_pattern, 'SS')

    #test10
    def test_huge_pattern_should_return_empty_string(self):
        pattern = 'sssssstttttssssttttttssssttttttsssstttt'
        integer = 10
        modified_pattern = modify_string(pattern, integer)
        self.assertEqual(modified_pattern, '')

    #test11
    def test_retrieve_message_all_strings(self):
        pattern = ['sst', 'sstsst', 'ss']
        retrieved_message = get_message_of_all_strings(pattern)
        self.assertEqual(retrieved_message, ['soft soft tough ', 'soft soft tough soft soft tough ', 'soft soft '])

     #test12
    def test_retrive_message_single_string(self):
         single_string = 'ssttssts'
         retrieved_message = get_message_single_string(single_string)
         self.assertEqual(retrieved_message, 'soft soft tough tough soft soft tough soft ')

    #test13
    def test_string_beyond_20_characters_should_return_empty_string(self):
        bigger_string = 'stststststssttssttssststs'
        retrieved_message = get_message_single_string(bigger_string)
        self.assertEqual(retrieved_message, '')

    #test14
    def test_string_less_than_one_characters_should_return_empty_string(self):
        bigger_string = ''
        retrieved_message = get_message_single_string(bigger_string)
        self.assertEqual(retrieved_message, '')

    #test15
    def test_check_apply_format(self):
        test_string = 'ssttsts'
        integer_list = [5, 3, 2]
        result = apply_format(test_string, integer_list)
        self.assertEqual(result, ['SSTTS', 'SST', 'SS'])


#Run all unit Tests
if __name__ == '__main__':
    #unittest.main()
    test_classes = [TestIntegers, TestStringPatterns]
    loader = unittest.TestLoader()
    all_suites = []

    for test_class in test_classes:
        suite = loader.loadTestsFromTestCase(test_class)
        all_suites.append(suite)

    entire_suite = unittest.TestSuite(all_suites)
    runner = unittest.TextTestRunner(verbosity=2)
    results = runner.run(entire_suite)
