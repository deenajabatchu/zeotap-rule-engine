# test_cases.py
from rule_engine import create_rule, combine_rules, evaluate_rule

def run_tests():
    # Test rule creation
    rule1 = create_rule("age > 30 AND department = 'Sales'")
    rule2 = create_rule("age < 25 AND department = 'Marketing'")
    print(f"Rule 1 AST: {rule1}")
    print(f"Rule 2 AST: {rule2}")
    
    # Test rule combination
    combined_rule = combine_rules([rule1, rule2])
    print(f"Combined Rule AST: {combined_rule}")
    
    # Test rule evaluation
    test_data = {"age": 35, "department": "Sales", "salary": 60000}
    result = evaluate_rule(combined_rule, test_data)
    print(f"Evaluation Result: {result}")

if __name__ == "__main__":
    run_tests()
