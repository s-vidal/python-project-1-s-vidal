import os
import datetime
from math import sqrt


def my_log():
    try:
        try:
            if not os.path.exists("./log_folder"):
                os.makedirs("./log_folder", )
        except Exception as e:
            print(e)
        try:
            f = open("./log_folder/log_file.txt", "a")
        except Exception as e:
            print(e)
        time = datetime.datetime.now()
        f.write("\n" + time.strftime("%p%m%Y, %H:%M:%S") + " logged successfully")
    except Exception as e:
        print(e)


print("\nex1 my_log()")
my_log()


def change_words_starting_with_a(list_to_check):
    try:
        modified_list = [i + " hello" if i[0].lower() == "a" else i for i in list_to_check]
        print(modified_list)
        return modified_list
    except Exception as e:
        print(e)


print("\nex2 change_words_starting_with_a(list_to_check):")
change_words_starting_with_a(["test", "two", "apple"])
change_words_starting_with_a(["test", "aroma", "Apple"])
change_words_starting_with_a(["test", 1, "Apple"])


def list_square_even_power_odd(list_range):
    if list_range:
        try:
            modified_list_range = [sqrt(list_range.index(i)) if i % 2 == 0 else list_range.index(i) ^ 2 for i in
                                   list_range]
            print(modified_list_range)
        except Exception as e:
            print(e)


print("\ne3 list_square_even_power_odd(list_range):")
list_square_even_power_odd(range(1, 5, 1))
list_square_even_power_odd(range(5, 13, 2))


def name_checker(list_of_names):
    try:
        modified_list_of_names = (full_name for full_name in list_of_names if " " in full_name)
        print(list(modified_list_of_names))
        return list(modified_list_of_names)
    except Exception as e:
        print(e)


print("\ne4 name_checker(list_of_names):")
name_checker(["Emma Jhonson", "Alex", "Jonathan Joe"])
name_checker(["Emma", "Alex Ben", "Jonathan J."])
name_checker(["Emma", 23, "Jonathan J."])

print("\n 5) List generators are lower level and thus much faster than generators. "
      "\n However, they take up much more memory space.")

def get_roots(first, second, third):
    try:
        calc = lambda a, b, c: (b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        print(calc(first, second, third))
    except Exception as e:
        print(e)


print("\ne6 get_roots(first, second, third):")
print(get_roots(3, 4, 5))
print(get_roots(5, 2, 1))


# def root(one, two, three):
#     try:
#         calc = lambda a, b, c: a + b + c
#         return calc(one, two, three)
#     except Exception as e:
#         print(e)
#
#
# print(root(3, 4, 5))
