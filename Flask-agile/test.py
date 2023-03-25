import unittest

#unit test to test sting correction used in application validation
class Test1(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()

#unit test for logic used in CRUD operaiton updates when equating values 
class Test2(unittest.TestCase):
    def test_string(self):
        a = 'some'
        b = 'some'
        self.assertEqual(a, b)

    def test_boolean(self):
        a = True
        b = True
        self.assertEqual(a, b)

if __name__ == '__main__':
    unittest.main()

#unit test for User database get requests and User name display 
class Test3(unittest.TestCase):
      def test_1_get_name(self):
        print("\nStart get_name test\n")
        """
        Any method that starts with ``test_`` will be considered as a test case.
        """
        length = len(self.user_id)  # total number of stored user information
        print("user_id length = ", length)
        print("user_name length = ", len(self.user_name))
        for i in range(6):
            # if i not exceed total length then verify the returned name
            if i < length:
                # if the two name not matches it will fail the test case
                self.assertEqual(self.user_name[i], self.person.get_name(self.user_id[i]))
            else:
                print("Testing for get_name no user test")
                # if length exceeds then check the 'no such user' type message
                self.assertEqual('There is no such user', self.person.get_name(i))
        print("\nFinish get_name test\n")


#unit test for password validation and login 
if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()

class Test3(unittest.TestCase):
    class TestCommon(unittest.TestCase):
        pwd = getpass()

    class test_A(TestCommon):
        def test_a(self):
            self.assertEqual(self.pwd, 'secret')

    class test_B(TestCommon):
        def test_b(self):
            reversed_pwd = self.pwd[::-1]
            self.assertEqual(reversed_pwd, 'terces')


if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()