import unittest
import validators.validate_date as vd
import validators.validate_empid as vid


class Tests_Graham(unittest.TestCase):
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

    # VALID DATES

    # Graham
    def test_perfect_date_01(self):
        # Setup
        test_name = "Date Validator Test #1"
        data_to_test = "28/01/1998"
        class_to_test = vd.ValidateDate()
        expected_result = ["28/01/1998", True]

        # Action & Assert
        self.run_test(expected_result, test_name, class_to_test, data_to_test)

    def test_perfect_date_02(self):
        # Setup
        test_name = "Date Validator Test #2"
        data_to_test = "01 01 1998"
        class_to_test = vd.ValidateDate()
        expected_result = ["01/01/1998", True]

        # Action & Assert
        self.run_test(expected_result, test_name, class_to_test, data_to_test)


if __name__ == '__main__':
    # unittest.main(verbosity=2)  # with more details
    unittest.main()
