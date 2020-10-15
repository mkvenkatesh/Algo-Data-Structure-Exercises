class Fraction:
    # This is called the constructor. It provides a way to define the objects
    # that are created from the class
    def __init__(self, top, bottom): 
        if not (type(top) == int and type(bottom) == int):
            raise TypeError("Numerator and denominator should be of type: INT")

        if bottom < 0:
            bottom = abs(bottom)
            top = -(abs(top))

        # self - references the object that's instantiated from this class. 
        # For all Python methods in a class, self should be the first parameter
        gcd = self.gcd(top, bottom)
        self.num = top // gcd
        self.den = bottom //gcd

    def show(self):
        print(self.num, "/", self.den)

    # In Python, all classes have a set of standard methods that are provided
    # but may not work properly. One of these, __str__, is the method to convert
    # an object into a string. The default implementation for this method is to
    # return the instance address string. What we need to do is provide a
    # “better” implementation for this method. We will say that this
    # implementation overrides the previous one, or that it redefines the
    # method’s behavior. __str__ is for human readability
    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    # __repr__ returns a string containing a printable representation of the
    # object. It's unambiguous and helps with debugging for the programmer.
    def __repr__(self):
        return "Numerator: " + str(self.num) + "; Denominator: " + str(self.den)

    def get_num(self):
        return self.num
    
    def get_den(self):
        return self.den

    def __add__(self, other_fraction):
        new_num = (self.num * other_fraction.den) + (other_fraction.num * self.den)
        new_den = (self.den * other_fraction.den)
        # when you add fractions, the result won't necessarily be in the lowest
        # common terms. To get lct, divide num and den by the gcd of num, den
        # gcd = self.gcd(new_num, new_den)
        return Fraction(new_num, new_den)

    __radd__ = __add__

    # incremental add e.g. x += 1 (or) x = x.__iadd(y)
    def __iadd__(self, other_fraction):
        self = self.__add__(other_fraction)
        return self

    # The best-known algorithm for finding a greatest common divisor is Euclid’s
    # Algorithm. Euclid’s Algorithm states that the greatest common divisor of
    # two integers 𝑚 and 𝑛 is 𝑛 if 𝑛 divides 𝑚 evenly. However, if 𝑛 does
    # not divide 𝑚 evenly, then the answer is the greatest common divisor of 𝑛
    # and the remainder of 𝑚 divided by 𝑛.
    def gcd(self, m, n):
        if n == 0:
            return m
        else:
            return self.gcd(n, m % n)

    def __eq__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den
        return first_num == second_num

    def __mul__(self, other_fraction):
        first_num = self.num * other_fraction.num
        second_num = self.den * other_fraction.den
        # gcd = self.gcd(first_num, second_num)
        return Fraction(first_num, second_num)

    def __floordiv__(self, other_fraction):
        # 1/2 // 2/4 = 1/2 * 4/2
        temp = Fraction(other_fraction.den, other_fraction.num)    
        return self.__mul__(temp)
    
    def __sub__(self, other_fraction):
        # 1/2 - 1/4 = (4-2)/4*2 = 2/8 = 1/4
        new_num = (self.num * other_fraction.den) - (self.den * other_fraction.num)
        new_den = (self.den * other_fraction.den)
        return Fraction(new_num, new_den)

    def __le__(self, other_fraction):
        # 1/2 <= 1/4
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den
        return first_num <= second_num

    def __lt__(self, other_fraction):
        # 1/2 < 1/4
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den
        return first_num < second_num

    def __ge__(self, other_fraction):
        return not self.__le__(other_fraction)

    def __gt__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den
        return first_num > second_num

# To create an instance of the Fraction class, we must invoke the constructor.
# This happens by using the name of the class and passing actual values for the
# necessary state (note that we never directly invoke __init__)
print("\n***** Printing *****")
my_fraction = Fraction(1, 4)
print("my_fraction: ", end="")
my_fraction.show()

# convert object to a string representation
print("my_fraction: ", end="")
print(my_fraction)
print("my_fraction: ", end="")
print(my_fraction.__str__())
print("my_fraction: ", end="")
print(str(my_fraction))

my_fraction1 = Fraction(1, -2)

print("\n***** Addition *****")
# add fractions
print(my_fraction, "+", my_fraction1, "= ", end="")
added_fractions = my_fraction + my_fraction1 # or my_fraction.__add__(my_fraction1)
print(added_fractions)

# check equality. Shallow equality is if you don't override __eq__ for the
# object and then compare two objects. It only checks if the references to the
# objects are the same. Deep equality is when you override __eq__ to check for
# the actual object values
print("\n***** Equality *****")
my_fraction2 = Fraction(2, 4)
print(my_fraction, " is equal to ", my_fraction1, ": ", end="")
print(my_fraction == my_fraction1)

print(my_fraction1, " is equal to ", my_fraction2, ": ", end="")
print(my_fraction1 == my_fraction2)

print(my_fraction1, " is equal to ", my_fraction2, ": ", end="")
print(my_fraction1.__eq__(my_fraction2))

print("\n***** Multiply *****")
# multiply two fractions
print(my_fraction, " * ", my_fraction1, "= ", end="")
print(my_fraction * my_fraction1)

print(my_fraction1, " * ", my_fraction2, "= ", end="")
print(my_fraction1 * my_fraction2)


print("\n***** Division *****")
print(my_fraction, " // ", my_fraction1, "= ", end="")
print(my_fraction // my_fraction1)

print(my_fraction1, " // ", my_fraction2, "= ", end="")
print(my_fraction1 // my_fraction2)


print("\n***** Subtract *****")
print(my_fraction, " - ", my_fraction1, "= ", end="")
print(my_fraction - my_fraction1)

print(my_fraction1, " - ", my_fraction2, "= ", end="")
print(my_fraction1 - my_fraction2)


print("\n***** <= *****")
my_fraction3 = Fraction(5, 7)
print(my_fraction, " <= ", my_fraction1, "= ", end="")
print(my_fraction <= my_fraction1)

print(my_fraction3, " <= ", my_fraction1, "= ", end="")
print(my_fraction3 <= my_fraction1)

print("\n***** >= *****")
my_fraction3 = Fraction(5, 7)
print(my_fraction, " >= ", my_fraction1, "= ", end="")
print(my_fraction >= my_fraction1)

print(my_fraction3, " >= ", my_fraction1, "= ", end="")
print(my_fraction3 >= my_fraction1)


print("\n***** < *****")
print(my_fraction, " < ", my_fraction1, "= ", end="")
print(my_fraction < my_fraction1)

print(my_fraction1, " < ", my_fraction2, "= ", end="")
print(my_fraction1 < my_fraction2)

print("\n***** > *****")
print(my_fraction, " > ", my_fraction1, "= ", end="")
print(my_fraction > my_fraction1)

print(my_fraction1, " > ", my_fraction2, "= ", end="")
print(my_fraction1 > my_fraction2)


print("\n***** Get Numerator *****")
print(my_fraction3.get_num())

print("\n***** Get Denominator *****")
print(my_fraction3.get_den())


print("\n***** radd *****")
print(my_fraction, "+", my_fraction1, "= ", end="")
added_fractions = my_fraction.__radd__(my_fraction1)
print(added_fractions)

print("\n***** iadd *****")
print(my_fraction, "+=", my_fraction1, "= ", end="")
my_fraction += my_fraction1
print(my_fraction)


print("\n***** repr *****")
print(repr(my_fraction))

print("\n***** Fraction with non-ints *****")
my_fraction4 = Fraction(1, 2.0)