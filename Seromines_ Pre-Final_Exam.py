print('CS112: COMPUTER PROGRAMMING 1 - PRE-FINAL EXAM\nCreated by: Ralph Joshua A. Seromines.\n')

while True:
    # ako ra bag o nahibal an Sir, pampawala sa white spaces ang .strip() hehehe
    # if accidentally ma tap ang space bar, e read dyapun niya sag naay white spaces
    num1 = int(input("First Number: ").strip())

    if num1 == 0:
        print("Program Terminated.\n")
    elif num1 <= -1:
        print(f"{num1} is a negative number.\nPlease enter a valid non-negative number for First number.\n")
    else:
        num2 = int(input("Second Number: ").strip())

        if num2 == 0:
            print("Program Terminated.\n")
        elif num2 == num1:
            print("Please do not enter the same number.\n")
        elif num2 <= -1:
            print(f"{num2} is a negative number.\nPlease enter a valid non-negative number for Second number.\n")
        elif num2 <= num1:
            print("Please enter a First number greater than the Second number.\n")
        else:
            notfound = False

            print(f"Prime numbers between {num1} and {num2} are:")

            for num in range(num1, num2 + 1):
                if num > 1:
                    for i in range(2, num):
                        if num % i == 0:
                            break
                    else:
                        print(num)
                        notfound = True

            if not notfound:
                print(f"There is no prime number between {num1} and {num2}.\n")
