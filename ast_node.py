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
