def isbn13(isbn):
    # Check if given string consist of numbers except for
    # last index which may contain an 'X'
    try:
        int(isbn[0:len(isbn)-1])
    except ValueError:
        return "Invalid"

    # Determine length of string and call appropriate function.
    if len(isbn) == 10:
        if isbn[-1].isnumeric() or isbn[-1] == "X":  # Check final index char
            return validate_isbn10(isbn)
    elif len(isbn) == 13:
        return validate_isbn13(isbn)

    return "Invalid"


def validate_isbn10(isbn):
    sum_of_products = 0
    x = 10
    # Get sum of products
    for num in isbn:
        if num == "X":
            sum_of_products += 10 * x
        else:
            sum_of_products += int(num)*x
            x -= 1
    # Determine if ISBN10 is valid. If ISBN10 is valid
    # call convert_to_isbn13 to return converted ISBN10
    if sum_of_products % 11 == 0:
        return convert_to_isbn13(isbn)
    else:
        return "Invalid"


def validate_isbn13(isbn):
    # Check last char in string to see if it is a number
    if isbn[-1] not in "0123456789":
        return "Invalid"
    sum_of_products = 0
    for i, num in enumerate(isbn):
        if i % 2 == 0:
            sum_of_products += int(num)
        else:
            sum_of_products += int(num)*3

    # Determine if ISBN13 is valid
    if sum_of_products % 10 == 0:
        return "Valid"
    else:
        return "Invalid"


def convert_to_isbn13(isbn):
    # replace last digit with '0' and test if ISBN13 number is valid
    # if ISBN13 number is not valid add 1 to the last digit and test
    # again
    isbn = isbn[0:len(isbn) - 1] + "0"
    while validate_isbn13("978" + isbn) == "Invalid":
        isbn = isbn[0:len(isbn)-1] + str(int(isbn[-1])+1)
    isbn = "978" + isbn
    return isbn


def run_solution():
    # Function alows user to test USBN umbers manually
    while True:
        choice = input("Enter and ISBN10 or ISBN13 to validate:"
                        + "\n(Enter '0' to quit)\n")

        if choice == '0':
            break

        print(isbn13(choice))
