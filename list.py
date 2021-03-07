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
