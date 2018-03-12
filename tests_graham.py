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

    # VALID DATES

    # Graham
    def test_perfect_date(self):
        # Setup
        test_name = "Date Validator Test #1"
        data_to_test = "28/21/1998"
        class_to_test = vd.ValidateDate()
        expected_result = ["28/01/1998", True]

        # Action
        result = class_to_test.is_valid(data_to_test)

        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] == expected_result[1])
        except:
            print("{} Failed - Should be {}, but was {}.".format(test_name, expected_result, result))

if __name__ == '__main__':
    # unittest.main(verbosity=2)  # with more details
    unittest.main()
