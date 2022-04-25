from unittest import TestCase, main
from selenium.common.exceptions import NoSuchElementException
from lesson_1_6_11 import check_regform_required_fields

right_answer = "Congratulations! You have successfully registered!"
url_good = 'http://suninjuly.github.io/registration1.html'
url_bad = 'http://suninjuly.github.io/registration2.html'

class Lesson_1_6_11_test(TestCase):
    def test_passed(self):
        self.assertEqual(check_regform_required_fields(url_good), right_answer)

    def test_failure(self):
        with self.assertRaises(NoSuchElementException):
            check_regform_required_fields(url_bad)

if __name__ == '__main__':
    main()