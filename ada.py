class TP2TestCases(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_ada(self, mock_stdout):
        ex1.ada()
        results = mock_stdout.getvalue().splitlines()
        self.assertEqual(results[0], "ada lovelace")
        self.assertEqual(results[1], "Ada Lovelace")
        self.assertEqual(results[2], "ADA LOVELACE")
        self.assertEqual(results[3], "\tada lovelace")
