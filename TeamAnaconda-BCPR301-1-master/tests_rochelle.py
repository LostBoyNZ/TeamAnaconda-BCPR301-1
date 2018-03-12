import unittest
import validators.validate_age as va


class Tests_Rochelle(unittest.TestCase):
    def setUp(self):
        # be executed before each test
        pass

    def tearDown(self):
        # be executed after each test case
        pass

    # Graham
    def run_test(self, expected_result, test_name, class_to_test, data_to_test):

        # Action
        result = class_to_test.is_valid(data_to_test)

        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] == expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name, expected_result, result))
        else:
            print("{} Passed".format(test_name))

    # VALIDATE AGES

    # Graham
    def test_perfect_date(self):
        # Setup
        test_name = "Age Validator Test #1"
        data_to_test = '45'
        class_to_test = va.ValidateAge()
        expected_result = ['45', True]

        # Action & Assert
        self.run_test(expected_result, test_name, class_to_test, data_to_test)

if __name__ == '__main__':
    # unittest.main(verbosity=2)  # with more details
    unittest.main()