from art import logo

# Add
def add(n1, n2):
  return  n1 + n2

# Subtract
def subtract(n1, n2):
  return n1 - n2

# Multiply
def multiply(n1, n2):
  return n1 * n2

# Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  '+': add, 
  '-': subtract, 
  '*': multiply, 
  '/': divide,
}

def calculator():
  print(logo)
  dec = 'y'
  num1 = float(input("What's the first number?: "))
  for operation in operations:
      print(operation)
  while(dec == 'y'):
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    answer = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    dec = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")
    if dec == 'y':
      num1 = answer
    else:
      calculator()

calculator()
