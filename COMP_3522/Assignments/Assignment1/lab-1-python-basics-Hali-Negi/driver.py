from hypotenuse import calculate_hypotenuse

def my_sum(a, b):
    """
    Returns the sum of two numbers
    """
    return a + b

def my_subtract(a, b):
    """
    Returns the difference of two numbers
    """
    return a - b

def my_multiply(a, b):
    """
    Return the product of two numbers
    """
    return a * b

def my_divide(a, b):
    """
    Return the quotient of two numbers
    """
    return a / b

def main():
   first_number  = float(input("First number: "))
   second_number = float(input("Second number: "))

   print("\nChoose an operation: ")
   print("1. Add")
   print("2. Subtract")
   print("3. Multiply")
   print("4. Divide")
   print("5. Find the hypotenuse")

   choice = input("Enter your choice (from 1 to 5): ")

   if choice == "1":
       result = my_sum(first_number, second_number)
       print("Result:", result)

   elif choice == "2":
        result = my_subtract(first_number, second_number)
        print("Result:", result)

   elif choice == "3":
       result = my_multiply(first_number, second_number)
       print("Result:", result)

   elif choice == "4":
       if second_number == 0:
           print("Cannot divide by zero")

       else:
           result = my_divide(first_number, second_number)
           print("Result:", result)

   elif choice == "5":
       result = calculate_hypotenuse(first_number, second_number)
       print("Hypotenuse:", result)

   else:
       print("Invalid choice")


if __name__ == "__main__":
    main()