while True:
    try:
        num = input()
        print(f"{eval(num)}\n")
    except (ValueError, SyntaxError, NameError) as e:
        print(f"Invalid input. Please enter a valid input. Error: {e} \n")