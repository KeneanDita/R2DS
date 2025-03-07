from convertor import lbs_to_kg

print(lbs_to_kg(100))

def sum_two_numbers(a, b):
  """Sums two numbers.

  Args:
    a: The first number.
    b: The second number.

  Returns:
    The sum of the two numbers.
  """
  return a + b

if __name__ == "__main__":
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))
  result = sum_two_numbers(num1, num2)
  print("The sum is:", result)
sum_two_numbers(2,3)