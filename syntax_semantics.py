class Parser:
    def __init__(self, text):
        # Remove spaces para pwede ring mag-input ng: 3 + 4 * 2
        self.text = text.replace(" ", "")
        self.position = 0

    def current_char(self):
        # Ibalik ang kasalukuyang character; None kapag dulo na ng input
        if self.position < len(self.text):
            return self.text[self.position]
        return None

    def consume(self, expected=None):
        # Kumain o mag-advance ng isang character
        char = self.current_char()

        if char is None:
            raise SyntaxError(
                f"Unexpected end of input at position {self.position}"
            )

        if expected is not None and char != expected:
            raise SyntaxError(
                f"Expected '{expected}' at position {self.position}, "
                f"but found '{char}'"
            )

        self.position += 1
        return char

    # Grammar rule:
    # <expr> -> <term> { (+ | -) <term> }
    def parse_expr(self):
        value = self.parse_term()

        while self.current_char() in ("+", "-"):
            operator = self.consume()
            right_value = self.parse_term()

            if operator == "+":
                value = value + right_value
            else:
                value = value - right_value

        return value

    # Grammar rule:
    # <term> -> <factor> { (* | /) <factor> }
    def parse_term(self):
        value = self.parse_factor()

        while self.current_char() in ("*", "/"):
            operator = self.consume()
            right_value = self.parse_factor()

            if operator == "*":
                value = value * right_value
            else:
                if right_value == 0:
                    raise ZeroDivisionError("Cannot divide by zero.")
                value = value / right_value

        return value

    # Grammar rule:
    # <factor> -> ( <expr> ) | <digit>
    def parse_factor(self):
        char = self.current_char()

        # RECURSION happens here:
        # If the factor starts with (, call parse_expr() again.
        if char == "(":
            self.consume("(")
            value = self.parse_expr()

            if self.current_char() != ")":
                found = self.current_char()
                if found is None:
                    raise SyntaxError(
                        f"Missing ')' for '(' at position {self.position}"
                    )
                raise SyntaxError(
                    f"Expected ')' at position {self.position}, "
                    f"but found '{found}'"
                )

            self.consume(")")
            return value

        # Accept only one digit: 0 to 9
        elif char is not None and char.isdigit():
            self.consume()
            return int(char)

        # Invalid token
        else:
            if char is None:
                raise SyntaxError(
                    f"Expected a digit or '(' at position {self.position}"
                )

            raise SyntaxError(
                f"Invalid token '{char}' at position {self.position}. "
                "Expected a digit or '('."
            )

    def parse(self):
        # Reject empty input
        if self.text == "":
            raise SyntaxError("Input cannot be empty.")

        # Start from <expr>
        value = self.parse_expr()

        # Input should be completely consumed
        if self.current_char() is not None:
            raise SyntaxError(
                f"Unexpected token '{self.current_char()}' "
                f"at position {self.position}"
            )

        return value


def check_and_evaluate(expression):
    print(f"\nInput: {expression}")

    try:
        parser = Parser(expression)
        result = parser.parse()

        print("Syntax: Valid")
        print(f"Value: {result}")

    except SyntaxError as error:
        print("Syntax: Invalid")
        print(f"Invalid syntax: {error}")

    except ZeroDivisionError as error:
        print("Syntax: Invalid for evaluation")
        print(f"Error: {error}")


def naive_left_to_right(expression):
    """
    Demonstration only:
    A naive evaluator that treats + and * with equal precedence
    and calculates strictly left to right.

    For 2+3*4:
    (2+3)*4 = 20
    """
    tokens = list(expression)

    if len(tokens) != 5:
        return "Demo only supports an expression like 2+3*4."

    value = int(tokens[0])
    operator1 = tokens[1]
    number1 = int(tokens[2])
    operator2 = tokens[3]
    number2 = int(tokens[4])

    if operator1 == "+":
        value = value + number1
    elif operator1 == "*":
        value = value * number1

    if operator2 == "+":
        value = value + number2
    elif operator2 == "*":
        value = value * number2

    return value


# Stretch requirement: Ambiguous grammar demonstration
print("=== Ambiguous Grammar Demonstration ===")
expression_demo = "2+3*4"

print(f"Expression: {expression_demo}")
print("Naive left-to-right result:", naive_left_to_right(expression_demo))
print("Correct precedence result: 14")

print("\n=== Required Test Cases ===")

test_cases = [
    "3+4*2",
    "(3+4)*2",
    "8/2-1",
    "3++4",
    "(3+4",
    "2+3*4"
]

for test in test_cases:
    check_and_evaluate(test)


# Optional: Let the user enter their own expression
print("\n=== Try Your Own Expression ===")
user_input = input("Enter an arithmetic expression: ")
check_and_evaluate(user_input)