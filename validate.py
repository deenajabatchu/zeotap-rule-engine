<<<<<<< HEAD
# validate.py
def validate_rule_string(rule_string):
    # Basic check for valid operators and parentheses
    valid_operators = ['AND', 'OR', '>', '<', '=']
    if rule_string.count('(') != rule_string.count(')'):
        raise ValueError("Unbalanced parentheses in rule string")
    for op in rule_string.split():
        if op.isalpha() and op not in valid_operators:
            raise ValueError(f"Invalid operator found: {op}")
    return True

def validate_attributes(data, valid_attributes):
    # Ensures data only contains valid keys
    for key in data.keys():
        if key not in valid_attributes:
            raise ValueError(f"Invalid attribute: {key}")
=======
# validate.py
def validate_rule_string(rule_string):
    # Basic check for valid operators and parentheses
    valid_operators = ['AND', 'OR', '>', '<', '=']
    if rule_string.count('(') != rule_string.count(')'):
        raise ValueError("Unbalanced parentheses in rule string")
    for op in rule_string.split():
        if op.isalpha() and op not in valid_operators:
            raise ValueError(f"Invalid operator found: {op}")
    return True

def validate_attributes(data, valid_attributes):
    # Ensures data only contains valid keys
    for key in data.keys():
        if key not in valid_attributes:
            raise ValueError(f"Invalid attribute: {key}")
>>>>>>> e5fef81 (Initial commit with rule engine code)
    return True