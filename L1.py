
def is_even(number):
    try:
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
    except Exception as e:
        raise ValueError(e.args[0])


is_even(4)
is_even(3)
is_even(2.2)


def is_parsable(input):
    if isinstance(input, int):
        print("input:", input, ", is of type int")
        return True
    else:
        try:
            parsed_input = int(input)
            print("input string:", parsed_input, ", can be parsed")
            return True
        except Exception as e:
            print("input:", input, e.args[0])
            return False


is_parsable(768)
is_parsable("ab")
is_parsable("137")


def build_pyramid_with_given_height_and_direction(height, direction="up"):
    try:
        if isinstance(height, int) and height > 0:
            if direction == "up":
                asterisks_count = 1
                for i in range(0, height):
                    asterisks = "*" * asterisks_count
                    empty_spaces = (height - i) * " "
                    print(empty_spaces + asterisks)
                    asterisks_count += 2
            elif direction == "down":
                asterisks_count = 1
                for i in range(0, height):
                    empty_spaces = " " * (1 + i)
                    asterisks = "*" * (height * 2 - asterisks_count)
                    print(empty_spaces + asterisks)
                    asterisks_count += 2
        else:
            print("height must be int and greater than 0")
    except Exception as e:
        raise ValueError(e.args[0])


build_pyramid_with_given_height_and_direction(6)
build_pyramid_with_given_height_and_direction(-1)
build_pyramid_with_given_height_and_direction(5, "down")
build_pyramid_with_given_height_and_direction("4")


def solve_math(string, *args):
    try:
        if isinstance(string, str):
            array = []
            for i in string:
                array.append(i)
            arg_index = 0
            for i in range(0, len(array)):
                if array[i].isalpha():
                    array[i] = str(args[arg_index])
                    arg_index += 1
                else:
                    continue
            result = eval("".join(array))
            print("".join(array), "=", result)
        else:
            print("Please enter valid input")
    except Exception as e:
        raise ValueError(e.args[0])


solve_math("x*x-x/x+x", 1, 2, 3, 4, 5)
solve_math("x-x/x+x*2", 1, 5, 3, 4, 2)
solve_math("a+d*c+d/5-w", 5, 2, 3.5, 6, 3)





