class ASTNode:
    def __init__(self, type, value=None, left=None, right=None):
        """
        Represents a node in the Abstract Syntax Tree (AST).
        type: "operator" (for AND/OR) or "operand" (for conditions)
        value: The actual value for operand nodes (e.g., age > 30) or the operator (e.g., AND, OR)
        left, right: The left and right child nodes (if applicable)
        """
        self.type = type
        self.value = value
        self.left = left
        self.right = right


def parse_condition(condition):
    """
    Parses a condition like "age > 30" or "department = 'Sales'" into its components.
    Returns the attribute, operator, and value.
    """
    parts = condition.split()
    attribute = parts[0]
    operator = parts[1]
    value = parts[2]

    # Handle numeric and string values
    if value.isdigit():
        value = int(value)  # Convert to integer if it's a number
    else:
        value = value.strip("'")  # Remove quotes for string values like 'Sales'

    return attribute, operator, value


def evaluate_rule(ast, data):
    """
    Recursively evaluates the AST against the provided data.
    The data is a dictionary containing attributes like {"age": 35, "department": "Sales"}.
    """
    if ast.type == "operator":
        if ast.value == "AND":
            return evaluate_rule(ast.left, data) and evaluate_rule(ast.right, data)
        elif ast.value == "OR":
            return evaluate_rule(ast.left, data) or evaluate_rule(ast.right, data)

    elif ast.type == "operand":
        attribute, operator, value = parse_condition(ast.value)

        if attribute not in data:
            raise ValueError(f"Attribute {attribute} not found in data")

        # Perform the comparison
        if operator == ">":
            return data[attribute] > value
        elif operator == "<":
            return data[attribute] < value
        elif operator == "=":
            return data[attribute] == value

    return False


def create_rule(rule_string):
    """
    Takes a rule string (e.g., "age > 30 AND department = 'Sales'") and converts it into an AST.
    Simplified example for demonstration purposes.
    """
    # For this example, we'll assume a basic two-part rule and a single AND/OR operator
    if "AND" in rule_string:
        operator = "AND"
        left, right = rule_string.split("AND")
    elif "OR" in rule_string:
        operator = "OR"
        left, right = rule_string.split("OR")
    else:
        # Single condition, no AND/OR
        return ASTNode(type="operand", value=rule_string.strip())

    # Create AST nodes
    left_node = ASTNode(type="operand", value=left.strip())
    right_node = ASTNode(type="operand", value=right.strip())
    root_node = ASTNode(type="operator", value=operator, left=left_node, right=right_node)

    return root_node


def combine_rules(rules):
    """
    Takes a list of rule ASTs and combines them into a single AST using OR as the combining operator.
    """
    if len(rules) == 0:
        return None
    if len(rules) == 1:
        return rules[0]

    combined_ast = rules[0]
    for rule_ast in rules[1:]:
        combined_ast = ASTNode(type="operator", value="OR", left=combined_ast, right=rule_ast)

    return combined_ast


class RuleEngine:
    def __init__(self):
        # Initialization logic
        pass

    def evaluate(self, user_data):
        # Example eligibility logic (replace with actual rules)
        if user_data['age'] > 25 and user_data['income'] > 30000:
            return True
        else:
            return False


if __name__ == "__main__":
    # Sample user data
    user_data = {
        'age': 30,
        'income': 40000,
        'department': 'Sales'
    }

    # Create an instance of RuleEngine
    engine = RuleEngine()

    # Evaluate user data
    eligibility = engine.evaluate(user_data)
    print(f"User eligibility: {eligibility}")

    # Example rule parsing and evaluation
    rule_string = "age > 25 AND income > 30000"
    rule_ast = create_rule(rule_string)
    result = evaluate_rule(rule_ast, user_data)
    print(f"Rule evaluation result: {result}")
