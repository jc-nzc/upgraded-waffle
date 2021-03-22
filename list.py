thislist = ["jac", "df", "agv"]

print(thislist[2])
print(thislist[-1])
print(thislist[1:4])
print(thislist[:2])
if "agv" in thislist:
  print("Yes, 'Ale is present' is in the fruits list")

if "jac" in thislist:
    print(True)

print(len(thislist))

print(type(thislist))


thatlist = list(("peanuts", "tofu", "fruit rollup")) # note the double round-brackets

print(thatlist)


# change an item in the list
thislist = ["apple", "banana", "cherry", "watermelon", "lemon", "peach"]
print(thislist)

thislist[2] = "blackcurrant"
print(thislist)

thislist[1:3] = ["blueberry", "dragonfruit"]
print(thislist)

hitlist = ["donut", "ale", "jorge"]
# print(hitlist)
# hitlist.insert(2, "lemon")
# print(hitlist)
# hitlist.insert(4, "dino")
# print(hitlist)

for i in range(len(hitlist)):
  print(hitlist[i])

print("**now this**")

for i in range(len(hitlist)):
    # hitlist.insert(0, "caviar")
    print(hitlist[i])

print('____')

# Example
# https://stackoverflow.com/questions/31040525/insert-element-in-python-list-after-every-nth-element

letters = ['a','b','c','d','e','f','g','h','i','j']
i = 3
while i < len(letters):
    letters.insert(i, 'x')
    i += 4

print(letters)

print('__ search through rhymes for text')
rhymes = ["bones", "jones", "homes", "loans", "stones"]
newlist = []

for x in rhymes:
  if "on" in x:
    newlist.append(x)

print(newlist)


print("____ zip lists exercises")

letters = ['a', 'b', 'c']
numbers = [0, 1, 2]
for l, n in zip(letters, numbers):
    print(f'Letter: {l}')
    print(f'Number: {n}')

# another thought
a_zip = zip(letters, numbers) #Create zip object.
zipped_list = list(a_zip) #Convert zip to list.
print(zipped_list)

# iterate and zip through existing lists once... a,0 then b, 1, then c,2. Now append those 3 instances into a single list
a = ['a', 'b', 'c']
b = [0, 1, 2]
temp = []
for i in zip(a, b):
    for j in i:
        temp.append(j)
print(temp)

print("__functions exercise__")

a = 35
b = 28
if b > a:
  print("B is greater than A")
else:
  print("A is greater than B")

c = 22
d = 11
if c > d: print("c is greater than d")

ch = 330
sh = 330
print("Left") if ch > sh else print("Straight") if ch == sh else print("Right")

# now lets test pass statements
dor = 33
sor = 200

if dor != sor:
    print("oops")
    if sor > dor:
        pass
    print("howdy")

lead = {
    "first_name": "John",
    "last_name": "Kravitz",
    "phone_1": "5128318889999",
    "email": "SimpleSyrup@donut.com"
}

print(lead)

f_name = lead.get("first_name")
print(f_name)
l_name = lead.get("last_name")
print(l_name)
email = lead.get("email")
print(email)
phone = lead.get("phone_1")
print(phone)

keys = lead.keys()
print(keys)

values = lead.values()
print(values)

list_of_things = x = lead.items()
print(list_of_things)

payloads = lead.values()
print(payloads)


for k in lead.keys():
    print(k)

# iterate through lead for value
for v in lead.values():
    print(v)


if "email" in lead:
  print("Yes, 'email' is one of the keys in the 'lead' dictionary")

print(f"{f_name}")

# lambda example
x = lambda a : a + 35
print(x(5))

y = lambda b : b + 7
print(y(7))

# multi arg lambda

x = lambda a, b : a * b
print(x(5, 6))
