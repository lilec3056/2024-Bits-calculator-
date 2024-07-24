def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


def instructions():
    statement_generator("Instructions", "-")

    print('''
- Insert a supported file type (Text, Image, Integer)
- Press xxx to exit
''')

# asks user for file type (integer / image / text / xxx)


def get_filetype():

    while True:

        response = input("File type: ").lower()

        # check for 'i' or the exit code
        if response == "xxx" or response == "i":
            return response

        # check if it's an integer
        elif response in ['integer', 'int']:
            return "Integer"

        # check for text

        elif response in ['text', 'txt', 't']:
            return "Text"

        # check for an image

        elif response in ['image', 'picture', 'img', 'p']:
            return "Image"

        # if the response is invalid, output an error

        else:
            print("Please enter a valid file type")


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
    print()

    return answer


def text_bit_cal():

    # get text from user
    response = input("Enter some text: ")

    # calculate bits needed
    num_chars = len(response)
    num_bits = num_chars * 8

    # Set up answer and return it
    answer = f"{response} has {num_chars} characters." \
             f"\nWe need {num_chars} x 8 bits to represent it which is {num_bits} bits"
    print()

    return answer


def image_cal():
    width = integer_checker("Width (in pixels): ", 1)
    height = integer_checker("Height (in pixels): ", 1)

    # multiply the number of pixels by 24 to get the number of bits
    num_pixels = width * height
    num_bits = num_pixels * 24

    # set up answer and return it

    answer = f"Number of bits: {width} width x {height} height x 24 bits = {num_bits} "
    print()
    return answer


# Main routine goes here

statement_generator("Bits Calculator", "-")

print()
want_instructions = input("Press <enter> to read the instructions or any key to continue ")

if want_instructions == "":
    instructions()

print()

while True:

    file_type = get_filetype()

    if file_type == "xxx":
        print("Thanks for using the bit calculator")
        break

    # if user choose 'i', ask if they want image / integer

    if file_type == 'i':

        want_image = input("Press <enter> for an image or any key for an integer. ")
        if want_image == "":
            file_type = "Image"
        else:
            file_type = "Integer"

    print(f"You chose {file_type}")

    if file_type == "Image":
        img_answer = image_cal()
        print(img_answer)

    elif file_type in ['Text']:
        txt_answer = text_bit_cal()
        print(txt_answer)

    elif file_type in ['Integer']:
        int_answer = integer_cal()
        print(int_answer)
