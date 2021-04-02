class MyClass:
  x = 5

p1 = MyClass()
# print(p1.x)

class SecondaryClass:
    m = "Howdy, my age is"

p2 = SecondaryClass()
print(p2.m, p1.x)

types_of_people = 10
df = f"There are {types_of_people} types of people"

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(df)
print(y)


price = 49
txt = "The price is {} dollars"
print(txt.format(price))
