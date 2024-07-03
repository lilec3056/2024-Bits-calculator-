# ask the user for width and loop until they enter a number more than 0

def integer_checker(question, low):
    error = f"Please enter a whole number or number equal to {low}\n"
    while True:
        try:
            # ask the user for a width
            response = int(input(question))

            # check the number is more than 0
            if response >= low:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def integer_cal():
    # ask the user for an integer more than / equal to 0

    integer = integer_checker("Integer: ", 0)

    # convert the integer to binary and workout the number of bits needed

    raw_binary = bin(integer)

    binary_int = raw_binary[2:]
    num_bits = len(binary_int)
    # set up answer and return it

    answer = f"{integer} in binary is {binary_int}. We need {num_bits} bits to represent it. "

    return answer


# main routine goes here

image_ans = integer_cal()
print(image_ans)
