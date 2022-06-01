"""
This is the example script for working with classes in Python. Here I will show
you how to define your own class, how to create a constructor, how to define
member methods and last but not least how to use the string-method, a magic
function for working with print().
"""
# To define a class we need the keyword class and the name of our class. Here
# we define a class called Bike.
class Bike:
    # Everything beneath our class definition is seen as part of our class as
    # long as we leave the indent at the same level. The first thing I want to
    # do, is to define a constructor. The constructor is always exectued when we
    # create a new object of our class. You don't have to define it, since there
    # is always a default one running in the background, but if you do only your
    # constructor will be executed on the creation of a new object. The
    # constructor always has the name __init__ and takes at least the object
    # itself as argument (thus the self here). We can add additional arguments
    # to the constructor (here brand, displacement and hp) to hand over values
    # to our attributes. If we do so, these arguments have to be handed over to
    # our class when we create a new object (Down below in line 105).
    def __init__(self, brand, displacement, hp):
        # Inside the constructor I can now assign the arguments to my attributes
        # to give them the specified value. Here I create three different types
        # of attributes (public, protected and private) so you can see how to
        # define these with the usage of underscores. In most cases you would
        # only define public and private attributes. We can access the values of
        # these attributes (for public and protected at least) later on with the
        # point notation (line 109 for example).
        self.brand = brand  # public
        self.__displacement = displacement  # private
        self._hp = hp  # protected

    # Now we want to define a setter-method. These kind of member methods are
    # used to change the value of our private attributes, since we can't
    # interact with them otherwise. Here I define a method called
    # set_displacement which allows us to change the value of our attribute
    # __displacement. This method takes the object itself (self) and the new
    # value (cubic) as arguments
    def set_displacement(self, cubic):
        # I included a small security check to make sure, that we set the value
        # of this attribute to postive values only.
        if cubic <= 0:
            # If you try to set __displacement to a negative value, you get the
            # print out blow as Error message.
            print("Error: Negative value for displacement!")
        else:
            # If you use a positive number as argument for this method we can
            # now assign a new value to our attribute __displacement and give
            # the user a heads up that the value of this attribute was changed.
            self.__displacement = cubic
            print("displacement was changed")

    # Now I want to define a getter method to be able to access the value of my
    # private attribute __displacement. As we saw we can NOT access the value of
    # this attribute with a simple point notation and thus need some kind of
    # method to get the value. These getter methods are very simple functions
    # that take the object itself (self) as argument and just return the
    # corresponding attribute value. The nomenclature of these functions follows
    # the rules we discussed for variables, that means when we have multiple
    # words in our name they should be separated by an underscore
    def get_displacement(self):
        # After we defined our function, we just put a simple return statement
        # in it, that hands back the value of our attribute. This method here
        # simply returns the value of our private attribute __displacement.
        return self.__displacement

    # Now I define two simple methods to adjust the values of my protected
    # attribute _hp. As soon as you work with protected attributes you should
    # make sure to always use these kind of methods. I created two methods here
    # one that increases the value of our attribute _hp by just one and thus
    # takes only the object itself as argument and one that increases the value
    # of our attribute _hp by a specified number and thus takes a second
    # argument called addition. Both methods work in place and thus make
    # permanent changes to the value of our object as soon as they are exectued
    # down below (line 140).
    def add_hp(self):
        # This method increases the value of our attribute _hp simply by 1
        self._hp += 1

    def add_hp_multi(self, addition):
        # This method increases the value of our attribute _hp by a specific
        # number that is handed over to the method (addition)
        self._hp += addition

    # Last but not least I want to show you how you can define a magic function
    # In this case we will define the function __str__() which returns a string
    # That we can use in combination with other methods like print() for
    # example. This method only takes the object itself as an argument and
    # returns a string. So the variable your return has to be ALWAYS a string.
    def __str__(self):
        # Here I define a simpel f-string that contains the values of our three
        # attributes, so that I can print them out.
        printout = f"Your bike from {self.brand} has {self._hp} hp and a displacement of {self.__displacement} cubic"
        # Now I return this string so that it can be used outside of the class
        # definition.
        return printout


# Now we can create an object of our class harley. To do this we have to use an
# assignment similiar to our variable assignment or to the call back of
# functions. As you remember we defined our constructor with three additional
# arguments alongside self. These arguments were brand, displacement and hp. On
# the creation of our object we now have to hand these arguments over to our
# constructor, by writing them inside of brackets.
harley = Bike("Harley Davidson", 500, 80)
# Now we can access the value of our attributes with the point notation. Here I
# want to print out the value of the attributes brand and _hp of my object
# harley from the class Bike
print("Value of the attribute brand of object harley:", harley.brand)
print("Value of the attribute _hp of object harley:", harley._hp)
# As we saw this worked just fine for our public (brand) and protected (_hp)
# attributes. If we would try something similiar with our private attribute
# __diplacement, we would get the following Error message in the terminal:
# AttributeError: 'Bike' object has no attribute '__displacement'
# That means we can access this attribute here, so something like the print
# command below does NOT work.
# print(harley.__displacement)
# Since we defined a getter method for our attribute __displacement we can now
# use it to access the value of this attribute in our main program. Here I use
# it in a simple print out, but we could use it for mathematical calculations
# and other stuff as well.
print(
    "Value of the attribute __displacement of object harley:", harley.get_displacement()
)
# Now I want to show you the setter method in action. First I try to set the
# value of my attribute __displacement to -500 and get the Error message I
# defined beforehand in line 45
harley.set_displacement(-500)
# Afterwards I try to set the value to 600, which is totally fine and thus get
# the message that the displacement was changed just like I defined it in line
# 51
harley.set_displacement(600)
print(
    "Value of the attribute __displacement of object harley:", harley.get_displacement()
)
# Now I want to show you the usage of the methods we defined for changing the
# value of our protected attribute _hp. You will see that the value is increased
# by one after the usage of the add_hp() method and than by 20 after the usage
# of the add_hp_multi() method witht he argument 20.
harley.add_hp()
print("Value of the attribute _hp of object harley:", harley._hp)
harley.add_hp_multi(20)
print("Value of the attribute _hp of object harley:", harley._hp)
# For public attributes like brand we can change the value with simple
# assignments
harley.brand = "Orange County Choppers"
print("Value of the attribute brand of object harley:", harley.brand)
# The same is true for our protected attribute _hp, but you should try to avoid
# using it like this.
harley._hp = 90
print("Value of the attribute _hp of object harley:", harley._hp)
# Of course we can also change the value of our protected attribute _hp with
# mathematical operations similiar to the ones we saw in our method definitions
# BUT you should try to NOT use things like this.
harley._hp += 5
print("Value of the attribute _hp of object harley:", harley._hp)
# If we use print() the string method we defined in line 90 is executed and the
# string I returned in line 96 is now handed over to my print function.
print(harley)
