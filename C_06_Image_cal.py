# ask the user for width and

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

def image_cal():
    width = integer_checker("Width: ", 1)
    height = integer_checker("Height: ", 1)

    # multiply the number of pixels by 24 to get the number of bits
    num_pixels = width * height
    num_bits = num_pixels * 24

    # set up answer and return it

    answer = f"Number of pixels: {width} * {height} = {num_pixels} " \
             f"\nNumber of bits: {num_pixels} * 24 = {num_bits} "

    return answer

# main routine goes here

image_ans = image_cal()
print(image_ans)
