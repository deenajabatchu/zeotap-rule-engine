import unittest
from rule_engine import RuleEngine  # Import the class or module you're testing

class TestRuleEngine(unittest.TestCase):
    
    def setUp(self):
        # This method is called before each test case, you can initialize the RuleEngine object here
        self.rule_engine = RuleEngine()

    def test_eligibility(self):
        # Example test case for user eligibility
        user_data = {
            'age': 30,
            'department': 'Sales',
            'income': 50000,
            'spend': 2000
        }
        result = self.rule_engine.evaluate(user_data)
        expected_result = True  # Adjust this to what the correct output should be
        self.assertEqual(result, expected_result)

    def test_ineligibility(self):
        # Example test case for user ineligibility
        user_data = {
            'age': 18,
            'department': 'Intern',
            'income': 10000,
            'spend': 500
        }
        result = self.rule_engine.evaluate(user_data)
        expected_result = False  # Adjust based on your rule logic
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()