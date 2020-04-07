class CarLot:
    amount_of_free_places = 0
    is_open = "True"

    def __init__(self, amount_of_free_places, is_open="True"):
        self.is_open = is_open
        self.amount_of_free_places = "amount of free spaces:" + str(amount_of_free_places)
        self.__square_meters = 55

    def set_is_open(self, input_value):
        self.is_open = input_value

    def set_amount_of_free_places(self, input_value):
        self.amount_of_free_places = "amount of free spaces:" + str(input_value)

    def get_is_open(self):
        return self.is_open

    def get_amount_of_free_places(self):
        return self.amount_of_free_places

    def get_square_meters(self):
        return self.__square_meters


print("\nex2:")
car_lot = CarLot(20, 10)
print(car_lot.get_amount_of_free_places())
car_lot.set_amount_of_free_places(8)
print(car_lot.get_amount_of_free_places())
print(car_lot.get_square_meters())


class Vehicle:
    need_repairs = False
    is_clean = True

    def __init__(self, need_repairs, is_clean):
        self.need_repairs = need_repairs
        self.is_clean = is_clean

    def set_need_repairs(self, boolean):
        self.need_repairs = boolean

    def set_is_clean(self, boolean):
        self.is_clean = boolean

    def get_need_repairs(self):
        try:
            if self.need_repairs:
                return "The vehicle needs to be repaired"
            else:
                return "The vehicle is in good shape"
        except Exception as e:
            print(e)

    def get_is_clean(self):
        if self.is_clean:
            return "the vehicle is clean"
        else:
            return "the vehicle needs to be cleaned"

    def load_from_csv(self, path):
        try:
            f = open(str(path), "r")
            return f.read()
        except Exception as e:
            print(e)

    def write_to_csv(self, path, text):
        try:
            f = open(str(path), "a")
            f.write("\n" + text)
        except Exception as e:
            print(e)


class Car(Vehicle):
    brand = ""

    def __init__(self, brand, need_repairs, is_clean):
        self.brand = brand
        super().__init__(need_repairs, is_clean)

    def get_brand(self):
        return self.brand


print("\nex3 and ex4:\n")
car_nr_12 = Car("Audi", True, False)
print(car_nr_12.brand)
print(car_nr_12.get_is_clean())
car_nr_12.set_need_repairs(False)
print(car_nr_12.get_need_repairs())


class Bike(Vehicle):
    bike_type = "standard"

    def __init__(self, bike_type, need_repairs, is_clean, what_needs_to_be_repaired):
        self.bike_type = bike_type
        self.what_needs_to_be_repaired = what_needs_to_be_repaired
        super().__init__(need_repairs, is_clean)

    def get_bike_type(self):
        return "the bike type is" + self.bike_type

    def get_need_repairs(self):
        if self.need_repairs:
            return self.what_needs_to_be_repaired + " need to be repaired"
        else:
            return "no repairs are needed"


print("\n")
bike_nr_3 = Bike("Mountain Bike", True, True, "gears")
print(bike_nr_3.bike_type)
print(bike_nr_3.get_need_repairs())
print(bike_nr_3.get_is_clean())

print("\nex optional 1:")
print(bike_nr_3.load_from_csv("l03.sql"))
bike_nr_3.write_to_csv("l03.sql", "new entry number 3")
print(bike_nr_3.load_from_csv("l03.sql"))


