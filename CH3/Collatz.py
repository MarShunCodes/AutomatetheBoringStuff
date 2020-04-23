# Write your code here :-)


def checkinput():
        try:
            userinput = int(input("Enter a number: "))
            collatz(userinput)
        except ValueError:
            print("not an integer")
        else:
            return userinput


def collatz(number):
    if number !=1:
        if number % 2 == 0:
            print(number // 2)
            newNumber = number // 2
            collatz(newNumber)
        elif number % 2 == 1:
            print(3 * number + 1)
            newNumber = 3 * number + 1
            collatz(newNumber)
    else:
       if number == 1:
        return

checkinput()
