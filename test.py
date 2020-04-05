
def is_even(number):

    if isinstance(number, int):
        if number % 2 == 0:
            print("True")
            return True
        else:
            print("False")
            return False
    else:
        print("number must be an int")
        return


is_even(4)
is_even(3)
is_even(2.2)

def is_parsable(input):
    if isinstance(input, int):
        print(input, "is int")
        return True
    try:
        "".split(input)
        print(input, "is parsable")
        return True
    except Exception as e:
        raise ValueError("not parsable", e.args[0])
        return False


is_parsable("ab")
is_parsable(768)

def build_pyramid_with_given_height_and_direction(height, direction="up"):

    if isinstance(height, int) and height > 0:
        if direction == "up":
            increase_asterisks_count = 1
            for i in range(0, height):
                asterisks = "*" * increase_asterisks_count
                empty_spaces = (height - i) * " "
                print(empty_spaces + asterisks)
                increase_asterisks_count += 2
        elif direction == "down":
            reduce_asterisks_count = 1
            for i in range(0, height):
                empty_spaces = " " * (1 + i)
                asterisks = "*" * (height * 2 - reduce_asterisks_count)
                print(empty_spaces + asterisks)
                reduce_asterisks_count += 2
    else:
        print("height must be int and greater than 0")


build_pyramid_with_given_height_and_direction(5)
build_pyramid_with_given_height_and_direction(5, "down")
build_pyramid_with_given_height_and_direction(-1)
build_pyramid_with_given_height_and_direction("4")


def solve_math(string, *args):

    if isinstance(string, str):
        array = []
        for i in string:
            array.append(i)
        p = 0
        for i in range(0, len(array)):
            if array[i] == "x":
                array[i] = str(args[p])
                p += 1
            else:
                continue
        result = eval("".join(array))
        print("".join(array), "=", result)
    else:
        print("Please enter valid input")


solve_math("x*x-x/x+x", 1, 2, 3, 4, 5)
solve_math("x-x/x+x*2", 1, 2, 3, 4, 5)



