import unittest
import anaconda.validate_gender as va
import anaconda.validate_bmi as bm


class MainTests(unittest.TestCase):
    def setUp(self):
        # be executed before each test
        pass

    def tearDown(self):
        # be executed after each test case
        pass

    # MALE GENDER   V V V V V V V

    def test_gender_male(self):
        i = va.ValidateGender('male')
        i = i.is_valid()
        self.assertTrue(i == "M", "the value of test should be M")

    def test_gender_m(self):
        i = va.ValidateGender('m')
        i = i.is_valid()
        self.assertTrue(i == "M", "the value of test should be M")

    def test_gender_boy(self):
        i = va.ValidateGender('boy')
        i = i.is_valid()
        self.assertTrue(i == "M", "the value of test should be M")

    def test_gender_dude(self):
        i = va.ValidateGender('dude')
        i = i.is_valid()
        self.assertTrue(i == "M", "the value of test should be M")

    # FEMALE GENDER      V V V V V

    def test_gender_female(self):
        i = va.ValidateGender('female')
        i = i.is_valid()
        self.assertTrue(i == "F", "the value of test should be F")

    def test_gender_f(self):
        i = va.ValidateGender('f')
        i = i.is_valid()
        self.assertTrue(i == "F", "the value of test should be F")

    def test_gender_lady(self):
        i = va.ValidateGender('lady')
        i = i.is_valid()
        self.assertTrue(i == "F", "the value of test should be F")

    def test_gender_girl(self):
        i = va.ValidateGender('girl')
        i = i.is_valid()
        self.assertTrue(i == "F", "the value of test should be F")

    #  Gender with special characters (spaces, numbers and symbols) V V V V V

    def test_gender_male_with_special_characters(self):
        i = va.ValidateGender(' 23123 #$@#$ ma $#@$ le 9876@# ')
        i = i.is_valid()
        self.assertTrue(i == "M", "the value of test should be M")

    def test_gender_female_with_special_characters(self):
        i = va.ValidateGender(' $@#$ fe #$# ma @#@$ 454 le 3435')
        i = i.is_valid()
        self.assertTrue(i == "F", "the value of test should be F")

    # BMI TEST CASES

    def test_bmi_obesity(self):
        i = bm.ValidateBmi('obesity')
        i = i.is_valid()
        self.assertTrue(i == "Obesity", "the value of test should be Obesity")

    def test_bmi_normal(self):
        i = bm.ValidateBmi('normal')
        i = i.is_valid()
        self.assertTrue(i == "Normal", "the value of test should be Normal")

    def test_bmi_overweight(self):
        i = bm.ValidateBmi('over weight ')
        i = i.is_valid()
        self.assertTrue(i == "Overweight", "the value of test should be Overweight")

    def test_bmi_underweight(self):
        i = bm.ValidateBmi('underweight')
        i = i.is_valid()
        self.assertTrue(i == "Underweight", "the value of test should be underweight")

    # BMI WITH SPECIAL CHARACTERS

    def test_bmi_with_special_characters(self):
        i = bm.ValidateBmi('4234un    derwei#$#$ght     ')
        i = i.is_valid()
        self.assertTrue(i == "Underweight", "the value of test should be underweight")


if __name__ == '__main__':
    # unittest.main(verbosity=2)  # with more details
    unittest.main()
