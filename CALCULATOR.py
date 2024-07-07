#using lamda expressions to perform basic arithmetic operations 
add = lambda a, b: a + b
sub = lambda a, b: a - b
multiply = lambda a, b: a * b
divide = lambda a, b: "Not possible to divide by zero" if b == 0 else a / b

while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    
    n = input("Choose the operation to be performed: ")
    if n == '5':
        print("Exiting. Adios!")
        break
    
    if n in ('1', '2', '3', '4'):
        try: #Exception Handling
            n1 = float(input("Enter the first number: "))
            n2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input")
            continue
        
        if n == '1':
            result = add(n1, n2)
            print(result)
        elif n == '2':
            result = sub(n1, n2)
            print(result)
        elif n == '3':
            result = multiply(n1, n2)
            print(result)
        elif n == '4':
            result = divide(n1, n2)
            print(result)

    else:
        print("Make sure to enter the correct number w.r.t. operation (1/2/3/4)")
