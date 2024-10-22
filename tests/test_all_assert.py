import unittest

SERVER = 'server_b'

class AllAssertsTests(unittest.TestCase):

    def test_assert(self):
        self.assertEqual(10, 10)
        self.assertEqual('Hola', 'Hola')

    def test_assert_true_or_false(self):
        self.assertTrue(True)
        self.assertFalse(False)


    def test_assert_raises(self):
        with self.assertRaises(ValueError): # que envie el error 
            int('no_soy_un_numero')        

    def test_assert_in(self):
        self.assertIn(10, [2,4,5,10]) # que el elemento este en la lista
        self.assertNotIn(5,[1,2,4,6]) # que el elemento no este en la lista

    def test_assert_dicts(self):
        user = {"first_name": "Luis", "last_name": "Martinez"}
        self.assertDictEqual(
            {"first_name": "Luis", "last_name": "Martinez"},
            user 
        )
        self.assertSetEqual(
            {1,2,3},
            {1,2,3}
        )
    @unittest.skip('Trabajo en progreso sera habilitada nuevamente')
    def test_skip(self):
        self.assertEqual('Hola', 'Chao')

    @unittest.skipIf(SERVER == 'server_b', 'Saltada porque no estamos en el servidor') # true
    def test_skip_if(self):
        self.assertEqual(100, 100)

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(100, 50)
