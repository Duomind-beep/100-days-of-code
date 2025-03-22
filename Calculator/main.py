import art
print(art.logo)

def add(n1, n2):
    return n1 + n2

def divide(n1, n2):
    return n1 / n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

operations = {
    "+" : add,
    "/" : divide,
    "-" : subtract,
    "*" : multiply,
}
def my_calculator():
    should_accumulate = True
    num1 = float(input("What's the first number?: "))
    while should_accumulate:
        for key in operations:
            print(key)
        operation = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        result = (operations[f"{operation}"] (num1,num2))

        print(f"{num1} {operation} {num2} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        if choice == "y":
            num1 = result
        else:
            should_accumulate = False
            my_calculator()

my_calculator()
