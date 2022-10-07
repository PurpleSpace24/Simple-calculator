def calculate():
    flag = True

    while flag:
        print("\nEnter first number : ")
        n1 = float(input())
        print("Enter second number : ")
        n2 = float(input())
        print("\n-----------------\n")
        print("Choose operation: \n +, -, *, /, even, max, min\n")
        c = input("Enter: ")
        print("\n-----------------\n")

        if c == "+":
            print("Result (round): ", n1 + n2)
        elif c == "-":
            print("Result (round): ", n1 - n2)
        elif c == "*":
            print("Result (round): ", n1 * n2)
        elif c == "/":
            print("Result (round): ", n1 / n2)
        elif c == "even":
            print("Result (round): ", (n1 + n2) / 2)
        elif c == "max":
            print("Result (round): ", max(n1, n2))
        elif c == "min":
            print("Result (round): ", min(n1, n2))

        print("\nOne more try? yes/no ")
        answ = input()

        if answ.lower() == 'no' or answ.lower() == 'n':
            flag = False
            break
        elif answ.lower() == 'yes' or answ.lower() == 'y':
            continue