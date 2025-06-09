import unittest
from main import customerSuccessBalancing

class TestCustomerSuccessBalancing(unittest.TestCase):
    def test_example_case(self):
        cs = [
            {"id": 1, "score": 60},
            {"id": 2, "score": 20},
            {"id": 3, "score": 95},
            {"id": 4, "score": 75}
        ]
        clients = [
            {"id": 1, "score": 90},
            {"id": 2, "score": 20},
            {"id": 3, "score": 70},
            {"id": 4, "score": 40},
            {"id": 5, "score": 60},
            {"id": 6, "score": 10}
        ]
        away = [2, 4]
        result = customerSuccessBalancing(cs, clients, away)
        self.assertEqual(result, 1)

    def test_tie_case(self):
        cs = [
            {"id": 1, "score": 50},
            {"id": 2, "score": 50}
        ]
        clients = [
            {"id": 1, "score": 40},
            {"id": 2, "score": 40}
        ]
        away = []
        result = customerSuccessBalancing(cs, clients, away)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
