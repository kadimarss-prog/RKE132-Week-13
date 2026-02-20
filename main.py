from animal import Animal, Cat
from animal import Animal, Dog

my_cat = Cat("Kiisu")
my_dog = Dog("Kutsu")
neighbours_dog = Dog("Chilli")

"""for i in range(10):
    my_cat.sleep() """

#my_dog.bark()

#my_cat.sees(my_dog)
#my_dog.sees(my_cat)
#my_dog.dog_sees(neighbours_dog)
#my_dog.dog_sees(my_cat)
my_cat.cat_sees(my_dog)
my_cat.cat_sees(my_cat)
my_cat.cat_sees(neighbours_dog)